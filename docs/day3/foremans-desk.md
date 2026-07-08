---
layout: default
title: "The Foreman's Desk"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/foremans-desk/
---

# The Foreman's Desk

<div data-room-id="d3-foremans-desk"></div>

*The foreman's desk is buried under scrolls, each one a binding contract with the cluster. Every scroll specifies the same things: how many workers, how long they may toil, which shaft of the mine, where to carve the error glyphs. Forge a sloppy scroll and the mine ignores you entirely. Forge a perfect one and a hundred cores snap to attention — doing exactly your bidding, long after you've gone to sleep.*

---

## 🗡️ Main Quest

The cluster doesn't take verbal orders. You must hand it a script — a scroll that describes your job down to the last directive. Forge yours now.

{: .important }
> **Quest:** Write a SLURM job script from scratch, understand every directive, and submit your first batch job.

**Create `jobs/extract.sh`:**

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
#SBATCH --partition=normal             # which queue (ask instructor for correct partition)

# --- Setup ---
echo "Job started on $(hostname) at $(date)"
cd ~/rf-bootcamp-2026
source .venv/bin/activate

# --- Your actual work ---
python scripts/extract_form_3_batch.py

echo "Job finished at $(date)"
```

**Test before submitting** — run the script locally to catch path or venv errors before it enters the queue:

```bash
bash jobs/extract.sh
```

This runs your script exactly as SLURM would, but right now on the interactive node. If it completes without errors, you're ready to submit.

**Submit:**
```bash
sbatch jobs/extract.sh
# Submitted batch job 12345678
```

Note your job ID — you'll need it in The Watch Tower.

{: .note }
> **While your job runs:** Head to [The Chronicle](../chronicle/) now and write your README — the job may sit in the queue for a few minutes. Come back to [The Watch Tower](../watch-tower/) once `sacct` shows your job as `COMPLETED`.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="main"> Main Quest complete</label>
