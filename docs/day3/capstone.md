---
layout: default
title: "Day 3 Capstone"
parent: "Day 3 — Cluster Computing"
nav_order: 10
permalink: /day3/capstone/
---

# Day 3 Capstone

---

## The Capstone — Scale to 100 filings

All day you've profiled and run **10 filings**. The capstone: scale to **100** — and **estimate what it needs *before* you run it**.

**Step back — what are we actually doing?** Each "filing" is a real **SEC Form 3**; your script hands it to the **Stanford AI API**, which reads it and returns the structured fields. Scaling to 100 doesn't change that shape: the batch still walks the filings **one at a time**, making one blocking API call per filing and waiting for the answer before starting the next. That's why this job is **I/O-bound** — as you saw in profiling, the wall-clock time grows with the number of filings while RAM and CPU stay about flat.

### 1. Estimate the resources for 100 filings — and write it down first

You're running the same loop, just over 100 files instead of 10. Think about what **CPU**, **RAM**, and **time** it will take. Open `scripts/extract_form_3_batch.py` (or have Claude read it) and reason it out:

> Look at `scripts/extract_form_3_batch.py` and my Profiling README (the 10-filing numbers) and help me estimate the CPU, RAM, and wall-clock time this needs for 100 filings.

**Before you submit anything**, write in your `README.md`: which resources you think will **scale** with the number of filings processed and which will stay about flat — and **why** — along with your CPU, RAM, and wall-clock **estimate for 100**. Committing to a number *before* you run it is the whole point.

**Zoom out:** *the task hasn't changed — you're still sending each SEC Form 3 filing to the Stanford AI API to extract its structured fields. There are just **100** of them now, processed one after another in a loop. You're sizing the resources for that loop.*

### 2. Write a SLURM script for the batch

You already built `slurm/extract_form_3_batch.slurm` for **10 filings** on the SLURM-job page. Now scale it: bump `NUM_FILINGS` to `100` in `scripts/extract_form_3_batch.py`, and re-tune `--time`, `--mem`, and `--cpus-per-task` in the `.slurm` with **your estimates for 100** (make sure the email-notification lines are there so you get a completion email).

**Zoom out:** *it's still one Python script with a big `for` loop — for each of the 100 Form 3 filings: read it, send it to the API, save the structured data. The SLURM script just runs that single script, once, on the cluster.*

### 3. Submit and confirm it ran

```bash
sbatch slurm/extract_form_3_batch.slurm
squeue --me
```

Wait for the completion email. From it — and from `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS` — note **how long it took** and **how much CPU/RAM it actually used** versus what you requested.

**Zoom out:** *right now the cluster is working through 100 Form 3 filings, one API call at a time, pulling structured fields out of each.*

### 4. Compare actual vs. your estimate

Back in `README.md`, next to the estimate you wrote in step 1, add the **actual** numbers from the email and `sacct`, and note whether you **over- or under-estimated** each resource — and by how much. That comparison is the payoff; next time you'll estimate better.

**Zoom out:** *those numbers are the real cost of 100 sequential API calls extracting data from Form 3 filings — the actual work, now measured.*

### 5. Commit and push from the Yens

Ask Claude Code to handle it:

> Add and commit `slurm/extract_form_3_batch.slurm` and my README changes with a message like "Day 3 Capstone: 100-filing batch", then push to my fork.

**Zoom out:** *what you're saving is that pipeline — loop over Form 3 filings, extract structured data via the API — now proven at 100.*

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-capstone" data-key="commit"> I estimated resources for 100 filings, ran the batch, compared actual vs. requested from the email, documented over/under-estimation in my README, and pushed to my fork</label>

---

## Finished early? Climb the leaderboard

Got time left? Go back through Day 3 and knock out any quests you skipped — every quest you complete and sync bumps your total and your rank on the leaderboard. (Each checked quest has a **🔮 Cast to the leaderboard** button; run its `./cast` spell from your repo root on the Yens to update your standing.)

{: .note }
> **Done and synced?** Bring any lingering Day 3 questions to the instructors — now's the time to ask.

---

## Day 3 — What You Learned

- **Compute environments** — CPU cores, RAM, and storage, and how laptop vs. Yens vs. cloud trade off.
- **Profiling** — measuring a script's time, CPU, and RAM with `time`, `userload`, and `htop`; telling **serial from parallel** and **CPU-bound from I/O-bound** work.
- **Reading real cluster data** — exploring a live monitoring snapshot, and per-user vs. whole-node limits.
- **SLURM** — why a scheduler exists; reading the queue and partitions (`squeue`, `sinfo`, QoS caps).
- **Running jobs** — writing a SLURM script from scratch, submitting/monitoring/cancelling, reading `.out`/`.err` logs, and **debugging failed jobs** (code bug vs. OOM vs. timeout).
- **Resource estimation & scaling** — profiling a small run, estimating a bigger one, and checking your estimate against what the job actually used.
- **Reproducibility** — a README a colleague (or future you) can actually rerun.

You now have the full loop every real research pipeline needs: **estimate → request → run → check → document.**
