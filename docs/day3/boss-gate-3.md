---
layout: default
title: "Boss Gate 3"
parent: "Day 3 — The Hearth"
nav_order: 10
permalink: /day3/boss-gate-3/
---

# Boss Gate 3

---

## Boss Gate 3 — First SLURM Submission

Submit your Day 2 LLM extraction script as a SLURM batch job:

1. Write `slurm/extract_form_3_one_file.slurm` with correct `#SBATCH` directives — time, memory, and cores based on your profiling from The Scales
2. Submit with `sbatch`; confirm the job enters the queue with `squeue --me`
3. Wait for it to complete; inspect the output with `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS`
4. Update `README.md` with SLURM instructions — how to submit, how to monitor, where the output goes
5. Commit and push:

```bash
git add slurm/extract_form_3_one_file.slurm README.md
git commit -m "Boss Gate 3: first SLURM submission complete"
git push
```

Your commit should include:
- `slurm/extract_form_3_one_file.slurm` with `#SBATCH` directives based on real profiling, not guesses
- `README.md` — what the script does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## 📊 End of Day 3 — Sync Your Progress

Let your instructor see where you landed today. Takes 2 minutes.

**Step 1 — Export your quest log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/rf-bootcamp-2026`) → **Add file** → **Upload files** → drag `quest_log.json` in → **Commit changes** to main.

The leaderboard updates within 2 minutes. Your instructor can see how many quests you completed and whether you cleared the Boss Gate.

---

## Skills This Boss Gate Tests

- Write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- Submit a job and confirm it entered the queue
- Read `sacct` output and identify whether the job succeeded or failed
- Write a README clear enough that a colleague could rerun the job without asking you
- Commit and push a complete deliverable: script and documentation together
