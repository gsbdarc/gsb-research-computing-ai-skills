---
layout: default
title: "The Watch Tower"
parent: "Day 3 — The SLURM Mines"
nav_order: 6
permalink: /day3/watch-tower/
---

# The Watch Tower

<div data-room-id="d3-watch-tower"></div>

*You climb the spiral stairs and emerge into open air. The entire SLURM Mines sprawl below you — a living map of computation. Glowing threads mark jobs racing across nodes, amber embers pulse where work waits in line, and cold dark patches mark jobs that have already died. Most adventurers throw their jobs into the queue and hope for the best. You will be different. From this tower, nothing moves without your knowledge.*

---

## 🗡️ Main Quest

Your jobs are running somewhere in the cluster right now — let's find them, watch them breathe, and pull the plug if anything goes wrong.

{: .important }
> **Quest:** Monitor the job you submitted in The Foreman's Desk using `squeue`, `scancel`, and `sacct`.

**Check your jobs:**
```bash
squeue -u $USER              # show only your jobs
squeue -u $USER -l           # long format: more details
```

Status codes:
- `PD` — pending (waiting for resources)
- `R` — running
- `CG` — completing
- `F` — failed

**Watch a job live:**
```bash
watch -n 5 squeue -u $USER   # refresh every 5 seconds — Ctrl-C to stop
```

**Read the output as it writes:**
```bash
tail -f logs/extract_JOBID.out       # follow the log file live (replace JOBID with your number)
```

**Cancel a job:**
```bash
scancel JOBID                # cancel one job
scancel -u $USER             # cancel all your jobs (use carefully)
```

**Audit after completion:**
```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS,CPUTime --starttime=today
```

{: .warning }
> **Job shows `FAILED`?**
> 1. Read the log: `cat logs/extract_JOBID.out` (and `.err` if it exists)
> 2. Fix the issue — wrong path, missing module, out-of-memory, script error
> 3. Resubmit: `sbatch jobs/extract.sh`

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="main"> Main Quest complete</label>
