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

## 💻 Exercise 1 — Run Your Script

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

While it runs (or after it finishes), discuss as a class:

- ❓ **Why** do we want to estimate the resources a script uses?
- ❓ Do you know what resources this script is using right now?
- ❓ How would you estimate them?

This page will teach you **how to estimate the resources your script is actually using**. This matters whether you wrote the script yourself or someone handed it to you.

---

## Exercise — Profile a Mystery Script

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

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="mystery"> I profiled scripts with time, watch userload, and htop, and can tell serial from parallel execution</label>

---

## 💻 Exercise 3 — Profile Your Day 2 Script

Now apply the same technique to a script you already know: `extract_form_3_one_file.py` from Day 2.

Terminal 1:
```bash
time python scripts/extract_form_3_one_file.py
```

Terminal 2:
```bash
watch userload
```

Note the `real`, `user`, and `sys` times when it finishes. Is this script serial or parallel?

---

## Exercise — Document Your Script's Resource Needs

Now that you have profiled `extract_form_3_one_file.py`, write down what you found. Open the `README.md` in your repo and add a **Resource Profile** section:

```markdown
## Resource Profile

### extract_form_3_one_file.py (one file)

- Wall-clock time (real):
- CPU time (user):
- CPU cores used:
- RAM peak:
- Serial or parallel:
```

Fill in the actual numbers from your `time` and `userload` output. This documents what the script needs to process a single file — a baseline you will use when scaling up.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="readme"> I documented the script's time, CPU, and RAM in README.md</label>

---

## Optional practice — Vectorized vs. Non-Vectorized

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

## Optional practice — Catch What `userload` Misses

{: .note }
> Finished early? Try one or both of these.

`watch userload` only samples every 2 seconds — a short memory spike between samples can hide from it entirely. Run the mystery script again with `/usr/bin/time -v` instead:

```bash
/usr/bin/time -v python scripts/mystery_script.py
```

Look for **Maximum resident set size** in the output — this is the script's true peak RAM over its whole run. Compare it to what `watch userload` showed you earlier. Did `userload` miss a spike?

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side6"> I compared /usr/bin/time -v's peak RAM to what watch userload showed me</label>

**Optional practice — Profile an I/O-Bound Script**

Everything you've profiled so far is CPU-bound (`user` time dominates). Write a tiny script that's I/O-bound instead — for example, one that reads and re-writes a large file in a loop — and profile it the same way. Compare its `sys` and `user` times to the mystery script's.

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side7"> I profiled an I/O-bound script and compared its sys vs. user time to the mystery script's</label>

