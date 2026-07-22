---
layout: default
title: "Putting It All Together"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 7
permalink: /day4/putting-it-all-together/
---

# Putting It All Together

<div data-room-id="d4-capstone"></div>

This capstone combines everything from the week into one pipeline — all at once.

---

## The Challenge

{: .important }
> **Part 1 — Scale with an array job:**
> Reuse your `jobs/array_extract.sh` from [Submitting an Array Job](../array-exercise/) (`--array=1-100`). Each task processes one filing and writes its result to `/scratch/shared/$USER/results/filing_N.json`. After the array completes, merge all outputs into `results/extracted_filings.csv`.
>
> **Part 2 — Swap the endpoint:**
> Modify your array script to call **Ollama on the H200** instead of the Stanford AI API Gateway. The Ollama server must be running on `yen-gpu4` in a `screen` session before you submit the array.
>
> **Part 3 — Compare outputs:**
> Run the same 5 filings through both the Playground (`gpt-4o-mini`) and Ollama (your chosen model). Save the results side-by-side in `results/comparison.csv` with columns: `filename`, `playground_name`, `ollama_name`, `playground_role`, `ollama_role`.
>
> **Part 4 — Commit your README:**
> Ensure `README.md` describes the full pipeline: array job, both endpoints, how to rerun.
>
> **Submit:**
> ```bash
> git add results/extracted_filings.csv results/comparison.csv README.md
> git commit -m "Capstone complete"
> git push
> ```

{: .tip }
> **New to `screen`?** It keeps a process running on a node after you disconnect — so the Ollama server stays up while your array job runs. Start a session with `screen -S ollama`, launch the server inside it, then press `Ctrl-A` then `D` to detach and leave it running (`screen -r ollama` reattaches). Full guide: [rcpedia — `screen`](https://rcpedia.stanford.edu/_user_guide/screen/).

{: .tip }
> The Ollama base URL from JupyterHub is `http://localhost:11434/v1` — but only if Ollama is serving on the same node. If you're on a different node than `yen-gpu4`, the URL needs to point to `yen-gpu4` explicitly. Ask the instructor for the correct URL for your setup.

<label class="quest-check"><input type="checkbox" data-room="d4-capstone" data-key="commit"> Committed and pushed all capstone deliverables</label>

---

## The Full Stack You've Built

Every row in this table is a tool you used this week and where you learned it — in the order you met them, from Day 1 to Day 4.

| Layer | Tool | Where you learned it |
|-------|------|---------------------|
| Shell & files | CLI + wildcards + scp | Day 1 — Command Line Basics, Bulk File Operations, Transferring Files |
| Remote access | SSH | Day 1 — Connecting to a Cluster |
| Version control | Git fork → commit → push | Day 1 — Version Control with Git |
| Python environment | venv + pip + dotenv | Day 2 — environment setup |
| LLM extraction | Stanford AI API Gateway + Pydantic | Day 2 — structured extraction |
| Data governance | 3-bucket privacy rule | Day 2 — data classification |
| Batch jobs | SLURM `sbatch` + profiling | Day 3 — batch jobs |
| Documentation | README + project layout | Day 3 — reproducibility |
| Parallel scaling | SLURM job arrays | Day 4 — SLURM Job Arrays |
| Fault tolerance | Skip work already done on rerun | Day 4 — SLURM Job Arrays |
| GPU computing | GPU via `--gres=gpu:1` | Day 4 — How to Run LLMs on the Yens |
| Local LLMs | Ollama on cluster hardware | Day 4 — How to Run LLMs on the Yens |
| Handling failures | Validation + guardrails | Day 4 — Handling LLM Failure Modes |

---

## 📊 Final Sync

This is the last sync — make it count.

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Look at the `DAYS` list in `docs/assets/js/quest-log.js` for the exact `room.key` names for Day 4, and in `quest_log.json` at my repo root (create it if missing) set to `true` every key for what I finished today — [list what you completed, e.g. the parallelization and SLURM-arrays quests, the array exercise, running an LLM, and this capstone]. Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

The leaderboard updates within a couple of minutes — this is your final rank.

---

{: .important }
> **All four days complete.**
>
> Check the leaderboard to see how many optional exercises you completed and where you rank.
>
> But note that there's still more to learn: Sherlock (Stanford's HPC), Redivis (data platform), fine-tuning, multi-node jobs, and whatever your research demands. This week was just the foundation.
