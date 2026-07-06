---
layout: default
title: "The Data Mine"
parent: "Day 3 — The SLURM Mines"
nav_order: 3
permalink: /day3/data-mine/
---

# The Data Mine

<div data-room-id="d3-data-mine"></div>

*Before you can request resources from the mountain, you must understand what the mountain has already given away. Generations of miners have left behind records — who ran what, how long they toiled, how much ore they consumed. The ledgers are thick and unreadable at a glance. But to a researcher with the right tools, they're a map of the cluster itself: when it strains, who takes the most, and what a reasonable request actually looks like.*

---

## 🖊️ What Is System Data?

The Yens cluster keeps detailed records of everything that runs on it. Four sources tell the full story:

| Source | What it shows |
|--------|--------------|
| `userload` | **Your own** CPU and memory usage on the current interactive Yen node |
| `squeue` | All queued and running SLURM jobs cluster-wide — who submitted what, resource requests, wait time |
| `sacct` | Historical record of past jobs — elapsed time, peak memory, CPU hours, exit status |
| `ps aux` | All running processes on a node — what's executing and what it's consuming right now |
| Disk stats | How much shared storage is in use — `df -h /scratch/shared` |

Before you write a single `#SBATCH` directive, it helps to see what real jobs on this cluster actually look like.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Dig into real Yens cluster data. Use an AI coding agent or your notebook to find patterns — who runs what, which jobs go over budget, when the cluster is quiet.

**Step 1 — Open the data**

A snapshot of recent Yens monitoring data is included in your course repo:

```bash
cat ~/rf-bootcamp-2026/data/yens_sample.txt
```

Take a moment to read it. You'll see output from `userload`, `sacct`, and `ps` — the same tools you'll use in The Scales to profile your own script.

---

**Step 2 — Analyze with an AI agent (tool of your choice)**

Open whichever tool you prefer:

**Option A — Claude Code on the Yens** *(recommended — you set this up on Day 1)*
```bash
claude
```

**Option B — Notebook** — open a Jupyter notebook and load the file:
```python
with open("data/yens_sample.txt") as f:
    data = f.read()
print(data)
```
Then paste sections into the AI of your choice.

**Option C — Any other AI coding agent** — paste the content directly.

---

**Step 3 — Ask for insights**

Paste the contents of `yens_sample.txt` and try these prompts:

*"Here is system monitoring data from a shared HPC cluster. Tell me: which users are using the most CPU and memory? Which jobs ran over their resource request? Are there any jobs that look like they might have failed or been killed? What does this suggest about when to submit new jobs?"*

*"Look at the sacct output. For the jobs that completed successfully, what is the typical ratio of requested time to actual elapsed time? What does this tell me about how much margin I should add when writing my own `--time` directive?"*

*"Based on the userload snapshot, when would be a good time for a new user to submit a resource-intensive job?"*

---

**Step 4 — Class discussion**

Take 10 minutes to share what you found:

- Who dominated CPU during this snapshot? What kind of jobs?
- Which jobs ran over their memory request? What does that mean for the job?
- What pattern do you see in elapsed time vs. requested time?
- If you were submitting your own job right now, what would you request — and when?

{: .note }
> The goal here isn't to copy numbers from this dataset into your own job script. The goal is to build intuition: what does "this cluster is under load" look like in data? What does an overrun job look like? You'll measure your own script in The Scales — this gives you a mental model for what the output means.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="main"> Main Quest complete — I've analyzed Yens system data and can read resource usage patterns</label>

---

## 🧠 Skills Learned

- You can read `userload`, `sacct`, and `ps` output and understand what each column means
- You know what an overrun job looks like (MaxRSS > requested memory, elapsed > requested time)
- You can use an AI coding agent to find patterns in tabular cluster data
- You have intuition for when the cluster is busy vs. quiet — useful for scheduling your own submissions
