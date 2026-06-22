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

## 📦 Chests

Two chests are wedged behind the foreman's filing cabinet — one hums with the promise of passive alerts, the other holds the secret to scripts that never grow stale.

{: .chest }
> **Chest 1 — Mail Medallion:** Add `#SBATCH --mail-type=END,FAIL` and `#SBATCH --mail-user=YOUR_EMAIL` to your job script. Submit it and wait for the notification email. When is this more useful than watching `squeue`?

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="chest1"> Mail Medallion unlocked</label>

{: .chest }
> **Chest 2 — Template Tome:** Rewrite `first_job.sh` to accept the input directory as `$1` (the first argument), so you can submit `sbatch jobs/first_job.sh ~/grimoire/` and the script uses that path. This makes one script handle any input.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="chest2"> Template Tome unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Mail Medallion** — `--mail-type=END,FAIL` to get an email when your job finishes or crashes; monitor long jobs without staring at `squeue`.
>
> **Template Tome** — parameterize job scripts with `$1`, `$2` arguments; one script handles any input without editing — just change the `sbatch` command.

---

## 🧠 Skills Learned

- You can write a complete, submission-ready SLURM job script from a blank file
- You can read any `#SBATCH` directive at a glance and know what it controls: name, output path, time limit, memory, CPUs, partition
- You can submit with `sbatch` and hold onto the job ID like the key it is
- You can test your script locally with `bash job.sh` before ever touching the queue — no wasted allocations, no mystery failures
