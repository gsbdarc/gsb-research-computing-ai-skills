---
layout: default
title: "Writing & Submitting a SLURM Job"
parent: "Day 3 — Cluster Computing"
nav_order: 7
permalink: /day3/slurm-job/
---

# Writing & Submitting a SLURM Job

<div data-room-id="d3-slurm-job"></div>

---

## Main quest — Write a SLURM Script

{: .important }
> **Task:** Build a SLURM job script line by line to run your Form 3 extraction script on a compute node.

**Create the file:**

Your repo already has a `slurm/` folder (with a few prepared scripts). Just make sure a `logs/` folder exists for job output:

```bash
mkdir -p logs
```

Create a new file `slurm/extract_form_3_batch.slurm` and open it in your editor — you'll build it up line by line below.

{: .note }
> No preferred terminal editor? You can create it right in **JupyterHub**: in the file browser, open the `slurm/` folder, click **+ New → Text File** (or **File → New → Text File**), edit it in the browser, then **rename** the file to `extract_form_3_batch.slurm` and save with `Cmd/Ctrl+S`.

---

**Step 1 — The shebang**

The first line of every shell script is the **shebang**:

```bash
#!/bin/bash
```

The `#!` tells the operating system which interpreter to run the rest of the file with — here, the Bash shell at `/bin/bash`. Without it, the system doesn't know whether your script is Bash, Python, or something else. It has to be the very first line of the file.

---

**Step 2 — SBATCH directives**

These are instructions to the SLURM scheduler — add them at the top of the file, right after the shebang:

```bash
#SBATCH --job-name=<job-name>
#SBATCH --output=logs/extract_%j.out
#SBATCH --error=logs/extract_%j.err
#SBATCH --time=<HH:MM:SS>
#SBATCH --mem=<RAM>
#SBATCH --cpus-per-task=<cores>
```

What each one is:

- `--job-name` — a short label **you pick** so you can spot this job in the queue (e.g. `form3-extract`). It doesn't affect resources; name it whatever's memorable.
- `--output` / `--error` — files where the job's normal output and errors get written; `%j` is auto-filled with the job ID, so each run gets its own log. **Leave these as-is.**
- `--time`, `--mem`, `--cpus-per-task` — the resources you're **requesting**. Fill these in from the **time**, **RAM**, and **CPU cores** you recorded in your Profiling README (formatted like `00:10:00`, `4G`, and `2`).

{: .note }
> **About the `--output` and `--error` files:**
> - A batch job has **no terminal** — you're not watching it run. So SLURM redirects everything your script would normally print: normal output goes to the **`--output` (`.out`) file**, and error messages/tracebacks go to the **`--error` (`.err`) file**. Those files are how you see what the job did and debug it when it fails.
> - `%j` gets replaced with the job ID, so each run writes its own `logs/extract_<jobid>.out` and `.err` instead of overwriting the last.
> - **Combine them if you like:** omit `--error` entirely and SLURM sends *both* normal output and errors to the single `--output` (`.out`) file. Keeping them separate just makes errors easier to spot.
> - The `logs/` directory must exist before the job runs — SLURM won't create it, which is why `mkdir -p logs` came first.

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

**Step 4 — Add the line that runs your script**

The last line of the file is the actual work — the command SLURM will run on the compute node when the job starts. It's a line you write *inside* the script, **not** something you run yourself right now:

```bash
python scripts/extract_form_3_batch.py
```

This runs the **10-filing batch you profiled** — `scripts/extract_form_3_batch.py` loops over `NUM_FILINGS` (10) SEC Form 3 filings from `data/aws_links.csv` — so the `--time`, `--mem`, and `--cpus-per-task` you filled in above come straight from your Profiling README.

Save the file.

{: .warning }
> **SLURM starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

When your script is complete — put a **🟢 green sticky** on your laptop.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="main"> I wrote extract_form_3_batch.slurm and understand every line</label>

---

## Submit

```bash
sbatch slurm/extract_form_3_batch.slurm
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

Replace `JOBID` with your job's actual number — the one `sbatch` printed (`Submitted batch job 12345678`) and that shows in `squeue --me`. It's not the literal word `JOBID`.

Confirm it is gone:

```bash
squeue --me
```

{: .note }
> You may briefly see your job's status change to **CG** (completing) before it disappears from the queue — that's normal, not an error.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="submit"> I submitted with `sbatch`, confirmed it in the queue, and cancelled it with `scancel`</label>

---

## Add Email Notifications

Open `slurm/extract_form_3_batch.slurm` and add these two lines with your other `#SBATCH` directives:

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

`ALL` sends an email when the job starts, ends, and fails — including a utilization summary showing how much CPU and RAM it actually used.

Resubmit:

```bash
sbatch slurm/extract_form_3_batch.slurm
```

Once your job runs, check your inbox. You should receive two emails: one when the job **starts** and one when it **ends**. The start email tells you when it began — compare that to when you submitted to see how long it **waited in the queue**. The end email includes a **utilization summary** (how much CPU time and memory the job actually used) and the job's **exit status**: `0` means success; any other value means it failed.

Once you've got the emails and your job finished with exit status `0` — put a **🟢 green sticky** on your laptop. If it failed or the emails didn't arrive, put up a **🔴 red sticky** and an instructor will help.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side1"> My job completed without fail and I got emails from SLURM</label>

---

## Watch a Job Run on Its Node

The extraction job is quick and barely touches the CPU, so it's hard to catch in the act. We've shipped a heavier demo — `slurm/mystery.slurm`, which runs the mystery script from Profiling for about **30 seconds** across a few cores — long enough to watch it live.

Submit it:

```bash
sbatch slurm/mystery.slurm
```

While your job is running you can SSH to the node it's on and watch it work. (Nodes are **shared** — other users' jobs run on them too — but your job has its own **dedicated cores and RAM**.) The `NODELIST` column from `squeue --me` shows which node it landed on (e.g. `yen10`). SSH there and watch your processes live:

```bash
ssh SUNetID@yen10.stanford.edu   # use your job's actual node
htop -u $USER                    # or: top -u $USER
```

You'll see the mystery script's Python workers pinning the cores you requested. Press `q` to quit `htop`, then `exit` to leave the node.

{: .note }
> You can only SSH to a compute node **while you have a job running on it** — once the job ends (or if you never had one there), SSH to that node is refused. You can't hop onto arbitrary compute nodes.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side4"> I found my job's node with squeue and watched it run live with htop</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Go Interactive Instead of Batch**

Everything so far has been batch submission — write a script, `sbatch` it, wait. SLURM also supports an interactive allocation on a dedicated node — handy when you're debugging and re-running over and over: you hold the allocation, so you don't re-queue for resources every time a job fails and you fix it:

```bash
srun --pty --cpus-per-task=2 --mem=4G --time=00:30:00 bash
```

Once it drops you into a shell on your allocated node, you're on a fresh shell — do the same setup your batch script does, then run the script directly:

```bash
cd $HOME/gsb-research-computing-ai-skills   # into your project
source .venv/bin/activate                   # activate your environment
python scripts/extract_form_3_batch.py   # run it and watch the output live
```

Because you're interactive, you see the output as it happens and can re-run instantly after a fix — no re-queuing. Type `exit` to release the allocation when you're done.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side2"> I requested an interactive allocation with `srun --pty` and ran my script there</label>

**Side quest — Chain Two Jobs**

Real pipelines are often more than one step. Submit a second job that only starts if your first one succeeds:

```bash
sbatch --dependency=afterok:JOBID slurm/extract_form_3_batch.slurm
```

Replace `JOBID` with the job ID of a job you already submitted. Confirm with `squeue --me` that the new job shows as pending until the first one completes.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side3"> I chained two SLURM jobs with --dependency=afterok</label>

**Side quest — The `dev` partition**

The Yens have a dedicated **`dev` partition** for short, interactive debugging jobs — quick test runs while you're getting a script working, **not** production runs. It has tighter time limits but is meant to turn around fast, so you're not stuck in the main queue while iterating. Read up on it on RCpedia, then try submitting to it with `-p dev` (on `sbatch` or `srun`).

Learn more: [Yen SLURM partitions](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side5"> I read about the dev partition on RCpedia and know when to use it (short debug jobs, not production)</label>

**Side quest — Debug a broken job**

Your repo ships a few SLURM scripts that are **deliberately broken** — each fails the way a real "worked on my laptop" job dies on a fresh compute node. Fix them one at a time, and **work with Claude**: paste the error into Claude Code, ask it to explain what went wrong and how to fix it, then apply the fix yourself.

Submit the first one and watch it fail:

```bash
sbatch slurm/fix_me.slurm
sacct -u $USER --format=JobID,JobName,State,Elapsed --starttime=today
```

When it shows `FAILED`, read the error log to find out *why*:

```bash
cat logs/fix_me_*.err
```

Fix the bug in `slurm/fix_me.slurm`, add the email-notification lines (from **Add Email Notifications** above) so you get a completion email, then resubmit. Do the same for `slurm/fix_me_2.slurm` and `slurm/fix_me_3.slurm` — each hides a different setup mistake (a missing step, a wrong path, a bad directory).

**Bonus:** `slurm/extract_form_3_one_file_broken.slurm` has *two* bugs — one in the SLURM script and one in the Python it runs (`scripts/extract_form_3_one_file_broken.py`). Fix both.

Only check this off once a job you fixed actually **completed** — you'll know because the SLURM email says it finished with **exit status `0`**.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="debug"> I worked with Claude to fix a broken job, resubmitted, and got the SLURM email confirming it COMPLETED (exit status 0)</label>

