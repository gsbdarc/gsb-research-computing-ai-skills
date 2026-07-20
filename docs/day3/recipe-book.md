---
layout: default
title: "Documenting Your Pipeline"
parent: "Day 3 — Cluster Computing"
nav_order: 9
permalink: /day3/recipe-book/
---

# Documenting Your Pipeline

<div data-room-id="d3-chronicle"></div>

---

## Exercise — Write a README

Write your README while the code is still fresh — before you close the terminal. Your memory of every flag and design choice is sharpest right now.

{: .important }
> **Task:** Write a `README.md` for your Day 3 pipeline.

{: .note }
> This is the same `README.md` you started in Exploring Cluster Usage Data and added to in Profiling Resource Usage — keep those sections and add this pipeline writeup alongside them, don't start a new file.

Create `README.md` in your repo root (or a `day3/` subdirectory):

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

## What this does

Extracts insider name, role, and transaction date from SEC Form 3 filings
using the Stanford AI API via a SLURM batch job.

## How to run

### Prerequisites
- Access to the Stanford Yens cluster
- Stanford AI API key in `.env`
- Python venv at `.venv/` (see Day 2 setup)

### Steps
# 1. Submit the batch job
sbatch slurm/extract_form_3_one_file.slurm

# 2. Monitor
squeue --me
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS

# 3. Check output
cat logs/extract_JOBID.out

## Outputs

- `logs/extract_JOBID.out` — extraction results
- `logs/extract_JOBID.err` — error log if any

## Data

Input: SEC Form 3 filings from EDGAR (public domain).

## Known limitations

- Non-standard filing formats may produce empty fields
```

{: .note }
> You will update this README in Boss Gate 4 when you scale with a job array.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="main"> README written and covers what the script does, how to run it, and where output lands</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-chronicle.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

---

## Optional practice

{: .note }
> Finished early? Try one or both of these.

**Optional practice — Have Claude Stress-Test Your README**

Ask Claude Code to read your README as if it were a labmate seeing this pipeline for the first time, and to flag anything that would stop them from rerunning it without asking you a question. Fix at least one thing it flags.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="side1"> I had Claude critique my README as a first-time reader and fixed at least one issue it flagged</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-chronicle.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Optional practice — Explain It to Your PI**

Write 2-3 sentences explaining what this pipeline does for a non-technical reader — your PI, your committee, an IRB reviewer. No SLURM, no flags, no jargon.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="side2"> I wrote a plain-language explanation of my pipeline for a non-technical reader</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-chronicle.side2` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>
