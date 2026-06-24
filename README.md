# RF Coding Bootcamp 2026 — DARC Dungeon

> **Stanford GSB DARC · Pre-doctoral Researcher Training · 4 days · Hands-on**

You are a pre-doctoral researcher at Stanford GSB. You have four days to learn the tools that serious computational researchers use every day: the command line, the Yens cluster, SLURM, GPU jobs, LLM APIs, and how to document and scale your work.

The course is structured as a dungeon game. Each day is a floor. Each hands-on block is a room. You earn skills by completing main quests, unlock optional depth with side quests, and advance to the next floor by passing a Boss Gate — a real deliverable you commit to GitHub.

**Everyone clears all four floors. The real competition is who reaches the highest level — main quests and side quests earn XP, XP drives your level.**

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

### Floor 2 — The Alchemist's Lab *(Day 2, ~3h 15min)*
> *Transmutation in progress. Turn raw text into structured data. Keep your secrets secret.*

- **JupyterHub:** run code on cluster hardware from a browser; connect your venv as a kernel
- **Python environments:** create and manage `venv`; never break another project's dependencies again
- **Stanford AI Playground:** why it exists, what data governance it provides, how it differs from a personal API key
- **Secrets management:** `.env`, `python-dotenv`, `.gitignore` — what leaves your machine on every API call
- **Claude Code:** AI-assisted coding as a research tool; when to trust it, when to verify
- **LLM API calls:** call any OpenAI-compatible API from Python; extract structured data with Pydantic
- **Cost intuition:** when to use `grep` instead of GPT-4; how to estimate cost before scaling
- **`screen`:** run a script that keeps going after you close your laptop

**Boss Gate 2:** Run 5 earnings call transcripts through the LLM, extract structured sentiment data, commit as JSON.

---

### Floor 3 — The SLURM Mines *(Day 3, ~3 hrs)*
> *Deep in the mountain, the forges never sleep. You describe the work; the foreman assigns the crew.*

- **Why batch scheduling:** see real resource contention live on the Yens before writing a single script
- **Resource estimation:** measure what your script actually costs in cores, memory, and time — before requesting it
- **SLURM scripts:** write `sbatch` scripts from scratch; understand every directive
- **Job monitoring:** `squeue`, `scancel`, `sacct` — track and audit jobs without staring at a terminal
- **Job arrays:** run the same script on 100 inputs in parallel with one command
- **Combining outputs:** merge 100 JSON results into one clean CSV
- **Documentation:** write a README while the code is fresh — treat it as a research artifact

**Boss Gate 3:** Process 100 SEC filings in parallel via a SLURM job array, merge the results into a CSV, write a README. Commit everything.

---

### Floor 4 — The GPU Fortress *(Day 4, ~2h 40min)*
> *The walls hum with tensor cores. Here you run your first GPU job, summon a local LLM, and learn what it means to do this work responsibly.*

- **GPU landscape:** A30 / A40 / H200 on the Yens — what each is good for, how to request one
- **GPU jobs:** `--gres=gpu:1`, `nvidia-smi` inside a job, why model size matters
- **Ollama:** pull and run a local LLM on cluster hardware; the OpenAI-compatible interface
- **Local vs. cloud APIs:** Ollama (on Yens) vs. Stanford AI Playground vs. third-party — same Python code, different `base_url`; privacy and cost trade-offs
- **Privacy and data governance:** the 3-bucket rule (public / restricted / PII); when cloud APIs are off-limits; classify your own research datasets
- **Agent failure modes:** hallucination at scale, runaway loops, prompt injection, irreversibility — name them before they appear in your pipeline

**Boss Gate 4:** Swap your Day 3 pipeline to the Ollama endpoint, compare outputs against the cloud API, update your README, commit.

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

### Step 2 — Enable GitHub Pages on your fork

In your fork, go to **Settings → Pages → Source → GitHub Actions → Save**.

Your personal dungeon site will be live at:

```
https://YOUR-USERNAME.github.io/rf-bootcamp-2026/
```

The first build takes ~2 minutes. After that, every push to `main` rebuilds automatically.

### Step 3 — Clone your fork to the Yens

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
| **Gate 3** | `results/great_scroll_sweep.csv` · `results/failed_tasks.txt` · `README.md` | Floor 4 — The GPU Fortress |
| **Gate 4** | `results/comparison.csv` · `results/privacy_ruling.md` · updated `README.md` | All floors cleared ⚔️ |

The grader checks that the files exist and contain valid data — it does not grade quality. The goal is to prove you ran the pipeline, not that it was perfect.

---

## Leaderboard

The leaderboard at `/leaderboard/` ranks students by:
1. **Level** — each completed main quest or side quest earns 1 XP; XP total determines level (max Level 10 — Archmage at 73 XP)
2. **Boss Gates cleared** (tiebreaker) — everyone should reach 4

To update your position: open the **Quest Log** widget (bottom-left of any dungeon page) → **Sync to leaderboard** → save `quest_log.json` to your repo root → commit and push. The grader updates your ranking automatically.

## Chests and Weapons

Every room has optional **Side Quests** — one-line challenges you figure out yourself (no walkthrough). Completing one earns a named **Weapon**: a skill that pays off later in the course.

You don't need to complete any side quests to pass Boss Gates. But every main quest and side quest earns **XP**, and XP drives your **Level**. All main quests only → Level 4 Journeyman. Every side quest complete → 73 XP → Level 10 Archmage, fully equipped researcher.

---

## Instructor Setup

### Before Day 1 — Grimoire

Students download the grimoire zip directly to their laptops at the start of Day 1 (Grimoire Vault exercise). Generate and host it before class:

**1. Generate the grimoire:**
```bash
cd /scratch/shared
git clone https://github.com/gsbdarc/rf-bootcamp-2026.git
cd rf-bootcamp-2026
python scripts/generate_grimoire.py --seed 2026 --count 300
# creates grimoire/ with ~300 .spell files
zip -r /scratch/shared/rf_bootcamp_2026/grimoire.zip grimoire/
ml rclone
rclone copy /scratch/shared/rf_bootcamp_2026/grimoire.zip <shared-space on G drive>
```

**2. Get the shareable link:**
- Open Google Drive, find `grimoire.zip`
- Set sharing to **Anyone with the link → Viewer**
- Copy the shareable link

**3. Share on Day 1:**
Paste the Google Drive link in the class chat when students reach the Grimoire Vault room. They download and unzip on their local machine before SSHing to the Yens.

> The download link also needs to be added to the Grimoire Vault page (`docs/day1/grimoire-vault.md`) before class — search for `YOUR_GDRIVE_LINK` and replace it.

---

### Before Day 1 — Yens staging

Stage the grimoire and Boss Gate vault on the Yens:

```bash
# Copy grimoire to shared scratch for the Scroll Transfer exercise
cp -r grimoire/ /scratch/shared/rf_bootcamp_2026/grimoire/

# Stage the Boss Gate 1 vault (hidden spell files)
# Place the target file in: /scratch/shared/rf_bootcamp_2026/vault/
```

---

### General notes

- The main course site (`gsbdarc.github.io/rf-bootcamp-2026`) is the read-only instructor reference — students work on their own forks
- `docs/_data/progress.yml` tracks which floors are unlocked; the grader commits updates automatically on each student's fork
- Grader source: `scripts/check_boss_gates.py` — stdlib only, no dependencies
