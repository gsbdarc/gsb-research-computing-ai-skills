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

In Profiling Resource Usage you measured **10 filings** and estimated 100. Now actually run **100**: open `scripts/extract_form_3_batch.py`, change `NUM_FILINGS` to `100`, and it loops over 100 filings from `data/aws_links.csv`, writing one JSON per filing into `results/`.

1. Write `slurm/extract_form_3_batch.slurm` — shebang, `#SBATCH` directives, `cd`, `source .venv/bin/activate`, then `python scripts/extract_form_3_batch.py` (with `NUM_FILINGS = 100`).
2. **Re-estimate your resources.** You profiled *10* filings back in Profiling Resource Usage. The batch processes filings one at a time, so **RAM and cores stay about the same**, but **wall-clock time scales with the number of filings** — set `#SBATCH --time` to roughly your 10-filing time × 10, plus headroom. Don't just reuse your 10-filing number. Did your estimate hold up?
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
- `slurm/extract_form_3_batch.slurm` with `#SBATCH` directives **re-estimated for 100 filings**, not guesses and not just your 10-filing numbers
- `README.md` — what the batch does, how to run it, where output lands

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed job script + README</label>

---

## Side quest — Feel the Pain Point

Your batch ran the 100 filings **one after another**. Now imagine thousands: even in a batch, they run serially, so the wall-clock time just keeps climbing. Bump `NUM_FILINGS` up — try `200` — resubmit, and watch `Elapsed` grow roughly linearly with the file count. Running them **in parallel** — many at once instead of one at a time — is exactly what Day 4's job arrays exist to do.

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="side1"> I grew the batch, saw the elapsed time climb, and can describe why serial processing doesn't scale and how job arrays would help</label>

---

## 📊 End of Day 3 — Sync Your Progress

Let your instructor see where you landed today:

1. Open the **Quest Log** (bottom-left corner) → click **Sync**.
2. Click **Copy token**.
3. On the Yens, inside your clone, run `python3 scripts/quest_sync.py <paste-token>`.

The leaderboard updates within ~2 minutes. (First time only: sign in once with `gh auth login` — see Day 1 — so the push works.)

---

## Skills This Challenge Tests

- Write a SLURM job script from scratch with `#SBATCH` directives grounded in real profiling data
- Scale a single-file job to a batch and re-estimate resources (time scales with the workload; memory often doesn't)
- Submit a job and confirm it entered the queue
- Read `sacct` output and identify whether the job succeeded or failed
- Write a README clear enough that a colleague could rerun the job without asking you
- Commit and push a complete deliverable: script and documentation together
