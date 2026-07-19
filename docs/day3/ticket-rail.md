---
layout: default
title: "The Ticket Rail"
parent: "Day 3 — The Hearth"
nav_order: 7
permalink: /day3/ticket-rail/
---

# The Ticket Rail

<div data-room-id="d3-foremans-desk"></div>

---

## Main Exercise — Write a SLURM Script

{: .important }
> **Exercise:** Build a SLURM job script line by line to run your Form 3 extraction script on a compute node.

**Create the file:**

```bash
mkdir -p slurm logs
```

Open `slurm/extract_form_3_one_file.slurm` in your editor.

---

**Step 1 — The shebang**

Every shell script starts here:

```bash
#!/bin/bash
```

---

**Step 2 — SBATCH directives**

These are instructions to the head chef. Fill in each placeholder using the measurements you took in The Scales:

```bash
#SBATCH --job-name=<job-name>
#SBATCH --output=logs/<output-file>_%j.out
#SBATCH --time=<HH:MM:SS>            # e.g. 00:10:00
#SBATCH --mem=<RAM>                  # e.g. 4G
#SBATCH --cpus-per-task=<cores>      # e.g. 2
```

---

**Step 3 — Set up the environment**

```bash
# Navigate to your project
cd $HOME/rf-bootcamp-2026

# Activate your virtual environment
source .venv/bin/activate
```

---

**Step 4 — Run your script**

```bash
python scripts/extract_form_3_one_file.py
```

Save the file.

{: .warning }
> **SLURM starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

{: .note }
> **Three things worth understanding before you submit:**
> - `%j` in the output filename gets replaced with the job ID — so each run writes to its own log file instead of overwriting the last one.
> - The `logs/` directory must exist before the job runs — SLURM won't create it for you. That's why `mkdir -p logs` comes first.
> - Paths in the script are resolved on the compute node, not your login node. Absolute paths (`$HOME/...`) are safer than relative ones.

When your script is complete — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="main"> I wrote extract_form_3_one_file.slurm and understand every line</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## Submit

```bash
sbatch slurm/extract_form_3_one_file.slurm
# Submitted batch job 12345678
```

Monitor the queue:

```bash
squeue --me
```

---

## Cancel

```bash
scancel JOBID
```

Confirm it is gone:

```bash
squeue --me
```

{: .note }
> You may briefly see your job's status change to **CG** (completing) before it disappears from the queue — that's normal, not an error.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="submit"> I submitted with sbatch, confirmed it in the queue, and cancelled it with scancel</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.submit` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## Add Email Notifications

Open `slurm/extract_form_3_one_file.slurm` and add these two lines with your other `#SBATCH` directives:

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

`ALL` sends an email when the job starts, ends, and fails — including a utilization summary showing how much CPU and RAM it actually used.

Resubmit:

```bash
sbatch slurm/extract_form_3_one_file.slurm
```

Once your job runs, check your inbox. You should receive two emails: one when the job **starts** and one when it **ends** — the end email includes a utilization summary showing how much CPU time and memory the job actually used.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side1"> I added email notifications and resubmitted</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## Side Quest — Go Interactive Instead of Batch

Everything so far has been batch submission — write a script, `sbatch` it, wait. SLURM also supports an interactive allocation on a dedicated node, useful for debugging without fighting other users for resources:

```bash
srun --pty --cpus-per-task=2 --mem=4G --time=00:30:00 bash
```

Once it drops you into a shell on your allocated node, run your script there directly.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side2"> I requested an interactive allocation with srun --pty and ran my script there</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side2` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

**Side Quest — Chain Two Jobs**

Real pipelines are often more than one step. Submit a second job that only starts if your first one succeeds:

```bash
sbatch --dependency=afterok:JOBID slurm/extract_form_3_one_file.slurm
```

Replace `JOBID` with the job ID of a job you already submitted. Confirm with `squeue --me` that the new job shows as pending until the first one completes.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side3"> I chained two SLURM jobs with --dependency=afterok</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.
