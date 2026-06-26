# RF Coding Bootcamp 2026 — DARC Dungeon

> **Stanford GSB DARC · Pre-doctoral Researcher Training · 4 days · Hands-on**

You are a pre-doctoral researcher at Stanford GSB. You have four days to learn the tools that serious computational researchers use every day: the command line, the Yens cluster, SLURM, GPU jobs, LLM APIs, and how to document and scale your work.

The course is structured as a dungeon game. Each day is a floor. Each hands-on block is a room. You earn skills by completing main quests, unlock optional depth with side quests, and advance to the next floor by passing a Boss Gate — a real deliverable you commit to GitHub.

**Everyone clears all four floors. The real competition is who reaches the highest level — every completed quest adds to your Quest Log, and your Quest Log total drives your level.**

At any point, open your Quest Log (bottom-left of any page), click **Sync to leaderboard**, save the file, and push it. Your position on the [leaderboard](https://gsbdarc.github.io/rf-bootcamp-2026/leaderboard/) updates automatically.

**Reference site:** https://gsbdarc.github.io/rf-bootcamp-2026/
**Leaderboard:** https://gsbdarc.github.io/rf-bootcamp-2026/leaderboard/

---

## What You'll Learn

### Floor 1 — The Gatehouse *(Day 1, ~3 hrs)*
> *The outer wall. Learn to move through a Unix system, connect to a remote server, and never lose your work.*

- **Command line:** `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv` — navigate any Unix system without clicking
- **File wrangling:** sort hundreds of files with wildcards; think in patterns, not individual clicks
- **SSH:** connect to the Stanford Yens cluster (17 nodes, 256 cores/node); understand interactive vs. scheduled compute
- **Cluster file system:** `/home`, `/yen/projects`, `/scratch/shared` — know where data lives and why
- **Git:** fork → branch → commit → push; version-control every project from day one

**Boss Gate 1:** Find a hidden spell file buried in the shared cluster file system. Commit it.

---

### Floor 2 — The Alchemist's Lab *(Day 2)*
> *Transmutation in progress. Turn raw SEC filings into structured data. Keep your secrets secret.*

- **JupyterHub:** run code on cluster hardware from a browser; connect your venv as a kernel
- **Python environments:** `venv`, `pip`, modules, `$PATH` — manage dependencies without breaking other projects
- **Stanford AI Playground:** web GUI and API gateway; what leaves the cluster; tokens, costs, context windows
- **Secure key management:** `.env`, `python-dotenv`, `.gitignore` — keep credentials out of your code and git history
- **LLM API calls:** call any OpenAI-compatible API from Python; extract structured data with Pydantic validation
- **AI coding agents at Stanford:** data privacy and security; what context agents send; best practices for research

**Boss Gate 2:** Write a Python script that calls the LLM API, extracts structured data from one SEC filing, validates with Pydantic, and commits to your fork.

---

### Floor 3 — The SLURM Mines *(Day 3)*
> *Deep in the mountain, the forges never sleep. You describe the work; the foreman assigns the crew.*

- **SLURM (the kitchen analogy):** see live resource contention; understand why shared compute needs a scheduler
- **Resource estimation:** measure your script's wall time and memory before writing a single `#SBATCH` directive
- **Job lifecycle:** submit → queue → run → complete → logs; understand every stage
- **Job monitoring:** `squeue`, `sacct`, `scancel` — track, audit, and cancel jobs from any terminal
- **Documentation:** write a README while the details are fresh — treat it as a research artifact

**Boss Gate 3:** Submit your Day 2 LLM script as a SLURM batch job; update the README with how to run it. Commit and push.

---

### Floor 4 — The GPU Fortress *(Day 4)*
> *The walls hum with tensor cores. Scale your pipeline, claim the GPU, summon a local LLM.*

- **Job arrays:** one script, one `--array` flag, hundreds of inputs in parallel; fault-tolerant with checkpoint logs
- **GPU tiers:** A30 / A40 / H200 on the Yens — VRAM constraints, use cases, how to request one
- **Local LLMs:** Ollama on the H200; model weights on cluster hardware; nothing leaves the Yens
- **OpenAI-compatible API:** swapping `base_url` is the only code change between Ollama, AI Playground, and third-party
- **Human vs. LLM:** when to trust results at scale; validation strategies before running 10,000 jobs
- **Reproducibility:** README as the deliverable that makes a pipeline rerunnable by anyone

**Boss Gate 4:** Scale your pipeline to a 100-filing job array, swap the endpoint to Ollama, compare outputs side-by-side, finalize your README. Commit and push.

---

## Prerequisites

- A **GitHub account** — free at [github.com](https://github.com). That's it.
- No other software needed before Day 1. Everything else gets set up during class.

---

## Student Setup

### Step 1 — Fork this repository

Click **Fork** in the top-right corner of this page. GitHub creates your own copy at:

```
https://github.com/YOUR-USERNAME/rf-bootcamp-2026
```

### Step 2 — Enable GitHub Actions on your fork

GitHub disables workflows on forks by default. You have to opt in once:

In your fork, click the **Actions** tab → click **"I understand my workflows, go ahead and enable them"**.

### Step 3 — Enable GitHub Pages on your fork

In your fork, go to **Settings → Pages → Build and deployment → Source → GitHub Actions → Save**.

Your personal dungeon site will be live at:

```
https://YOUR-USERNAME.github.io/rf-bootcamp-2026/
```

The first build takes ~2 minutes. After that, every push to `main` rebuilds automatically.

### Step 4 — Clone your fork to the Yens

```bash
git clone https://github.com/YOUR-USERNAME/rf-bootcamp-2026.git
cd rf-bootcamp-2026
```

Work from this directory for all Boss Gate submissions.

---

## Unlocking Floors — How Boss Gates Work

Each floor is locked until you pass the Boss Gate from the previous floor. Here's exactly how it works:

1. **Complete the Boss Gate quest** described on the Boss Gate page for your current floor
2. **Commit the required files** to your fork's `main` branch using the exact `git commit` command shown on the page
3. **Push to GitHub:** `git push`
4. **Wait ~60 seconds** — a grader runs automatically in your fork's Actions tab
5. **Check the result:** go to your fork → **Actions** tab → look for a green ✓ or red ✗
   - Green: floor unlocked — your site will rebuild and the next floor will appear
   - Red: click the failed run to see exactly what's missing, fix it, and push again
6. **Refresh your dungeon site** after the Pages build finishes (~2 min)

| Boss Gate | Files to commit | What unlocks |
|-----------|----------------|--------------|
| **Gate 1** | `signature_spell.txt` | Floor 2 — The Alchemist's Lab |
| **Gate 2** | `results/mood_ring.json` | Floor 3 — The SLURM Mines |
| **Gate 3** | `jobs/extract.sh` · `README.md` | Floor 4 — The GPU Fortress |
| **Gate 4** | `results/great_scroll_sweep.csv` · `results/comparison.csv` · `README.md` | All floors cleared ⚔️ |

The grader checks that the files exist and contain valid data — it does not grade quality. The goal is to prove you ran the pipeline, not that it was perfect.

---

## Leaderboard

The leaderboard at `/leaderboard/` ranks students by:
1. **Level** — completing all main quests advances you through the floors; side quests push your level higher and separate the top of the leaderboard
2. **Boss Gates cleared** (tiebreaker) — everyone should reach 4

To update your position: open the **Quest Log** widget (bottom-left of any dungeon page) → **Sync to leaderboard** → save `quest_log.json` to your repo root → commit and push. The grader updates your ranking automatically.

## Chests and Weapons

Every room has optional **Side Quests** — one-line challenges you figure out yourself (no walkthrough). Completing one earns a named **Weapon**: a skill that pays off later in the course.

You don't need to complete any side quests to pass Boss Gates. But every side quest you finish pushes your level higher — that's what separates the top of the leaderboard from everyone else who cleared the main path.