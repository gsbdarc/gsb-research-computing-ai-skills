---
layout: default
title: "The Recipe Book"
parent: "Day 3 — The Hearth"
nav_order: 9
permalink: /day3/recipe-book/
---

# The Recipe Book

<div data-room-id="d3-chronicle"></div>

*Every cook who passes through this kitchen is expected to leave a record. Not the ingredients — those are in the script. Not the timing — that's in sacct. The record is the method: what you were trying to make, how you set up the station, what failed first, and how you fixed it. The Recipe Book is the document that means a colleague can walk in cold and start where you left off, without having to ask you anything.*

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
sbatch slurm/extract_form_3_one_file.slurm

# 2. Monitor
squeue --me
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
> You will update this README in Boss Gate 4 when you scale with a job array.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="main"> README written and covers what the script does, how to run it, and where output lands</label>
