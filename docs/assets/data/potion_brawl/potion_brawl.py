#!/usr/bin/env python3
"""
⚗️  POTION BRAWL  ⚗️  —  a rock-paper-scissors bottle brawl for The Alchemist's Lab.

Three enchanted potions bounce around the shop floor. When two collide, the
stronger reagent transmutes the weaker into its own kind. Left alone, one potion
eventually floods the whole lab.

The point of this little spectacle is NOT the brawl — it's the *virtual
environment*. This script leans on a whole shelf of reagents (numpy, scipy,
matplotlib, networkx, imageio, rich, pyfiglet, ...). Pin them in
``requirements.txt``, rebuild the venv anywhere, and the brawl runs identically.
Better still: it keeps a **lab journal** (``output/lab_journal.pkl``) so you can
`cp` the folder to a brand-new lab, rebuild the reagents from the recipe scroll,
and pick the brew up *exactly where you left off*.

Run it:   python potion_brawl.py
Run again and it resumes the same brawl, mid-brew.
"""
from __future__ import annotations

import os
import pickle
from dataclasses import dataclass, field

import numpy as np
from scipy.spatial import cKDTree

# --------------------------------------------------------------------------- #
#  The three potions and the Law of the Brawl                                 #
# --------------------------------------------------------------------------- #
# Potion of type ``t`` transmutes potion of type ``(t + 1) % 3`` on contact:
#   0 Ember   scorches  1 Verdant
#   1 Verdant drinks    2 Tide
#   2 Tide    douses    0 Ember


@dataclass(frozen=True)
class Potion:
    name: str
    element: str
    verb: str        # what it does to the potion it beats
    emoji: str
    color: str       # hex, used everywhere we draw


POTIONS = (
    Potion("Draught of Emberfury", "Fire",  "scorches", "🔴", "#d64545"),
    Potion("Verdant Elixir",       "Earth", "drinks",   "🟢", "#3fa34d"),
    Potion("Tears of the Tide",    "Water", "douses",   "🔵", "#3b7dd8"),
)
N_KINDS = len(POTIONS)
COLORS = [p.color for p in POTIONS]


def beats(a: int, b: int) -> bool:
    """True if potion kind ``a`` transmutes potion kind ``b``."""
    return (a + 1) % N_KINDS == b


# --------------------------------------------------------------------------- #
#  The brawl engine                                                           #
# --------------------------------------------------------------------------- #
@dataclass
class Brawl:
    """A cauldron full of bouncing, brawling potions.

    Positions/velocities live in ``dim``-dimensional space (2 or 3). Every
    ``step`` advances the physics, resolves collisions, and records the
    population of each potion so we can chart the war afterwards.
    """

    n_per_type: int = 40
    dim: int = 3
    size: float = 8.0          # box is [0, size] on every axis
    radius: float = 0.40       # collision when centres are within 2*radius
    speed: float = 0.15        # constant speed of every bottle
    seed: int = 7

    # runtime state (populated in __post_init__ or by load)
    pos: np.ndarray = field(default=None, repr=False)
    vel: np.ndarray = field(default=None, repr=False)
    kind: np.ndarray = field(default=None, repr=False)
    tick: int = 0
    history: list = field(default_factory=list, repr=False)
    frames: list = field(default_factory=list, repr=False)  # (tick, pos, kind) — not persisted
    rng: np.random.Generator = field(default=None, repr=False)

    def __post_init__(self):
        if self.pos is not None:          # already populated (e.g. via load)
            return
        self.rng = np.random.default_rng(self.seed)
        n = self.n_per_type * N_KINDS
        self.pos = self.rng.uniform(self.radius, self.size - self.radius, size=(n, self.dim))
        directions = self.rng.normal(size=(n, self.dim))
        directions /= np.linalg.norm(directions, axis=1, keepdims=True)
        self.vel = directions * self.speed
        self.kind = np.repeat(np.arange(N_KINDS), self.n_per_type)
        self._record()

    # -- physics ----------------------------------------------------------- #
    def _record(self):
        counts = np.bincount(self.kind, minlength=N_KINDS)
        self.history.append((self.tick, *counts.tolist()))

    def step(self):
        # move
        self.pos += self.vel
        # reflect off the walls of the cauldron
        low, high = self.radius, self.size - self.radius
        under, over = self.pos < low, self.pos > high
        self.vel[under | over] *= -1
        np.clip(self.pos, low, high, out=self.pos)

        # collisions: everyone within 2*radius of each other
        pairs = cKDTree(self.pos).query_pairs(2 * self.radius)
        if pairs:
            old = self.kind.copy()               # freeze kinds so a tick can't cascade
            for i, j in sorted(pairs):           # sorted → deterministic resolution
                a, b = old[i], old[j]
                if a == b:                       # kin recognise kin: just bounce apart
                    self.vel[i], self.vel[j] = self.vel[j].copy(), self.vel[i].copy()
                elif beats(a, b):
                    self.kind[j] = a
                else:                            # b beats a
                    self.kind[i] = b
        self.tick += 1
        self._record()

    def run(self, ticks: int, progress: bool = True, capture_every: int | None = None):
        it = range(ticks)
        if progress:
            try:
                from tqdm import tqdm
                it = tqdm(it, desc="brewing", unit="tick")
            except ImportError:
                pass
        for _ in it:
            self.step()
            if capture_every and self.tick % capture_every == 0:
                self.frames.append((self.tick, self.pos.copy(), self.kind.copy()))
        return self

    # -- results ----------------------------------------------------------- #
    def populations_df(self):
        import pandas as pd
        cols = ["tick"] + [p.name for p in POTIONS]
        return pd.DataFrame(self.history, columns=cols).set_index("tick")

    def counts(self):
        return np.bincount(self.kind, minlength=N_KINDS)

    def winner(self):
        """Return the sole surviving potion kind, or ``None`` if still contested."""
        alive = np.flatnonzero(self.counts())
        return int(alive[0]) if len(alive) == 1 else None

    def leader(self):
        return int(np.argmax(self.counts()))

    # -- the lab journal (save / resume) ----------------------------------- #
    def save(self, path: str):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        blob = {
            "params": dict(n_per_type=self.n_per_type, dim=self.dim, size=self.size,
                           radius=self.radius, speed=self.speed, seed=self.seed),
            "pos": self.pos, "vel": self.vel, "kind": self.kind,
            "tick": self.tick, "history": self.history,
            "rng_state": self.rng.bit_generator.state,
        }
        with open(path, "wb") as fh:
            pickle.dump(blob, fh)

    @classmethod
    def load(cls, path: str) -> "Brawl":
        with open(path, "rb") as fh:
            blob = pickle.load(fh)
        self = cls(**blob["params"], pos=blob["pos"], vel=blob["vel"],
                   kind=blob["kind"], tick=blob["tick"], history=blob["history"])
        self.rng = np.random.default_rng()
        self.rng.bit_generator.state = blob["rng_state"]   # bit-identical resume
        return self


# --------------------------------------------------------------------------- #
#  Drawings & charts                                                          #
# --------------------------------------------------------------------------- #
def plot_cycle(path: str | None = None):
    """The Law of the Brawl as a 3-node directed cycle (networkx + matplotlib)."""
    import matplotlib.pyplot as plt
    import networkx as nx

    g = nx.DiGraph()
    for t, p in enumerate(POTIONS):
        g.add_node(t, label=f"{p.emoji} {p.element}")
    for t, p in enumerate(POTIONS):
        g.add_edge(t, (t + 1) % N_KINDS, verb=p.verb)

    pos = nx.circular_layout(g)
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    nx.draw_networkx_nodes(g, pos, node_color=COLORS, node_size=3200, ax=ax)
    nx.draw_networkx_labels(g, pos, labels=nx.get_node_attributes(g, "label"),
                            font_size=11, font_color="white", font_weight="bold", ax=ax)
    nx.draw_networkx_edges(g, pos, ax=ax, node_size=3200, width=2.5,
                           arrowsize=28, connectionstyle="arc3,rad=0.18",
                           edge_color="#555")
    nx.draw_networkx_edge_labels(
        g, pos, edge_labels=nx.get_edge_attributes(g, "verb"),
        font_size=10, label_pos=0.5, ax=ax,
        bbox=dict(boxstyle="round", fc="white", ec="none", alpha=0.8))
    ax.set_title("⚗️  The Law of the Brawl  ⚗️", fontsize=14, fontweight="bold")
    ax.axis("off")
    fig.tight_layout()
    if path:
        fig.savefig(path, dpi=120, bbox_inches="tight")
    return fig


def plot_populations(brawl: "Brawl", path: str | None = None):
    """Stacked-area chart of the potion populations over the whole brawl."""
    import matplotlib.pyplot as plt

    df = brawl.populations_df()
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.stackplot(df.index, [df[p.name] for p in POTIONS],
                 labels=[f"{p.emoji} {p.name}" for p in POTIONS],
                 colors=COLORS, alpha=0.9)
    ax.set_xlim(df.index.min(), df.index.max())
    ax.set_ylim(0, df.iloc[0].sum())
    ax.set_xlabel("tick"); ax.set_ylabel("bottles on the floor")
    ax.set_title("Fortunes of the Brawl", fontsize=13, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False)
    fig.tight_layout()
    if path:
        fig.savefig(path, dpi=120, bbox_inches="tight")
    return fig


def render_gif(brawl: "Brawl", path: str, fps: int = 20):
    """Top-down animation of the captured frames → an animated GIF (imageio)."""
    import imageio.v2 as imageio
    import matplotlib.pyplot as plt

    if not brawl.frames:
        raise ValueError("no frames captured — run(..., capture_every=k) first")

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    images = []
    for tick, pos, kind in brawl.frames:
        fig, ax = plt.subplots(figsize=(5, 5), dpi=90)
        ax.scatter(pos[:, 0], pos[:, 1], c=[COLORS[k] for k in kind],
                   s=90, edgecolors="white", linewidths=0.5)
        ax.set_xlim(0, brawl.size); ax.set_ylim(0, brawl.size)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
        ax.set_title(f"tick {tick}", fontsize=11)
        fig.tight_layout(pad=0.4)
        fig.canvas.draw()
        images.append(np.asarray(fig.canvas.buffer_rgba()).copy())
        plt.close(fig)
    imageio.mimsave(path, images, fps=fps, loop=0)
    return path


def plotly_scene(brawl: "Brawl"):
    """Interactive 3-D scene of the brawl with a Play button (for the notebook)."""
    import plotly.graph_objects as go

    if not brawl.frames:
        raise ValueError("no frames captured — run(..., capture_every=k) first")

    def scatter(pos, kind):
        z = pos[:, 2] if brawl.dim >= 3 else np.zeros(len(pos))
        return go.Scatter3d(
            x=pos[:, 0], y=pos[:, 1], z=z, mode="markers",
            marker=dict(size=5, color=[COLORS[k] for k in kind]),
            hoverinfo="skip", showlegend=False)

    frames = [go.Frame(data=[scatter(p, k)], name=str(t)) for t, p, k in brawl.frames]
    t0, p0, k0 = brawl.frames[0]
    fig = go.Figure(data=[scatter(p0, k0)], frames=frames)
    ax = dict(range=[0, brawl.size], showbackground=True, backgroundcolor="#1a1420")
    fig.update_layout(
        title="⚗️ The Alchemist's Shop Floor ⚗️",
        template="plotly_dark", height=640,
        scene=dict(xaxis=ax, yaxis=ax, zaxis=ax, aspectmode="cube"),
        updatemenus=[dict(type="buttons", showactive=False, x=0.05, y=0.05,
            buttons=[dict(label="▶ Brew", method="animate",
                          args=[None, dict(frame=dict(duration=60, redraw=True),
                                           fromcurrent=True)])])])
    return fig


# --------------------------------------------------------------------------- #
#  The command-line spectacle                                                 #
# --------------------------------------------------------------------------- #
HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "output")
JOURNAL = os.path.join(OUTPUT, "lab_journal.pkl")


def main(ticks: int = 300, capture_every: int = 3):
    import matplotlib
    matplotlib.use("Agg")            # headless: we only ever save figures, never .show()
    import matplotlib.pyplot as plt  # noqa: F401  (ensures the Agg backend is bound)

    import pyfiglet
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel

    console = Console()
    console.print(f"[bold magenta]{pyfiglet.figlet_format('Potion Brawl', font='slant')}[/]")

    os.makedirs(OUTPUT, exist_ok=True)

    # Resume the lab journal if the former you left one behind.
    if os.path.exists(JOURNAL):
        brawl = Brawl.load(JOURNAL)
        console.print(Panel.fit(
            f"📜 Found a lab journal — resuming the brew at [bold]tick {brawl.tick}[/].\n"
            f"   (Delete [italic]output/lab_journal.pkl[/] to start a fresh brawl.)",
            border_style="green"))
    else:
        brawl = Brawl()
        console.print(Panel.fit(
            "🧪 No journal found — mixing a [bold]fresh[/] batch of potions.",
            border_style="cyan"))

    start_tick = brawl.tick
    brawl.run(ticks, progress=True, capture_every=capture_every)

    # Populations table
    counts = brawl.counts()
    table = Table(title=f"The floor after {brawl.tick} ticks", title_style="bold")
    table.add_column("Potion"); table.add_column("Bottles", justify="right")
    for p, c in zip(POTIONS, counts):
        table.add_row(f"{p.emoji} {p.name}", str(int(c)))
    console.print(table)

    # Charts + animation + journal
    plot_cycle(os.path.join(OUTPUT, "law_of_the_brawl.png"))
    plot_populations(brawl, os.path.join(OUTPUT, "populations.png"))
    gif = render_gif(brawl, os.path.join(OUTPUT, "brawl.gif"))
    brawl.save(JOURNAL)

    won = brawl.winner()
    if won is not None:
        verdict = f"🏆 [bold]{POTIONS[won].emoji} {POTIONS[won].name}[/] has flooded the lab!"
    else:
        lead = POTIONS[brawl.leader()]
        verdict = (f"⚔️  Still contested — [bold]{lead.emoji} {lead.name}[/] leads. "
                   f"Run me again to brew {ticks} more ticks from tick {brawl.tick}.")
    with open(os.path.join(OUTPUT, "victor.txt"), "w") as fh:
        fh.write(f"tick={brawl.tick} counts={counts.tolist()} winner={won}\n")

    console.print(Panel.fit(
        f"{verdict}\n\n"
        f"Brewed ticks [bold]{start_tick} → {brawl.tick}[/].\n"
        f"🎞  {os.path.relpath(gif, HERE)}   📈 output/populations.png   "
        f"🔁 output/law_of_the_brawl.png\n"
        f"📜 Journal saved to output/lab_journal.pkl — [italic]cp this folder + "
        f"requirements.txt anywhere and resume.[/]",
        title="⚗️  brew complete  ⚗️", border_style="magenta"))


if __name__ == "__main__":
    main()
