---
layout: default
title: "The Watch Tower"
parent: "Day 3 — The SLURM Mines"
nav_order: 8
permalink: /day3/watch-tower/
---

# The Watch Tower

<div data-room-id="d3-watch-tower"></div>

---

## Main Exercise — Monitor Your Job

{: .important }
> **Exercise:** Monitor the job you submitted in The Ticket Rail using `squeue`, `scancel`, and `sacct`.

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

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="main"> My job shows COMPLETED in sacct and I have read the output log</label>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Audit your resource usage**

After your job completes, run sacct with a custom format to compare requested vs used:

```bash
sacct -j JOBID --format=JobID,AllocCPUS,CPUTime,MaxRSS,ReqMem,Elapsed
```

- **AllocCPUS** — CPUs you requested
- **MaxRSS** — peak RAM the job actually used
- **ReqMem** — RAM you requested

Did you over-request memory (MaxRSS much smaller than ReqMem)? Use these numbers to calibrate your next job's `--mem` and `--cpus-per-task`.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side1"> I audited my resource usage with sacct and know whether I over- or under-requested</label>

**Bonus 2 — Read a failure**

Open your `.err` log:

```bash
cat logs/extract_JOBID.err
```

Is it empty? Good — that means no errors were written to stderr.

Now intentionally break the script — edit `jobs/extract.sh` to use a wrong path (e.g., change `.venv` to `.venv_broken`) and run it locally:

```bash
bash jobs/extract.sh
```

What does a failure look like? This is the same thing you'd see in the `.err` log when a SLURM job fails. Put the path back when you're done.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side2"> I intentionally broke and read a failed run — I know what errors look like</label>
