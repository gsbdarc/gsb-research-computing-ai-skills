---
layout: default
title: "The Storage Pantry"
parent: "Day 3 — The Hearth"
nav_order: 4
permalink: /day3/storage-pantry/
---

# The Storage Pantry

<div data-room-id="d3-data-mine"></div>

---

## What Is This Data?

The Yens run a monitoring script every few minutes that calls `top` in batch mode — the same tool you'd run interactively, but automated. It captures a snapshot of every process running on the node at that instant, then saves it as a CSV.

The file below is one such snapshot from yen1, taken on July 10, 2026 at 20:56. Each row is one process.

| Column | What it means |
|--------|---------------|
| `timestamp` | When the snapshot was taken |
| `host` | Which Yen node |
| `pid` | Process ID — unique number the OS assigns to each running program |
| `user` | SUNetID of the process owner |
| `pr` | Scheduling priority — lower numbers run first (`rt` means real-time priority) |
| `ni` | Nice value — a user-adjustable priority offset; negative = higher priority, positive = lower |
| `virt` | Virtual memory reserved by the process (bytes) |
| `res` | Resident memory — RAM physically in use right now (bytes) |
| `shr` | Shared memory (bytes) — memory the process shares with others, e.g. loaded libraries |
| `s` | Status: `R` = running (using CPU), `S` = sleeping (idle, holding RAM), `I` = idle kernel thread |
| `cpu_pct` | % of one CPU core in use — 100% means one full core (yen1 has 256 cores) |
| `mem_pct` | % of total node RAM in use |
| `time_plus` | Cumulative CPU time since the process started |
| `command` | Program name (`top` truncates long names to 8 characters) |
| `type` | `u` = user process, `s` = system/kernel process |

---

## Your Turn

Load the file and explore. Use Claude, a notebook, a script — whatever works for you. There are no required questions.

```python
import pandas as pd

cols = ['timestamp','host','pid','user','pr','ni','virt','res','shr',
        's','cpu_pct','mem_pct','time_plus','command','type']

DATA = '/scratch/shared/rf-bootcamp-2026/data/yenstop_2026-07-10-20-56-06.csv'

df = pd.read_csv(DATA, header=None, names=cols, on_bad_lines='skip')
df.head()
```

Some directions if you want a place to start — but don't feel limited to these:

- Who is using the most CPU? The most memory? Are they the same person?
- How many processes are actually running right now versus just sleeping?
- What commands appear most often? What do you think they are?
- How long have some of these processes been running? Does anything surprise you?
- What does virtual memory look like compared to resident memory for the same process?

Make a plot. Ask Claude to explain something. Follow a thread that looks interesting.

---

## Write It Up

Find one thing in the data worth keeping. Add a short section to your `README.md` — a few sentences describing what you found and what it tells you about how shared research nodes actually get used.

It doesn't have to be the most impressive finding. It just has to be true, specific, and explained in plain language.

{: .note }
> This `README.md` keeps growing today — you'll add a Resource Profile section in The Scales and a full pipeline writeup in The Recipe Book. Same file the whole time.

When you're ready — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="main"> I loaded the data, explored it, and wrote up one true, specific finding in my README</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## Side Quests

{: .note }
> Finished early? Try one or both of these.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side1"> I made at least one plot or visualization</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

**Side Quest — Check the Per-User Limits**

Group the processes by `user` and compute total `cpu_pct` and `mem_pct` per person. Is anyone close to the per-user limits mentioned back in The Scales?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side3"> I grouped processes by user and checked their usage against the per-user limits</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.
