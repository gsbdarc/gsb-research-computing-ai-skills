---
layout: default
title: "Boss Gate 3"
parent: "Day 3 — The SLURM Mines"
nav_order: 7
permalink: /day3/boss-gate-3/
---

# Boss Gate 3

*The Foreman steps aside and the gate swings open — but only for the researcher who can prove they've handed their pipeline to the scheduler. Not an interactive session. Not a manual run on the login node. A proper SLURM job: resourced, submitted, documented. When the output file lands in `logs/` and the README can explain what happened to anyone who wasn't there, you've crossed the threshold.*

---

## 🔑 The Challenge

{: .boss }
> **Boss Battle — The First Submission**
>
> Submit your Day 2 LLM extraction script as a SLURM batch job:
>
> 1. Write `jobs/extract.sh` with correct `#SBATCH` directives — time, memory, and partition based on your profiling from The Scales
> 2. Submit with `sbatch`; confirm the job enters the queue with `squeue -u $USER`
> 3. Wait for it to complete; inspect the output with `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS`
> 4. Update `README.md` with SLURM instructions — how to submit, how to monitor, where the output goes
> 5. Commit and push
>
> **Submit:**
> ```bash
> git add jobs/extract.sh README.md
> git commit -m "Boss Gate 3: first SLURM submission complete"
> git push
> ```
>
> **Your commit should include:**
> - The job script (`jobs/extract.sh`) with `#SBATCH` directives you measured, not guessed
> - `README.md` from The Chronicle — what the script does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## 📊 End of Day 3 — Sync Your Progress

Let your instructor see where you landed today. Takes 2 minutes.

**Step 1 — Export your quest log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/rf-bootcamp-2026`) → **Add file → Upload files** → drag `quest_log.json` in → **Commit changes** to `main`.

The leaderboard updates within 2 minutes. Your instructor can see your level, which boss gates you've cleared, and how many side quests you completed.

---

## ⚔️ Skills This Gate Tests

- You can write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- You can submit a job and confirm it entered the queue
- You can read `sacct` output and identify whether the job succeeded or failed
- You can write a README clear enough that a stranger could rerun the job without asking you
- You can commit and push a complete deliverable: script and documentation together
