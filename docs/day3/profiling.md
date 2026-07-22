---
layout: default
title: "Profiling Resource Usage"
parent: "Day 3 — Cluster Computing"
nav_order: 3
permalink: /day3/profiling/
---

# Profiling Resource Usage

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

## 💻 Main quest — Run Your Script

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

You are going to run a script you have never seen before and figure out what resources it uses — without reading the code. This is called **profiling**: measuring a script's time, CPU, and RAM usage as it runs. The technique is simple: one terminal runs the script, a second terminal on the **same node** watches it live.

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

**Each row in `htop` is one process.** In each row, the `CPU%` column shows how hard that process is pushing — here **100% = one full core busy**, 200% = two cores, and so on, so a single process reading over 100% is spreading across multiple cores. For memory, watch **`RES`** — the real RAM the process is actually using. `htop` shows it in **KB** by default, so `9000` ≈ **9 MB**; larger values get an `M` or `G` suffix (like `111M`). **`MEM%`** is that same RES as a share of the **whole node's** RAM — on a 1 TB node a few MB rounds to **0.0%**, which is why `userload` can read `0% Mem` even though the process really is using memory. Ignore **`VIRT`** — that's memory the process *reserved*, not what it's using.

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

When you can describe what the mystery script does to your CPU and RAM — put a **🟢 green sticky** on your laptop. If something is not working, put up a **🔴 red sticky** and an instructor will come help.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="mystery"> I profiled the mystery script and compared with my neighbor, and can describe the resources it needs to run</label>

<details markdown="1">
<summary>💡 Open after you've discussed and checked the box</summary>

You saw about **4 `python` processes** in `htop` and roughly **4 Cores** in `userload` — no accident. Open `scripts/mystery_script.py` and you'll find `num_cores = 4`: the script deliberately starts 4 worker processes, one per core, which is exactly what made it a **parallel, multi-core** program. The amount of parallelism is a **choice in the code** — change that number and the processes and cores you'd see change with it.

</details>

---

## 💻 Main quest — Profile Your Day 2 Script

Now apply the same technique to your **real Day 2 workload**. `extract_form_3_batch.py` runs the same Form 3 extraction you did on Day 2 with `extract_form_3_one_file.py` — but loops over many filings instead of one. Process **10 filings** and profile it.

Terminal 2 (start this first):
```bash
watch userload
```

The script is set to process **10 filings** (see `NUM_FILINGS` near the top — kept small so a stray run doesn't fire hundreds of paid API calls).

Terminal 1:
```bash
time python scripts/extract_form_3_batch.py
```

Watch Terminal 2 as the 10 filings process one after another:

- **Cores and % Mem barely move.** Almost all the time is spent *waiting on the Stanford API* to extract each filing — this is an **I/O-bound** (network-bound) job, not CPU-bound like the mystery script. One filing sits in memory at a time, so RAM stays low no matter how many you run.
- **`real` time is large but `user` time is small.** The process barely touches the CPU; it's mostly waiting. That gap (`real` ≫ `user`) is the signature of an I/O-bound, serial job.

Note the `real`, `user`, and `sys` times when it finishes. Is this script **serial** or **parallel**?

{: .note }
> **What you should see:** just **one `python` process** in `htop`, and **less than 1 Core** in `userload`. A typical run: `real 0m22.5s`, `user 0m1.9s`, `sys 0m0.5s` — the `user` CPU time (~2s) is a tiny slice of the `real` wall-clock (~22s); the other ~20s was spent **waiting on the API**. That's a textbook **I/O-bound** profile: it barely touches the CPU — its cost is time spent waiting, not compute.
>
> Two more things: per-filing times are **spiky** (each is however long the API takes, so 10 ≠ exactly 10 × one), and the script pins `OPENBLAS_NUM_THREADS=1` so a job that only makes API calls doesn't spin up a thread per core on the shared node.

---

## Main quest — Document Your Script's Resource Needs

Now that you've profiled **10 filings**, write down what you measured — and use it to **estimate what 100 filings would need**. Open the `README.md` in your repo and add a **Resource Profile** section:

```markdown
## Resource Profile

### extract_form_3_batch.py — 10 filings (measured)

- Wall-clock time (real):
- CPU cores used:
- RAM peak (RES / % Mem):
- Serial or parallel:

### Estimate for 100 filings

- Wall-clock time (real): ~10 × the 10-filing time
- CPU cores used: (same as 10 — serial work doesn't need more cores)
- RAM peak: (same as 10 — one filing in memory at a time)
```

Fill in the actual numbers from your `time` and `userload` output. Because this job is **API-bound and serial**, cores and RAM stay flat as you add files — **only wall-clock time grows.** That's the kind of estimate you'll reach for later when you ask the cluster to run this at scale: modest CPU and RAM, but a time budget that scales with the number of filings.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="readme"> I profiled 10 filings, documented the time/CPU/RAM, and estimated what 100 filings would need</label>

---

## Side quest — Vectorized vs. Non-Vectorized

{: .note }
> Finished early? This one is self-contained — no script of your own required.

The single biggest speedup in scientific Python is usually **vectorization**: pushing a computation into NumPy (compiled C loops) instead of a Python `for` loop. We ship a script that computes the same sum of squares both ways — profile it and see the difference.

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

**Have a script from your own research?** Even better — copy it over and profile it the same way, then hunt for a hot `for` loop you could vectorize:

```bash
scp /path/to/your/script.py SUNetID@yen.stanford.edu:~/your-project/
```

Record what you find in your `README.md`:

```
## Resource Profile — vectorized vs. loop

- Python loop time (real):
- NumPy vectorized time (real):
- Speedup:
- (If you profiled your own script) a loop you could vectorize:
```

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side2"> I profiled the vectorized vs. non-vectorized demo (and/or my own script) and recorded the speedup</label>

---

## Side quest — Change the number of cores

{: .note }
> Finished early? Try one or both of these.

Open `scripts/mystery_script.py` and change `num_cores = 4` to a different number — try **1**, or **8**. Then **profile it again** just like you did above: `watch userload` in one terminal, and `time` + `htop` in the other.

```bash
time python scripts/mystery_script.py
```

Document what changes and discuss with your neighbor: How many `python` processes appear in `htop` now? How many **Cores** in `userload`? Did the `real` (wall-clock) time go up or down? Does the resource usage match the number you set?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side6"> I changed num_cores in the mystery script, re-profiled it, and can explain how the processes and cores changed</label>

**Side quest — Profile an I/O-Bound Script**

Everything you've profiled so far is CPU-bound (`user` time dominates). Write a tiny script that's I/O-bound instead — for example, one that reads and re-writes a large file in a loop — and profile it the same way. Compare its `sys` and `user` times to the mystery script's.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side7"> I profiled an I/O-bound script and compared its sys vs. user time to the mystery script's</label>

