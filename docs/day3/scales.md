---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 3
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

*Every job request must be weighed before it is granted. Ask for too little and your script runs out of memory and crashes. Ask for too much and you wait in queue while the scheduler looks for a node big enough to satisfy your greedy request. The Scales teach you to measure what you actually need.*

---

## Main Quest

{: .important }
> **Quest:** Measure how long your script takes and how much memory it uses before writing a single `#SBATCH` directive.

**Step 1 — Time a script:**

```bash
time python3 count_spells.py ~/grimoire/
# Output:
# python3 count_spells.py ~/grimoire/  0.12s user 0.04s system 98% cpu 0.163 total
# The "real" (wall-clock) time is what matters for --time in SLURM
```

**Step 2 — Monitor memory with `htop`:**

In one terminal, start your script:
```bash
python3 my_pipeline.py &   # run in background
```

In another terminal (or screen pane):
```bash
htop -u $USER              # filter to your processes, watch RES column (resident memory)
```

**Step 3 — Run `userload` to see your impact:**

```bash
userload
# Find your username — confirm you're only using what you expected
```

**Rule of thumb for `#SBATCH` requests:**

- `--time`: take your measured wall-clock time × 2 (give yourself margin)
- `--mem`: take your peak memory × 1.5
- `--cpus-per-task`: count your actual Python threads; most single-threaded scripts need 1

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Sacct Scythe:** After your first sbatch job runs (from The Foreman's Desk), come back and run `sacct -j JOBID --format=JobID,Elapsed,MaxRSS,CPUTime`. Compare the actual usage to what you requested. Were your estimates close?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="chest1"> Sacct Scythe unlocked</label>

{: .chest }
> **Chest 2 — Seff Sigil:** After a job completes, run `seff JOBID`. It shows CPU and memory efficiency as a percentage. What does it tell you about how well you estimated? What would you change in your `#SBATCH` directives?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="chest2"> Seff Sigil unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Sacct Scythe** — `sacct` post-mortem analysis of any job; see exactly what a job used in CPU time, wall time, and memory after it finishes.
>
> **Seff Sigil** — `seff JOBID` for a one-line efficiency report: CPU % and memory % of what you requested; find wasteful jobs before they become a pattern.

---

## Skills Learned

- Measure wall-clock time with `time` before writing `--time` in a SLURM script
- Monitor memory usage with `htop` to set `--mem` accurately
- Understand that over-requesting delays your own jobs by making the scheduler search for larger nodes
- Use `sacct` and `seff` after a job to calibrate future requests
