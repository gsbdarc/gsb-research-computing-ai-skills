---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

---

## Main Exercise — Profile Your Script

Before submitting a job to SLURM, you need to know what resources it actually needs:

```
  How many CPUs?     →  --cpus-per-task
  How long?          →  --time
  How much RAM?      →  --mem
```

You measure first, then request. Not the other way around.

{: .important }
> **Exercise:** Run the extraction script interactively and measure its resource footprint before writing any `#SBATCH` directives.

**Step 0 — Run the script and understand it:**

```bash
# Look at the script you built in Day 2
cat ~/rf-bootcamp-2026/scripts/extract_form_3_one_file.py

# Run it on one filing
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python scripts/extract_form_3_one_file.py
```

What does the script do? What output do you see? How long did it seem to take?

When the script finishes successfully — put a **🟢 green sticky** on your laptop. If it errors or the venv won't activate, put up a **🔴 red sticky**.

**Step 1 — Time it:**

```bash
time python scripts/extract_form_3_one_file.py
# Output:
# python scripts/extract_form_3_one_file.py  1.83s user 0.21s system 97% cpu 2.099 total
# The "real" (wall-clock) time is what matters for --time in SLURM
```

**Step 2 — Monitor memory with htop:**

In one terminal, start your script:
```bash
python scripts/extract_form_3_one_file.py &   # run in background
```

In another terminal:
```bash
htop -u $USER              # filter to your processes, watch RES column (resident memory)
```

**Step 3 — Check your impact with userload:**

```bash
userload
# Shows YOUR CPU and memory usage on this interactive Yen node
# Confirm you're only using what you expected
```

---

**Rule of thumb for `#SBATCH` requests:**

- `--time`: measured wall-clock time × 2 (give yourself margin)
- `--mem`: peak memory × 1.5
- `--cpus-per-task`: count your actual Python threads; most single-threaded scripts need 1

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="main"> I profiled extract_form_3_one_file.py and know what --time, --mem, and --cpus-per-task to request</label>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Verbose time**

The `/usr/bin/time -v` command gives much more detail than the shell `time` builtin:

```bash
/usr/bin/time -v python scripts/extract_form_3_one_file.py
```

Find the line that says **"Maximum resident set size"** in the output. This is the peak RAM the process held at any point. How does it compare to what you saw in `htop`?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side1"> I used /usr/bin/time -v and found the peak memory (maximum resident set size)</label>

**Bonus 2 — Scaling estimate**

Edit `scripts/extract_form_3_batch.py` to process only 5 filings. Find the line that builds the URL list and add a slice:

```python
urls = [u for u in urls if u.endswith(".txt")][:5]
```

Time it. Then try 10. Does the time scale roughly linearly? Based on that, estimate how long processing all 994 filings would take.

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side2"> I estimated scaling: how long would processing all 994 filings take?</label>
