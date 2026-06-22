---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 3
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

*In the heart of the Mines hangs an ancient pair of scales, each arm tipped with iron. On one side: your job request. On the other: the truth of what your script actually consumes. Ask for too little and your process crashes mid-run, memory exhausted, data lost. Ask for too much and the scheduler hunts the entire cluster for a node massive enough to satisfy you — while your job rots in the queue. The Scales do not forgive guessing. They reward those who measure.*

---

## 🗡️ Main Quest

Before you write a single `#SBATCH` directive, you must step onto the floor of the Scales and weigh your work honestly.

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

## 📦 Side Quests

Two artifacts are hidden in this room for those willing to look back at their own footprints.

{: .chest }
> **Side Quest 1 — Sacct Scythe:** After your first sbatch job runs (from The Foreman's Desk), come back and run `sacct -j JOBID --format=JobID,Elapsed,MaxRSS,CPUTime`. Compare the actual usage to what you requested. Were your estimates close?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side1"> Sacct Scythe unlocked</label>

A second side quest waits — this one shows you not just what you used, but how wasteful (or prescient) your estimate really was.

{: .chest }
> **Side Quest 2 — Seff Sigil:** After a job completes, run `seff JOBID`. It shows CPU and memory efficiency as a percentage. What does it tell you about how well you estimated? What would you change in your `#SBATCH` directives?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side2"> Seff Sigil unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Sacct Scythe** — `sacct` post-mortem analysis of any job; see exactly what a job used in CPU time, wall time, and memory after it finishes.
>
> **Seff Sigil** — `seff JOBID` for a one-line efficiency report: CPU % and memory % of what you requested; find wasteful jobs before they become a pattern.

---

## 🧠 Skills Learned

- You can now time any script with `time` and translate wall-clock seconds directly into a confident `--time` request
- You can now watch memory climb in real time with `htop` and lock in a `--mem` value that won't lie
- You know that over-requesting isn't "safe" — it is the thing that makes the scheduler punish you with a longer wait
- You can now run `sacct` and `seff` after any job to audit your own estimates and sharpen every future request
