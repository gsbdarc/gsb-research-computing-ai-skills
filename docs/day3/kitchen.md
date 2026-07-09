---
layout: default
title: "The Kitchen"
parent: "Day 3 — The SLURM Mines"
nav_order: 2
permalink: /day3/kitchen/
---

# The Kitchen

<div data-room-id="d3-kitchen"></div>

---

## The Kitchen Analogy

Every computer — your laptop, the Yens, a cloud server — is just a kitchen. The hardware is the equipment; the software is the recipe. Once you see this mapping, reading cluster tools like `htop` becomes natural: you're just watching the kitchen work.

---

**Your kitchen — your laptop**

![Your Kitchen = Your Laptop]({{ site.baseurl }}/assets/images/kitchen-laptop.png)

| Kitchen | Your laptop |
|---------|-------------|
| Burner | CPU core — does the computation |
| Fridge | RAM — holds what you're actively working with |
| Warehouse / pantry | Storage (SSD) — holds everything long-term |
| Recipe | Your Python script |

**How data moves: storage → RAM → CPU**

When you run a script, Python reads your data files from **storage** (the warehouse), loads the relevant parts into **RAM** (the fridge), and the **CPU** (the burner) crunches through it. This flow is the bottleneck in almost every research computing job.

- Storage: large and slow — terabytes, but milliseconds per read
- RAM: medium and fast — gigabytes, nanoseconds
- CPU cache: tiny and extremely fast — megabytes, right next to the processor

If your dataset doesn't fit in RAM, your job will be slow — it has to keep fetching from the warehouse. This is why memory matters when requesting SLURM resources.

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

## Your Research Project in Computing Terms

Every research computing project has three questions:

**What** am I doing?
Talk to your PI — this is your task. For this bootcamp: extract names and CIKs from SEC Form 3 filings.

**Where** am I doing it?
Pick your environment: your laptop, the Yens, Sherlock, the cloud. Each has different resources. You choose based on how much compute you need and who else is using the system.

**How** am I doing it?
Your Python script is the recipe — step-by-step instructions:

```python
# Recipe: pasta.py
# 1. Boil water
# 2. Add pasta
# 3. While pasta cooks:
#      → make_sauce()   ← calls another function
# 4. Mix and serve
```

Each step is an operation or a function call. The result is your output — extracted names, CIKs, a CSV.

---

## Class Discussion

*Your instructor will walk through the kitchen slides and lead the discussion.*

- Which computing environment are you using for this bootcamp?
- What are the tradeoffs between your laptop, the Yens, and the cloud?
- What happens when many researchers all run jobs at once on the shared Yens?

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

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> I can SSH into the Yens and read the shared node with htop and userload</label>

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

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main2"> I profiled mystery_script.py and can describe what it uses</label>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Sort htop by memory**

In htop, press `F6`, select `MEM%`, press Enter. What is the #1 memory-consuming process on this node right now? How much RAM is it using?

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="side1"> I sorted htop by memory and identified the top consumer</label>

**Bonus 2 — Read ps output**

```bash
ps aux --sort=-%mem | head -15
```

Look at the VSZ and RSS columns. What is the difference between virtual memory (VSZ) and resident memory (RSS)?

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="side2"> I can explain the difference between VSZ and RSS</label>

---

## Key Concepts

- Every computer maps to a kitchen: CPU core = burner, RAM = fridge, storage = warehouse
- The three environments: your laptop (small, yours), the Yens (shared), cloud (rented)
- `htop` shows all users and all processes on the current node; `userload` shows only your footprint
- You measured a script's runtime, memory, and CPU usage before guessing at resource requests
