---
layout: default
title: "The Head Chef"
parent: "Day 3 — The SLURM Mines"
nav_order: 3
permalink: /day3/head-chef/
---

# The Head Chef

<div data-room-id="d3-head-chef"></div>

---

## The Shared Cluster Problem

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else.

- CPU cores are **shared** between all users on the same node
- Per-user limits apply to CPU and RAM — but many researchers running at once still slows everyone down
- Long-running or CPU-heavy jobs belong on dedicated resources, not on a shared interactive node

The solution: a scheduler that reads every job request, knows what resources each job needs, and assigns work to **dedicated nodes** where nothing else is running.

---

## SLURM Is the Scheduler

SLURM manages **12 dedicated nodes** on the Yens — completely separate from the 5 interactive nodes — where batch jobs run with their own dedicated resources.

| Kitchen analogy | Yens / SLURM |
|---------|--------------|
| Head chef | SLURM scheduler |
| Station (stove) | Compute node |
| Burner | CPU core |
| Fridge | RAM |
| Warehouse | Shared storage (`/scratch`) |
| Order ticket | Job script (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Recipe | Your Python / R / shell script |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef, specify what resources you need, and come back when the job is done.

---

## Interactive Yens vs SLURM Nodes

| | Interactive Yens | SLURM Scheduled Nodes |
|---|---|---|
| Nodes | 5 | 12 |
| How to access | SSH directly | Submit a job script |
| Wait for resources? | No | Yes — may queue |
| Cores shared between users? | Yes | No — yours alone |
| Notebooks? | Yes | No |
| Usage reporting | `userload`, `htop` | `sacct` |

You do **not** SSH to SLURM nodes — the scheduler sends your job there.

---

## Main Exercise — Peek at the Queue

{: .important }
> **Exercise:** Look at the live SLURM queue to see what jobs are waiting or running right now.

```bash
squeue
```

Look at the columns:
- **JOBID** — unique ID for each job
- **ST** — status: `R` = running, `PD` = pending (waiting in queue for resources)
- **TIME** — how long the job has been running
- **NODELIST** — which compute node it landed on

Check your own queue (probably empty for now):

```bash
squeue -u $USER
```

Every `PD` job is waiting for a node with the resources it requested. When SLURM finds a matching node — it runs.

When you can read the queue and explain the difference between `R` and `PD` to a neighbor — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="main"> I understand why SLURM exists and can read the job queue with squeue</label>

---

## Optional Exercises

{: .note }
> Finished early? Try this.

**Bonus 1 — Explore partitions with sinfo**

```bash
sinfo
```

- How many compute nodes are currently idle (`STATE=idle`)?
- What partitions (queues) exist? Which one would you use for a normal job?
- What is the maximum time limit for each partition?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side1"> I ran sinfo and can describe the Yens partitions and node states</label>

---

## Key Concepts

- SLURM is the scheduler that manages 12 dedicated compute nodes on the Yens
- You do not SSH to SLURM nodes — you submit a job script with `sbatch`
- `squeue` shows the job queue; `R` = running, `PD` = pending
- Interactive Yens (5 nodes): shared, instant, for development; SLURM nodes (12): dedicated, queued, for production
