---
layout: default
title: "The Ticket Rail"
parent: "Day 3 — The SLURM Mines"
nav_order: 7
permalink: /day3/foremans-desk/
---

# The Ticket Rail

<div data-room-id="d3-foremans-desk"></div>

---

## Main Exercise — Write and Submit a SLURM Job

{: .important }
> **Exercise:** Write a SLURM job script from scratch, understand every directive, and submit your first batch job.

**Create `jobs/extract.slurm`:**

```bash
mkdir -p jobs logs
```

```bash
#!/bin/bash
#SBATCH --job-name=form3_extract        # appears in squeue
#SBATCH --output=logs/extract_%j.out    # %j = job ID
#SBATCH --error=logs/extract_%j.err     # separate stderr log
#SBATCH --time=00:10:00                 # max wall time HH:MM:SS — set from your Scales measurement
#SBATCH --mem=2G                        # memory request — set from your Scales measurement
#SBATCH --cpus-per-task=1              # CPU cores
#SBATCH --partition=normal

# --- Setup ---
echo "Job started on $(hostname) at $(date)"
cd ~/rf-bootcamp-2026
source .venv/bin/activate

# --- Your actual work ---
python scripts/extract_form_3_batch.py

echo "Job finished at $(date)"
```

{: .warning }
> **Your SLURM script must set up its own environment.** When SLURM runs your job, it starts a fresh shell on a compute node — your virtual environment is not active, your working directory is not set, and no modules are loaded. Every command you need must be in the script: `cd` to the right directory, `source .venv/bin/activate` before calling Python, and any `module load` commands you rely on.

**Test interactively on the Yens before submitting** — run the commands directly on an interactive node to confirm there are no errors before handing it to the head chef:

```bash
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python scripts/extract_form_3_batch.py
```

If it completes without errors, you're ready to submit.

When the interactive test passes — put a **🟢 green sticky** on your laptop. If it errors, put up a **🔴 red sticky** and fix it before submitting.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="main"> I wrote extract.slurm and the interactive test passed without errors</label>

**Submit:**
```bash
sbatch jobs/extract.slurm
# Submitted batch job 12345678
```

Note your job ID — you'll need it in The Watch Tower.

{: .note }
> **While your job runs:** Head to [The Chronicle](../chronicle/) now and write your README — the job may sit in the queue for a few minutes. Come back to [The Watch Tower](../watch-tower/) once `sacct` shows your job as `COMPLETED`.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="submit"> I submitted with sbatch and my job entered the queue (I have a JOBID)</label>

---

## Optional Exercises

{: .note }
> Finished early? Try this.

**Bonus 1 — Email notifications**

Add these two lines to your job script (right after the `#SBATCH --partition` line):

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

Re-submit with `sbatch jobs/extract.slurm`. `ALL` sends an email when the job starts, ends, and fails — including a utilization summary so you can see how much CPU and RAM the job actually used.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side1"> I added email notifications to my job script</label>
