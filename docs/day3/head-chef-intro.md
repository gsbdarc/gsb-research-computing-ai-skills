---
layout: default
title: "The Head Chef"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/head-chef/
---

# The Head Chef

<div data-room-id="d3-head-chef"></div>

---

## Interactive Yens

The interactive Yens are unusual compared to most HPC clusters: they serve double duty as both login nodes and compute nodes. You can SSH in and run work right there. Most clusters don't allow this — on typical HPC systems, the login node is strictly for job submission.

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else. CPU cores and RAM are **shared** between all users on the same node, and per-user limits are enforced — but many researchers running at once still slows everyone down.

| | Interactive Yens |
|---|---|
| Nodes | 5 (`yen1`–`yen5`) |
| How to access | SSH directly |
| Wait for resources? | No |
| CPU / RAM shared among users? | Yes |
| Notebooks? | Yes |
| GPUs? | No |

Use the interactive Yens for: exploring data, testing code, runs where you're watching the terminal (or using [`screen`](https://rcpedia.stanford.edu/_user_guide/screen/) to keep a session alive).

---

## The Yen-SLURM Cluster

Long-running or CPU-heavy jobs belong on dedicated resources, not on a shared interactive node.

The solution: a scheduler. SLURM reads every job request, knows what resources each job needs, and assigns work to **dedicated nodes** where nothing else is running.

| Kitchen analogy | Yens / SLURM |
|---------|--------------|
| Head chef | SLURM scheduler |
| Station (stove) | Compute node |
| Burner | CPU core |
| Fridge | RAM |
| Warehouse | Shared file system (VAST) |
| Order ticket | Job script (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Recipe | Your Python / R / shell script |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef, specify what resources you need, and come back when the job is done.

{: .note }
> **Why does this matter?** When you submit a job to the cluster, you have to tell the scheduler exactly how much CPU, RAM, and time your job needs. If you ask for too little, your job fails. If you ask for too much, you wait longer in the queue and waste shared resources. The only way to know what to ask for is to **measure first**.

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
