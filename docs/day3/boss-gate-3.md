---
layout: default
title: "Boss Gate 3"
parent: "Day 3 — The Hearth"
nav_order: 10
permalink: /day3/boss-gate-3/
---

# Boss Gate 3

---

## Boss Gate 3 — First SLURM Submission

Submit your Day 2 LLM extraction script as a SLURM batch job:

1. Write `slurm/extract_form_3_one_file.slurm` with correct `#SBATCH` directives — time, memory, and cores based on your profiling from The Scales
2. Submit with `sbatch`; confirm the job enters the queue with `squeue --me`
3. Wait for it to complete; inspect the output with `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS`
4. Update `README.md` with SLURM instructions — how to submit, how to monitor, where the output goes
5. Commit and push:

```bash
git add slurm/extract_form_3_one_file.slurm README.md
git commit -m "Boss Gate 3: first SLURM submission complete"
git push
```

Your commit should include:
- `slurm/extract_form_3_one_file.slurm` with `#SBATCH` directives based on real profiling, not guesses
- `README.md` — what the script does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## Side Quest — Feel the Pain Point

Cleared the gate early? Manually rerun your script against 2-3 more filings, one at a time — editing paths, renaming outputs, resubmitting by hand each time. Notice what gets tedious. That tedium is exactly what Day 4's job arrays exist to eliminate.

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="side1"> I manually reran my script against a few more filings and can describe what would need to change to scale to hundreds</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-boss-gate.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## 📊 End of Day 3 — Sync Your Progress

Let your instructor see where you landed today. You already have Claude Code open on the Yens — ask it to handle the sync.

In your terminal, inside `~/rf-bootcamp-2026`, tell Claude something like:

> Look at the `DAYS` list in `docs/assets/js/quest-log.js` to find the exact `room.key` names for Day 3. In `quest_log.json` at my repo root (create it if it doesn't exist yet), set those keys to `true` for everything I completed today: [list what you finished, e.g. "the Head Chef and Data Mine main quests, and Boss Gate 3"]. Then commit and push it to my fork.

The leaderboard updates within 2 minutes once Claude pushes. Your instructor can see how many quests you completed and whether you cleared the Boss Gate.

---

## Skills This Boss Gate Tests

- Write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- Submit a job and confirm it entered the queue
- Read `sacct` output and identify whether the job succeeded or failed
- Write a README clear enough that a colleague could rerun the job without asking you
- Commit and push a complete deliverable: script and documentation together
