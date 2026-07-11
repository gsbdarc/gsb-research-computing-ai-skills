---
layout: default
title: "The Scales"
parent: "Day 3 — The Hearth"
nav_order: 3
permalink: /day3/scales/
---

# The Scales

*On a shelf near the ticket rail hangs a set of scales, old and precise. Every seasoned cook knows to use them before writing an order — because the head chef does not accept estimates. "About an hour" is not a time limit. "Probably needs 2G" is not a memory request. These numbers go on the parchment, and the parchment goes to the chef, and the chef does not negotiate. This room is where you learn to weigh the work before you commit to it.*

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

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="exercise2"> I profiled extract_form_3_one_file.py and understand its time, CPU, and RAM usage</label>

---

## Main Quest — Document Your Script's Resource Needs

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

## Side Quest — Profile Your Own Research Script

{: .note }
> Finished early? Have a script from your own research? Try this.

Copy a script from your research project onto the Yens and profile it using the same two-terminal technique.

```bash
# Copy your script to the Yens (run this on your laptop)
scp /path/to/your/script.py SUNetID@yen.stanford.edu:~/your-project/
```

Then profile it:

Terminal 1:
```bash
time python your-project/script.py
```

Terminal 2:
```bash
watch userload
```

Record what you observe in a `README.md` in that project folder:

```
## Resource Profile

- Script: script.py
- Wall-clock time (real):
- CPU time (user):
- CPU cores used:
- RAM peak:
- Serial or parallel?
```

<label class="quest-check"><input type="checkbox" data-room="d3-head-chef" data-key="side2"> I profiled my own research script and recorded its time, CPU, and RAM in a README</label>
