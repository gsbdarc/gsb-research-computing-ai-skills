# RF Coding Bootcamp 2026 — DARC Dungeon

> **Stanford GSB DARC · Pre-doctoral Researcher Training · 4 days · Hands-on**

A four-day hands-on course covering the command line, the Yens cluster, SLURM, GPU jobs, LLM APIs, and AI coding tools. The course runs as a dungeon game — complete rooms, earn skills, pass Boss Gates to advance floors.

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

In your fork, go to **Settings → Pages → Build and deployment → Source → select **GitHub Actions** (saves automatically).

### Step 4 — Trigger the first build

Go to **Actions → "Deploy Jekyll site to Pages" → Run workflow → Run workflow**.

Your personal dungeon site will be live at:

```
https://YOUR-USERNAME.github.io/rf-bootcamp-2026/
```

Wait ~2 minutes, then open the URL. After that, every push to `main` rebuilds automatically.

### Step 5 — Clone your fork to the Yens

```bash
git clone https://github.com/YOUR-USERNAME/rf-bootcamp-2026.git
cd rf-bootcamp-2026
```

Work from this directory for all Boss Gate submissions.

---

## How Boss Gates Work

Each floor is locked until you pass the Boss Gate from the previous floor:

1. Complete the Boss Gate quest on the Boss Gate page
2. Commit the required files to your fork's `main` branch
3. Push: `git push`
4. Wait ~60 seconds — a grader runs automatically in your fork's Actions tab
5. Green ✓ = floor unlocked; Red ✗ = click the run to see what's missing

| Boss Gate | Files to commit | What unlocks |
|-----------|----------------|--------------|
| **Gate 1** | `signature_spell.txt` | Floor 2 — The Alchemist's Lab |
| **Gate 2** | `results/mood_ring.json` | Floor 3 — The SLURM Mines |
| **Gate 3** | `slurm/extract_form_3_one_file.slurm` · `README.md` | Floor 4 — The GPU Fortress |
| **Gate 4** | `results/great_scroll_sweep.csv` · `results/comparison.csv` · `README.md` | All floors cleared ⚔️ |

---

## Prerequisites

- A **GitHub account** — free at [github.com](https://github.com). That's it.
- No other software needed before Day 1. Everything else gets set up during class.

---

## What You'll Learn

| Floor | Day | Skills |
|-------|-----|--------|
| 1 — The Gatehouse | Day 1 | CLI · SSH · Yens file system · Git · Claude Code |
| 2 — The Alchemist's Lab | Day 2 | JupyterHub · Python envs · AI Playground · Secure key management · Pydantic · AI agents & data privacy |
| 3 — The SLURM Mines | Day 3 | SLURM · Resource estimation · Job lifecycle · Job monitoring |
| 4 — The GPU Fortress | Day 4 | Job arrays · GPU tiers · Local LLMs · OpenAI-compatible API · Human vs LLM |
