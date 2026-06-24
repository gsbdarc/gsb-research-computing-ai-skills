---
layout: default
title: "The Array Cavern"
parent: "Day 3 — The SLURM Mines"
nav_order: 7
permalink: /day3/array-cavern/
---

# The Array Cavern

<div data-room-id="d3-array-cavern"></div>

*A thousand identical alcoves stretch into the dark, each one lit by the faint glow of a running process. The walls hum in unison — the same script, a hundred times over, each instance tearing through a different filing. This is the Array Cavern, where the researcher's oldest curse is finally broken: "I need to do this to 10,000 files." You write the spell once. The cavern multiplies it across an army of workers. When the last task falls silent, you summon the streams together into a single, clean river of data.*

---

## 🗡️ Main Quest

The cluster is waiting. A hundred SEC filings sit untouched — until now. Write the script once, unleash the array, and forge the combined CSV that proves you were here.

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

<label class="quest-check"><input type="checkbox" data-room="d3-array-cavern" data-key="main"> Main Quest complete — array submitted, CSV merged</label>
