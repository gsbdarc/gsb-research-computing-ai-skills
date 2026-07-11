---
layout: default
title: "The Storage Pantry"
parent: "Day 3 — The Hearth"
nav_order: 4
permalink: /day3/data-mine/
---

# The Storage Pantry

<div data-room-id="d3-data-mine"></div>

*Behind the kitchen, past a low doorway, the castle keeps its receipts. Stacks of ledgers record every job that has passed through the hearth: who ran it, which station, how long it burned, how much it consumed. Most of it looks like noise. But noise has a structure — and if you know how to read it, you can see exactly who has been hogging the burners and whose jobs have been running for three days straight. Someone hands you a lantern.*

---

## What Is This Data?

The Yens run a monitoring script every few minutes that captures what `top` would show — a ranked list of the most active processes on the node at that instant. Each row is one process.

| Column | What it means |
|--------|---------------|
| `timestamp` | When the snapshot was taken |
| `host` | Which Yen node |
| `pid` | Process ID |
| `user` | SUNetID of the owner |
| `virt` | Virtual memory — address space reserved by the process |
| `res` | Resident memory — RAM actually in use right now |
| `s` | Status: `R` = running, `S` = sleeping |
| `cpu_pct` | % of one CPU core used right now |
| `mem_pct` | % of total node RAM used |
| `time_plus` | Cumulative CPU time since the process started (HH:MM:SS) |
| `command` | Program name (truncated to 8 chars by `top`) |

---

## Main Exercise — Read the Pantry Ledger

{: .important }
> **Exercise:** Load a real monitoring snapshot from yen1 and answer four questions about who is using the node.

Open JupyterHub or Claude Code, then load the file:

```python
import pandas as pd

cols = ['timestamp','host','pid','user','pr','ni','virt','res','shr',
        's','cpu_pct','mem_pct','time_plus','command','type']

# Path on scratch — your instructor will confirm the exact location
DATA = '/scratch/users/nrapstin/rf-bootcamp-2026/yenstop_2026-07-10-20-56-06.csv.gz'

df = pd.read_csv(DATA, header=None, names=cols)
df.head(10)
```

Work through these four questions:

**Q1 — Who is burning the most CPU right now?**

```python
df.sort_values('cpu_pct', ascending=False)[['user','command','cpu_pct','s']].head(10)
```

Which user is at the top? What are they running?

**Q2 — Running vs sleeping**

```python
df['s'].value_counts()
```

`R` = running (burner is on), `S` = sleeping (burner off but still holding fridge space). Which is more common? What does that tell you about shared nodes?

**Q3 — Who has been cooking the longest?**

```python
df[['user','command','time_plus','cpu_pct']].sort_values('time_plus', ascending=False).head(5)
```

`time_plus` is cumulative CPU time. Find the process that has been running the longest. How many hours?

**Q4 — The VIRT vs RES puzzle**

```python
df[df['command'] == 'claude'][['user','virt','res','cpu_pct']]
```

Look at `virt` vs `res` for these processes. What do you notice? Why would a process reserve far more memory than it actually holds?

{: .note }
> **Virtual vs resident memory.** `virt` is the address space a process has *reserved* — like reserving an entire shelf in the fridge. `res` is what it's actually *using* — the food currently on that shelf. Claude Code and notebook kernels often reserve enormous virtual address space (for memory-mapped files, libraries, etc.) while using a fraction of it as resident RAM. When the fridge fills up and slows everyone down, it's `res` that matters — not `virt`.

**Compare with a neighbor** before the class discussion:
- What did you each notice first?
- Which user surprised you most?
- What questions do you have?

When you've worked through all four questions — put a **🟢 green sticky** on your laptop.

{: .important }
> **Class discussion:** Which user caught your attention? Which process has been running the longest — and what does that tell you about how some researchers use the Yens? The monitoring script itself (`topdump`) shows up in the data — what does that mean?

---

{: .highlight }
> **Key concepts**
> - A process is one running program. One user can have many processes — each one a recipe on a burner.
> - `cpu_pct` tells you who is actively computing. `res` tells you who is holding fridge space.
> - A sleeping process (`S`) still occupies RAM. The fridge fills up even when nobody is cooking.
> - `time_plus` reveals long-running jobs — processes that have been going for hours or days.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="main"> I read the yenstop snapshot and can identify who is using the most CPU and memory on yen1</label>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Total memory footprint per user**

```python
df[df['type'] == 'u'].groupby('user')['mem_pct'].sum().sort_values(ascending=False)
```

Which user has the largest total memory footprint across all their processes? Is it the same user who has the highest single-process CPU?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side1"> I aggregated memory by user and found who holds the most RAM across all their processes</label>

**Bonus 2 — What are people running?**

```python
df[df['type'] == 'u']['command'].value_counts()
```

What tools appear most often? `top` truncates long names to 8 characters — `jupyter+` and `remote-+` are cut off. Can you guess the full names from context?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side2"> I explored the process names and identified what tools researchers are running on yen1</label>
