---
layout: default
title: "The Watch Tower"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/watch-tower/
---

# The Watch Tower

<div data-room-id="d3-watch-tower"></div>

*From the tower you can see every job moving through the kitchen. Which ones are running, which are waiting, which have failed. The Watch Tower is not exciting — but it has saved more research projects than any other room in the dungeon. Know what your jobs are doing before they finish.*

---

## Main Quest

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
tail -f logs/first_job_JOBID.out     # follow the log file live
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

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="main"> Main Quest complete</label>

---

## Chest

{: .chest }
> **Chest 1 — Watch Wand:** Set up a one-liner alias in `~/.bash_profile` that runs `watch -n 5 squeue -u $USER` with the command `myq`. You should be able to type `myq` at any time and see your live job queue.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="chest1"> Watch Wand unlocked</label>

---

## Weapon Earned

{: .weapon }
> **Watch Wand** — `watch -n 5 squeue -u $USER` as a live dashboard alias; never open a browser to check job status when a terminal command does it better.

---

## Skills Learned

- Check job status with `squeue` and interpret state codes (PD/R/CG/F)
- Cancel a running or pending job with `scancel`
- Audit completed jobs with `sacct` to see actual resource usage
- Follow job output live with `tail -f` without waiting for the job to finish
