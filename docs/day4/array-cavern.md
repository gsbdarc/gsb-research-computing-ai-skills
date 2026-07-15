---
layout: default
title: "The Array Cavern"
parent: "Day 4 — The GPU Fortress"
nav_order: 2
permalink: /day4/array-cavern/
---

# The Array Cavern

<div data-room-id="d4-array-cavern"></div>

---

## Why Parallelize?

Your Day 3 script processes one SEC filing at a time. You have 100 filings. Running them sequentially takes 100× as long — and ties up a node while you wait.

The Yens have hundreds of cores sitting idle. SLURM's job: hand each core a different filing so all 100 run simultaneously. Total time stays roughly the same as one filing — just multiplied across independent work.

```
  One at a time (sequential):        Parallelized (job array):
  filing 1 → 5s                      filing 1  ┐
  filing 2 → 5s                      filing 2  │ all start at once
  filing 3 → 5s                      filing 3  │ → ~5s total
  ...                                ...       ┘
  filing 100 → 5s
  ─────────────
  Total: ~500s                        Total: ~5s + queue wait
```

This only works when tasks are **independent** — each filing doesn't need the results from another. Your extraction script qualifies perfectly.

---

## Main Quest

{: .important }
> **Quest:** Submit a SLURM job array that processes 100 SEC filings in parallel, then combine all outputs into one CSV.

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

python3 ~/rf-bootcamp-2026/extract_filing.py \
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

<label class="quest-check"><input type="checkbox" data-room="d4-array-cavern" data-key="main"> Main Quest complete — array submitted, CSV merged</label>
