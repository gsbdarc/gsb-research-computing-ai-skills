---
layout: default
title: "The Chronicle"
parent: "Day 3 — The SLURM Mines"
nav_order: 8
permalink: /day3/chronicle/
---

# The Chronicle

<div data-room-id="d3-chronicle"></div>

*Torchlight flickers across the dungeon's library — floor-to-ceiling shelves of forgotten pipelines, abandoned repos, README files that were never written. Somewhere in the queue, your jobs are still running. Your memory of every flag, every design choice, every "I'll just use 4 GB and see what happens" is still sharp and alive. This is the only moment you will ever have this clarity. Write it down now — carve it into the stone — because six months from now you will open this repository in the dark, and there will either be a map waiting for you, or there won't.*

---

## 🗡️ Main Quest

The terminal is still warm. The jobs are still humming. This is your window — seal the knowledge before it fades.

{: .important }
> **Quest:** Write a `README.md` for your Day 3 pipeline while the code is still fresh — before you close the terminal.

Create `README.md` in your repo root (or a `day3/` subdirectory):

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

## What this does

Extracts insider name, role, and transaction date from SEC Form 3 filings
using the Stanford AI Playground (GPT-4o-mini) and a SLURM job array.
Results are combined into a single CSV.

## How to run

### Prerequisites
- Access to the Stanford Yens cluster
- Stanford AI Playground API key in `.env`
- Python venv at `.venv/` (see Day 2 setup)

### Steps
```bash
# 1. Prepare input list
ls data/sec_filings/*.txt > /scratch/shared/$USER/filings_list.txt

# 2. Submit the array
sbatch jobs/array_extract.sh

# 3. Monitor
watch -n 5 squeue -u $USER

# 4. Merge
python3 scripts/merge_results.py
```

## Outputs

- `results/extracted_filings.csv` — one row per filing
- Console warning if any tasks failed

## Data

Input: SEC Form 3 filings from EDGAR (public domain).

## Known limitations

- Only the first 4,000 characters of each filing are sent to the model
- Non-standard filing formats may produce empty fields
```

{: .note }
> You will update this README in the Day 4 capstone when you swap in the Ollama endpoint.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="main"> Main Quest complete — README written</label>
