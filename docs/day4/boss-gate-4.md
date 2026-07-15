---
layout: default
title: "Boss Gate 4"
parent: "Day 4 — The GPU Fortress"
nav_order: 8
permalink: /day4/boss-gate-4/
---

# Boss Gate 4

{: .note }
> **How the course assistant worked:** The bot you've asked questions all week used the same tools you've now learned. System prompt → context injection → Stanford AI Playground call → structured response. Every answer it returned was a Pydantic model; every "hint" was a retrieval-augmented lookup over the room map. You didn't just use it — you now know how to build one.

---

## The Challenge

This capstone combines everything from the week into one pipeline — all at once.

{: .boss }
> **Boss Gate 4 — Full Pipeline**
>
> **Part 1 — Scale with an array job:**
> Reuse your `jobs/array_extract.sh` from The Array Cavern (`--array=1-100`). Each task processes one filing and writes its result to `/scratch/shared/$USER/results/filing_N.json`. After the array completes, merge all outputs into `results/extracted_filings.csv`.
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
> git commit -m "Boss Gate 4 complete"
> git push
> ```

💡 The Ollama base URL from JupyterHub is `http://localhost:11434/v1` — but only if Ollama is serving on the same node. If you're on a different node than `yen-gpu4`, the URL needs to point to `yen-gpu4` explicitly. Ask the instructor for the correct URL for your setup.
{: .tip }

---

<label class="quest-check"><input type="checkbox" data-room="d4-boss-gate" data-key="commit"> Committed and pushed all Boss Gate 4 deliverables</label>

---

## The Full Stack You've Built

Every row in this table is a tool you used this week and the room where you learned it.

| Layer | Tool | Room |
|-------|------|------|
| Shell & files | CLI + wildcards + scp | The Command Spire, The Grimoire Vault |
| Remote access | SSH + screen | The SSH Gate, The Persistence Chamber |
| Version control | Git fork → commit → push | The Repository |
| Python environment | venv + pip + dotenv | The Venv Forge, The Key Vault |
| LLM extraction | Stanford AI Playground + Pydantic | The Oracle's Chamber, The Binding Room |
| Batch scaling | SLURM job array | The Foreman's Desk, The Array Cavern |
| Fault tolerance | Completed log + skip (Checkpoint Charm) | The Array Cavern |
| GPU computing | H200 via `--gres=gpu:1` | The H200 Chamber |
| Local LLMs | Ollama on cluster hardware | The Summoning Circle |
| Documentation | README + project layout | The Chronicle |
| Data governance | 3-bucket privacy rule | The Crucible (Day 2) |

---

{: .important }
> **All four days complete.**
>
> Check the leaderboard and sync your quest log to see how many side quests you completed and where you rank.
>
> What's next: Sherlock (Stanford's HPC), Redivis (data platform), fine-tuning, multi-node jobs, and whatever your research demands. This week was the foundation — you now know where each piece fits.
