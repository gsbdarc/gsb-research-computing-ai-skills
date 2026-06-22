---
layout: default
title: "The Array Cavern"
parent: "Day 3 — The SLURM Mines"
nav_order: 7
permalink: /day3/array-cavern/
---

# The Array Cavern

<div data-room-id="d3-array-cavern"></div>

*A thousand identical alcoves, each one running the same recipe on a different ingredient. The Array Cavern answers the researcher's most common scaling problem: "I need to do this to 10,000 files." You write the recipe once. The cavern handles the rest. When the jobs finish, you combine the streams into one river.*

---

## Main Quest

{: .important }
> **Quest:** Submit a SLURM job array that processes 100 SEC filings in parallel, then combine all outputs into one CSV.

**Part 1 — Prepare the input list:**

```bash
ls ~/rf_bootcamp_2026/data/sec_filings/*.txt > /scratch/$USER/filings_list.txt
wc -l /scratch/$USER/filings_list.txt   # confirm: should be 100
mkdir -p /scratch/$USER/results logs
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

source ~/rf_bootcamp_2026/.venv/bin/activate

FILING=$(sed -n "${SLURM_ARRAY_TASK_ID}p" /scratch/$USER/filings_list.txt)
echo "Task $SLURM_ARRAY_TASK_ID processing: $FILING"

python3 ~/rf_bootcamp_2026/extract_filing.py \
    --input "$FILING" \
    --output "/scratch/$USER/results/filing_${SLURM_ARRAY_TASK_ID}.json"
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

RESULTS_DIR = Path(f"/scratch/{os.environ['USER']}/results")
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

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="main"> Main Quest complete — array submitted, CSV merged</label>

---

## Chests

{: .chest }
> **Chest 1 — Dependency Dagger:** Chain two job arrays with `--dependency=afterok:JOBID`. The second array runs only after all tasks in the first succeed. Write a two-stage pipeline: extract → validate. What happens when one extraction task fails?

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="chest1"> Dependency Dagger unlocked</label>

{: .chest }
> **Chest 2 — Dynamic Draught:** Instead of hardcoding `--array=1-100`, write a wrapper that counts lines in the input file and submits `sbatch --array=1-$(wc -l < filings_list.txt) array_extract.sh`. Never hard-code a count that changes when the dataset changes.

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="chest2"> Dynamic Draught unlocked</label>

{: .chest }
> **Chest 3 — Checkpoint Charm:** Add 5 lines to `extract_filing.py`: before doing any work, check if the task ID already appears in `completed.log`. If yes, exit early. If no, process the filing and append the task ID to the log on success. Resubmit the array — only incomplete tasks run.

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="chest3"> Checkpoint Charm unlocked</label>

{: .chest }
> **Chest 4 — Siege Scale:** Extend the fault-tolerant pattern to 10,000 inputs. Organize outputs into dated subdirectories (`results/2026-06-22/`) so reruns don't overwrite previous runs. How does this change the merge step?

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="chest4"> Siege Scale unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Dependency Dagger** — `--dependency=afterok` to chain jobs; run stage B only after all of stage A succeeds.
>
> **Dynamic Draught** — generate array size from the input file at submission time; works for any dataset size.
>
> **Checkpoint Charm** — log completed task IDs and skip already-done work on rerun; resume interrupted pipelines without restarting from zero.
>
> **Siege Scale** — fault-tolerant pipelines with dated output directories; handle tens of thousands of inputs without losing progress.

---

## Skills Learned

- Understand `$SLURM_ARRAY_TASK_ID` and how to look up per-task input from a file list
- Submit a job array and monitor the individual tasks in `squeue`
- Combine parallel JSON outputs into a single CSV; surface failures explicitly
- (Optional) Write checkpointing logic so a resubmitted array only retries failed tasks
