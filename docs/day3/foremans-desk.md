---
layout: default
title: "The Foreman's Desk"
parent: "Day 3 — The SLURM Mines"
nav_order: 4
permalink: /day3/foremans-desk/
---

# The Foreman's Desk

<div data-room-id="d3-foremans-desk"></div>

*The foreman sits here and reads recipes. Every recipe specifies the same things: how many cooks, how long, which pantry section, where to log mistakes. Write a bad recipe and the kitchen ignores it. Write a good one and the kitchen runs it exactly as written, every time, without you watching.*

---

## Main Quest

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
source ~/rf_bootcamp_2026/.venv/bin/activate

# --- Your actual work ---
python3 ~/rf_bootcamp_2026/count_spells.py ~/grimoire/

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

---

## Chests

{: .chest }
> **Chest 1 — Mail Medallion:** Add `#SBATCH --mail-type=END,FAIL` and `#SBATCH --mail-user=YOUR_EMAIL` to your job script. Submit it and wait for the notification email. When is this more useful than watching `squeue`?

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="chest1"> Mail Medallion unlocked</label>

{: .chest }
> **Chest 2 — Template Tome:** Rewrite `first_job.sh` to accept the input directory as `$1` (the first argument), so you can submit `sbatch jobs/first_job.sh ~/grimoire/` and the script uses that path. This makes one script handle any input.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="chest2"> Template Tome unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Mail Medallion** — `--mail-type=END,FAIL` to get an email when your job finishes or crashes; monitor long jobs without staring at `squeue`.
>
> **Template Tome** — parameterize job scripts with `$1`, `$2` arguments; one script handles any input without editing — just change the `sbatch` command.

---

## Skills Learned

- Write a complete SLURM job script with all required directives
- Understand what each `#SBATCH` line controls: name, output path, time limit, memory, CPUs, partition
- Submit with `sbatch` and capture the job ID
- Know that the script is valid bash — you can test it locally with `bash job.sh` before submitting
