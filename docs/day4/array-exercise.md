---
layout: default
title: "Submitting an Array Job"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 3
permalink: /day4/array-exercise/
---

# Submitting an Array Job

<div data-room-id="d4-array-exercise"></div>

You'll submit a job array that processes 100 SEC filings in parallel, then combine the per-task outputs into one CSV.

---

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

python3 ~/rf-bootcamp-2026/scripts/extract_form_3_cli.py "$FILING" "/scratch/shared/$USER/results/filing_${SLURM_ARRAY_TASK_ID}.json"
```

**Part 3 — Submit and monitor:**

```bash
sbatch jobs/array_extract.sh
watch -n 5 squeue -u $USER    # Ctrl-C when done
```

{: .note }
> If some tasks fail, just resubmit the same script — `extract_form_3_cli.py` skips any filing whose output already exists (see [Failure Resilience](../slurm-arrays/#failure-resilience)), so only the missing ones rerun.

**Part 4 — Combine outputs into one CSV:**

```python
# scripts/merge_results.py — combine the array's per-task JSON files into one CSV
import json, csv, os
from pathlib import Path

RESULTS_DIR = Path(f"/scratch/shared/{os.environ['USER']}/results")   # where tasks wrote output
OUTPUT_CSV  = Path("results/extracted_filings.csv")                   # combined output
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)                  # create results/ if missing

rows, failed = [], []   # parsed filings; task IDs we couldn't read

for task_id in range(1, 101):
    f = RESULTS_DIR / f"filing_{task_id}.json"
    if not f.exists():
        failed.append(task_id)   # no output: crashed, timed out, or still running
        continue
    try:
        data = json.loads(f.read_text())
        data["task_id"] = task_id   # track which task this row came from
        rows.append(data)
    except json.JSONDecodeError:
        failed.append(task_id)   # file exists but is empty/corrupt

# a non-empty list is truthy in Python (an empty one is falsy), so this runs only
# when at least one task succeeded — which also guards rows[0] just below
if rows:
    with open(OUTPUT_CSV, "w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=rows[0].keys())   # columns from the first row
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")

# separate `if`, not `else`: a run can have both successes and failures
if failed:
    print(f"FAILED ({len(failed)}): {failed}")
```

```bash
python3 scripts/merge_results.py
```

**Part 5 — Verify the merged file:**

Confirm the CSV was written and has a row for every filing:

```bash
ls -l results/extracted_filings.csv     # the merged file should exist
wc -l results/extracted_filings.csv     # expect 101 lines: 1 header + 100 filings
head -3 results/extracted_filings.csv   # sanity-check the columns and first rows
```

`wc -l` counts the header line too, so 100 filings should give **101** lines. If it's short, the `FAILED (...)` list printed by `merge_results.py` tells you which task IDs to resubmit — rerun the array and the finished tasks will skip themselves.

<label class="quest-check"><input type="checkbox" data-room="d4-array-exercise" data-key="main"> Exercise complete — array submitted, merged, and verified</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-array-exercise.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- You built and submitted a real SLURM job array across 100 filings on the Yens
- You mapped `SLURM_ARRAY_TASK_ID` to a filing and wrote one output file per task
- You monitored the array with `squeue` and resubmitted safely thanks to the skip-if-done check
- You combined the per-task JSON outputs into a single CSV for analysis
