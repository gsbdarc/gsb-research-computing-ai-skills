---
layout: default
title: "Boss Gate 4"
parent: "Day 4 — The GPU Fortress"
nav_order: 8
permalink: /day4/boss-gate-4/
---

# Boss Gate 4

*The Archmage's chamber looms before you — ancient stone humming with the heat of a thousand GPU cores. The final seal pulses like a heartbeat. Four days of battle have led here: the shell commands you carved into muscle memory, the SSH tunnels you bored through solid rock, the venvs you forged in the Forge, the Pydantic models you bound like spells, the SLURM arrays you unleashed like war parties, the H200 you bent to your will, the local LLM you summoned from raw silicon. The Champion's Ascent asks for nothing new. It asks you to prove that everything old is now, irrevocably, yours.*

{: .note }
> **Oracle's Revelation — the course bot unmasked:** The dungeon's oracle was powered by the same tools you've now mastered. System prompt → context injection → Stanford AI Playground call → structured response. Every answer it gave was a Pydantic model. Every "hint" was a retrieval-augmented lookup over the dungeon room map. You didn't just learn to use the oracle — you learned to build one.

---

## 🔑 The Challenge

The Archmage does not test you with riddles. It tests you with the full stack — all at once.

{: .boss }
> **Boss Battle — Champion's Ascent**
>
> **Part 1 — Scale with an array job:**
> Reuse your `jobs/array_extract.sh` from The Array Cavern (`--array=1-100`). Each task processes one filing and writes its result to `/scratch/shared/$USER/results/filing_N.json`. After the array completes, merge all outputs into `results/great_scroll_sweep.csv`.
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
> git add results/great_scroll_sweep.csv results/comparison.csv README.md
> git commit -m "Boss Gate 4: Champion's Ascent complete"
> git push
> ```

💡 The Ollama base URL from JupyterHub is `http://localhost:11434/v1` — but only if Ollama is serving on the same node. If you're on a different node than `yen-gpu4`, the URL needs to point to `yen-gpu4` explicitly. Ask the instructor for the correct URL for your setup.
{: .tip }

---

<label class="quest-check"><input type="checkbox" data-room="d4-boss-gate" data-key="commit"> Committed and pushed all Champion's Ascent deliverables</label>

---

## ⚔️ The Full Stack You've Demonstrated

Every row in this table is a weapon you forged, a door you unlocked, a skill no one can take back from you.

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

## 📊 End of Day 4 — Final Sync

This is the last sync. Make it count.

**Step 1 — Export your quest log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/gsb-research-computing-ai-skills`) → **Add file → Upload files** → drag `quest_log.json` in → **Commit changes** to `main`.

The leaderboard updates within 2 minutes — this is your final rank.

---

{: .important }
> **All four floors cleared.**
>
> Every skill in the table above is yours — not borrowed, not half-understood, yours. Now check the leaderboard — the dungeon isn't over until everyone sees how many side quests you completed. Sync your quest log and see where you rank.
>
> What's next: Sherlock (Stanford's HPC), Redivis (data platform), fine-tuning, multi-node jobs, and whatever your research actually demands. The dungeon was the foundation. You know where every door leads. Go build something real.
