---
layout: default
title: "Documenting Your Pipeline"
parent: "Day 3 — Cluster Computing"
nav_order: 9
permalink: /day3/documenting-pipeline/
---

# Documenting Your Pipeline

<div data-room-id="d3-documenting-pipeline"></div>

<svg viewBox="0 0 720 164" role="img" aria-labelledby="docmap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="docmap-title">Day 3 map — you are on the document step.</title>
  <defs>
    <marker id="docmap-gray" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">profile</text>
  <text x="210" y="28" text-anchor="middle" font-size="17" fill="#8a94a6">submit to</text><text x="210" y="48" text-anchor="middle" font-size="17" fill="#8a94a6">Slurm</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" fill="#8a94a6">read logs</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">document</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="600" fill="#8a94a6">scale (Day 4)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="622" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#docmap-gray)"/>
  <path d="M350,101 L350,124 Q350,130 344,130 L216,130 Q210,130 210,124 L210,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#docmap-gray)"/>
  <text x="280" y="150" text-anchor="middle" font-size="15" fill="#8a94a6">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">3</text>
  <circle cx="490" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#9aa4b0" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8a94a6">5</text>
</svg>

---

## Main quest — Write a README

Write your README while the code is still fresh — before you close the terminal.

{: .important }
> **Task:** Write a `README.md` for your Day 3 pipeline.

{: .note }
> This is the same `README.md` you've been building since Day 1 — keep adding to it, don't start a new file.

Add a pipeline writeup to your `README.md`. Here's a skeleton — fill in each section yourself:

```markdown
# Day 3 Pipeline — SEC Form 3 Extraction

**Author:**
**Date:**

## What this does

<!-- one or two sentences: what does this pipeline extract, from what, using what? -->

## How to run

### Prerequisites
<!-- what someone needs before running: cluster access, API key, venv, ... -->

### Steps
<!-- the commands to submit the job, monitor it, and check the output -->

## Outputs

<!-- which files land where, and what's in them -->

## Data

<!-- the input data and where it comes from -->
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

<label class="quest-check"><input type="checkbox" data-room="d3-documenting-pipeline" data-key="main"> README written and covers what the script does, how to run it, and where output lands</label>

---

## Side quests

{: .note }
> Finished early? Try this one.

**Side quest — Have Claude Stress-Test Your README**

Ask Claude Code to read your README as if it were a labmate seeing this pipeline for the first time, and to flag anything that would stop them from rerunning it without asking you a question. Fix at least one thing it flags.

<label class="quest-check"><input type="checkbox" data-room="d3-documenting-pipeline" data-key="side1"> I had Claude critique my README as a first-time reader and fixed at least one issue it flagged</label>

---

{: .note }
> **Go further — let Claude keep the record.** You don't have to write all of this by hand. You can have Claude draft the README straight from the code and then **review** it, or go a step further and keep a **research log** — a running record of what you ran, when, and where the results landed — that Claude updates each time you launch a job (see the `claude -p` batch-mode idea in [Writing a Slurm Job with Claude](../slurm-with-claude/#side-quests)). Documentation only earns its keep if it helps *you* later, so keep whatever form is most useful for your research and drop the rest.

