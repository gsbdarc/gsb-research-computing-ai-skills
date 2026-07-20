---
layout: floor
title: "Day 3 — Cluster Computing"
nav_order: 3
has_children: true
has_toc: false
permalink: /day3/
floor: 3
---

# Day 3 — Cluster Computing

Today shifts from running scripts interactively to submitting them as real **batch jobs**. You'll start with a shared vocabulary for **CPU**, **RAM**, and **storage**, see why the cluster needs a **scheduler** at all, and dig into real usage data from the Yens. From there you'll learn to **profile** a script so you know what resources to request instead of guessing, write and submit a **SLURM** job from scratch, **debug** one that fails, and document the whole pipeline in a **README**. The **Day 3 Challenge** caps the day with a SLURM job backed by real measurements — the foundation Day 4 scales up with **GPU jobs** and **job arrays**.

---

## Day 2 Recap

- Built a virtual environment on the Yens and installed dependencies from `requirements.txt`
- Wrote `scripts/extract_form_3_one_file.py` — calls the Stanford AI API to extract structured fields from one SEC Form 3 filing
- Used Pydantic to validate and structure the LLM output

Any questions about Day 1–2 we can discuss before we move on.

---

## Sections

| Room | Format | What you master |
|------|--------|-----------------|
| [Compute Environments](compute-environments/) | 🥪💬 Demo + discussion | **Compute environments** — so you pick the right one (laptop, Yens, or cloud) instead of wasting your advisor's compute budget (or your afternoon) |
| [Profiling Resource Usage](profiling/) | 💻 Hands-on | **Profiling** — so your own jobs request the resources they actually need instead of guessing and stalling in the queue |
| [Exploring Cluster Usage Data](cluster-usage-data/) | 💻🤖 Hands-on (Claude-assisted) | **Data exploration** — the same messy-real-data instinct you'll need on your own datasets |
| [The SLURM Scheduler](slurm-scheduler/) | 💬💻 Discussion + hands-on | **Interactive vs. scheduled Yen nodes** — so your research jobs get dedicated resources instead of competing with everyone else on a shared login node |
| [Writing & Submitting a SLURM Job](slurm-job/) | 💻 Hands-on | **Batch jobs** — the actual mechanism you'll use to run your own research code on the cluster |
| [Debugging Failed Jobs](debugging-jobs/) | 💻 Hands-on | **Debugging** — the skill that saves you hours when your own job fails and you need to know why |
| [Documenting Your Pipeline](documenting-pipeline/) | 💻🤖 Hands-on (Claude-assisted) | **Reproducibility** — what makes collaborators, and your future self, trust and rerun your results |
| [Day 3 Challenge](boss-gate-3/) | 🔑 Capstone | **Profiled submission** — the exact loop you'll repeat for every real research pipeline from here on |
