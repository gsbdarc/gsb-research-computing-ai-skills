---
layout: default
title: "The Data Mine"
parent: "Day 3 — The SLURM Mines"
nav_order: 4
permalink: /day3/data-mine/
---

# The Data Mine

<div data-room-id="d3-data-mine"></div>

*Before you can request resources from the mountain, you must understand what the mountain has already given away. Generations of miners have left behind records — who ran what, how long they toiled, how much ore they consumed. The ledgers are thick and unreadable at a glance. But to a researcher with the right tools, they are a map of the cluster itself.*

---

## 🗡️ Main Quest — Read the Mine Records

{: .important }
> **Quest:** Open the Yens monitoring snapshot and figure out what it is telling you — without being told what to look for.

**Step 1 — Open the data**

```bash
cd ~/rf-bootcamp-2026
cat data/yens_sample.txt
```

Read the whole file slowly. Don't skim. There are several sections — notice how they are different from each other.

**Step 2 — Explore**

Use whatever tool you want. Spend 10–15 minutes digging in.

```bash
claude          # open Claude Code and ask it anything you want
```

Or open JupyterHub and work in a notebook. Or just read and think. No direction — just look.

**Step 3 — Write down your observations**

Before we discuss as a class, write down at least 3 things you noticed. Some questions to consider:

- Who is using the most resources? How can you tell?
- Do you see anything that looks like it went wrong?
- What do you not understand? What columns are confusing?
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

- What stood out to you in the data?
- Which user caught your attention? Why?
- What do you think the different sections of the file represent?
- What confused you?

---

## What You Were Looking At

*Your instructor will walk through this after the discussion.*

The snapshot has four sections:

**User summary** — how much CPU and memory each researcher is using on the cluster right now. Each row is one person.

**Job history** — a record of past jobs: who ran them, how long they ran, how much memory they used, whether they finished or something went wrong.

**Process list** — every individual running program on one node at one moment. Each row is one process.

**Disk usage** — how much shared storage each user has consumed.

Key vocabulary you just saw in the data:

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

## Skills Learned

- You can read raw system monitoring data and extract meaning from it
- You know what a process is, what a user is, what CPU% and RSS mean
- You understand the difference between a per-user summary and a per-process listing
