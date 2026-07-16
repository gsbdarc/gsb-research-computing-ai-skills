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

## Main Exercise — Debug and Fix Your Job

{: .important }
> **Exercise:** Your job failed. Find out why, fix the script, and resubmit until it completes successfully.

**Step 1 — Check the status**

```bash
sacct -u $USER --format=JobID,JobName,State,Elapsed,MaxRSS --starttime=today
```

Look for your job in the `State` column. A failed job shows `FAILED`.

**Step 2 — Read the logs**

Your job writes output to `logs/extract_JOBID.out` and errors to `logs/extract_JOBID.err`. Start with the error log:

```bash
cat logs/extract_JOBID.err
```

Then check the output log:

```bash
cat logs/extract_JOBID.out
```

The error message tells you what went wrong — a wrong path, a missing module, a Python exception. Read it carefully.

**Step 3 — Fix the script**

Once you've found the bug, fix it. Test interactively on the Yens first to confirm the fix works:

```bash
cd ~/rf-bootcamp-2026
source .venv/bin/activate
python scripts/extract_form_3_one_file.py
```

**Step 4 — Resubmit**

```bash
sbatch slurm/extract_form_3_one_file.slurm
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
