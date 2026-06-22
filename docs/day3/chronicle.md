---
layout: default
title: "The Chronicle"
parent: "Day 3 — The SLURM Mines"
nav_order: 8
permalink: /day3/chronicle/
---

# The Chronicle

<div data-room-id="d3-chronicle"></div>

*The dungeon's library. Write the record now — while the pipeline is still running in the queue, while you remember what every flag does and why you chose 4 GB of memory instead of 2. Six months from now you will open this repository and thank yourself. Or you won't have written it, and you won't remember.*

---

## Main Quest

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

## Chests

{: .chest }
> **Chest 1 — Structure Sigil:** Reorganize your repo into the standard research layout: `data/` for inputs, `scripts/` for code, `results/` for outputs, `jobs/` for SLURM scripts. Update your README paths to match. Does the repo make more sense to a first-time reader now?

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="chest1"> Structure Sigil unlocked</label>

{: .chest }
> **Chest 2 — Changelog Charm:** Create a `CHANGELOG.md` with an entry for today: what you built, what model you used, what the output schema looks like. Add a second entry for Day 4 when you swap in Ollama. Why does this matter for reproducibility?

<label class="quest-check"><input type="checkbox" data-room="d3-chronicle" data-key="chest2"> Changelog Charm unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Structure Sigil** — standard research project layout (`data/`, `scripts/`, `results/`, `jobs/`, `README.md`) that any collaborator recognizes immediately.
>
> **Changelog Charm** — `CHANGELOG.md` with dated entries; future-you reading it in six months will understand *why* the pipeline changed, not just what changed.

---

## Skills Learned

- Write a README that answers: what does this do, how do I run it, what do I get, what are the limits
- Document while the code is fresh — not as a final step, but as part of the workflow
- Apply a standard project directory layout that makes repos immediately navigable
