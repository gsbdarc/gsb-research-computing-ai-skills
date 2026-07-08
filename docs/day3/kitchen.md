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

## 🖊️ The Kitchen Analogy

Every computer — your laptop, the Yens, a cloud server — is just a kitchen. The hardware is the kitchen equipment. The software is the recipe. Let's draw it out.

---

**Your kitchen — your laptop**

![Your Kitchen = Your Laptop]({{ site.baseurl }}/assets/images/kitchen-laptop.png)

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

Every research computing project has three questions. Answer them and you know what kitchen to cook in and what to cook.

**What** am I doing?
Talk to your PI — this is your task. For this bootcamp: extract names and CIKs from SEC Form 3 filings. In kitchen terms, you're making a specific dish.

**Where** am I doing it?
Pick your kitchen: your laptop, the Yens, Sherlock, the cloud. Each is a different kitchen with different equipment. You choose based on how much you need to cook and who else is cooking.

**How** am I doing it?
Your Python script is the recipe. A recipe is step-by-step instructions to produce a dish — and many recipes can produce the same dish:

```python
# Recipe: pasta.py
# 1. Boil water
# 2. Add pasta
# 3. While pasta cooks:
#      → make_sauce()   ← calls another recipe (a function)
# 4. Mix and serve
```

Your research script works the same way:
- Each step = an operation or a call to another function/script
- Some steps call *other* recipes (helper functions, imported modules)
- The result = your final dish — the output (extracted names, CIKs, a CSV)

---

## 🗡️ Main Quest — Kitchen Demo

*Your instructor will lead this activity with slides. Follow along and participate.*

---

## ✏️ Interactive Yens

The Yens has **5 interactive nodes** (`yen1`–`yen5`). These are the machines you SSH into — Days 1 and 2 happened entirely here.

- You SSH in and run scripts directly in a terminal
- No waiting — you get CPU and RAM immediately
- Burners (cores) **can be shared** between users on the same node
- Per-user limits apply to CPU and RAM: [rcpedia.stanford.edu/policies/user_limits](https://rcpedia.stanford.edu/_policies/user_limits/)
- JupyterHub notebooks run here too — same limits apply

**See who's on this node right now:**

```bash
userload    # YOUR CPU and memory usage on this interactive node
htop        # all processes on this node — including other researchers; press q to quit
```

**The problem:** Imagine everyone is trying to cook as fast as they can on the same 5 nodes:
- One person: 15-minute cookie recipe, 1 burner, a little fridge space
- Second person: 3-hour dish, 2 burners, a little fridge space
- Third person: 10 burners for 8 hours, the **entire** fridge

*How do you decide who cooks first?* You need a schedule — and the person with the giant recipe should probably wait. That's exactly what SLURM does.

---

## SLURM Is the Head Chef

Here's how every kitchen concept maps to SLURM:

| Kitchen | Yens / SLURM |
|---------|--------------|
| Head chef | SLURM scheduler |
| Station (stove) | Compute node |
| Burner | CPU core |
| Fridge | RAM |
| Pantry / warehouse | Shared storage (`/scratch`) |
| Order ticket | Job script (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Recipe | Your Python/R/shell script |
| Time limit (Chef de Temps) | `#SBATCH --time` |
| Resource request | `#SBATCH --mem`, `--cpus-per-task` |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef (`sbatch`), specify what burners, fridge space, and time you need (`#SBATCH` directives), and come back when the meal is done.

---

## ✏️ Yen-SLURM Cluster

SLURM is a scheduler — software that makes a schedule for sharing cluster resources. On the Yens, SLURM manages **12 dedicated scheduled nodes** that are completely separate from the interactive Yens.

| | Interactive Yens | SLURM Scheduled Nodes |
|---|---|---|
| Nodes | 5 | 12 |
| How to access | SSH directly | Submit a job script (`sbatch`) |
| Run style | Interactive terminal | Batch — script runs unattended |
| Wait for resources? | No | Yes — may queue |
| Burners shared between users? | Yes | **No** — yours alone |
| Notebooks? | Yes (same limits) | No |
| Can exceed interactive limits? | — | Yes |
| Usage reporting | `userload`, `htop` | `sacct` — actual cpu/RAM/time used |

- You do **not** SSH to scheduled nodes — SLURM sends your job there
- Your Python script runs inside a submission script (coming up in The Foreman's Desk)
- You request specific cores, RAM, and wall time up front — SLURM finds a node that fits
- `squeue` shows the full job queue across all scheduled nodes

{: .important }
> **What happens if you get the resource request wrong?**
>
> | Directive | Underestimate | Overestimate |
> |-----------|--------------|--------------|
> | `--time` | Job gets killed before it finishes | Longer queue wait; wastes reservation |
> | `--mem` | Job crashes with out-of-memory error | Blocks RAM other jobs could use |
> | `--cpus-per-task` | Script is slower than it could be | Reserves cores your script never uses |

Before you submit a job, you need to know what your script actually consumes. Head to **The Scales** to measure it.

---

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> Kitchen demo complete — I understand why SLURM exists</label>

---

## 🧠 Skills Learned

- You can map every computer to a kitchen: burner = CPU core, fridge = RAM, pantry/warehouse = storage
- You know the three kitchen types: your laptop (small, yours alone), the Yens (shared, many burners), cloud (all yours, pay per hour)
- You know the Yens has two separate sets of machines: 5 interactive nodes (where you SSH) and 12 SLURM scheduled nodes (where batch jobs run)
- You know `userload` and `htop` show the interactive node you're on; `squeue` and `sacct` are for the SLURM scheduled nodes
- You understand what happens when you under- or over-request time, memory, and cores in a SLURM job
