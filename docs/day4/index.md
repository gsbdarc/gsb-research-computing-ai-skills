---
layout: floor
title: "Day 4 — Parallelization & GPUs"
nav_order: 4
has_children: true
has_toc: false
permalink: /day4/
floor: 4
---

# Day 4 — Parallelization & GPUs

Day 4 scales yesterday's single SLURM job into a full research pipeline. You'll fan one script across hundreds of filings with **job arrays**, then move onto **GPU nodes** — comparing the A30, A40, and H200 and seeing how VRAM sets a ceiling on the model size you can load. From there you'll run a **local LLM** on cluster hardware with Ollama, weigh it against the Stanford AI Playground and third-party APIs, and learn to spot where LLMs fail before their output reaches your results. The Day 4 Challenge caps the day — and the bootcamp — with the full stack running end to end: **SLURM → GPU → local LLM**, documented so it reruns.

**Duration:** ~3 hours

---

## Day 3 Recap

- Profiled the extraction script to measure its real time and memory needs
- Wrote and submitted `slurm/extract_form_3_one_file.slurm` as a batch job, with `#SBATCH` directives grounded in those measurements
- Monitored the job with `squeue` and `sacct`, and documented the pipeline in `README.md`

Any questions about Day 1–3 we can discuss before we move on.

---

## Sections

Work through the sections in order — later ones build on earlier ones, and the Day 4 Challenge draws on everything you've learned.

| Section | Format | What you'll learn |
|------|--------|-----------------|
| [Parallelization Basics](parallelization/) | 🖊️ Concept | What running work in parallel means, when it helps, and why independent tasks are the key |
| [Parallel Jobs with SLURM Arrays](array-cavern/) | 💻 Hands-on | Process hundreds of filings in one submission with job arrays, combine the outputs, and avoid recomputation when jobs fail |
| [Choosing a GPU](armory/) | 🖊️ Concept | Why LLMs need GPUs, the GPU types on the Yens (A30, A40, H200), and how they map to nodes |
| [Running GPU Jobs](h200-chamber/) | 💻 Hands-on | Submit a job to the GPU partition and see how VRAM limits the model size you can load |
| [Local LLMs with Ollama](summoning-circle/) | 💻 Hands-on | Run a model entirely on cluster hardware with Ollama and keep your data on the Yens |
| [Local vs. Cloud Inference](engine-room/) | 💬 Concept | Pick between Ollama, the Stanford AI Playground, and third-party APIs for a given task |
| [LLM Failure Modes](trap-garden/) | 💬 Discussion | Validate LLM outputs by comparing across models, and catch where an LLM goes wrong before it corrupts results at scale |
| [Day 4 Challenge](boss-gate-4/) | 🔑 Capstone | Run an array job across two LLMs, combine and compare the outputs, and write a README so a colleague could rerun it |
| [Staying Connected](research-guild/) | 🏛️ Community | Where to get help and how to stay plugged in after the bootcamp |
