# ⚗️ Potion Brawl — a love letter to virtual environments

Three enchanted potions bounce around the alchemist's shop floor. When two
collide, the stronger reagent transmutes the weaker into its own kind — it's
rock-paper-scissors with bottles:

> 🔴 **Emberfury** *scorches* 🟢 **Verdant** *drinks* 🔵 **Tide** *douses* 🔴 **Emberfury** …

Left to brew, one potion eventually floods the whole lab. You get an animated
GIF of the bottles bouncing, a stacked-area chart of the war, an interactive
3-D scene, and — the whole point — a demonstration of **why a virtual
environment is the greatest trick in the alchemist's book.**

---

## Why this exists

This brawl leans on a *shelf full* of reagents — `numpy`, `scipy`, `matplotlib`,
`plotly`, `networkx`, `imageio`, `rich`, `pyfiglet`, and more. On your bare
system that's a recipe for "it works in my lab but nowhere else." A **venv** wards
off that curse:

- **The venv** is a sealed laboratory — reagents you summon inside it never leak
  out and contaminate your other quests, and the cluster's system Python never
  contaminates *you*.
- **`requirements.txt`** is the *recipe scroll* — hand it to any alchemist and
  they can reconstitute the exact same shelf of reagents.
- You **cannot** just copy someone's `.venv/` folder around (the shared lab's
  `former_apprentice/.venv/` is the cautionary tale — its Python symlink points
  at an account that isn't yours, so it's dead on arrival). You *rebuild* from
  the scroll instead.

## Build the lab

Use the cluster's system Python (the same `/usr/bin/python3` the Venv Forge uses):

```bash
cd potion_brawl
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# make this venv available to Jupyter as its own kernel
python -m ipykernel install --user --name potion-brawl --display-name "Potion Brawl (venv)"
```

## Brew

```bash
python potion_brawl.py
```

You'll get a `POTION BRAWL` banner, a progress bar, a populations table, and
these artifacts in `output/`:

| file | what it is |
|------|------------|
| `brawl.gif` | top-down animation of the bouncing brawl |
| `populations.png` | stacked-area chart of the war over time |
| `law_of_the_brawl.png` | the 3-potion cycle diagram |
| `lab_journal.pkl` | the **save state** (positions, velocities, RNG — everything) |
| `victor.txt` | the tick count + final tally |

Prefer the story with pictures? Open **`the_alchemists_lab.ipynb`** and pick the
**"Potion Brawl (venv)"** kernel, then *Kernel → Restart & Run All*.

## The punchline: pick up your work in a brand-new lab

The brawl writes a **lab journal**. Run it once, then `cp` the *code* and the
*recipe scroll* to a lab that has never seen your venv, rebuild the reagents,
and continue the exact same brew:

```bash
cp -r potion_brawl ~/a_new_lab          # code + requirements.txt + output/lab_journal.pkl
cd ~/a_new_lab
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt         # the scroll rebuilds the shelf
python potion_brawl.py                  # 📜 "resuming the brew at tick 300"
```

Because the journal restores the random-number generator's state too, the
resumed brawl is **bit-for-bit identical** to one that never paused. That's
reproducibility you can *see*: a fresh directory, a fresh machine even, and the
work simply continues.

> Run `python potion_brawl.py` again (same folder) and it resumes another 300
> ticks. Delete `output/lab_journal.pkl` to start a fresh batch.

## The truly reproducible scroll

The pinned `requirements.txt` here lists the top-level reagents. After building,
capture the *entire* transitive tree the way the assignment teaches:

```bash
pip freeze > requirements.lock.txt
```

That lock file is the real "any alchemist, any lab, same brew" guarantee. ⚗️
