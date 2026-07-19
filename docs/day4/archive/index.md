---
layout: default
title: "Day 4 — The GPU Fortress (archived index)"
nav_exclude: true
search_exclude: true
---

# Day 4 — The GPU Fortress

Today scales yesterday's single SLURM job into a full research pipeline. You'll fan one script across hundreds of filings with **job arrays**, then move onto **GPU nodes** — comparing the A30, A40, and H200 and seeing how **VRAM** sets a ceiling on the model size you can load. From there you'll run a **local LLM** on cluster hardware with **Ollama**, weigh it against the **Stanford AI Playground** and third-party APIs, and learn to spot where LLM agents fail before their output reaches your results. **Boss Gate 4** caps the day — and the bootcamp — with the full stack running end to end: **SLURM → GPU → local LLM**, documented so it reruns.

---

## Day 3 Recap

- Profiled the extraction script to measure its real time and memory needs
- Wrote and submitted `slurm/extract_form_3_one_file.slurm` as a batch job, with `#SBATCH` directives grounded in those measurements
- Monitored the job with `squeue` and `sacct`, and documented the pipeline in `README.md`

Any questions about Day 1–3 we can discuss before we move on.

---

## Rooms

| Room | Format | What you master |
|------|--------|-----------------|
| [The Array Cavern](array-cavern/) | 💻 Hands-on | **Job arrays** — so you process hundreds of filings in one submission instead of resubmitting them by hand one at a time |
| [The Armory](armory/) | 🖊️ Concept | **GPU selection** — so you request the right card (A30, A40, or H200) for your model instead of over- or under-asking |
| [The H200 Chamber](h200-chamber/) | 💻 Hands-on | **GPU jobs** — so you can run work on a GPU node and understand how VRAM limits the model size you can load |
| [The Summoning Circle](summoning-circle/) | 💻 Hands-on | **Local LLMs** — so you can run a model entirely on cluster hardware with Ollama and keep your data on the Yens |
| [The Engine Room](engine-room/) | 💬 Concept | **Local vs. cloud inference** — so you can pick between Ollama, the Stanford AI Playground, and third-party APIs for a given task |
| [The Trap Garden](trap-garden/) | 💬 Discussion | **LLM failure modes** — so you catch where an agent goes wrong before it corrupts your results at scale |
| [Boss Gate 4](boss-gate-4/) | 🔑 Capstone | **Full pipeline** — the complete loop from SLURM to GPU to local LLM, documented so a colleague could rerun it |
| [The Research Guild](research-guild/) | 🏛️ Community | **Staying connected** — where to get help and how to stay plugged in after the bootcamp |
