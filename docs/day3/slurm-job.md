---
layout: default
title: "Writing & Submitting a SLURM Job"
parent: "Day 3 — Cluster Computing"
nav_order: 7
permalink: /day3/slurm-job/
---

# Writing & Submitting a SLURM Job

<div data-room-id="d3-foremans-desk"></div>

---

## Exercise — Write a SLURM Script

{: .important }
> **Task:** Build a SLURM job script line by line to run your Form 3 extraction script on a compute node.

**Create the file:**

```bash
mkdir -p slurm logs
```

Open `slurm/extract_form_3_one_file.slurm` in your editor.

---

**Step 1 — The shebang**

The first line of every shell script is the **shebang**:

```bash
#!/bin/bash
```

The `#!` tells the operating system which interpreter to run the rest of the file with — here, the Bash shell at `/bin/bash`. Without it, the system doesn't know whether your script is Bash, Python, or something else. It has to be the very first line of the file.

---

**Step 2 — SBATCH directives**

These are instructions to the SLURM scheduler. Fill in each placeholder using the measurements you took in Profiling Resource Usage:

```bash
#SBATCH --job-name=<job-name>
#SBATCH --output=logs/extract_%j.out
#SBATCH --error=logs/extract_%j.err
#SBATCH --time=<HH:MM:SS>            # e.g. 00:10:00
#SBATCH --mem=<RAM>                  # e.g. 4G
#SBATCH --cpus-per-task=<cores>      # e.g. 2
```

---

**Step 3 — Set up the environment**

```bash
# Navigate to your project
cd $HOME/gsb-research-computing-ai-skills

# Activate your virtual environment
source .venv/bin/activate
```

{: .note }
> **What's already installed.** Your `.venv` was built from `requirements.txt` on Day 2. Once it's activated, any job can use these packages:
>
> | Package | Used for |
> |---|---|
> | `openai` | Calling the Stanford AI API (LLM extraction) |
> | `python-dotenv` | Loading your API key from `.env` |
> | `pydantic` | Validating and structuring the LLM output |
> | `pandas` | Tabular data |
> | `numpy` | Vectorized numerics (installed with pandas) |
> | `requests` | Downloading filings over HTTP |
> | `ipykernel` / `jupyter` | Notebook and JupyterHub kernels |
> | `matplotlib` | Plots |
>
> Need something else? `pip install` it into your `.venv` (never system-wide) and add it to `requirements.txt` so your work stays reproducible.

---

**Step 4 — Run your script**

```bash
python scripts/extract_form_3_one_file.py
```

Save the file.

{: .warning }
> **SLURM starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

{: .note }
> **What the log files are, and other things worth knowing before you submit:**
> - A batch job has **no terminal** — you're not watching it run. So SLURM redirects everything your script would normally print to the screen: normal output goes to the **`--output` (`.out`) file**, and error messages/tracebacks go to the **`--error` (`.err`) file**. Those two files are how you see what your job did and debug it when it fails.
> - `%j` gets replaced with the job ID, so each run writes its own `logs/extract_<jobid>.out` and `.err` instead of overwriting the last.
> - The `logs/` directory must exist before the job runs — SLURM won't create it for you. That's why `mkdir -p logs` comes first.
> - Paths in the script are resolved on the compute node, not your login node. Absolute paths (`$HOME/...`) are safer than relative ones.

When your script is complete — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="main"> I wrote extract_form_3_one_file.slurm and understand every line</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

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

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.submit` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

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

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

---

## Optional practice — Go Interactive Instead of Batch

Everything so far has been batch submission — write a script, `sbatch` it, wait. SLURM also supports an interactive allocation on a dedicated node, useful for debugging without fighting other users for resources:

```bash
srun --pty --cpus-per-task=2 --mem=4G --time=00:30:00 bash
```

Once it drops you into a shell on your allocated node, run your script there directly.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side2"> I requested an interactive allocation with srun --pty and ran my script there</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side2` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Optional practice — Chain Two Jobs**

Real pipelines are often more than one step. Submit a second job that only starts if your first one succeeds:

```bash
sbatch --dependency=afterok:JOBID slurm/extract_form_3_one_file.slurm
```

Replace `JOBID` with the job ID of a job you already submitted. Confirm with `squeue --me` that the new job shows as pending until the first one completes.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side3"> I chained two SLURM jobs with --dependency=afterok</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Optional practice — Watch Your Job on Its Node**

A running batch job has a compute node all to itself — and while it's running, you can SSH in and watch it work. First find out where it landed:

```bash
squeue --me
```

The `NODELIST` column shows the node your job is on (e.g. `yen10`). SSH to that node and watch your job's processes live:

```bash
ssh SUNetID@yen10.stanford.edu   # use your job's actual node
htop -u $USER                    # or: top -u $USER
```

You'll see your Python process using the CPU and RAM you requested in the script. Press `q` to quit `htop`, then `exit` to leave the node. This only works while the job is running, and only on a node where you actually have a job — you can't SSH to arbitrary compute nodes.

<label class="quest-check"><input type="checkbox" data-room="d3-foremans-desk" data-key="side4"> I found my job's node with squeue and watched it run live with htop</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-foremans-desk.side4` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>
