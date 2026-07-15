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
> Finished early? Try any of these.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side1"> I made at least one plot or visualization</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

**Side Quest — Check the Per-User Limits**

Group the processes by `user` and compute total `cpu_pct` and `mem_pct` per person. Is anyone close to the per-user limits mentioned back in The Scales?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side3"> I grouped processes by user and checked their usage against the per-user limits</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

**Side Quest — Cores vs. Threads (the double-booked chef)**

The table above says yen1 has "256 cores." That's not the whole story. Many Yen nodes are **double-threaded**: they have **128 physical cores** but present **256 logical CPUs** (threads) to the operating system. `nproc`, `top`, and the `cpu_pct` column all count the 256 logical ones.

{: .note }
> 🍳 **The double-booked chef.** A physical core is one chef at one station — one pair of hands. **Hyper-threading** lets a single chef work two tickets at once: real cooking spends a lot of time *waiting* — for water to boil, the oven to preheat, an ingredient to arrive (for a CPU: waiting on memory or disk). While ticket A waits, the chef quietly makes progress on ticket B. The kitchen *looks* like it has 256 chefs, but there are really 128 — each juggling two orders.
>
> The catch: when both tickets need chopping at the *same* instant, they fight over the one pair of hands. A second thread usually buys ~20–30% more throughput, not 2×. So a CPU-bound job (constant chopping, no waiting) won't run twice as fast on 256 threads as on 128 — the **physical** cores are the real ceiling. A job that waits a lot (heavy I/O) benefits more.

Find out for yourself. SSH to a Yen node and run:

```bash
lscpu | grep -E 'Socket|Core|Thread'
```

Read three lines:
- `Socket(s)` — how many physical CPU chips the node has
- `Core(s) per socket` — physical cores on each chip
- `Thread(s) per core` — `2` means hyper-threading is on

Then work it out: **physical cores = Socket(s) × Core(s) per socket**, and **logical CPUs = physical cores × Thread(s) per core** (this should match `nproc`). Add one line to your `README.md`: is the node you're on double-threaded, and how many physical cores back its logical CPUs?

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side2"> I ran `lscpu`, worked out physical cores vs. logical threads, and noted whether my node is double-threaded</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side2` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

**Side Quest — How Far Is the Ingredient from the Stove? (cache & memory levels)**

RAM isn't the only place a CPU keeps data. Between the cores and main memory sits a hierarchy of ever-smaller, ever-faster **caches**. The rule is always the same: the closer to the stove, the faster — but the less room there is.

{: .note }
> 🍳 **Distance from the stove.** The CPU works fastest on data that's *closest* to it, and closeness always trades against size:
> - **Registers** — what's literally in the chef's hands right now: the knife, a pinch of salt. Instant, but only a few items.
> - **L1 cache** — the little rack on the cutting board, right at the station. A handful of ingredients within arm's reach, no walking.
> - **L2 cache** — the cabinet next to the stove. Bigger, one step away, still quick.
> - **L3 cache** — the shared shelf in the middle of the kitchen, used by all the chefs (cores). Bigger still, a short walk.
> - **RAM** — the fridge across the room. Lots of space, but you walk over every time.
> - **Disk / scratch** — the pantry in the basement, or the grocery store down the road. Practically unlimited, but slow to fetch from.
>
> Each step down is roughly 10–100× more space and 10–100× slower to reach. Fast programs keep the ingredients they're actively using close to the stove; a **cache miss** is having to walk to the fridge mid-recipe — or worse, drive to the store.

See your node's caches:

```bash
lscpu | grep -i cache
```

You'll see `L1d` (data), `L1i` (instructions), `L2`, and `L3` with their sizes. Order them smallest → largest, match each to the analogy above, and note which level is **shared across all cores** (hint: the big one). Add one line to your `README.md` explaining why the *smallest* cache is the *fastest*.

<label class="quest-check"><input type="checkbox" data-room="d3-data-mine" data-key="side4"> I found the cache sizes with `lscpu`, ordered them by size, and can explain why the smallest cache is the fastest</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-data-mine.side4` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.
