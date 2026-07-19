---
layout: default
title: "SLURM Job Arrays"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 2
permalink: /day4/slurm-arrays/
---

# SLURM Job Arrays

<div data-room-id="d4-slurm-arrays"></div>

You've seen *why* parallelization helps and when a workload qualifies. This section is about *how* to implement it on the Yens. There are a few ways to run work in parallel on a cluster; for embarrassingly parallel jobs like ours, the standard, purpose-built tool is a **SLURM job array**. This page covers how arrays work; you'll build and submit one in [Submitting an Array Job](array-exercise/).

---

## Recap: One Job on SLURM (Day 3)

On Day 3 you didn't run your extraction script directly on a login node — you handed it to **SLURM**, the cluster's scheduler, in an `sbatch` script. SLURM found a free slot on a compute node, ran your job there, and saved the output. That was one filing, one job.

To scale up, the question is *how* to run that work in parallel across the cluster's cores — and which mechanism to reach for.

---

## From One Filing to Many

The goal is a single script that handles *all* your filings — not one you edit and rerun by hand for each. The natural way to write that is a **`for` loop** over the filings:

```python
for filing in filings:       # your list of filings
    result = extract(filing)
    save(result)
```

That gives you one script that processes every filing. But it works through them **one at a time** on a single core — this isn't parallelization, it's just your work organized into a single, re-runnable script (the serial picture from [Parallelization Basics](parallelization/)).

---

## Running Them at the Same Time

The loop's iterations are independent, so rather than one core grinding through them in sequence, we want many cores working at once. You *could* do that by submitting the script by hand, once per filing — 100 `sbatch` calls, 100 job IDs, and 100 output names to wrangle. But that's clumsy and effortful. SLURM has a purpose-built tool for exactly this pattern instead.

---

## The Idea: One Script, Many Tasks

A **job array** is a single script that SLURM launches many times, each run as an independent **task**. You add one directive to your `sbatch` script — alongside the other `#SBATCH` lines at the top, like the ones you wrote on Day 3:

```bash
#SBATCH --array=1-100
```

and that one submission becomes 100 tasks. Every task runs the same script — identical except for one number, its **`SLURM_ARRAY_TASK_ID`** (1, 2, 3, … 100). You use that number to decide which filing *this* task should process.

<svg viewBox="0 0 562 212" role="img" aria-labelledby="array-title array-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:560px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="array-title">One array script fans out into many tasks</title>
  <desc id="array-desc">A single submission script with the directive array equals 1 to 100 fans out into many independent tasks. Task 1 processes filing 1, task 2 processes filing 2, and so on up to task 100, each selected by its array task ID.</desc>
  <!-- fan-out connectors (drawn first, behind boxes) -->
  <line x1="188" y1="106" x2="330" y2="30"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="106" x2="330" y2="68"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="106" x2="330" y2="106" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="106" x2="330" y2="172" stroke="#cbd3e0" stroke-width="1.5"/>
  <!-- submission script -->
  <rect x="24" y="80" width="164" height="52" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="106" y="101" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">SLURM script</text>
  <text x="106" y="119" font-size="10.5" fill="#6a7280" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, monospace">--array=1–100</text>
  <!-- task boxes -->
  <rect x="330" y="15"  width="208" height="30" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="434" y="35"  font-size="12" fill="#2c3e50" text-anchor="middle">task 1  →  filing 1</text>
  <rect x="330" y="53"  width="208" height="30" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="434" y="73"  font-size="12" fill="#2c3e50" text-anchor="middle">task 2  →  filing 2</text>
  <rect x="330" y="91"  width="208" height="30" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="434" y="111" font-size="12" fill="#2c3e50" text-anchor="middle">task 3  →  filing 3</text>
  <text x="434" y="146" font-size="16" fill="#9aa2b1" text-anchor="middle">⋮</text>
  <rect x="330" y="157" width="208" height="30" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="434" y="177" font-size="12" fill="#2c3e50" text-anchor="middle">task 100  →  filing 100</text>
  <!-- caption -->
  <text x="281" y="205" font-size="12.5" fill="#6a7280" text-anchor="middle">One submission becomes 100 independent tasks; each task's ID selects its filing.</text>
</svg>

---

## Mapping a Task to a Filing

The task ID is just an integer — *you* decide what it points to. The usual pattern has four steps:

**1. List the filings, one file path per line.** Write the paths to a file such as `filings_list.txt`; the line number is what each task ID will refer to.

**2. Have each task grab its own line.** Use `SLURM_ARRAY_TASK_ID` to pull the matching line from that list:

```bash
# each line of filings_list.txt is the path to one filing;
# grab the line whose number matches this task's ID
FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" filings_list.txt)
```

Now `$FILING` holds the **path to a different filing** in each task — task 1 gets the path on line 1, task 2 the path on line 2, and so on.

**3. Use a script that accepts the path as an argument.** The Day 3 `extract_form_3_one_file.py` hard-codes its `FILING_PATH`, so it can't be pointed at a different filing per task. We've provided `scripts/extract_form_3_cli.py` — the same extraction logic, with a few lines added so it reads the paths from the command line:

```python
import sys
from pathlib import Path

FILING_PATH = Path(sys.argv[1])     # 1st argument: the filing to process
OUTPUT_PATH = Path(sys.argv[2])     # 2nd argument: where to write the result
```

Now you can point it at any filing (the two paths are passed in order):

```bash
python scripts/extract_form_3_cli.py path/to/filing.txt results/filing.json
```

**4. Put it all in the array script,** which hands each task its own input and output paths:

```bash
#!/bin/bash
#SBATCH --job-name=extract_array
#SBATCH --output=logs/extract_%A_%a.out    # %A = array job ID, %a = task ID
#SBATCH --error=logs/extract_%A_%a.err
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --array=1-100                        # one task per filing

source .venv/bin/activate

# this task's filing path = the matching line of the list
FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" filings_list.txt)

# hand that path — and a per-task output file — to the script
python scripts/extract_form_3_cli.py "$FILING" "results/filing_${SLURM_ARRAY_TASK_ID}.json"
```

{: .note }
> **More filings than the scheduler allows?** SLURM caps how many tasks an array can have, so if you have more filings than that limit, you can't give each one its own task. The fix is to hand each task a *chunk* of filings: task *n* processes a fixed block of lines from the list, with a `for` loop working through that block in sequence. The array runs the chunks in parallel; the loop handles the filings within each chunk.

**5. Combine the outputs (optional).** Each task writes its own result file, so when the array finishes you're left with a folder of per-task outputs — `results/filing_1.json`, `filing_2.json`, and so on. For analysis you'll usually want to stitch those into a single dataset, such as one CSV. That's a short post-processing step once all the tasks are done (the [exercise](array-exercise/) walks through it).

---

## Why an Array Beats Submitting by Hand

- **SLURM schedules the tasks for you** across whatever cores are free — including the ["waves"](parallelization/) that happen when there are more filings than cores.
- **The tasks are independent.** One task failing doesn't touch the others, and you can resubmit just the failures instead of rerunning everything.
- **There's one thing to track.** A single job ID (with per-task sub-IDs) to monitor with `squeue` or cancel with `scancel`.
- **The outputs are predictable.** `filing_${SLURM_ARRAY_TASK_ID}.json` gives you a tidy set of files, ready to combine into one CSV.

---

## Failure Resilience

Array jobs fail in pieces. A node reboots, a task hits its time limit, the API times out — and a handful of your 100 tasks come back empty. You don't want to redo the ones that already succeeded: that wastes compute, and with a paid API, money.

The fix is to make each task safe to run again. Before doing the work, a task checks whether its output already exists and skips if it does. Then, after a partial failure, you resubmit the *same* array: the finished tasks see their output and exit immediately, and only the missing ones do real work.

`scripts/extract_form_3_cli.py` includes exactly this check, right after it reads the output path:

```python
import sys
from pathlib import Path

OUTPUT_PATH = Path(sys.argv[2])

# already done? skip — makes the array safe to resubmit after a partial failure
if OUTPUT_PATH.exists():
    print(f"{OUTPUT_PATH} already exists — skipping")
    sys.exit(0)
```

---

<label class="quest-check"><input type="checkbox" data-room="d4-slurm-arrays" data-key="main"> I understand how a SLURM job array turns one script into many parallel tasks</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-slurm-arrays.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- You can explain what a SLURM **job array** is: one script, submitted once, that SLURM runs as many independent tasks
- You know that `#SBATCH --array=1-N` creates the tasks and `SLURM_ARRAY_TASK_ID` distinguishes them
- You can map a task ID to a unit of work — e.g. selecting the matching line from a list of filings
- You know how to make a task safe to rerun — skip it if its output already exists — so a partially failed array only redoes the missing work
- You can say why an array beats submitting jobs by hand: scheduling, independence, tracking, and tidy outputs

The hands-on exercise, [Submitting an Array Job](array-exercise/), puts this into practice.
