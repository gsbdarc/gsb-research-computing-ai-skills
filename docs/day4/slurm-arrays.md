---
layout: default
title: "SLURM Job Arrays"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 2
permalink: /day4/slurm-arrays/
---

# SLURM Job Arrays

<div data-room-id="d4-slurm-arrays"></div>

This is a concept section. You've seen *why* parallelization helps; now we turn it into something you can actually run on the Yens. The tool for embarrassingly parallel work like ours is a **SLURM job array**.

---

## Recap: One Job on SLURM (Day 3)

On Day 3 you didn't run your extraction script directly on a login node — you handed it to **SLURM**, the cluster's scheduler, in an `sbatch` script. SLURM found a free slot on a compute node, ran your job there, and saved the output. That was one filing, one job.

To scale up, the question is simply: how do we get SLURM to run that script once per filing, across many cores at the same time?

---

## The Naive Ways (and Why They're Clumsy)

- **A loop inside one job.** You could write a `for` loop over the filings in a single `sbatch` job. But that's exactly the serial picture from [Parallelization Basics](parallelization/) — one core, one filing at a time. No speedup.
- **Submit the script 100 times by hand.** Running `sbatch` once per filing *does* run them in parallel, but now you're juggling 100 separate submissions, 100 job IDs, and 100 output names — tedious to track, combine, and rerun when a few fail.

There's a tool built for exactly this pattern.

---

## The Idea: One Script, Many Tasks

A **job array** is a single script that SLURM launches many times, each run as an independent **task**. You add one directive:

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
  <text x="106" y="101" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, monospace">array_extract.sh</text>
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

The task ID is just an integer — *you* decide what it points to. A common pattern: list the filings in a file, and have each task grab the line matching its ID.

```bash
#!/bin/bash
#SBATCH --array=1-100          # create tasks 1 through 100
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

# the line number to read = this task's ID
FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" filings_list.txt)

python extract_filing.py \
    --input  "$FILING" \
    --output "results/filing_${SLURM_ARRAY_TASK_ID}.json"
```

Task 1 reads line 1 of `filings_list.txt` and writes `filing_1.json`; task 2 reads line 2 → `filing_2.json`; and so on. One script, one submission, 100 outputs.

---

## Why an Array Beats a Manual Loop

- **SLURM schedules the tasks for you** across whatever cores are free — including the [waves](parallelization/) that happen when there are more filings than cores.
- **The tasks are independent.** One task failing doesn't touch the others, and you can resubmit just the failures instead of rerunning everything.
- **There's one thing to track.** A single job ID (with per-task sub-IDs) to monitor with `squeue` or cancel with `scancel`.
- **The outputs are predictable.** `filing_${SLURM_ARRAY_TASK_ID}.json` gives you a tidy set of files, ready to combine into one CSV.

---

## Up Next

You'll write, submit, and combine a real job array on the Yens in [Parallel Jobs with SLURM Arrays](array-cavern/).

<label class="quest-check"><input type="checkbox" data-room="d4-slurm-arrays" data-key="main"> I understand how a SLURM job array turns one script into many parallel tasks</label>

---

## What You Learned

- You can explain what a SLURM **job array** is: one script, submitted once, that SLURM runs as many independent tasks
- You know that `#SBATCH --array=1-N` creates the tasks and `SLURM_ARRAY_TASK_ID` distinguishes them
- You can map a task ID to a unit of work — e.g. selecting the matching line from a list of filings
- You can say why an array is better than a hand-managed loop of jobs: scheduling, independence, tracking, and tidy outputs
