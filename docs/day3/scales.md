---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 4
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

*In the heart of the Mines hangs an ancient pair of scales, each arm tipped with iron. On one side: your job request. On the other: the truth of what your script actually consumes. Ask for too little and your process crashes mid-run, memory exhausted, data lost. Ask for too much and the scheduler hunts the entire cluster for a node massive enough to satisfy you — while your job rots in the queue. The Scales do not forgive guessing. They reward those who measure.*

---

## 🖊️ Why Parallelize?

Your Day 2 script processes one SEC filing in a few seconds. You have 100 filings. Running them one at a time takes 100× as long — and ties up a terminal window while you wait.

The Yens have hundreds of cores sitting idle. SLURM's job: hand each core a different filing so all 100 run simultaneously. Total time stays roughly the same as one filing — just multiplied across independent work.

```
  One at a time (your laptop):       Parallelized (SLURM):
  filing 1 → 5s                      filing 1  ┐
  filing 2 → 5s                      filing 2  │ all start at once
  filing 3 → 5s                      filing 3  │ → ~5s total
  ...                                ...       ┘
  filing 100 → 5s
  ─────────────
  Total: ~500s                        Total: ~5s + queue wait
```

This only works when tasks are **independent** — each filing doesn't need the results from another. Your extraction script qualifies perfectly.

---

## 🗡️ Main Quest

Before you write a single `#SBATCH` directive, you must step onto the floor of the Scales and weigh your work honestly.

The tricky part of ordering from the head chef: when you write your recipe, you don't yet know how much kitchen you need.

```
  Before submitting a SLURM job, you need to know:

  How many burners (CPUs)?   →  --cpus-per-task
  How long on the stove?     →  --time
  How much fridge (RAM)?     →  --mem
  How many trips to the      →  (affects wall time — I/O bound vs compute bound)
  warehouse?
```

You measure first, then request. Not the other way around.

{: .important }
> **Quest:** Run the extraction script interactively, understand what it does, then measure its resource footprint before writing a single `#SBATCH` directive.

**Step 0 — Run the script and understand it:**

```bash
# Look at the script you built in Day 2
cat ~/rf-bootcamp-2026/form3_test.py

# Run it on one filing
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python form3_test.py
```

What does the script do? What output do you see? How long did it seem to take? Now you're ready to measure it properly.

**Step 1 — Time a script:**

```bash
time python form3_test.py
# Output:
# python form3_test.py  1.83s user 0.21s system 97% cpu 2.099 total
# The "real" (wall-clock) time is what matters for --time in SLURM
```

**Step 2 — Monitor memory with `htop`:**

In one terminal, start your script:
```bash
python3 my_pipeline.py &   # run in background
```

In another terminal:
```bash
htop -u $USER              # filter to your processes, watch RES column (resident memory)
```

**Step 3 — Run `userload` to see your impact:**

```bash
userload
# Shows YOUR CPU and memory usage on this interactive Yen node
# Confirm you're only using what you expected — not accidentally pegging a shared machine
```

**Step 4 — Monitor a script you haven't profiled before:**

Open two terminal tabs. In the first, run a script whose resource profile you don't know:

```bash
python scripts/mystery_script.py
```

Immediately in the second terminal, watch it:

```bash
htop -u $USER     # watch RES (resident memory) and CPU % columns
userload          # see your footprint vs other users on the cluster
```

If it finishes too quickly to catch, wrap it with `time`:

```bash
time python scripts/mystery_script.py
```

Compare with a neighbor — do you see the same numbers? Based on what you measured, what `--time`, `--mem`, and `--cpus-per-task` would you request?

---

**Rule of thumb for `#SBATCH` requests:**

- `--time`: take your measured wall-clock time × 2 (give yourself margin)
- `--mem`: take your peak memory × 1.5
- `--cpus-per-task`: count your actual Python threads; most single-threaded scripts need 1

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="main"> Main Quest complete</label>
