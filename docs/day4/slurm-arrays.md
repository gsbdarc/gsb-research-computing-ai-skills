---
layout: default
title: "SLURM Job Arrays"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 2
permalink: /day4/slurm-arrays/
---

# SLURM Job Arrays

<div data-room-id="d4-slurm-arrays"></div>

You've seen *why* parallelization helps and when a workload qualifies. This section is about *how* to implement it on the Yens. There are a few ways to run work in parallel on a cluster; for embarrassingly parallel jobs like ours, the standard, purpose-built tool is a **SLURM job array**. We'll cover how arrays work, then you'll build and submit one yourself.

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

The task ID is just an integer — *you* decide what it points to. A common pattern: list the filings in a file, **one file path per line**, and have each task grab the line matching its ID.

```bash
# each line of filings_list.txt is the path to one filing;
# grab the line whose number matches this task's ID
FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" filings_list.txt)
```

So `$FILING` holds the **path to a different filing** in each task — task 1 gets the path on line 1, task 2 the path on line 2, and so on — and that's the path you hand to your extraction script.

Putting it together takes two pieces: a script that *accepts* a filing path, and an array that hands a different path to each task.

**First, a script that takes the path as an argument.** The Day 3 `extract_form_3_one_file.py` hard-codes its `FILING_PATH`, so it can't be pointed at a different filing per task. `scripts/extract_form_3_cli.py` is the same extraction logic wired up to take `--input` and `--output` on the command line:

```bash
python scripts/extract_form_3_cli.py --input path/to/filing.txt --output results/filing.json
```

**Then the array script** that hands each task its own input and output paths:

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
python scripts/extract_form_3_cli.py \
    --input  "$FILING" \
    --output "results/filing_${SLURM_ARRAY_TASK_ID}.json"
```

{: .note }
> **More filings than tasks?** If you'd rather have fewer tasks than filings — say 50 tasks for 100 filings (array size is capped, and very short jobs aren't worth a whole task each) — hand each task a *chunk* of filings instead: task *n* processes a fixed block of lines from the list, with a `for` loop working through that block in sequence. The array runs the chunks in parallel; the loop handles the filings within each chunk.

You'll build and submit an array script like this in the exercise below.

---

## Why an Array Beats Submitting by Hand

- **SLURM schedules the tasks for you** across whatever cores are free — including the [waves](parallelization/) that happen when there are more filings than cores.
- **The tasks are independent.** One task failing doesn't touch the others, and you can resubmit just the failures instead of rerunning everything.
- **There's one thing to track.** A single job ID (with per-task sub-IDs) to monitor with `squeue` or cancel with `scancel`.
- **The outputs are predictable.** `filing_${SLURM_ARRAY_TASK_ID}.json` gives you a tidy set of files, ready to combine into one CSV.

<label class="quest-check"><input type="checkbox" data-room="d4-slurm-arrays" data-key="main"> I understand how a SLURM job array turns one script into many parallel tasks</label>

---

## Exercise

{: .important }
> **Goal:** Submit a SLURM job array that processes 100 SEC filings in parallel, then combine all outputs into one CSV.

**Part 1 — Prepare the input list:**

```bash
ls ~/rf-bootcamp-2026/data/sec_filings/*.txt > /scratch/shared/$USER/filings_list.txt
wc -l /scratch/shared/$USER/filings_list.txt   # confirm: should be 100
mkdir -p /scratch/shared/$USER/results logs
```

**Part 2 — Write `jobs/array_extract.sh`:**

```bash
#!/bin/bash
#SBATCH --job-name=extract_array
#SBATCH --output=logs/extract_%A_%a.out    # %A = array job ID, %a = task index
#SBATCH --error=logs/extract_%A_%a.err
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --array=1-100
#SBATCH --partition=normal

source ~/rf-bootcamp-2026/.venv/bin/activate

FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" /scratch/shared/$USER/filings_list.txt)
echo "Task $SLURM_ARRAY_TASK_ID processing: $FILING"

python3 ~/rf-bootcamp-2026/scripts/extract_form_3_cli.py \
    --input "$FILING" \
    --output "/scratch/shared/$USER/results/filing_${SLURM_ARRAY_TASK_ID}.json"
```

**Part 3 — Submit and monitor:**

```bash
sbatch jobs/array_extract.sh
watch -n 5 squeue -u $USER    # Ctrl-C when done
```

**Part 4 — Combine outputs into one CSV:**

```python
# scripts/merge_results.py
import json, csv, os
from pathlib import Path

RESULTS_DIR = Path(f"/scratch/shared/{os.environ['USER']}/results")
OUTPUT_CSV  = Path("results/extracted_filings.csv")
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

rows, failed = [], []

for task_id in range(1, 101):
    f = RESULTS_DIR / f"filing_{task_id}.json"
    if not f.exists():
        failed.append(task_id)
        continue
    try:
        data = json.loads(f.read_text())
        data["task_id"] = task_id
        rows.append(data)
    except json.JSONDecodeError:
        failed.append(task_id)

if rows:
    with open(OUTPUT_CSV, "w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")

if failed:
    print(f"FAILED ({len(failed)}): {failed}")
```

```bash
python3 scripts/merge_results.py
```

<label class="quest-check"><input type="checkbox" data-room="d4-slurm-arrays" data-key="exercise"> Exercise complete — array submitted, CSV merged</label>

---

## What You Learned

- You can explain what a SLURM **job array** is: one script, submitted once, that SLURM runs as many independent tasks
- You know that `#SBATCH --array=1-N` creates the tasks and `SLURM_ARRAY_TASK_ID` distinguishes them
- You can map a task ID to a unit of work — e.g. selecting the matching line from a list of filings
- You built and submitted a real array job on the Yens, and combined its per-task outputs into a single CSV
- You can say why an array beats submitting jobs by hand: scheduling, independence, tracking, and tidy outputs
