---
layout: floor
title: "Day 3 — The Hearth"
nav_order: 3
has_children: true
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
| [The Kitchen](kitchen/) | 🖊️ Demo + discussion | The shared kitchen analogy — CPU, RAM, and storage on your laptop vs. the Yens vs. the cloud |
| [The Back Kitchen](back-kitchen/) | 🖊️💻 Demo + discussion | Why SLURM exists; interactive Yens vs dedicated compute nodes |
| [The Storage Pantry](storage-pantry/) | 💻 Hands-on | Dig into real Yens cluster data; find patterns in CPU, memory, and job history |
| [The Scales](scales/) | 💻 Hands-on | Profile a mystery script with time, userload, and htop — stop guessing at resource requests |
| [The Ticket Rail](ticket-rail/) | 💻 Hands-on | Forge a SLURM script from a blank page and submit it yourself |
| [Failed Order](failed-order/) | 💻 Hands-on | Stalk, debug, and autopsy your batch jobs like a pro |
| [The Recipe Book](recipe-book/) | 💻 Hands-on | Capture your pipeline in a README while the details are still hot |
| [Boss Gate 3](boss-gate-3/) | 🔑 Capstone | Submit a properly profiled SLURM job — documented and delivered |
