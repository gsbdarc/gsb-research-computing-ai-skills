---
layout: default
title: "Compute Environments"
parent: "Day 3 — Cluster Computing"
nav_order: 2
permalink: /day3/compute-environments/
---

# Compute Environments

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

Here is that same flow as a moving picture — the identical trip in hardware terms, then in kitchen terms. Notice the first leg (disk → RAM) is the slow one; once the data is close to the processor, the rest is quick:

<svg viewBox="0 0 600 210" role="img" aria-labelledby="hwflow-title hwflow-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:600px;height:auto;margin:1.25rem auto 0.25rem" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="hwflow-title">How your program uses the hardware</title>
  <desc id="hwflow-desc">A packet of data loops from Storage to RAM to the CPU and back to Storage. Reading from disk into RAM is the slow leg; once the data is in RAM the CPU reaches it quickly; then results are written back to disk.</desc>
  <defs><marker id="bk-hw" markerWidth="9" markerHeight="9" refX="6.5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#8a94a6"/></marker></defs>
  <text x="12" y="20" font-size="12" font-weight="700" letter-spacing="0.4" fill="#8a94a6">🖥  HOW YOUR PROGRAM USES THE HARDWARE</text>
  <line x1="80" y1="44" x2="520" y2="44" stroke="#cdd4e6" stroke-width="2" stroke-dasharray="4 5"/>
  <text x="190" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#c0392b">read — slow (I/O)</text>
  <text x="410" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3f4f74">fast</text>
  <rect x="20" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="80" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#2c3e50">Storage</text>
  <text x="80" y="117" text-anchor="middle" font-size="10.5" fill="#6a7280">disk — large, slow</text>
  <rect x="240" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="300" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#2c3e50">RAM</text>
  <text x="300" y="117" text-anchor="middle" font-size="10.5" fill="#6a7280">fast, limited</text>
  <rect x="460" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="520" y="93" text-anchor="middle" font-size="14" font-weight="700" fill="#2c3e50">CPU</text>
  <rect x="487" y="103" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="503" y="103" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="519" y="103" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="535" y="103" width="12" height="12" rx="2" fill="#cdd4e6"/>
  <text x="520" y="128" text-anchor="middle" font-size="10" fill="#6a7280">cores do the work</text>
  <line x1="520" y1="162" x2="90" y2="162" stroke="#8a94a6" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#bk-hw)"/>
  <text x="305" y="156" text-anchor="middle" font-size="11" font-weight="600" fill="#8a94a6">write results back to disk</text>
  <g>
    <circle cx="80" cy="44" r="8" fill="#0072B2"><animate attributeName="r" values="8;10;8" dur="1s" repeatCount="indefinite"/></circle>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,0; 220,0; 220,0; 440,0; 440,0; 440,118; 0,118; 0,0" keyTimes="0; 0.05; 0.42; 0.50; 0.60; 0.72; 0.82; 0.95; 1" dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="198" text-anchor="middle" font-size="12" fill="#6a7280">Data crawls from disk into RAM (the slow step), the CPU works in RAM, then results are written back to disk.</text>
</svg>

<svg viewBox="0 0 600 210" role="img" aria-labelledby="kflow-title kflow-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:600px;height:auto;margin:0.25rem auto 0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="kflow-title">The same trip, in the kitchen</title>
  <desc id="kflow-desc">A shopping cart loops from the convenience store to the fridge to the stove and back to the store. Biking from the store is the slow leg; once ingredients are in the fridge they are within arm's reach of the stove; then leftovers go back to the store.</desc>
  <defs><marker id="bk-k" markerWidth="9" markerHeight="9" refX="6.5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#8a94a6"/></marker></defs>
  <text x="12" y="20" font-size="12" font-weight="700" letter-spacing="0.4" fill="#8a94a6">🍳  THE SAME TRIP, IN THE KITCHEN</text>
  <line x1="80" y1="44" x2="520" y2="44" stroke="#cdd4e6" stroke-width="2" stroke-dasharray="4 5"/>
  <text x="190" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#c0392b">the bike — slow</text>
  <text x="410" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3f4f74">arm's reach</text>
  <rect x="20" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="80" y="99" text-anchor="middle" font-size="18">🏪</text>
  <text x="80" y="121" text-anchor="middle" font-size="11" font-weight="700" fill="#2c3e50">Store = disk</text>
  <rect x="240" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="300" y="99" text-anchor="middle" font-size="18">🧊</text>
  <text x="300" y="121" text-anchor="middle" font-size="11" font-weight="700" fill="#2c3e50">Fridge = RAM</text>
  <rect x="460" y="72" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="520" y="95" text-anchor="middle" font-size="16">🔥</text>
  <circle cx="497" cy="110" r="5" fill="#cdd4e6"/><circle cx="512" cy="110" r="5" fill="#cdd4e6"/><circle cx="527" cy="110" r="5" fill="#cdd4e6"/><circle cx="542" cy="110" r="5" fill="#cdd4e6"/>
  <text x="520" y="126" text-anchor="middle" font-size="11" font-weight="700" fill="#2c3e50">Stove = CPU</text>
  <line x1="520" y1="162" x2="90" y2="162" stroke="#8a94a6" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#bk-k)"/>
  <text x="305" y="156" text-anchor="middle" font-size="11" font-weight="600" fill="#8a94a6">leftovers go back to the store</text>
  <g>
    <text x="80" y="50" text-anchor="middle" font-size="18">🛒</text>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,0; 220,0; 220,0; 440,0; 440,0; 440,118; 0,118; 0,0" keyTimes="0; 0.05; 0.42; 0.50; 0.60; 0.72; 0.82; 0.95; 1" dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="198" text-anchor="middle" font-size="12" fill="#6a7280">Bike groceries from the store (slow) to the fridge, cook at the stove, then leftovers go back to the store.</text>
</svg>

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

## Exercise — Class Participation

{: .important }
> 🥪 **Demo + Discussion:** 🥪 We will all participate in a class demo together. 🥪

<details markdown="1">
<summary><strong>After the demo:</strong></summary>

- What are the tradeoffs between your laptop, the Yens, and the cloud?
- What happens when many researchers all run jobs at once on the shared Yens?

</details>

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> I participated in the class demo and discussion</label>

{: .note }
> **📤 Sync your progress to the leaderboard**
>
> 1. Open the **Quest Log** (bottom-left corner) → click **Sync**.
> 2. Click **Copy token**.
> 3. **First time only:** sign in once with `gh auth login` (see Day 1) so the push works.
> 4. On the Yens, inside your clone, run `python3 scripts/quest_sync.py <paste-token>`.
>
> **Each time you finish more quests,** tick the new boxes, then repeat: **Sync → Copy token → re-run the command** with the fresh token (the one-time sign-in is already done). Each token is a full snapshot of everything you've checked, so the latest sync always reflects *all* your progress.

---

## Optional practice

{: .note }
> Finished early? Try one or both of these.

**Optional practice 1 — Know your own machine**

Check your own laptop's CPU core count and RAM, and compare them to a Yen node (256 cores). On Mac: `system_profiler SPHardwareDataType`. On Windows: Task Manager → Performance tab. On Linux: `nproc` and `free -h`.

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="side1"> I checked my own laptop's CPU cores and RAM and compared them to a Yen node</label>

**Optional practice 2 — Price the rented kitchen**

Look up on-demand pricing for a cloud VM comparable to a Yen node (similar CPU/RAM), and estimate what it would cost to run your Day 2 extraction job there for an hour. Grant budgets aren't infinite — this is a real judgment call you'll make in your own research.

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="side2"> I estimated the cost of running my Day 2 job in the cloud for an hour</label>

**Optional practice 3 — Laptop vs. a Yen node**

You looked up your laptop's specs in the *Know your own machine* practice above. Enter them below to see just how much bigger one Yen node is.

<style>
.yen-widget { border: 1px solid #ddd; border-radius: 6px; padding: 1rem 1.25rem; margin: 1rem 0; }
.yen-widget label { display: block; margin: 0.35rem 0; }
.yen-widget input { width: 6rem; margin-left: 0.4rem; }
.yen-widget button { margin-top: 0.6rem; padding: 0.35rem 0.9rem; cursor: pointer; border-radius: 4px; border: 1px solid #ccc; background: #f0f0f0; }
#yw-out { margin-top: 0.75rem; line-height: 1.5; }
</style>

<div class="yen-widget">
  <label>Your laptop's CPU cores: <input id="yw-cores" type="number" min="1" step="1" value="8"></label>
  <label>Your laptop's RAM (GB): <input id="yw-ram" type="number" min="1" step="1" value="16"></label>
  <button id="yw-go">Compare</button>
  <p id="yw-out"></p>
</div>

<script>
(function () {
  var YEN_CORES = 256, YEN_RAM = 1024; // one Yen node: 256 logical cores, ~1 TB RAM
  function compare() {
    var c = parseFloat(document.getElementById('yw-cores').value);
    var r = parseFloat(document.getElementById('yw-ram').value);
    var out = document.getElementById('yw-out');
    if (!(c > 0) || !(r > 0)) { out.textContent = 'Enter your laptop’s cores and RAM above.'; return; }
    var coreX = YEN_CORES / c, ramX = YEN_RAM / r;
    var fit = Math.floor(Math.min(coreX, ramX));
    out.innerHTML =
      'A Yen node has <strong>' + coreX.toFixed(0) + '×</strong> your cores (' + YEN_CORES + ' vs ' + c + ')'
      + ' and <strong>' + ramX.toFixed(0) + '×</strong> your RAM (' + YEN_RAM + ' GB vs ' + r + ' GB).<br>'
      + 'About <strong>' + fit + '</strong> of your laptop' + (fit === 1 ? '' : 's') + ' would fit inside one Yen node.';
  }
  document.getElementById('yw-go').addEventListener('click', compare);
  compare();
})();
</script>

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="side3"> I used the widget to compare my laptop to a Yen node</label>

