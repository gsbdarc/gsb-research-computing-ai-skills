---
layout: default
title: "The Ticket Rail"
parent: "Day 3 — The Hearth"
nav_order: 7
permalink: /day3/ticket-rail/
---

# The Ticket Rail

<div data-room-id="d3-foremans-desk"></div>

*You step up to the rail. A blank slip of parchment waits on the counter — the order form, the thing that stands in for you when you're not in the kitchen. It has to contain everything: the recipe, the station you need, the time limit, the resources. The head chef will read it cold, without context. If it's vague, it gets rejected. If it's wrong, the job fails. Write it right the first time.*

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
#SBATCH --time=<HH:MM:SS>
#SBATCH --mem=<RAM>
#SBATCH --cpus-per-task=<cores>
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

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="submit"> I submitted with sbatch and my job entered the queue (I have a JOBID)</label>

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

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="cancel"> I cancelled my job with scancel and confirmed it left the queue</label>

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
