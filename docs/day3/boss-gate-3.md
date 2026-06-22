---
layout: default
title: "Boss Gate 3"
parent: "Day 3 — The SLURM Mines"
nav_order: 9
permalink: /day3/boss-gate-3/
---

# Boss Gate 3

*The Foreman steps aside and gestures at a towering wall of parchment — one hundred SEC filings, each sealed with wax, each hiding secrets of insider trades. The torches flicker. The cluster hums. This is what the whole descent was for: a single array job that processes them all in parallel, fails gracefully, and leaves behind a clean CSV and a chronicle anyone could follow. You've learned the recipe, calibrated the resources, and armored your pipeline against failure. Now prove it.*

---

## 🔑 The Challenge

The final gate stands open — but only your output will unlock it.

{: .boss }
> **Boss Battle — The Great Scroll Sweep**
>
> Process all 100 SEC filings from `data/sec_filings/` using a SLURM job array:
>
> 1. Each array task extracts the insider name, role, and transaction date from one filing
> 2. Outputs are written to `/scratch/$USER/results/filing_N.json` (one per task)
> 3. A merge script combines all results into `results/great_scroll_sweep.csv`
> 4. Failed tasks are listed in `results/failed_tasks.txt`
> 5. Your array job script, merge script, and `README.md` are committed to your fork
>
> **Submit:**
> ```bash
> git add jobs/array_extract.sh scripts/merge_results.py results/great_scroll_sweep.csv results/failed_tasks.txt README.md
> git commit -m "Boss Gate 3: Great Scroll Sweep complete"
> git push
> ```
>
> **Your commit should include:**
> - The job script (`jobs/array_extract.sh`)
> - The merge script (`scripts/merge_results.py`)
> - The final CSV (`results/great_scroll_sweep.csv`)
> - The failure log (`results/failed_tasks.txt` — can be empty if all tasks succeeded)
> - `README.md` from The Chronicle — what the pipeline does, how to run it, known limitations

{: .tip }
> 💡 Check `results/failed_tasks.txt` before committing. If tasks failed, resubmit the array. If you completed the Checkpoint Charm side quest in the Array Cavern, your pipeline will skip already-completed tasks automatically.

---

<label class="quest-check"><input type="checkbox" data-room="d3-boss-gate" data-key="commit"> Committed and pushed CSV + scripts + README</label>

---

## ⚔️ Skills This Gate Tests

- You can design and fire a SLURM job array that fans out across 100 inputs simultaneously
- You can wield `$SLURM_ARRAY_TASK_ID` to route each task to exactly the right file
- You can merge parallel outputs into a single clean CSV with explicit failure reporting
- You can write a README clear enough that a stranger — or future-you — could rerun the whole pipeline cold
- You can commit and push the complete deliverable: scripts, results, and documentation, all in one move
