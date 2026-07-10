---
layout: default
title: "The Data Mine"
parent: "Day 3 — The SLURM Mines"
nav_order: 5
permalink: /day3/data-mine/
---

# The Data Mine

<div data-room-id="d3-data-mine"></div>

---

## Main Exercise — Explore the Yens Monitoring Data

{: .important }
> **Exercise:** Open the Yens monitoring snapshot and figure out what it is telling you — without being told what to look for.

**Step 1 — Open the data**

```bash
cd ~/rf-bootcamp-2026
cat data/yens_sample.txt
```

Read the whole file. There are several sections — notice how they differ from each other.

**Step 2 — Explore**

Use whatever tool you want. Spend 10–15 minutes digging in.

```bash
claude          # open Claude Code and ask it anything
```

Or open JupyterHub and work in a notebook. Or just read and think.

**Step 3 — Write down your observations**

Before the class discussion, write down at least 3 things you noticed:

- Who is using the most resources? How can you tell?
- Do you see anything that looks like it went wrong?
- What columns are confusing?
- Does anything surprise you?

When you have written down your observations — put a **🟢 green sticky** on your laptop. If the file won't open or you are stuck, put up a **🔴 red sticky**.

---

## Compare with a Neighbor

Before the class discussion, talk to the person next to you:

- What did you each notice first?
- Did you find the same things, or different things?
- What questions do you both have?

---

## Class Discussion

*Your instructor will lead this. Share what you found.*

- What stood out in the data?
- Which user caught your attention? Why?
- What do you think the different sections represent?
- What confused you?

---

## What You Were Looking At

*Your instructor will walk through this after the discussion.*

The snapshot has four sections:

**User summary** — how much CPU and memory each researcher is using on the cluster right now. Each row is one person.

**Job history** — a record of past jobs: who ran them, how long they ran, how much memory they used, whether they finished or failed.

**Process list** — every individual running program on one node at one moment. Each row is one process.

**Disk usage** — how much shared storage each user has consumed.

Key vocabulary:

| Term | What it means |
|------|---------------|
| **Process** | One running program. A single Python script = one process. A notebook kernel = one process. |
| **User** | The account that owns a process. Every researcher is a user on the Yens. |
| **CPU%** | How much of one core this process is using. 100% = one full core. 200% = two cores. |
| **RSS / MEM** | Resident memory — how much RAM this process is actively holding right now. |

When you run your extraction script on a Yen node, it becomes a process owned by your user. Its CPU% and RSS are exactly what you see in `htop` and `ps`.

---

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="main"> I explored the cluster data and can identify processes, users, CPU, and memory in the output</label>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Programmatic analysis**

Open JupyterHub or a Python shell. Load the process list from `data/yens_sample.txt` using pandas and write a single line that finds the username with the highest total CPU usage. (Hint: `read_csv` with a separator, `groupby`, `sum`, `idxmax`.)

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side1"> I wrote one line of pandas code to find the top CPU user</label>

**Bonus 2 — Find the longest job**

Look at the job history section of `data/yens_sample.txt`. Find the single longest-running job. How long did it run, and what command did it execute?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side2"> I found the longest-running job in the job history</label>

---

## Key Concepts

- A process is one running program; a user is the account that owns it
- CPU% and RSS are the two numbers that matter most when estimating resource needs
- You can read raw system monitoring data and extract meaning from it
