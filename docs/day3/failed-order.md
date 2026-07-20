---
layout: default
title: "Failed Order"
parent: "Day 3 — The Hearth"
nav_order: 8
permalink: /day3/failed-order/
---

# Failed Order

<div data-room-id="d3-watch-tower"></div>

---

## Main Exercise — Debug and Fix a Real Failure

We've staged a job that failed for a past cohort. Your task: submit it, watch it fail, read the logs to find out *why*, fix it, and resubmit until it completes.

{: .important }
> **Exercise:** Debug `slurm/last_year_bug.slurm` (which runs `scripts/last_year_bug.py`) until it shows `COMPLETED`.

**Step 1 — Submit the broken job**

```bash
cd ~/rf-bootcamp-2026
mkdir -p logs
sbatch slurm/last_year_bug.slurm
```

**Step 2 — Check the status**

```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS --starttime=today
```

Look for the job in the `State` column — it shows `FAILED`.

**Step 3 — Read the logs**

The job writes normal output to `logs/last_year_<jobid>.out` and errors to `logs/last_year_<jobid>.err`. Start with the error log:

```bash
cat logs/last_year_*.err
```

Read the traceback carefully. It's a Python exception — **what file or directory is it complaining about?** (This is one of the most common ways a job that "worked on my laptop" dies on a fresh compute node.)

**Step 4 — Fix the script**

Once you've found the bug, fix `scripts/last_year_bug.py`. Test interactively on the Yens first to confirm the fix works:

```bash
source .venv/bin/activate
python scripts/last_year_bug.py
```

**Step 5 — Resubmit**

```bash
sbatch slurm/last_year_bug.slurm
```

Check it enters the queue and eventually completes:

```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS --starttime=today
```

When your job shows `COMPLETED` — put a **🟢 green sticky** on your laptop.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="main"> I found the bug, fixed it, resubmitted, and my job shows COMPLETED</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Audit your resource usage**

After your job completes, compare what you requested vs what you actually used:

```bash
sacct -j JOBID --format=JobID,AllocCPUS,CPUTime,MaxRSS,ReqMem,Elapsed
```

- **AllocCPUS** — CPUs you requested
- **MaxRSS** — peak RAM the job actually used
- **ReqMem** — RAM you requested

Did you over-request memory? Use these numbers to calibrate your next job's `--mem` and `--cpus-per-task`.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side1"> I audited my resource usage and know whether I over- or under-requested</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Bonus 2 — Watch a job live**

While your job is running (status `R`), you can follow the output as it writes:

```bash
tail -f logs/extract_JOBID.out
```

Ctrl-C to stop following. This is useful for long jobs where you want to see progress without waiting for completion.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side2"> I followed a running job's output live with tail -f</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.side2` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Bonus 3 — Decode the exit code**

```bash
sacct -j JOBID --format=JobID,ExitCode,State
```

An `ExitCode` like `137` often means the job was killed for using too much memory (`SIGKILL`). Look up what your job's exit code means.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side3"> I decoded my job's ExitCode with sacct and can explain what it means</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.side3` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Bonus 4 — Trigger an OOM on purpose**

Edit your `#SBATCH --mem` directive down to something clearly too small (e.g. `--mem=10M`) and resubmit. Watch it get killed for running out of memory, then compare its `sacct` `State` and `.err` signature to the bug you fixed earlier — can you tell an OOM kill apart from a code bug at a glance now?

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side4"> I deliberately triggered an OOM kill and compared its failure signature to my original bug</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.side4` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

**Bonus 5 — Trigger a timeout on purpose**

The other way jobs die is running out of *time*. Submit a job that asks for far less time than it needs — `--wrap` runs an inline command as a throwaway job:

```bash
sbatch --time=00:00:10 --wrap="sleep 120"
```

It gets killed at the 10-second limit. Check how SLURM reports it:

```bash
sacct -j JOBID --format=JobID,State,Elapsed,ExitCode
```

The `State` shows `TIMEOUT` (and the log notes `CANCELLED ... DUE TO TIME LIMIT`). You've now seen three distinct failure fingerprints — a **code bug** (Python traceback), an **OOM kill** (`ExitCode 137`), and a **timeout** (`State TIMEOUT`) — and can tell them apart at a glance.

<label class="quest-check"><input type="checkbox" data-room="d3-watch-tower" data-key="side5"> I deliberately triggered a timeout and can tell TIMEOUT, OOM, and code-bug failures apart</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-watch-tower.side5` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>
