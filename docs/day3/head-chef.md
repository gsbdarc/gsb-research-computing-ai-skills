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

## Main Exercise — See Your Shared Cluster

{: .important }
> **Exercise:** SSH into a Yen node, observe who is using the cluster right now, and profile a mystery script to measure its resource footprint.

**Step 1 — Connect to the Yens**

```bash
ssh YOUR_USERNAME@yen.stanford.edu
```

You'll land on one of the five interactive Yen nodes (`yen1`–`yen5`). The load balancer picks which one.

**Step 2 — See every process on this node**

```bash
htop
```

`htop` shows every running process from every user on this node:
- How many researchers are active right now?
- Who is using the most CPU?
- Who is using the most memory?

Press `q` to quit.

**Step 3 — See your own footprint**

```bash
userload
```

`userload` shows only **your** CPU and memory usage on this node — not other users. Right now it should be near zero since you haven't run anything yet.

{: .note }
> `htop` shows everyone's processes on the node. `userload` shows only your footprint. Use `htop` to see the full picture; use `userload` to check what you specifically are consuming.

When you can read both outputs — put a **🟢 green sticky** on your laptop. If something is not working, put up a **🔴 red sticky** and an instructor will come help.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="ssh"> I can SSH into the Yens and read the shared node with htop and userload</label>

---

**Step 4 — Profile a mystery script**

You're about to run a script whose resource usage you don't know. Your job: figure out what it's doing.

Open **two terminal tabs**, both connected to the Yens, and activate your environment in each:

```bash
cd ~/rf-bootcamp-2026
source .venv/bin/activate
```

In the **first terminal**, start the mystery script:

```bash
python scripts/mystery_script.py
```

Immediately in the **second terminal**, watch what it does:

```bash
htop -u $USER     # filter to your processes — watch RES (memory) and CPU% columns
userload          # see your total footprint on this node
```

When the script finishes, time it:

```bash
time python scripts/mystery_script.py
```

Compare with a neighbor. Do you see the same numbers? Based on what you measured, what `--time`, `--mem`, and `--cpus-per-task` would you ask from a scheduler?

When you can describe what the mystery script does to your CPU and RAM — put a **🟢 green sticky** on your laptop. If something is not working, put up a **🔴 red sticky** and an instructor will come help.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="mystery"> I profiled mystery_script.py and can describe what it uses</label>

---

## Optional Exercises — Cluster Tools

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Sort htop by memory**

In htop, press `F6`, select `MEM%`, press Enter. What is the #1 memory-consuming process on this node right now? How much RAM is it using?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="htop-mem"> I sorted htop by memory and identified the top consumer</label>

**Bonus 2 — Read ps output**

```bash
ps aux --sort=-%mem | head -15
```

Look at the VSZ and RSS columns. What is the difference between virtual memory (VSZ) and resident memory (RSS)?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="ps"> I can explain the difference between VSZ and RSS</label>

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

The interactive Yens are unusual compared to most HPC clusters: they serve double duty as both login nodes and light compute nodes. You can SSH in and run small exploratory work right there. Most clusters don't allow this — on typical HPC systems, the login node is strictly for job submission, and all computation goes through the scheduler.

The SLURM nodes are the other half: 12 dedicated nodes where nothing else is running. You never SSH to them. You write a job script, hand it to SLURM, and SLURM decides when and where it runs.

| | Interactive Yens | SLURM Scheduled Nodes |
|---|---|---|
| Nodes | 5 | 12 |
| How to access | SSH directly | Submit a job script |
| Wait for resources? | No | Yes — may queue |
| Cores shared between users? | Yes | No — yours alone |
| Notebooks? | Yes | No |
| Usage reporting | `userload`, `htop` | `sacct` |

Use the interactive Yens for: exploring data, testing code, runs where you're watching the terminal (or using `screen` to keep a session alive). Use SLURM for: anything that needs guaranteed resources, runs unattended, or shouldn't compete with other users.

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
