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

## Your Research Project in Computing Terms

Every research computing project has three questions:

<div style="display:flex; gap:1rem; margin:1.5rem 0;">
  <div style="flex:1; border:2px solid #4a90d9; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🎯</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">What?</div>
    <div style="font-size:0.9rem;">Your research <strong>task</strong> — defined by your PI. For this bootcamp: extract names and CIKs from SEC Form 3 filings.</div>
  </div>
  <div style="flex:1; border:2px solid #27ae60; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🐍</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">How?</div>
    <div style="font-size:0.9rem;">Your Python <strong>script</strong> — a sequence of steps that produces your output: extracted names, CIKs, a CSV.</div>
  </div>
  <div style="flex:1; border:2px solid #e67e22; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🖥️</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">Where?</div>
    <div style="font-size:0.9rem;">Your compute environment — laptop, the Yens, or the cloud. Each has different <strong>resources</strong> (CPU cores, RAM, and storage).</div>
  </div>
</div>

The rest of this page answers the **Where** question — understanding the resources behind each environment: **CPU cores**, **RAM**, and **storage**.

---

## Under the Hood

In Days 1 and 2, you wrote a Python script and ran it on the Yens interactively. But what is actually inside the machine running your code?

Inside every computer — your laptop, a Yen node, a cloud server — there are the same few physical components. The diagram below shows a Yen server opened up: the **CPU** is the processor chip, **cores** are the individual workers inside it (each runs code independently), and **RAM** is the fast memory the CPU reads from while working.

![Server hardware diagram showing CPU, cores, and RAM]({{ site.baseurl }}/assets/images/server-hardware-cpu-ram.png)

Today we'll understand what each of these does when your script is running — and why they determine how fast (or slow) your code goes.

| Component | What it is |
|-----------|-----------|
| **CPU** | The processor chip — executes your code |
| **CPU core** | An individual worker inside the CPU — each runs independently |
| **RAM** | Fast memory the CPU reads from and writes to while working — limited in size |
| **Storage (disk / file system)** | Where your files live when nothing is running — large but slow |
| **I/O (Input/Output)** | Moving data from disk into RAM (read) and writing results back to disk (write) — the slowest step |

---

## The Kitchen Analogy

To make these concepts concrete, we're going to use a **kitchen analogy** that carries through the whole day — from your laptop to the Yens to the cloud. Your kitchen — your laptop — is all yours and only yours: a few burners (CPU cores), a small fridge (RAM), and a convenience store down the street (disk) that's bigger than your fridge but slow to access. Your bike (disk I/O) can only grab a few things from the store at a time.

![Your Laptop = Your Kitchen]({{ site.baseurl }}/assets/images/kitchen-laptop.png)

| Component | What it is | Kitchen analogy |
|-----------|-----------|-----------------|
| **CPU** | The processor chip — executes your code | The stove |
| **CPU core** | An individual worker inside the CPU — each runs independently | A single burner |
| **RAM** | Fast memory the CPU reads from and writes to while working — limited in size | The fridge |
| **Storage (disk / file system)** | Where your files live when nothing is running — large but slow | The convenience store |
| **I/O (Input/Output)** | Moving data from disk into RAM (read) and writing results back to disk (write) — the slowest step | Biking to the store and back |

---

**What happens when you run a script:**

When you run `python extract_form_3_one_file.py`, four things happen in sequence:

1. **Load from disk** — Python reads your script and data files from storage (the convenience store) onto the bike and hauls them into RAM.
2. **Into RAM** — the data lands in the fridge. Now the CPU can reach it quickly without another trip to the store.
3. **CPU does the work** — the stove fires up. Each CPU core executes the steps in your script against whatever is in the fridge.
4. **Save to disk** — results get written back to storage so they're there when you shut down.

![What Happens When You Run a Script]({{ site.baseurl }}/assets/images/kitchen-script-laptop.png)

{: .warning }
> **The tricky part: the bike ride is slow.** Reading from disk is orders of magnitude slower than reading from RAM. Your CPU can crunch through data in nanoseconds, but a disk read takes milliseconds — **a million times longer**. If your dataset is too large to fit in RAM all at once, your script keeps making bike trips mid-computation, and that is what makes jobs crawl. This is why knowing how much RAM your script needs matters — not just for the cluster, but on your laptop too.

Your script is a **recipe** — a numbered sequence of steps the **CPU** follows from top to bottom. Just like a recipe can say "make the sauce" and refer you to another page, a script can call **functions or other scripts**. Each call is a **sub-recipe**: the CPU pauses the main recipe, runs the sub-recipe to completion, then picks up where it left off.

```python
# Recipe: pasta.py
# 1. Boil water
# 2. Add pasta
# 3. While pasta cooks:
#      → make_sauce()   ← calls another function (a sub-recipe)
# 4. Mix and serve
```

| Component | What it is | Kitchen analogy |
|-----------|-----------|-----------------|
| **CPU** | The processor chip — executes your code | The stove |
| **CPU core** | An individual worker inside the CPU — each runs independently | A single burner |
| **RAM** | Fast memory the CPU reads from and writes to while working — limited in size | The fridge |
| **Storage (disk / file system)** | Where your files live when nothing is running — large but slow | The convenience store |
| **I/O (Input/Output)** | Moving data from disk into RAM (read) and writing results back to disk (write) — the slowest step | Biking to the store and back |
| **Script** | The sequence of steps the CPU follows to produce your output | The recipe |

---

**Shared restaurant kitchen — the Yens**

The Yens are a shared restaurant kitchen. Many cooks are working at the same time — you share the **burners (CPU cores)**, the **fridge (RAM)**, and the **file system (VAST)** with everyone else on the node. **They are not infinite.** Per-user limits are enforced so one chef can't claim every burner, but if the kitchen is busy, you feel it.

{: .note }
> **Shared file system:** A file you write on yen1 is instantly visible on every other Yen node — because they all read from and write to the same VAST storage. This is powerful for collaboration, but it also means everyone is hitting the same warehouse at once.

![Yen Cluster = A Shared Restaurant Kitchen]({{ site.baseurl }}/assets/images/kitchen-yens.png)

| Component | What it is | Kitchen analogy |
|-----------|-----------|-----------------|
| **Node** | One physical server — each node has its own CPU and RAM, independent from other nodes | A station in the restaurant kitchen — its own stove and fridge |
| **CPU** | The processor chip — executes your code | The stove |
| **CPU core** | An individual worker inside the CPU — each runs independently | A single burner |
| **RAM** | Fast memory the CPU reads from and writes to while working — limited in size | The fridge |
| **Storage (disk / file system)** | VAST — a shared file system across all nodes, ~1 PB, every node reads and writes the same files | The shared data warehouse |
| **I/O (Input/Output)** | Moving data from disk into RAM (read) and writing results back to disk (write) — the slowest step | Driving to the warehouse and back |
| **Script** | The sequence of steps the CPU follows to produce your output | The recipe |

---

**Rented kitchen — cloud (AWS / GCP / Azure)**

The cloud is a rented kitchen — and it's **just for you**. Unlike the Yens, you're not sharing burners or fridges with anyone. Cloud gives you **flexible and practically infinite** compute, memory, and storage: need 1,000 burners for an hour, rent them; need a warehouse the size of a city block, rent it.

{: .warning }
> **You pay for everything you rent, for as long as you rent it.** Leaving a large instance running overnight by accident can cost hundreds of dollars. Always shut down what you're not using.

![Cloud Computing = A Rented Kitchen]({{ site.baseurl }}/assets/images/kitchen-cloud.png)

---

## Class Participation Time

{: .important }
> **Demo + Discussion:** Your instructor will walk through the kitchen analogy and open the floor for questions.

- What are the tradeoffs between your laptop, the Yens, and the cloud?
- What happens when many researchers all run jobs at once on the shared Yens?

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> I participated in the class demo and discussion</label>
