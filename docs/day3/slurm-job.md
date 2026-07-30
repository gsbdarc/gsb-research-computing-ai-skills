---
layout: default
title: "Writing & Submitting a Slurm Job"
parent: "Day 3 — Cluster Computing"
nav_order: 7
permalink: /day3/slurm-job/
---

# Writing & Submitting a Slurm Job

<div data-room-id="d3-slurm-job"></div>

<svg viewBox="0 0 720 164" role="img" aria-labelledby="smap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="smap-title">Day 3 map — you are on the submit-to-Slurm step.</title>
  <defs>
    <marker id="smap-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#smap-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#smap-gray)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" fill="#8a94a6">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">1</text>
  <circle cx="210" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

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
- `--time`, `--mem`, `--cpus-per-task` — the resources you're **requesting**. Fill these in from the **time**, **RAM**, and **CPU cores** you recorded in your Profiling README.

{: .note }
> **About the `--output` and `--error` files:**
> - A batch job has **no terminal** — you're not watching it run. So Slurm redirects everything your script would normally print: normal output goes to the **`--output` (`.out`) file**, and error messages/tracebacks go to the **`--error` (`.err`) file**. Those files are how you see what the job did and debug it when it fails.
> - `%j` gets replaced with the job ID, so each run writes its own `logs/extract_JOBID.out` and `.err` instead of overwriting the last.
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

Save the file. Here's the whole script, with its four parts labeled:

<svg viewBox="0 0 700 272" role="img" aria-labelledby="anatomy-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:0.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="anatomy-title">The anatomy of a Slurm batch script: the shebang, the #SBATCH resource directives, the environment setup, and the run line(s) that do the work.</title>
  <rect x="16" y="10" width="440" height="252" rx="10" fill="#fbfcfe" stroke="#d5d8e2" stroke-width="1.5"/>
  <rect x="18" y="22" width="436" height="22" fill="#f3f4f7"/>
  <rect x="18" y="58" width="436" height="124" fill="#fdf0e3"/>
  <rect x="18" y="194" width="436" height="44" fill="#eaf1fb"/>
  <rect x="18" y="240" width="436" height="22" fill="#e9f5ee"/>
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" fill="#3a4452">
    <text x="32" y="38">#!/bin/bash</text>
    <text x="32" y="76">#SBATCH --job-name=&lt;job-name&gt;</text>
    <text x="32" y="96">#SBATCH --output=logs/extract_%j.out</text>
    <text x="32" y="116">#SBATCH --error=logs/extract_%j.err</text>
    <text x="32" y="136">#SBATCH --time=&lt;HH:MM:SS&gt;</text>
    <text x="32" y="156">#SBATCH --mem=&lt;RAM&gt;</text>
    <text x="32" y="176">#SBATCH --cpus-per-task=&lt;cores&gt;</text>
    <text x="32" y="212">cd $HOME/gsb-research-computing-ai-skills</text>
    <text x="32" y="232">source .venv/bin/activate</text>
    <text x="32" y="256">python scripts/extract_form_3_batch.py</text>
  </g>
  <circle cx="472" cy="33" r="6" fill="#8a94a6"/><text x="486" y="38" font-size="13.5" font-weight="700" fill="#2c3e50">shebang — the interpreter</text>
  <circle cx="472" cy="120" r="6" fill="#e67e22"/><text x="486" y="116" font-size="13.5" font-weight="700" fill="#2c3e50">#SBATCH — requests to the</text><text x="486" y="135" font-size="12.5" fill="#6a7280">scheduler (not commands)</text>
  <circle cx="472" cy="216" r="6" fill="#3a76c4"/><text x="486" y="212" font-size="13.5" font-weight="700" fill="#2c3e50">environment setup —</text><text x="486" y="231" font-size="12.5" fill="#6a7280">cd + activate venv, on the node</text>
  <circle cx="472" cy="256" r="6" fill="#2e8b57"/><text x="486" y="260" font-size="13.5" font-weight="700" fill="#2c3e50">run line(s) — your command(s)</text>
</svg>

*Every Slurm script has these four parts: the **shebang**, the **`#SBATCH`** directives (requests to the scheduler, not commands that run), the **environment setup** that runs on the compute node, and the **run line(s)** that do the actual work.*

{: .warning }
> **Slurm starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

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

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="submit"> I submitted with `sbatch`, confirmed it in the queue, and cancelled it with `scancel`</label>

---

## Add Email Notifications

**Ask Claude Code to add** the two email directives to your script — these two lines:

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

<details markdown="1">
<summary>💡 Hint — a prompt to try</summary>

> Add `--mail-type=ALL` and `--mail-user=SUNetID@stanford.edu` to the `#SBATCH` directives in `slurm/extract_form_3_batch.slurm`.

</details>

`ALL` sends an email when the job starts, ends, and fails — including a utilization summary showing how much CPU and RAM it actually used.

Resubmit:

```bash
sbatch slurm/extract_form_3_batch.slurm
```

Once your job runs, check your inbox. You should receive two emails: one when the job **starts** and one when it **ends**. The start email tells you when it began — compare that to when you submitted to see how long it **waited in the queue**. The end email includes a **utilization summary** (how much CPU time and memory the job actually used) and the job's **exit status**: `0` means success; any other value means it failed.

## Look at the Logs

<svg viewBox="0 0 720 164" role="img" aria-labelledby="rlmap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="rlmap-title">Day 3 map — you are on the read-logs step.</title>
  <defs>
    <marker id="rlmap-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" fill="#8a94a6">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" fill="#8a94a6">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#rlmap-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#rlmap-gray)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" fill="#8a94a6">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">2</text>
  <circle cx="350" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

The job wrote **log files** to `logs/` — the `.out` file has the script's normal output, the `.err` file has any errors:

```bash
cat logs/extract_*.out
cat logs/extract_*.err
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side1"> My job completed without fail, I got emails from Slurm, and I inspected the logs</label>

---

## Watch a Job Run on Its Node

`slurm/mystery.slurm` runs the mystery script from Profiling for about **30 seconds** across a few cores — long enough to watch it live.

Submit it:

```bash
sbatch slurm/mystery.slurm
```

While your job is running you can SSH to the node it's on and watch it work. (Nodes are **shared** — other users' jobs run on them too — but your job has its own **dedicated cores and RAM**.)

First, run `squeue --me` to find which node it landed on — the `NODELIST` column (e.g. `yen10`):

```bash
squeue --me
```

Then SSH to that node and watch your processes live:

```bash
ssh SUNetID@yen10   # use your job's actual node
htop -u SUNetID                  # or: top -u SUNetID
```

You'll see the mystery script's Python workers pinning the cores you requested. Press `q` to quit `htop`, then `exit` to leave the node.

{: .note }
> You can only SSH to a compute node **while you have a job running on it** — once the job ends (or if you never had one there), SSH to that node is refused. You can't hop onto arbitrary compute nodes.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

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

<svg viewBox="0 0 720 164" role="img" aria-labelledby="dmap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="dmap-title">Day 3 map — you are on the debug-and-resubmit step.</title>
  <defs>
    <marker id="dmap-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
    <marker id="dmap-red" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#8C1515"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" fill="#8a94a6">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" fill="#8a94a6">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#dmap-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#8C1515" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#dmap-red)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" font-weight="700" fill="#8C1515">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

Your repo ships a few Slurm scripts that are **deliberately broken**. Fix them one at a time, and **work with Claude**: point Claude Code at the job's error log and ask it to explain what went wrong and propose a fix. **Read its explanation, and if the fix makes sense, approve it** and let Claude apply it — you're the reviewer, so don't accept a change you don't understand.

{: .note }
> 💡 These error logs come back later — a later side quest uses a failed job's `logs/fix_me_*.err`. Even if you don't fix all of them, **submit at least the first one and let it fail** so you have a `logs/fix_me_*.err` to use then.

<details markdown="1">
<summary>📋 Show steps</summary>

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
- `scripts/chain_step2.py` — reads that file and does ~30 seconds more math, writing `step2_result.txt` beside it.

with `slurm/chain_step1.slurm` and `slurm/chain_step2.slurm` to run them.

**Step 1 — read both job scripts first** so you know what you're submitting. Notice they're ordinary Slurm scripts, and that step 2 reads the file step 1 wrote:

```bash
cat slurm/chain_step1.slurm slurm/chain_step2.slurm
```

**Step 2 — have Claude add the email lines to step 2** *before* you submit, so you get a note when the chain finishes:

> Add `#SBATCH --mail-type=ALL` and `#SBATCH --mail-user=SUNetID@stanford.edu` to `slurm/chain_step2.slurm`.

**Step 3 — submit both back-to-back.** Step 1 runs for ~2 minutes, so fire them off one after the other and let it crunch while step 2 queues behind it. Submit step 1 and note the `JOBID` it prints:

```bash
sbatch slurm/chain_step1.slurm
```

Then submit step 2 right away, chained to the first — replace `JOBID` with step 1's ID:

```bash
sbatch --dependency=afterok:JOBID slurm/chain_step2.slurm
```

**Step 4 — watch the queue.** Both jobs are in, but step 2 waits its turn. `watch` re-runs a command every couple of seconds, so you can see the handoff happen live:

```bash
watch squeue --me
```

Step 1 shows `R` (running) while step 2 sits `PD` with reason `(Dependency)`. When step 1 finishes, step 2 flips to `R` on its own — you do nothing. Press `Ctrl-C` to stop watching.

{: .note }
> 💡 If step 1 **fails**, `afterok` is never satisfied, so step 2's reason in `squeue` changes from `(Dependency)` to `(DependencyNeverSatisfied)`. That job will never run — but it won't clear itself either. It sits in the queue until **you** cancel it with `scancel JOBID`. Clear it, fix step 1, then requeue the chain.

**Step 5 — check the handoff** once both are done:

```bash
cat /scratch/users/SUNetID/chain_demo/step2_result.txt
```

Step 2's number is computed from step 1's — proof the scratch file passed between them. Had step 1 failed, step 2 would never have started.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-job" data-key="side3"> I chained the two jobs with `--dependency=afterok` — step 2 waited for step 1 and used its scratch file — and got the Slurm email that step 2 completed</label>

**Side quest — The `dev` partition**

The Yens have a dedicated **`dev` partition** for short, interactive debugging jobs — quick test runs while you're getting a script working, **not** production runs. It has tighter time limits but is meant to turn around fast, so you're not stuck in the main queue while iterating. Learn more: [Yen Slurm partitions](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).

<details markdown="1">
<summary>📋 Show steps</summary>

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

