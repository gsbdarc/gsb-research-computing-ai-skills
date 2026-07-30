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

Today you'll move from running your code **interactively** — one piece at a time, watching it go — to handing bigger jobs off to the **scheduled** Yens and letting them run on their own. You'll pick up the ideas and habits for that step by step: how to size up what a job needs before you run it, how to send it off and check how it went, how to fix it when something breaks, and how to write down what you did so you (or a labmate) can run it again. By the end you'll have run the whole thing on a real job.

Here's what we'll do today, start to finish:

<svg viewBox="0 0 720 164" role="img" aria-labelledby="d3loop-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="d3loop-title">The Day 3 research pipeline: profile your script to estimate resources, submit the batch job to Slurm, read the logs — debugging and resubmitting if it fails — then document, with scaling up on Day 4.</title>
  <defs>
    <marker id="d3loop-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" fill="#8a94a6">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" fill="#8a94a6">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#d3loop-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#d3loop-gray)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" fill="#8a94a6">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

---

## Day 2 Recap

- Built a virtual environment on the Yens and installed dependencies from `requirements.txt`
- Wrote `scripts/extract_form_3_one_file.py` — calls the Stanford AI API to extract structured fields from one SEC Form 3 filing
- Used Pydantic to validate and structure the LLM output

Any questions about Day 1–2 we can discuss before we move on.

---

## Sections

Work through the sections in order — later ones build on earlier ones, and the Day 3 Capstone draws on everything you've learned.

| Section | Format | What you master |
|------|--------|-----------------|
| [Compute Environments](compute-environments/) | 🥪💬 Demo + discussion | **Compute environments** — so you pick the right one (laptop, Yens, or cloud) instead of wasting your advisor's compute budget (or your afternoon) |
| [Profiling Resource Usage](profiling/) | 💻 Hands-on | **Profiling** — so your own jobs request the resources they actually need instead of guessing and stalling in the queue |
| [Exploring Cluster Usage Data](cluster-usage-data/) | 💻🤖 Hands-on (Claude-assisted) | **Data exploration** — the same messy-real-data instinct you'll need on your own datasets |
| [The Slurm Scheduler](slurm-scheduler/) | 💬💻 Discussion + hands-on | **Interactive vs. scheduled Yen nodes** — so your research jobs get dedicated resources instead of competing with everyone else on a shared login node |
| [Writing & Submitting a Slurm Job](slurm-job/) | 💻 Hands-on | **Batch jobs** — the actual mechanism you'll use to run your own research code on the cluster (plus debugging broken jobs) |
| [Writing a Slurm Job with Claude](slurm-with-claude/) | 💻🤖 Hands-on (Claude-assisted) | **Reusable skills** — distill a **global** Yen skill from the job you just ran, then make a figure and distill a **project** plotting skill from it, invoking each — project vs. global scope |
| [Documenting Your Pipeline](documenting-pipeline/) | 💻🤖 Hands-on (Claude-assisted) | **Reproducibility** — what makes collaborators, and your future self, trust and rerun your results |
| [Day 3 Capstone](capstone/) | 🔑 Capstone | **Profiled submission** — the exact loop you'll repeat for every real research pipeline from here on |
