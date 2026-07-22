---
layout: default
title: "Exploring Cluster Usage Data"
parent: "Day 3 — Cluster Computing"
nav_order: 4
permalink: /day3/cluster-usage-data/
---

# Exploring Cluster Usage Data

<div data-room-id="d3-cluster-usage-data"></div>

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## What Is This Data?

The Yens run a monitoring script every few minutes that calls `top` in batch mode — the same tool you'd run interactively, but automated. It captures a snapshot of every process running on the node at that instant, then saves it as a CSV.

The file below is one such snapshot from yen1, taken on July 10, 2026 at 20:56. Each row is one process.

| Column | What it means |
|--------|---------------|
| `timestamp` | When the snapshot was taken |
| `host` | Which Yen node |
| `pid` | Process ID — unique number the OS assigns to each running program |
| `user` | SUNetID of the process owner |
| `pr` | Scheduling priority — lower numbers run first (`rt` means real-time priority) |
| `ni` | Nice value — a user-adjustable priority offset; negative = higher priority, positive = lower |
| `virt` | Virtual memory reserved by the process (bytes) |
| `res` | Resident memory — RAM physically in use right now (bytes) |
| `shr` | Shared memory (bytes) — memory the process shares with others, e.g. loaded libraries |
| `s` | Status: `R` = running (using CPU), `S` = sleeping (idle, holding RAM), `I` = idle kernel thread |
| `cpu_pct` | % of one CPU core in use — 100% means one full core (yen1 has 256 cores) |
| `mem_pct` | % of total node RAM in use |
| `time_plus` | Cumulative CPU time since the process started |
| `command` | Program name (`top` truncates long names to 8 characters) |
| `type` | `u` = user process, `s` = system/kernel process |

---

## Your Turn

Load the file and explore it **with Claude** — ask it about the columns, dig into what's running, and have it help you **make a visualization** of an insight you find.

```python
import pandas as pd

cols = ['timestamp','host','pid','user','pr','ni','virt','res','shr',
        's','cpu_pct','mem_pct','time_plus','command','type']

DATA = '/scratch/shared/gsb-research-computing-ai-skills/data/yenstop_2026-07-10-20-56-06.csv'

df = pd.read_csv(DATA, header=None, names=cols, on_bad_lines='skip')
df.head()
```

Some directions if you want a place to start — but don't feel limited to these:

- Who is using the most CPU? The most memory? Are they the same person?
- How many processes are actually running right now versus just sleeping?
- What commands appear most often? What do you think they are?
- How long have some of these processes been running? Does anything surprise you?
- What does virtual memory look like compared to resident memory for the same process?
- yen1 has about **1 TB of RAM**, and `mem_pct` is each process's share of that. What is the single biggest process using, in **GB**? Cross-check your answer against the `res` column — that's the actual bytes resident in RAM.

Make a plot. Ask Claude to explain something. Follow a thread that looks interesting.

---

## Write It Up

Find one thing in the data worth keeping. Add a short section to your `README.md` — a few sentences describing what you found and what it tells you about how shared research nodes actually get used.

When you're ready — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-cluster-usage-data" data-key="main"> I used Claude to explore the data, made a visualization, and wrote up one finding in README</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Per-User Limits vs. the Whole Node**

Group the processes by `user` and compute total `cpu_pct` and `mem_pct` per person. Then compare two different ceilings:

- the **per-user limit** — the cap any single researcher gets, and
- the **whole node's capacity** — the total cores and RAM on the specific Yen node you're on.

Look both up on the [Yen user limits page](https://rcpedia.stanford.edu/_policies/user_limits/) — they vary by node, so don't assume a fixed number.

Is anyone close to their per-user limit? And how much of the *entire node* is actually in use? A node can sit far from full even while one user is maxed out — that's the per-user limit doing its job: keeping any one job from starving everyone else on a shared machine.

<label class="quest-check"><input type="checkbox" data-room="d3-cluster-usage-data" data-key="side3"> I compared per-user usage against both the per-user limit and the whole node's capacity</label>

**Side quest — Watch It Live (`top`)**

The CSV you've been analyzing is a **photograph** — one frozen instant, captured by a script that ran `top` once and saved the result. `top` itself is the **live view**: the same numbers, refreshing every few seconds. SSH to a Yen node and run it:

```bash
top
```

Two parts to read:
- **The header block** (top few lines) is node-wide: load averages, task counts, overall `%Cpu(s)`, and total memory used/free.
- **The table below** is one row per process — the same fields as your CSV: `PID`, `USER`, `%CPU`, `%MEM`, `TIME+`, `S` (status), `COMMAND`.

While it's running, try these keys:
- `P` — sort by CPU (the default) · `M` — sort by memory
- `u`, then type a username and press Enter — show only that person's processes
- `q` — quit

Watch for a few seconds: which processes churn near a full core, and which just sit `S` (sleeping)? Press `q` to quit when you're done.

<label class="quest-check"><input type="checkbox" data-room="d3-cluster-usage-data" data-key="side5"> I ran `top` live on a Yen node, read the header and per-process columns, and can explain how it relates to the CSV snapshot</label>

