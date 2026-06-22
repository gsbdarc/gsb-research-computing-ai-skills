---
layout: default
title: "The Watch Tower"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
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

## 📦 Chests

Hidden in the tower wall is a carved niche — inside, a wand that summons your entire job queue with a single whispered word.

{: .chest }
> **Chest 1 — Watch Wand:** Set up a one-liner alias in `~/.bash_profile` that runs `watch -n 5 squeue -u $USER` with the command `myq`. You should be able to type `myq` at any time and see your live job queue.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="chest1"> Watch Wand unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Watch Wand** — `watch -n 5 squeue -u $USER` as a live dashboard alias; never open a browser to check job status when a terminal command does it better.

---

## 🧠 Skills Learned

- You can now see exactly what your jobs are doing — live — and read their state codes (PD/R/CG/F) at a glance
- You can surgically cancel a runaway job with `scancel` before it wastes your compute allocation
- You can summon a full post-mortem on completed jobs with `sacct` and see exactly how much memory and CPU they really used
- You can tail a live log with `tail -f` and watch your results appear in real time, line by line, before the job even finishes
