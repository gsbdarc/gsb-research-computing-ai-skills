# Documenting Your Pipeline — README Solution Key

**Instructor use only.** This file is not served by GitHub Pages. Show it in class *after* students have attempted their own README.

A complete example of the filled-in `README.md` skeleton:

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

**Author:** Jane Researcher
**Date:** 2026-07-22

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
```

Good things to look for in a student's README:
- **Author and date** filled in.
- **What this does** in plain language (what's extracted, from what, using what).
- **Runnable steps** — the actual submit / monitor / check-output commands.
- **Outputs** — which files land where, and what's in them.
- **Data** — the input and its source.
