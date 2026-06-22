---
layout: default
title: "Boss Gate 4"
parent: "Day 4 — The GPU Fortress"
nav_order: 8
permalink: /day4/boss-gate-4/
---

# Boss Gate 4

*The Archmage's chamber. The final seal. Everything you've built across four days — the shell commands, the SSH aliases, the venvs, the Pydantic models, the SLURM arrays, the GPU job, the local LLM — all of it comes together here. The Champion's Ascent is not a new skill. It is a demonstration that the old ones are yours.*

{: .note }
> **Oracle's Revelation — the course bot unmasked:** The dungeon's oracle was powered by the same tools you've now mastered. System prompt → context injection → Stanford AI Playground call → structured response. Every answer it gave was a Pydantic model. Every "hint" was a retrieval-augmented lookup over the dungeon room map. You didn't just learn to use the oracle — you learned to build one.

---

{: .boss }
> **Boss Battle — Champion's Ascent**
>
> **Part 1 — Swap the endpoint:**
> Take your Day 3 array job (`array_extract.sh` / `extract_filing.py`) and modify it to call **Ollama on the H200** instead of the Stanford AI Playground. The Ollama server must be running on `yen-gpu4` in a `screen` session before you submit the array.
>
> **Part 2 — Compare outputs:**
> Run the same 5 filings through both the Playground (gpt-4o-mini) and Ollama (your chosen model). Save the results side-by-side in `results/comparison.csv` with columns: `filename`, `playground_name`, `ollama_name`, `playground_role`, `ollama_role`.
>
> **Part 3 — Privacy ruling:**
> Write one paragraph in `results/privacy_ruling.md` stating: which bucket do these SEC filings belong to, can they go to a cloud API, can they go to Ollama, and what would change if the filings contained unreported PII.
>
> **Part 4 — Commit your README:**
> Ensure `README.md` describes the full pipeline including both endpoints and the privacy ruling.
>
> **Submit:**
> ```bash
> git add results/comparison.csv results/privacy_ruling.md README.md
> git commit -m "Boss Gate 4: Champion's Ascent complete"
> git push
> ```

{: .tip }
> The Ollama base URL from JupyterHub is `http://localhost:11434/v1` — but only if Ollama is serving on the same node. If you're on a different node than `yen-gpu4`, the URL needs to point to `yen-gpu4` explicitly. Ask the instructor for the correct URL for your setup.

---

<label class="quest-check"><input type="checkbox" data-room="d4-boss-gate" data-key="commit"> Committed and pushed all Champion's Ascent deliverables</label>

---

## The Full Stack You've Demonstrated

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
| Data governance | 3-bucket privacy rule | The Grand Hall |

---

{: .important }
> **All four floors cleared.**
>
> Every skill in the table above is yours. Now check the leaderboard — the dungeon isn't over until everyone sees how many chests you opened. Sync your quest log and see where you rank.
>
> What's next from here: Sherlock (Stanford's HPC), Redivis (data platform), fine-tuning, multi-node jobs, and whatever your research actually needs. The dungeon was the foundation. You know where the doors are.

