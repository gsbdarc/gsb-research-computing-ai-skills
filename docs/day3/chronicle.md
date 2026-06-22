---
layout: default
title: "The Chronicle"
parent: "Day 3 — The SLURM Mines"
nav_order: 8
permalink: /day3/chronicle/
---

# The Chronicle

<div data-room-id="d3-chronicle"></div>

*Torchlight flickers across the dungeon's library — floor-to-ceiling shelves of forgotten pipelines, abandoned repos, README files that were never written. Somewhere in the queue, your jobs are still running. Your memory of every flag, every design choice, every "I'll just use 4 GB and see what happens" is still sharp and alive. This is the only moment you will ever have this clarity. Write it down now — carve it into the stone — because six months from now you will open this repository in the dark, and there will either be a map waiting for you, or there won't.*

---

## 🗡️ Main Quest

The terminal is still warm. The jobs are still humming. This is your window — seal the knowledge before it fades.

{: .important }
> **Quest:** Write a `README.md` for your Day 3 pipeline while the code is still fresh — before you close the terminal.

Create `README.md` in your repo root (or a `day3/` subdirectory):

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

## What this does

Extracts insider name, role, and transaction date from SEC Form 3 filings
using the Stanford AI Playground (GPT-4o-mini) and a SLURM job array.
Results are combined into a single CSV.

## How to run

### Prerequisites
- Access to the Stanford Yens cluster
- Stanford AI Playground API key in `.env`
- Python venv at `.venv/` (see Day 2 setup)

### Steps
```bash
# 1. Prepare input list
ls data/sec_filings/*.txt > /scratch/$USER/filings_list.txt

# 2. Submit the array
sbatch jobs/array_extract.sh

# 3. Monitor
watch -n 5 squeue -u $USER

# 4. Merge
python3 scripts/merge_results.py
```

## Outputs

- `results/extracted_filings.csv` — one row per filing
- Console warning if any tasks failed

## Data

Input: SEC Form 3 filings from EDGAR (public domain).

## Known limitations

- Only the first 4,000 characters of each filing are sent to the model
- Non-standard filing formats may produce empty fields
```

{: .note }
> You will update this README in the Day 4 capstone when you swap in the Ollama endpoint.

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="main"> Main Quest complete — README written</label>

---

## 📦 Chests

Two treasures are hidden in the walls of this library — crack them open and your repo transforms from a pile of scripts into a fortress any collaborator can navigate.

{: .chest }
> **Chest 1 — Structure Sigil:** Reorganize your repo into the standard research layout: `data/` for inputs, `scripts/` for code, `results/` for outputs, `jobs/` for SLURM scripts. Update your README paths to match. Does the repo make more sense to a first-time reader now?

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="chest1"> Structure Sigil unlocked</label>

The second chest rewards the researchers who think about their future selves — the ones who will return to this work months from now and need to know not just *what* changed, but *why*.

{: .chest }
> **Chest 2 — Changelog Charm:** Create a `CHANGELOG.md` with an entry for today: what you built, what model you used, what the output schema looks like. Add a second entry for Day 4 when you swap in Ollama. Why does this matter for reproducibility?

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="chest2"> Changelog Charm unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Structure Sigil** — standard research project layout (`data/`, `scripts/`, `results/`, `jobs/`, `README.md`) that any collaborator recognizes immediately.
>
> **Changelog Charm** — `CHANGELOG.md` with dated entries; future-you reading it in six months will understand *why* the pipeline changed, not just what changed.

---

## 🧠 Skills Learned

- You can now write a README that arms any reader with exactly what they need: what this does, how to run it, what comes out, and where the edges are
- You can now document while the code is fresh — treating the README as part of the build, not an afterthought left for never
- You can now impose a standard project directory structure that makes any repo immediately legible to collaborators, advisors, and future-you
