---
layout: default
title: "The Chronicle"
parent: "Day 3 — The SLURM Mines"
nav_order: 8
permalink: /day3/chronicle/
---

# The Chronicle

<div data-room-id="d3-chronicle"></div>

---

## Main Exercise — Write a README

Write your README while the code is still fresh — before you close the terminal. Your memory of every flag and design choice is sharpest right now.

{: .important }
> **Exercise:** Write a `README.md` for your Day 3 pipeline.

Create `README.md` in your repo root (or a `day3/` subdirectory):

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

## What this does

Extracts insider name, role, and transaction date from SEC Form 3 filings
using the Stanford AI API via a SLURM batch job.

## How to run

### Prerequisites
- Access to the Stanford Yens cluster
- Stanford AI API key in `.env`
- Python venv at `.venv/` (see Day 2 setup)

### Steps
# 1. Submit the batch job
sbatch jobs/extract.sh

# 2. Monitor
squeue -u $USER
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS

# 3. Check output
cat logs/extract_JOBID.out

## Outputs

- `logs/extract_JOBID.out` — extraction results
- `logs/extract_JOBID.err` — error log if any

## Data

Input: SEC Form 3 filings from EDGAR (public domain).

## Known limitations

- Non-standard filing formats may produce empty fields
```

{: .note }
> You will update this README in the Day 4 capstone when you scale with a job array.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="main"> README written and covers what the script does, how to run it, and where output lands</label>
