---
layout: default
title: "Day 4 Challenge"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 8
permalink: /day4/boss-gate-4/
---

# Day 4 Challenge

<div data-room-id="d4-boss-gate"></div>

{: .note }
> **How the course assistant worked:** The bot you've asked questions all week used the same tools you've now learned. System prompt → context injection → Stanford AI Playground call → structured response. Every answer it returned was a Pydantic model; every hint was a retrieval-augmented lookup. You didn't just use it — you now know how to build one.

---

## The Challenge

This capstone combines everything from the week into one pipeline — all at once.

{: .important }
> **Task — Full Pipeline**
>
> **Part 1 — Scale with an array job:**
> Reuse your `jobs/array_extract.sh` from [Parallel Jobs with SLURM Arrays](../array-cavern/) (`--array=1-100`). Each task processes one filing and writes its result to `/scratch/shared/$USER/results/filing_N.json`. After the array completes, merge all outputs into `results/extracted_filings.csv`.
>
> **Part 2 — Swap the endpoint:**
> Modify your array script to call **Ollama on the H200** instead of the Stanford AI Playground. The Ollama server must be running on `yen-gpu4` in a `screen` session before you submit the array.
>
> **Part 3 — Compare outputs:**
> Run the same 5 filings through both the Playground (gpt-4o-mini) and Ollama (your chosen model). Save the results side-by-side in `results/comparison.csv` with columns: `filename`, `playground_name`, `ollama_name`, `playground_role`, `ollama_role`.
>
> **Part 4 — Commit your README:**
> Ensure `README.md` describes the full pipeline: array job, both endpoints, how to rerun.
>
> **Submit:**
> ```bash
> git add results/extracted_filings.csv results/comparison.csv README.md
> git commit -m "Day 4 Challenge complete"
> git push
> ```

💡 The Ollama base URL from JupyterHub is `http://localhost:11434/v1` — but only if Ollama is serving on the same node. If you're on a different node than `yen-gpu4`, the URL needs to point to `yen-gpu4` explicitly. Ask the instructor for the correct URL for your setup.
{: .tip }

---

<label class="quest-check"><input type="checkbox" data-room="d4-boss-gate" data-key="commit"> Committed and pushed all Day 4 Challenge deliverables</label>

---

## The Full Stack You've Built

Every row in this table is a tool you used this week and where you learned it.

| Layer | Tool | Where you learned it |
|-------|------|---------------------|
| Shell & files | CLI + wildcards + scp | Day 1 — Command Line Basics, Bulk File Operations, Transferring Files |
| Remote access | SSH + screen | Day 1 — Connecting to a Cluster |
| Version control | Git fork → commit → push | Day 1 — Version Control with Git |
| Python environment | venv + pip + dotenv | Day 2 — environment setup |
| LLM extraction | Stanford AI Playground + Pydantic | Day 2 — structured extraction |
| Batch scaling | SLURM job array | Day 3 batch jobs; Day 4 — Parallel Jobs with SLURM Arrays |
| Fault tolerance | Completed log + skip on rerun | Day 4 — Parallel Jobs with SLURM Arrays |
| GPU computing | H200 via `--gres=gpu:1` | Day 4 — Running GPU Jobs |
| Local LLMs | Ollama on cluster hardware | Day 4 — Local LLMs with Ollama |
| Documentation | README + project layout | Day 3 — reproducibility |
| Data governance | 3-bucket privacy rule | Day 2 — data classification |

---

## 📊 End of Day 4 — Final Sync

This is the last sync. Make it count.

**Step 1 — Export your progress log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/rf-bootcamp-2026`) → **Add file → Upload files** → drag `quest_log.json` in → **Commit changes** to `main`.

The leaderboard updates within 2 minutes — this is your final rank.

---

{: .important }
> **All four days complete.**
>
> Check the leaderboard and sync your progress log to see how many optional exercises you completed and where you rank.
>
> What's next: Sherlock (Stanford's HPC), Redivis (data platform), fine-tuning, multi-node jobs, and whatever your research demands. This week was the foundation — you now know where each piece fits.
