---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

*In the heart of the Mines hangs an ancient pair of scales, each arm tipped with iron. On one side: your job request. On the other: the truth of what your script actually consumes. Ask for too little and your process crashes mid-run, memory exhausted, data lost. Ask for too much and the scheduler hunts the entire cluster for a node massive enough to satisfy you — while your job rots in the queue. The Scales do not forgive guessing. They reward those who measure.*

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
cat ~/rf-bootcamp-2026/scripts/extract_form_3_one_file.py

# Run it on one filing
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python scripts/extract_form_3_one_file.py
```

What does the script do? What output do you see? How long did it seem to take? Now you're ready to measure it properly.

When the script finishes successfully — put a **🟢 green sticky** on your laptop. If it errors or the venv won't activate, put up a **🔴 red sticky**.

**Step 1 — Time a script:**

```bash
time python scripts/extract_form_3_one_file.py
# Output:
# python scripts/extract_form_3_one_file.py  1.83s user 0.21s system 97% cpu 2.099 total
# The "real" (wall-clock) time is what matters for --time in SLURM
```

**Step 2 — Monitor memory with `htop`:**

In one terminal, start your script:
```bash
python scripts/extract_form_3_one_file.py &   # run in background
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

---

**Rule of thumb for `#SBATCH` requests:**

- `--time`: take your measured wall-clock time × 2 (give yourself margin)
- `--mem`: take your peak memory × 1.5
- `--cpus-per-task`: count your actual Python threads; most single-threaded scripts need 1

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="main"> Main Quest complete</label>
