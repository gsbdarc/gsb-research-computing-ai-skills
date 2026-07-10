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

## Computing Resources — A Quick Recap

On the last page we introduced the kitchen analogy. Before we run anything, let's make sure we have the vocabulary:

| Resource | What it is |
|----------|-----------|
| **CPU core** | An individual worker that executes your code |
| **RAM** | Fast memory the CPU reads from while working |
| **Storage (file system)** | Where your files live — VAST on the Yens |
| **Time** | How long your script takes to finish |

---

## 💻 Exercise 1 — Run Your Script

{: .important }
> **Exercise:** Run your Day 2 extraction script on the Yens interactively and think about its resource footprint.

If you're not already connected, SSH in:

```bash
ssh SUNetID@yen.stanford.edu
cd ~/rf-bootcamp-2026
source .venv/bin/activate
```

Run the script:

```bash
python scripts/extract_form_3_one_file.py
```

While it runs (or after it finishes), discuss as a class:

- ❓ **Why** do we want to estimate the resources a script uses?
- ❓ Do you know what resources this script is using right now?
- ❓ How would you estimate them?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="exercise3"> I ran the script and understand why we want to estimate its resource usage</label>

This page will teach you **how to estimate the resources your script is actually using**. This matters whether you wrote the script yourself or someone handed it to you.

---

## 💻 Exercise 2 — Profile a Mystery Script

You are going to run a script you have never seen before and figure out what resources it uses — without reading the code. This is called **profiling**: measuring a script's time, CPU, and RAM usage as it runs. The technique is simple: one terminal runs the script, a second terminal on the **same node** watches it live.

{: .important }
> **Exercise:** Run `mystery_script.py` and measure its resource usage in real time using two terminals — both on the **same Yen node**.

**Step 1 — Note which Yen you are on.**

In your current terminal, run:

```bash
hostname
```

You will see something like `yen2`. Remember this — your second terminal must connect to the exact same node.

**Step 2 — Open a second terminal on the same node.**

In the new terminal, SSH directly to that node by name (not the load-balanced `yen.stanford.edu`, which could land you on a different machine):

```bash
ssh SUNetID@yen2.stanford.edu   # replace yen2 with whatever hostname showed above
```

**Step 3 — Run the script in Terminal 1, monitor with `watch userload` in Terminal 2.**

Terminal 1:
```bash
time python scripts/mystery_script.py
```

When the script finishes, `time` prints three lines:

```
real    0m31.234s
user    2m0.682s
sys     0m2.212s
```

- **real** — wall-clock time: how long you actually waited
- **user** — CPU time your code consumed across all cores; if `user` > `real`, the script used multiple cores in parallel
- **sys** — CPU time spent on OS-level work (file I/O, memory allocation)

Terminal 2:
```bash
watch userload
```

- `userload` shows your **total CPU% and total RAM** across all your processes on this node — your footprint
- Jupyter processes are tracked separately and are not included
- `watch` re-runs it every 2 seconds so you can see it change while the script runs
- See the [current per-user limits](https://rcpedia.stanford.edu/_policies/user_limits/) for how much CPU and RAM any one user can use on an interactive Yen

**Step 4 — Run the script again. This time monitor with `htop -u $USER` in Terminal 2.**

Terminal 1:
```bash
time python scripts/mystery_script.py
```

Terminal 2:
```bash
htop -u $USER
```

**Compare with your neighbor:**
- How long did it take?
- How many CPU cores did it use?
- How much RAM did it peak at?
- Is this script **serial** (one core) or **parallel** (multiple cores)? How can you tell?

{: .note }
> **Definitions**
> - **Profiling** — measuring a script's resource usage (time, CPU, RAM) as it runs
> - **Serial** — the script uses one CPU core at a time; `user` time ≈ `real` time
> - **Parallel** — the script uses multiple cores simultaneously; `user` time > `real` time

When you can describe what the mystery script does to your CPU and RAM — put a **🟢 green sticky** on your laptop. If something is not working, put up a **🔴 red sticky** and an instructor will come help.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="mystery"> I profiled mystery_script.py and I understand its time, CPU, and RAM usage</label>

---

## Interactive Yens

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

## The Yen-SLURM Cluster

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else.

- CPU cores are **shared** between all users on the same node
- Per-user limits apply to CPU and RAM — but many researchers running at once still slows everyone down
- Long-running or CPU-heavy jobs belong on dedicated resources, not on a shared interactive node

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

---

## Key Concepts

- Measure resource usage before requesting — time, CPU cores, and RAM
- `htop` and `userload` show you what a script is consuming while it runs
- Interactive Yens (5 nodes): shared, instant, for development and testing
- SLURM nodes (12): dedicated, queued, for production jobs
- You do not SSH to SLURM nodes — you submit a job script with `sbatch`
- `squeue` shows the job queue; `R` = running, `PD` = pending
