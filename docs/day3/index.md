---
layout: floor
title: "Day 3 — The Hearth"
nav_order: 3
has_children: true
has_toc: false
permalink: /day3/
floor: 3
---

# Day 3 — The Hearth

Today shifts from running scripts interactively to submitting them as real **batch jobs**. You'll start with a shared vocabulary for **CPU**, **RAM**, and **storage**, see why the cluster needs a **scheduler** at all, and dig into real usage data from the Yens. From there you'll learn to **profile** a script so you know what resources to request instead of guessing, write and submit a **SLURM** job from scratch, **debug** one that fails, and document the whole pipeline in a **README**. **Boss Gate 3** caps the day with a SLURM job backed by real measurements — the foundation Day 4 scales up with **GPU jobs** and **job arrays**.

---

## Day 2 Recap

- Built a virtual environment on the Yens and installed dependencies from `requirements.txt`
- Wrote `scripts/extract_form_3_one_file.py` — calls the Stanford AI API to extract structured fields from one SEC Form 3 filing
- Used Pydantic to validate and structure the LLM output

Any questions about Day 1–2 we can discuss before we move on.

---

## Rooms

| Room | Format | What you master |
|------|--------|-----------------|
| [The Kitchen](kitchen/) | 🥪💬 Demo + discussion | **Compute environments** — so you pick the right one (laptop, Yens, or cloud) instead of wasting your advisor's compute budget (or your afternoon) |
| [The Scales](scales/) | 💻 Hands-on | **Profiling** — so your own jobs request the resources they actually need instead of guessing and stalling in the queue |
| [The Storage Pantry](storage-pantry/) | 💻🤖 Hands-on (Claude-assisted) | **Data exploration** — the same messy-real-data instinct you'll need on your own datasets |
| [The Back Kitchen](back-kitchen/) | 💬💻 Discussion + hands-on | **Interactive vs. scheduled Yen nodes** — so your research jobs get dedicated resources instead of competing with everyone else on a shared login node |
| [The Ticket Rail](ticket-rail/) | 💻 Hands-on | **Batch jobs** — the actual mechanism you'll use to run your own research code on the cluster |
| [Failed Order](failed-order/) | 💻 Hands-on | **Debugging** — the skill that saves you hours when your own job fails and you need to know why |
| [The Recipe Book](recipe-book/) | 💻🤖 Hands-on (Claude-assisted) | **Reproducibility** — what makes collaborators, and your future self, trust and rerun your results |
| [Boss Gate 3](boss-gate-3/) | 🔑 Capstone | **Profiled submission** — the exact loop you'll repeat for every real research pipeline from here on |
