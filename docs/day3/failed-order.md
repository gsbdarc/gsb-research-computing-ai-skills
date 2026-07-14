---
layout: default
title: "Failed Order"
parent: "Day 3 — The Hearth"
nav_order: 8
permalink: /day3/failed-order/
---

# Failed Order

<div data-room-id="d3-watch-tower"></div>

*The order came back. Parchment crumpled, stamped FAILED in red, sitting on the rail where you left it hours ago. You burned the pancakes. Maybe the venv wasn't active on the compute node. Maybe the path was wrong. Maybe you asked for 2G of fridge space and the recipe needed 8. The head chef doesn't explain. He just stamps it and sends it back. Reading the wreckage — that's your job.*

---

## Main Exercise — Debug and Fix Your Job

{: .important }
> **Exercise:** Your job failed. Find out why, fix the script, and resubmit until it completes successfully.

**Step 1 — Check the status**

```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS --starttime=today
```

Look for your job in the `State` column. A failed job shows `FAILED`.

**Step 2 — Read the logs**

Your job writes output to `logs/extract_JOBID.out` and errors to `logs/extract_JOBID.err`. Start with the error log:

```bash
cat logs/extract_JOBID.err
```

Then check the output log:

```bash
cat logs/extract_JOBID.out
```

The error message tells you what went wrong — a wrong path, a missing module, a Python exception. Read it carefully.

**Step 3 — Fix the script**

Once you've found the bug, fix it. Test interactively on the Yens first to confirm the fix works:

```bash
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python scripts/extract_form_3_batch.py
```

**Step 4 — Resubmit**

```bash
sbatch jobs/extract.slurm
```

Check it enters the queue and eventually completes:

```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS --starttime=today
```

When your job shows `COMPLETED` — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="main"> I found the bug, fixed it, resubmitted, and my job shows COMPLETED</label>

{: .note }
> 🔄 Ask Claude: "Set `d3-watch-tower.main` to `true` in `quest_log.json` at my repo root (create it if missing), then commit and push it."

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Audit your resource usage**

After your job completes, compare what you requested vs what you actually used:

```bash
sacct -j JOBID --format=JobID,AllocCPUS,CPUTime,MaxRSS,ReqMem,Elapsed
```

- **AllocCPUS** — CPUs you requested
- **MaxRSS** — peak RAM the job actually used
- **ReqMem** — RAM you requested

Did you over-request memory? Use these numbers to calibrate your next job's `--mem` and `--cpus-per-task`.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side1"> I audited my resource usage and know whether I over- or under-requested</label>

{: .note }
> 🔄 Ask Claude: "Set `d3-watch-tower.side1` to `true` in `quest_log.json` at my repo root (create it if missing), then commit and push it."

**Bonus 2 — Watch a job live**

While your job is running (status `R`), you can follow the output as it writes:

```bash
tail -f logs/extract_JOBID.out
```

Ctrl-C to stop following. This is useful for long jobs where you want to see progress without waiting for completion.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side2"> I followed a running job's output live with tail -f</label>

{: .note }
> 🔄 Ask Claude: "Set `d3-watch-tower.side2` to `true` in `quest_log.json` at my repo root (create it if missing), then commit and push it."
