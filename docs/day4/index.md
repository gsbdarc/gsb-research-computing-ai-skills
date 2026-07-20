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

Any questions about Day 1–3 before we move on?

---

## Sections

Work through the sections in order — later ones build on earlier ones, and the Day 4 Challenge draws on everything you've learned.

| Section | Format | What you'll learn |
|------|--------|-----------------|
| [Parallelization Basics](parallelization/) | 🖊️ Concept | What running work in parallel means, when it helps, and why independent tasks are the key |
| [SLURM Job Arrays](slurm-arrays/) | 🖊️ Concept | How to operationalize parallelization on the cluster: job arrays, `--array`, `SLURM_ARRAY_TASK_ID`, and making tasks safe to rerun |
| [Submitting an Array Job](array-exercise/) | 💻 Hands-on | Build, submit, and monitor a 100-filing array job, then combine the per-task outputs into one CSV |
| [Why Run LLMs on the Yens?](why-local-llms/) | 🖊️ Concept | When to run a model yourself on the Yens vs. calling a cloud API — privacy, cost, reproducibility, and open vs. proprietary models |
| [How to Run LLMs on the Yens](running-llms/) | 🖊️💻 Concept + Hands-on | Why LLMs need a GPU, how to request one on the Yens, and running an open model with Ollama (same code as the Playground, different `base_url`) |
| [Validating LLM Outputs](validating-llm-outputs/) | 💬 Discussion | 🚧 TODO — not written yet |
| [Putting It All Together](putting-it-all-together/) | 🔑 Capstone | 🚧 TODO — not written yet |
| [Staying In Touch](staying-in-touch/) | 🏛️ Community | 🚧 TODO — not written yet |
