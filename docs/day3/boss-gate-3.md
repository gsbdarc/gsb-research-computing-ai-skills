---
layout: default
title: "Boss Gate 3"
parent: "Day 3 — The SLURM Mines"
nav_order: 10
permalink: /day3/boss-gate-3/
---

# Boss Gate 3

---

## Capstone — First SLURM Submission

Submit your Day 2 LLM extraction script as a SLURM batch job:

1. Write `jobs/extract.sh` with correct `#SBATCH` directives — time, memory, and partition based on your profiling from The Scales
2. Submit with `sbatch`; confirm the job enters the queue with `squeue -u $USER`
3. Wait for it to complete; inspect the output with `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS`
4. Update `README.md` with SLURM instructions — how to submit, how to monitor, where the output goes
5. Commit and push:

```bash
git add jobs/extract.sh README.md
git commit -m "Boss Gate 3: first SLURM submission complete"
git push
```

Your commit should include:
- `jobs/extract.sh` with `#SBATCH` directives based on real profiling, not guesses
- `README.md` — what the script does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## Skills This Capstone Tests

- Write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- Submit a job and confirm it entered the queue
- Read `sacct` output and identify whether the job succeeded or failed
- Write a README clear enough that a colleague could rerun the job without asking you
- Commit and push a complete deliverable: script and documentation together
