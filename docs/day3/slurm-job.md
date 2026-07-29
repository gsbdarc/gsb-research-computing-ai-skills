---
layout: default
title: "Writing & Submitting a Slurm Job"
parent: "Day 3 — Cluster Computing"
nav_order: 7
permalink: /day3/slurm-job/
---

# Writing & Submitting a Slurm Job

<div data-room-id="d3-slurm-job"></div>

---

## Main quest — Write a Slurm Script

{: .important }
> **Task:** Build a Slurm job script line by line to run your Form 3 extraction script on a compute node.

**Start from a clean shell.** If you have a virtual environment active right now (you'll see `(.venv)` at the front of your prompt), deactivate it first:

```bash
deactivate
```

`sbatch` copies your current shell's environment into the job by default, so if `.venv` is active when you submit, it **rides along** — and the job can quietly succeed even if the script forgot to activate it. Deactivate first so the job runs on only what the **script** sets up (the `source .venv/bin/activate` in Step 3) — the way it'll run for a teammate, or for you from a clean login.

**Create the file:**

Your repo already has a `slurm/` folder (with a few prepared scripts). Just make sure a `logs/` folder exists for job output:

```bash
mkdir -p logs
```

{: .warning }
> **The `logs/` folder must exist before you submit.** Slurm opens your `--output`/`--error` files the moment the job starts — it does **not** create missing directories. If you point `--output` at `logs/…` but there's no `logs/` folder, the job **fails silently**: nothing runs and no log file appears to tell you why. Create it once, up front. (If instead you point `--output` at a bare `extract.out` with no folder, the file lands in whatever directory you ran `sbatch` from.)

Create a new file `slurm/extract_form_3_batch.slurm` and open it in your editor — you'll build it up line by line below.

{: .note }
> No preferred terminal editor? You can create it right in **JupyterHub**: in the file browser, open the `slurm/` folder, click **+ New → Text File** (or **File → New → Text File**), edit it in the browser, then **rename** the file to `extract_form_3_batch.slurm` and save with `Cmd/Ctrl+S`.

---

**Step 1 — The shebang**

The first line of every shell script is the **shebang**:

```bash
#!/bin/bash
```

The `#!` (the **shebang**) tells the operating system which **interpreter** — the program that reads your script and runs it line by line — to use for the rest of the file; here, the Bash shell at `/bin/bash`. Without it, the system doesn't know whether your script is Bash, Python, or something else. It has to be the very first line of the file.

---

**Step 2 — SBATCH directives**

These are instructions to the Slurm scheduler — add them at the top of the file, right after the shebang:

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
> - A batch job has **no terminal** — you're not watching it run. So Slurm redirects everything your script would normally print: normal output goes to the **`--output` (`.out`) file**, and error messages/tracebacks go to the **`--error` (`.err`) file**. Those files are how you see what the job did and debug it when it fails.
> - `%j` gets replaced with the job ID, so each run writes its own `logs/extract_<jobid>.out` and `.err` instead of overwriting the last.
> - **Combine them if you like:** omit `--error` entirely and Slurm sends *both* normal output and errors to the single `--output` (`.out`) file. Keeping them separate just makes errors easier to spot.
> - The `logs/` directory must exist before the job runs — Slurm won't create it, which is why `mkdir -p logs` came first.

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

The last line of the file is the actual work — the command Slurm will run on the compute node when the job starts. It's a line you write *inside* the script, **not** something you run yourself right now:

```bash
python scripts/extract_form_3_batch.py
```

This runs the **10-filing batch you profiled** — `scripts/extract_form_3_batch.py` loops over `NUM_FILINGS` (10) SEC Form 3 filings from `data/aws_links.csv` — so the `--time`, `--mem`, and `--cpus-per-task` you filled in above come straight from your Profiling README.

Save the file.

{: .warning }
> **Slurm starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

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

**Ask Claude Code to add** the two email directives to your script — these two lines:

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

A prompt like:

> Add `--mail-type=ALL` and `--mail-user=SUNetID@stanford.edu` to the `#SBATCH` directives in `slurm/extract_form_3_batch.slurm`.

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

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side1"> My job completed without fail and I got emails from Slurm</label>

---

## Watch a Job Run on Its Node

`slurm/mystery.slurm` runs the mystery script from Profiling for about **30 seconds** across a few cores — long enough to watch it live.

Submit it:

```bash
sbatch slurm/mystery.slurm
```

While your job is running you can SSH to the node it's on and watch it work. (Nodes are **shared** — other users' jobs run on them too — but your job has its own **dedicated cores and RAM**.) The `NODELIST` column from `squeue --me` shows which node it landed on (e.g. `yen10`). SSH there and watch your processes live:

```bash
ssh SUNetID@yen10   # use your job's actual node
htop -u SUNetID                  # or: top -u SUNetID
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

Everything so far has been batch submission — write a script, `sbatch` it, wait. Slurm also supports an interactive allocation on a dedicated node — handy when you're debugging and re-running over and over: you hold the allocation, so you don't re-queue for resources every time a job fails and you fix it:

```bash
srun --pty --cpus-per-task=2 --mem=4G --time=00:30:00 bash
```

Your interactive session is a Slurm job like any other — run `squeue --me` and you'll see it listed (state `R`) until you release it:

```bash
squeue --me
```

Once it drops you into a shell on your allocated node, you're on a fresh shell — do the same setup your batch script does, then run the script directly:

```bash
cd $HOME/gsb-research-computing-ai-skills   # into your project
source .venv/bin/activate                   # activate your environment
python scripts/extract_form_3_batch.py   # run it and watch the output live
```

Because you're interactive, you see the output as it happens and can re-run instantly after a fix — no re-queuing. Type `exit` to release the allocation when you're done.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side2"> I requested an interactive allocation with `srun --pty` and ran my script there</label>

**Side quest — Debug `fix_me.slurm`**

Your repo ships a few Slurm scripts that are **deliberately broken**. Fix them one at a time, and **work with Claude**: point Claude Code at the job's error log and ask it to explain what went wrong and propose a fix. **Read its explanation, and if the fix makes sense, approve it** and let Claude apply it — you're the reviewer, so don't accept a change you don't understand.

<details markdown="1">
<summary>Show steps</summary>

Submit the first one:

```bash
sbatch slurm/fix_me.slurm
```

Watch it move through the queue — `PD` (pending), then `R` (running), then gone once it finishes:

```bash
squeue --me
```

Once it's no longer in the queue, check how it ended:

```bash
sacct -u SUNetID --format=JobID,JobName,State,Elapsed --starttime=today
```

When it shows `FAILED`, read the error log to find out *why*:

```bash
cat logs/fix_me_*.err
```

**Put Claude Code in plan mode first** (press `Shift`+`Tab` to switch) so it lays out *what* it would change and *why* instead of editing right away. Then point it at the error log — a simple prompt is enough:

> Help me troubleshoot `logs/fix_me_*.err`

**Read the plan it comes back with.** If the fix makes sense, approve it and let Claude apply it — you're the reviewer.

You'll also want a completion email, so ask Claude to add the notification lines to this script:

> Add `#SBATCH --mail-type=ALL` and `#SBATCH --mail-user=SUNetID@stanford.edu` to `slurm/fix_me.slurm`.

Then resubmit — **keep debugging and resubmitting until the Slurm email says the job succeeded** (exit status `0`).

</details>

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="debug"> I worked with Claude to fix a broken job, resubmitted, and got the Slurm email confirming it completed</label>

**Side quest — Debug `fix_me_2.slurm`**

Same drill, a different setup mistake. Submit it, watch it fail, and read its error log:

```bash
sbatch slurm/fix_me_2.slurm
squeue --me
cat logs/fix_me_2_*.err
```

Troubleshoot with Claude in plan mode (`> Help me troubleshoot logs/fix_me_2_*.err`), approve the fix if it makes sense, have Claude add the email lines to `slurm/fix_me_2.slurm` too, and resubmit until the Slurm email says it succeeded.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="debug2"> I fixed fix_me_2.slurm and got the Slurm email confirming it completed</label>

**Side quest — Debug `fix_me_3.slurm`**

One more, hiding yet another setup mistake. Same process:

```bash
sbatch slurm/fix_me_3.slurm
squeue --me
cat logs/fix_me_3_*.err
```

Troubleshoot with Claude in plan mode, approve the fix, have Claude add the email lines to `slurm/fix_me_3.slurm`, and resubmit until it completes.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="debug3"> I fixed fix_me_3.slurm and got the Slurm email confirming it completed</label>

**Side quest — Debug `extract_form_3_one_file_broken.slurm`**

The trickiest one: it hides *two* bugs — one in the Slurm script and one in the Python it runs (`scripts/extract_form_3_one_file_broken.py`). Submit it, read the error log, and work through **both** with Claude the same way (plan mode → read the plan → approve → add the email lines → resubmit) until it completes.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="debug4"> I fixed both bugs in extract_form_3_one_file_broken.slurm and got the Slurm email confirming it completed</label>

**Side quest — Chain Two Jobs**

A real research pipeline is a chain of **stages**, each feeding the next. Scaled up, your Form 3 work is naturally three jobs: **(1) download** the raw filings from EDGAR, **(2) extract** the structured fields with the API (what your batch script does), then **(3) aggregate** the per-filing JSON into one dataset and compute summary stats. Each stage reads the file the one before it wrote — stage 2 can't start until stage 1's downloads land, and stage 3 needs stage 2's extractions. Rather than babysit them, launching each by hand the moment the last finishes, you queue the whole chain at once: `--dependency=afterok` tells Slurm to hold each job until the one before it **succeeds**. Your repo ships a small two-step version of this:

- `scripts/chain_step1.py` — crunches numbers for ~2 minutes, then writes its result to `/scratch/users/SUNetID/chain_demo/step1_result.txt`.
- `scripts/chain_step2.py` — reads that file and does more math, writing `step2_result.txt` beside it.

with `slurm/chain_step1.slurm` and `slurm/chain_step2.slurm` to run them.

**Step 1 — submit the first job** and note the `JOBID` it prints:

```bash
sbatch slurm/chain_step1.slurm
```

**Step 2 — submit the second right away**, chained to the first. First, have Claude add the email lines to `slurm/chain_step2.slurm` so you get a note when the chain finishes:

> Add `#SBATCH --mail-type=ALL` and `#SBATCH --mail-user=SUNetID@stanford.edu` to `slurm/chain_step2.slurm`.

Then submit it, replacing `JOBID` with step 1's ID:

```bash
sbatch --dependency=afterok:JOBID slurm/chain_step2.slurm
```

**Step 3 — watch the queue.** Both jobs are in, but step 2 waits its turn. `watch` re-runs a command every couple of seconds, so you can see the handoff happen live:

```bash
watch squeue --me
```

Step 1 shows `R` (running) while step 2 sits `PD` with reason `(Dependency)`. When step 1 finishes, step 2 flips to `R` on its own — you do nothing. Press `Ctrl-C` to stop watching.

**Step 4 — check the handoff** once both are done:

```bash
cat /scratch/users/SUNetID/chain_demo/step2_result.txt
```

Step 2's number is computed from step 1's — proof the scratch file passed between them. Had step 1 failed, step 2 would never have started.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side3"> I chained the two jobs with --dependency=afterok — step 2 waited for step 1 and used its scratch file — and got the Slurm email that step 2 completed</label>

**Side quest — The `dev` partition**

The Yens have a dedicated **`dev` partition** for short, interactive debugging jobs — quick test runs while you're getting a script working, **not** production runs. It has tighter time limits but is meant to turn around fast, so you're not stuck in the main queue while iterating. Learn more: [Yen Slurm partitions](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).

<details markdown="1">
<summary>Show steps</summary>

Fire a quick throwaway job at `dev` with `-p dev` (and `--wrap`, which runs an inline command as a job). It's tiny, so it schedules fast, and it emails you when it finishes:

```bash
sbatch -p dev --mail-type=ALL --mail-user=SUNetID@stanford.edu --wrap="hostname; sleep 30"
```

Watch it — `dev` usually starts right away:

```bash
squeue --me
```

You'll get a completion email in a moment. Confirm it says the job completed.

</details>

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side5"> I submitted the job to the dev partition and got an email that it completed</label>

