---
layout: default
title: "Profiling Resource Usage"
parent: "Day 3 — Cluster Computing"
nav_order: 3
permalink: /day3/profiling/
---

# Profiling Resource Usage

<svg viewBox="0 0 720 164" role="img" aria-labelledby="pmap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="pmap-title">Day 3 map — you are on step 1, profile your script.</title>
  <defs>
    <marker id="pmap-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" fill="#8a94a6">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" fill="#8a94a6">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#pmap-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#pmap-gray)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" fill="#8a94a6">debug</text>
  <circle cx="70" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

---

## Computing Resources — A Quick Recap

Before we run anything, let's make sure we have the vocabulary for the resources a program uses:

| Resource | What it is |
|----------|-----------|
| **CPU core** | An individual worker that executes your code |
| **RAM** | Fast memory the CPU reads from while working |
| **Storage (file system)** | Where your files live — VAST on the Yens |
| **Time** | How long your script takes to finish |

---

## Main quest — Run Your Script

{: .important }
> **Task:** Run your Day 2 extraction script on the Yens interactively and think about its resource footprint.

If you're not already connected, SSH in:

```bash
ssh SUNetID@yen.stanford.edu
cd ~/gsb-research-computing-ai-skills
source .venv/bin/activate
```

Run the script:

```bash
python scripts/extract_form_3_one_file.py
```

After the script is done running, let's discuss as a class:

<details markdown="1">
<summary>❓ Question 1</summary>

**Why** do we want to estimate the resources a script uses?

</details>

<details markdown="1">
<summary>❓ Question 2</summary>

Do you know what resources this script is using right now?

</details>

<details markdown="1">
<summary>❓ Question 3</summary>

How would you estimate them?

</details>

This page will teach you **how to estimate the resources your script is actually using**. This matters whether you wrote the script yourself or someone handed it to you.

---

## Main quest — Profile a Mystery Script

You are going to run a script you have never seen before and figure out what resources it uses — without reading the code. This is called **profiling**: measuring a script's time, CPU, and RAM usage as it runs. The technique: one terminal runs the script, a second terminal on the **same node** watches it live.

<svg viewBox="0 0 700 132" role="img" aria-labelledby="twoterm-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:1rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="twoterm-title">Profiling uses two terminals on the same Yen node: Terminal 1 runs the script, Terminal 2 watches its CPU and RAM live.</title>
  <rect x="16" y="8" width="668" height="116" rx="16" fill="#f7f9fc" stroke="#bcd4f2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="40" y="34" font-size="13.5" font-weight="700" letter-spacing="0.5" fill="#374151">🖥️ ONE YEN NODE · BOTH TERMINALS ON IT</text>
  <rect x="40" y="46" width="300" height="70" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="60" y="76" font-size="17" font-weight="700" fill="#111827">Terminal 1 · the worker</text>
  <text x="60" y="100" font-size="15" fill="#374151">runs the script</text>
  <rect x="360" y="46" width="300" height="70" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="380" y="76" font-size="17" font-weight="700" fill="#111827">Terminal 2 · the observer</text>
  <text x="380" y="100" font-size="15" fill="#374151">watches CPU + RAM live</text>
</svg>

*Two terminals on the **same** Yen node: one runs the script, the other watches it live.*

{: .important }
> **Task:** Run `mystery_script.py` and measure its resource usage in real time using two terminals — both on the **same Yen node**.

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

{: .note }
> 💡 **Skip the second login.** A fresh `ssh` means another password + Duo prompt. To avoid re-authenticating, open a terminal through JupyterHub instead: browse to that node's hub (e.g. `https://yen2.stanford.edu/jupyter/`), then **New → Terminal**. You're already authenticated there, and it drops you onto that exact node — ideal for the second monitoring terminal.

**Step 3 — Start `watch userload` in Terminal 2 *first*, before running anything.**

Terminal 2:
```bash
watch userload
```

- `userload` shows how many **cores** you're using and what **% of the node's memory** you're holding — your total footprint across all your processes on this node. It looks like `SUNetID  |  0.34 Cores  |  0.00% Mem  on yen2`
- `watch` re-runs it every 2 seconds, so the numbers refresh live
- Jupyter processes are tracked separately and are not included

**What are we seeing?** Right now — before you run anything — this is your **baseline**: **Cores** near 0 and **% Mem** near 0. That's what an idle account looks like. Keep this terminal visible; you'll watch these numbers move once the script starts. (See the [current per-user limits](https://rcpedia.stanford.edu/_policies/user_limits/) for how much CPU and RAM any one user can use on an interactive Yen.)

**Step 4 — Now run the script in Terminal 1 and watch Terminal 2 change.**

Terminal 1:
```bash
time python scripts/mystery_script.py
```

{: .note }
> **What's the `time` in front?** `time` is a wrapper — it runs whatever command follows (`python scripts/mystery_script.py`) exactly as normal, then, once it finishes, prints how long it took. It doesn't change what your script does; it just measures it. That's where the `real` / `user` / `sys` lines below come from.

As it runs, watch Terminal 2: **your Cores number climbs and % Mem grows** — that's the script's footprint stacking on top of your baseline. If Cores climbs above 1, the script is using more than one core at once. When it finishes, the numbers fall back toward baseline, and `time` prints three lines:

```
real    0m31.234s
user    2m0.682s
sys     0m2.212s
```

- **real** — wall-clock time: how long you actually waited
- **user** — CPU time your code consumed across all cores; if `user` > `real`, the script used multiple cores in parallel
- **sys** — CPU time spent on OS-level work (file I/O, memory allocation)

{: .note }
> **Definitions**
> - **Profiling** — measuring a script's resource usage (time, CPU, RAM) as it runs
> - **Serial** — the script uses one CPU core at a time; `user` time ≈ `real` time
> - **Parallel** — the script uses multiple cores simultaneously; `user` time > `real` time

**Step 5 — Run the script again, this time watching it in `htop`.**

First, in **Terminal 2**, stop `watch userload` by pressing **`Ctrl+C`**. Then start `htop`, filtered to just your own processes:

```bash
htop -u SUNetID
```

The `-u` flag limits `htop` to your processes, so the hundreds of other users' processes on the node don't drown yours out.

**Each row in `htop` is one process.** The columns that matter:

- **`CPU%`** — how hard that process is pushing. `100%` = one full core busy, `200%` = two cores, and so on — a single process reading over `100%` is spread across multiple cores.
- **`RES`** — the real RAM the process is actually using. Shown in **KB** by default, so `9000` ≈ **9 MB**; bigger values get an `M` or `G` suffix (like `111M`).
- **`MEM%`** — that same `RES` as a share of the **whole node's** RAM. On a 1 TB node a few MB rounds to **0.0%** — which is why `userload` can read `0% Mem` even though the process really is using memory.
- **`VIRT`** — ignore it. That's memory the process *reserved*, not what it's actually using.

Now, in **Terminal 1**, run the script again and watch your rows in `htop` light up:

```bash
time python scripts/mystery_script.py
```

As the script runs, watch new `python` rows appear — that's it spawning work. Count them to answer "how many processes did it run?"

**Compare with your neighbor:**
- How long did it take, and how much RAM did it peak at?
- How many CPU cores did it use?
- How many processes did it run?
- Is it therefore **serial** (one core) or **parallel** (multiple)?

{: .note }
> **Cores vs. processes:** we use these loosely here, almost interchangeably — but they're actually separate things (a single process can spread across several cores, and one core can take turns running many processes). Likewise, **multi-core**, **multiprocessing**, and **parallel** all mean roughly the same thing for now: your code doing work on more than one core at once. We'll dig into parallelism properly on **Day 4** — for now, just picture physical cores plus a program using multiple threads or processes as a **parallel, multi-core program**.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

<label class="quest-check"><input type="checkbox" data-room="d3-profiling" data-key="mystery"> I profiled the mystery script and compared with my neighbor, and can describe the resources it needs to run</label>

<details markdown="1">
<summary>✅ Check your answer</summary>

You saw about **4 `python` processes** in `htop` and roughly **4 Cores** in `userload` — no accident. Open `scripts/mystery_script.py` and you'll find `num_cores = 4`: the script deliberately starts 4 worker processes, one per core, which is exactly what made it a **parallel, multi-core** program. The amount of parallelism is a **choice in the code** — change that number and the processes and cores you'd see change with it.

</details>

---

## Main quest — Profile Your Day 2 Script

{: .important }
> **Task:** Profile your real Day 2 batch script on 10 filings using the same two-terminal technique.

Now apply the same technique to your **real Day 2 workload**. `extract_form_3_batch.py` runs the same Form 3 extraction you did on Day 2 with `extract_form_3_one_file.py` — but loops over many filings instead of one. Process **10 filings** and profile it.

First, open the script so you know what you're profiling — `cat scripts/extract_form_3_batch.py` (or open it in JupyterHub).

<details markdown="1">
<summary>💡 Hint — what the script does</summary>

It loops over the filings in `data/aws_links.csv`, calls the API for each, and writes one JSON per filing to `results/`.

</details>

The script is set to process **10 filings** (see `NUM_FILINGS` near the top — kept small so a stray run doesn't fire hundreds of paid API calls).

**First run — watch the load.** Terminal 2 (start this first):
```bash
watch userload
```

Terminal 1 — run it and note the `real`, `user`, and `sys` times when it finishes:
```bash
time python scripts/extract_form_3_batch.py
```

**Second run — watch the processes.** Switch Terminal 2 to `htop`, then run the script once more so you can see the processes live:

Terminal 2:
```bash
htop -u SUNetID
```

Terminal 1:
```bash
time python scripts/extract_form_3_batch.py
```

Watch Terminal 2 as the 10 filings process one after another.

{: .note }
> **Reminder — `real` / `user` / `sys`:**
> - **`real`** — wall-clock time: how long you actually waited
> - **`user`** — CPU time your code used across all cores (if `user` > `real`, it ran on multiple cores in parallel)
> - **`sys`** — CPU time spent on OS-level work (file I/O, memory allocation)

Let's open these and discuss as a class before revealing the answer:

<details markdown="1">
<summary>❓ Question 1</summary>

What did we observe in `userload` while the 10 filings ran — what happened to **Cores** and **% Mem**?

</details>

<details markdown="1">
<summary>❓ Question 2</summary>

Why do the **Cores** stay near 0, even with 10 filings running?

</details>

<details markdown="1">
<summary>❓ Question 3</summary>

Why does **% Mem** stay near 0?

</details>

<details markdown="1">
<summary>❓ Question 4</summary>

Is this script **serial** or **parallel**?

</details>

<details markdown="1">
<summary>✅ Check your answer</summary>

- **Cores and % Mem barely moved.** The job spends almost all its time **waiting on the Stanford API** to answer, not computing — so it barely touches the CPU. That makes it an **I/O-bound** job (waiting on the network), unlike the mystery script, which was **CPU-bound** (doing math). It also handles one filing at a time, so memory stays low no matter how many you run.
- **`real` is large, `user` is small.** `real` (wall-clock) is big because you waited on the API; `user` (actual CPU time) is tiny because the CPU had little to do. That gap — `real` ≫ `user` — is the fingerprint of a job that mostly waits.

A typical run: `real 0m22.5s`, `user 0m1.9s`, `sys 0m0.5s` — about 2 seconds of real work, ~20 seconds spent waiting. In `htop` you'll see just **one `python` process**, and **under 1 Core** in `userload`.

Two more things worth knowing:

- **Per-filing times vary** — each takes however long the API takes, so 10 filings isn't exactly 10× one.
- **Why the script sets `OPENBLAS_NUM_THREADS=1`.** Libraries like NumPy and pandas try to speed up math by grabbing *every* core on the machine — 256 on Yen2, for example. But the Yens enforce [per-user limits](https://rcpedia.stanford.edu/_policies/user_limits/) on how much CPU one person can use, so grabbing all 256 doesn't help — it just crowds a pile of threads onto the cores you're actually allowed, which can make the job *slower*. Setting it to `1` keeps the job to what it needs. The habit: on a shared node, don't let a library grab the whole machine — keep its thread count within your limits.

</details>

---

## Main quest — Document Your Script's Resource Needs

{: .important }
> **Task:** Write down the resources you measured for the 10-filing run in your README.

Now that you've profiled **10 filings**, write down what you measured. Open the `README.md` in your repo and add a **Resource Profile** section:

```markdown
## Resource Profile

### extract_form_3_batch.py — 10 filings

- Yen node used:
- Wall-clock time (real):
- CPU cores used:
- RAM used (RES from htop, or % Mem from userload):
- Serial or parallel:
```

{: .tip }
> If your RAM here is tiny — just a few MB (`RES`), showing as 0% Mem in `userload` — you can't ask for 0, so a good tip is to write down a small round number like `1G`.

Fill in the actual numbers from your `time`, `userload`, and `htop` output.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

<label class="quest-check"><input type="checkbox" data-room="d3-profiling" data-key="readme"> I profiled the LLM extraction script on 10 filings and documented the time / CPU / RAM (and which Yen node) in my README</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Vectorized vs. Non-Vectorized**

One quick way to speed up scientific Python is **vectorization** — doing the math on a whole array in one operation instead of looping element-by-element in Python. The array operation runs in fast, pre-compiled code, so it's often 10–100× faster. We ship a script that computes the same sum of squares both ways — profile it and see the difference.

Terminal 1 — run it:
```bash
source .venv/bin/activate
time python scripts/vectorize_demo.py
```

Terminal 2 — watch the load while it runs:
```bash
watch userload
```

Both versions produce the identical result; the script prints how much faster the vectorized one was (often 10× or more). Notice the slow Python loop pins a core the whole time, while the NumPy version finishes almost before you can look at Terminal 2.

<label class="quest-check"><input type="checkbox" data-room="d3-profiling" data-key="side2"> I profiled the vectorized vs. non-vectorized demo and saw the speedup</label>

**Side quest — Change the number of cores**

Open `scripts/mystery_script.py` and change `num_cores = 4` to a different number — try **1**, or **8**. Then **profile it again** with the same two-terminal setup: run `time python scripts/mystery_script.py` in Terminal 1, and watch it in Terminal 2 with `watch userload` (or `htop -u SUNetID`).

Document what changes and discuss with your neighbor:

- How many `python` processes appear in `htop` now?
- How many **Cores** in `userload`?
- Did the `real` (wall-clock) time go up or down?
- Does the resource usage match the number you set?

<label class="quest-check"><input type="checkbox" data-room="d3-profiling" data-key="side6"> I changed `num_cores` in the mystery script, re-profiled it, and can explain how the processes and cores changed</label>

**Side quest — Prompt caching**

Run the 10 filings, then delete the results and run them again:

```bash
time python scripts/extract_form_3_batch.py
rm -rf results/*
time python scripts/extract_form_3_batch.py
```

Compare the two `real` times — **was the second run different? If so, how, and why?**

<details markdown="1">
<summary>✅ Check your answer</summary>

Yes — the second run is noticeably faster, even though you cleared the output files. The Stanford AI Playground supports **prompt caching**: when a request repeats a large chunk the model has already processed (here, the system prompt and the filings you just sent), it reuses that cached work instead of re-reading it — so it answers faster and cheaper.

Read more: [AI API Gateway FAQs](https://uit.stanford.edu/service/ai-api-gateway/faqs).

</details>

<label class="quest-check"><input type="checkbox" data-room="d3-profiling" data-key="side7"> I re-ran the 10 filings and saw prompt caching make the second run faster and cheaper</label>

