---
layout: default
title: "The Head Chef"
parent: "Day 3 — The SLURM Mines"
nav_order: 3
permalink: /day3/head-chef/
---

# The Head Chef

<div data-room-id="d3-head-chef"></div>

*You watched the kitchen. Seventeen researchers, five stoves, no posted rules — someone's roast burns while someone else waits forever for a free burner. The interactive Yens have per-user limits, but nothing stops everyone's jobs from competing and slowing each other down. The solution is a head chef: someone — or something — that reads every order, knows what equipment each job needs, and routes work to dedicated stations where no one else is cooking. That is SLURM.*

---

## The Shared Kitchen Problem

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else.

- Cores are **shared** between all users on the same node
- Per-user limits apply to CPU and RAM — but many researchers running at once still slows everyone down
- Long-running or CPU-heavy jobs belong somewhere dedicated, not on a shared interactive node

You need a head chef who can assign work to **dedicated stations** where nothing else is running.

---

## SLURM Is the Head Chef

SLURM is a scheduler. On the Yens, SLURM manages **12 dedicated nodes** — completely separate from the interactive Yens — where batch jobs run with their own dedicated resources.

| Kitchen | Yens / SLURM |
|---------|--------------|
| Head chef | SLURM scheduler |
| Station (stove) | Compute node |
| Burner | CPU core |
| Fridge | RAM |
| Warehouse | Shared storage (`/scratch`) |
| Order ticket | Job script (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Recipe | Your Python / R / shell script |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef, tell them what equipment you need, and come back when the meal is done.

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

## 🗡️ Main Quest — Peek at the Queue

{: .important }
> **Quest:** Look at the live SLURM queue to see what jobs are waiting or running right now.

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

You're looking at the real Yens job queue. Every `PD` job is waiting for a node with the resources it requested. When SLURM finds a matching node — it runs.

When you can read the queue and explain the difference between `R` and `PD` to a neighbor — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="main"> I understand why SLURM exists and can read the job queue with squeue</label>

---

## Skills Learned

- SLURM is the scheduler that manages 12 dedicated compute nodes on the Yens
- You do not SSH to SLURM nodes — you submit a job script with `sbatch`
- `squeue` shows the job queue; `R` = running, `PD` = pending
- Interactive Yens (5 nodes): shared, instant, for development; SLURM nodes (12): dedicated, queued, for production
