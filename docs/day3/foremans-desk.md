---
layout: default
title: "The Foreman's Desk"
parent: "Day 3 — The SLURM Mines"
nav_order: 4
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

**Create `jobs/first_job.sh`:**

```bash
mkdir -p jobs
```

```bash
#!/bin/bash
#SBATCH --job-name=my_first_job         # appears in squeue
#SBATCH --output=logs/first_job_%j.out  # %j = job ID
#SBATCH --error=logs/first_job_%j.err   # separate stderr log
#SBATCH --time=00:10:00                 # max wall time HH:MM:SS
#SBATCH --mem=2G                        # memory request
#SBATCH --cpus-per-task=1              # CPU cores
#SBATCH --partition=normal             # which queue (ask instructor for correct partition)

# --- Setup ---
echo "Job started on $(hostname) at $(date)"
source ~/rf-bootcamp-2026/.venv/bin/activate

# --- Your actual work ---
python3 ~/rf-bootcamp-2026/count_spells.py ~/grimoire/

echo "Job finished at $(date)"
```

**Create the logs directory:**
```bash
mkdir -p logs
```

**Submit:**
```bash
sbatch jobs/first_job.sh
# Submitted batch job 12345678
```

Note your job ID. Check it immediately in The Watch Tower room.

{: .note }
> Every `#SBATCH` directive is just a comment to bash — the script still runs if you execute it directly with `bash jobs/first_job.sh` for testing. This is useful for debugging before submitting.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="main"> Main Quest complete</label>
