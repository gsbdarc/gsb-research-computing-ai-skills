---
layout: default
title: "Day 3 Challenge"
parent: "Day 3 — Cluster Computing"
nav_order: 10
permalink: /day3/boss-gate-3/
---

# Day 3 Challenge

---

## The Challenge — Scale Up to a Batch

In Writing & Submitting a SLURM Job you ran the extraction on a *single* filing. Now scale it to a **batch of ~10**: `scripts/extract_form_3_batch.py` loops over every filing listed in `data/aws_links.csv` and writes one JSON per filing into `results/`.

1. Write `slurm/extract_form_3_batch.slurm` — shebang, `#SBATCH` directives, `cd`, `source .venv/bin/activate`, then `python scripts/extract_form_3_batch.py`.
2. **Re-estimate your resources.** You profiled *one* filing back in Profiling Resource Usage. The batch processes filings one at a time, so **RAM stays about the same**, but **wall-clock time scales with the number of filings** — set `#SBATCH --time` to roughly single-file time × the number of filings, plus headroom. Don't just reuse your single-file number.
3. Submit with `sbatch`; confirm it enters the queue with `squeue --me`.
4. When it finishes, check `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS` and confirm `results/` has one JSON per filing.
5. Update `README.md` — how to run the batch, the resources you requested and *why*, and where the output lands.
6. Commit and push:

```bash
git add slurm/extract_form_3_batch.slurm README.md
git commit -m "Day 3 Challenge: batch SLURM submission complete"
git push
```

Your commit should include:
- `slurm/extract_form_3_batch.slurm` with `#SBATCH` directives **re-estimated for ~10 filings**, not guesses and not just your single-file numbers
- `README.md` — what the batch does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## Optional practice — Feel the Pain Point

Your batch ran the ~10 filings **one after another**. Now imagine hundreds or thousands: even in a batch, they run serially, so the wall-clock time just keeps climbing. Add a few more URLs to `data/aws_links.csv`, resubmit, and watch `Elapsed` grow roughly linearly with the file count. Running them **in parallel** — many at once instead of one at a time — is exactly what Day 4's job arrays exist to do.

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="side1"> I grew the batch, saw the elapsed time climb, and can describe why serial processing doesn't scale and how job arrays would help</label>

<details markdown="1">
<summary>🔄 Sync to leaderboard</summary>

**Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d3-boss-gate.side1` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

</details>

---

## 📊 End of Day 3 — Sync Your Progress

Let your instructor see where you landed today. You already have Claude Code open on the Yens — ask it to handle the sync.

In your terminal, inside `~/rf-bootcamp-2026`, tell Claude something like:

> Look at the `DAYS` list in `docs/assets/js/quest-log.js` to find the exact `room.key` names for Day 3. In `quest_log.json` at my repo root (create it if it doesn't exist yet), set those keys to `true` for everything I completed today: [list what you finished, e.g. "the profiling and data-exploration exercises, and the Day 3 Challenge"]. Then commit and push it to my fork.

The leaderboard updates within 2 minutes once Claude pushes. Your instructor can see how many quests you completed and whether you completed the Day 3 Challenge.

---

## Skills This Challenge Tests

- Write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- Scale a single-file job to a batch and re-estimate resources (time scales with the workload; memory often doesn't)
- Submit a job and confirm it entered the queue
- Read `sacct` output and identify whether the job succeeded or failed
- Write a README clear enough that a colleague could rerun the job without asking you
- Commit and push a complete deliverable: script and documentation together
