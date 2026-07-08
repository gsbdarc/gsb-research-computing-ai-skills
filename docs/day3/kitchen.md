---
layout: default
title: "The Kitchen"
parent: "Day 3 — The SLURM Mines"
nav_order: 2
permalink: /day3/kitchen/
---

# The Kitchen

<div data-room-id="d3-kitchen"></div>

*Steam hangs in the air. Seventeen other researchers are already in here — one has a slow roast that's been in the oven for six hours, two more are fighting over the last open burner, and somewhere in the back a job has been queued so long it's practically fossilized. This is the Yens cluster at peak hours, rendered in cast iron and fire. Watch it breathe before you even think about striking a match. Once you see the chaos, SLURM stops being bureaucracy and starts being salvation.*

---

## The Kitchen Analogy

Every computer — your laptop, the Yens, a cloud server — is just a kitchen. The hardware is the kitchen equipment. The software is the recipe.

---

**Your kitchen — your laptop**

![Your Kitchen = Your Laptop]({{ site.baseurl }}/assets/images/kitchen-laptop.png)

---

**What happens when you run a script:**

![What Happens When You Run a Python Script on Your Laptop?]({{ site.baseurl }}/assets/images/kitchen-script-laptop.png)

---

**Shared restaurant kitchen — the Yens**

![Yen Cluster = A Shared Restaurant Kitchen]({{ site.baseurl }}/assets/images/kitchen-yens.png)

---

**Rented kitchen — cloud (AWS / GCP / Azure)**

![Cloud Computing = A Rented Kitchen]({{ site.baseurl }}/assets/images/kitchen-cloud.png)

---

## Your Research Project in Kitchen Terms

Every research computing project has three questions:

**What** am I doing?
Talk to your PI — this is your task. For this bootcamp: extract names and CIKs from SEC Form 3 filings. In kitchen terms, you're making a specific dish.

**Where** am I doing it?
Pick your kitchen: your laptop, the Yens, Sherlock, the cloud. Each has different equipment. You choose based on how much you need to cook and who else is cooking.

**How** am I doing it?
Your Python script is the recipe — step-by-step instructions to produce a dish:

```python
# Recipe: pasta.py
# 1. Boil water
# 2. Add pasta
# 3. While pasta cooks:
#      → make_sauce()   ← calls another recipe (a function)
# 4. Mix and serve
```

Each step is an operation or a call to another function. The result is your dish — extracted names, CIKs, a CSV.

---

## Kitchen Demo

*Your instructor will walk through the kitchen slides and lead the discussion below.*

- Which kitchen are you working in for this bootcamp?
- What are the tradeoffs between your laptop, the Yens, and the cloud?
- What happens when 10 researchers all try to cook at once on the shared Yens?

---

## 🗡️ Main Quest — See Your Shared Kitchen

Before we talk about how to schedule work, let's see the shared kitchen in action right now.

{: .important }
> **Quest:** SSH into a Yen node and see who is cooking — and how much they're using.

**Step 1 — Connect to the Yens**

```bash
ssh YOUR_USERNAME@yen1.stanford.edu
```

**Step 2 — See all users on this node**

```bash
userload
```

Look at the table. How many researchers are active right now? Who is using the most CPU? The most memory?

**Step 3 — See every individual process**

```bash
htop
```

Press `u` and type your username to filter to your own processes. Look at the `CPU%` and `MEM%` columns. Press `q` to quit.

{: .note }
> `userload` gives a per-user summary. `htop` shows every individual running program. Together they answer: who is here, and what exactly are they running?

When you can see both outputs — put a **🟢 green sticky** on your laptop. If something is not working, put up a **🔴 red sticky** and an instructor will come help.

---

## The Shared Kitchen Problem

The Yens has **5 interactive nodes** (`yen1`–`yen5`). When you SSH in, you land on one of these — and so does everyone else.

- Cores are **shared** between users on the same node
- Per-user limits apply to CPU and RAM: [rcpedia.stanford.edu/policies/user_limits](https://rcpedia.stanford.edu/_policies/user_limits/)
- JupyterHub notebooks run here too — same limits

Imagine everyone tries to run a big job at the same time:
- One person: 15-minute script, 1 core, a little RAM
- Second person: 3-hour script, 2 cores, a little RAM
- Third person: needs 10 cores for 8 hours, all the RAM

*How do you decide who goes first?* You need a head chef. That is SLURM.

---

## SLURM Is the Head Chef

SLURM is a scheduler. On the Yens, SLURM manages **12 dedicated nodes** — separate from the interactive Yens — where batch jobs run with dedicated resources.

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

- You do **not** SSH to SLURM nodes — the scheduler sends your job there
- How to write a job script: **The Foreman's Desk**
- How to measure what your script actually needs before requesting resources: **The Scales**

---

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> I can see the shared kitchen with userload and htop — I understand why SLURM exists</label>

---

## Skills Learned

- You can map every computer to a kitchen: core = burner, RAM = fridge, storage = warehouse
- You know the three kitchen types: your laptop (small, yours), the Yens (shared), cloud (rented)
- You know the Yens has two separate sets of machines: 5 interactive nodes and 12 SLURM scheduled nodes
- You know `userload` and `htop` show the interactive node you're on; `squeue` and `sacct` are for SLURM nodes
