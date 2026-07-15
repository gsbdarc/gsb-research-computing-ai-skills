---
title: "Day 4 — Proposed Agenda (internal)"
nav_exclude: true
search_exclude: true
---

# Proposed Day 4 Sequencing

**Internal planning note — not a course page.** Proposed lecture flow for Day 4,
with pointers to the room file that covers each part. Excluded from site nav and
search via front matter. See [`TODO.md`](TODO.md) for the content gaps this
sequencing addresses.

---

1. **Parallelization (conceptual introduction)**
    - Draw a diagram on the whiteboard: one input SEC filing, one core moving from filing to filing
        - Compare with having multiple cores (ideally, have more filings than cores)
    - Potentially: demo this in practice (compare runtime of a SLURM script that repeatedly invokes the single-file script versus running an array)

2. **How to operationalize parallelization**
    - The simplest way on the Yens: SLURM array jobs
        - And combining outputs
    - Avoiding recomputation when jobs fail
    - **Exercise:** Running through all this, as described in [`array-cavern.md`](array-cavern.md)

3. **Running LLM jobs on Stanford infrastructure: why?**
    - So far, we've been using APIs → query and data gets sent to a third-party server, response gets sent back to us
    - Why we might want to instead use local LLMs / LLMs running on Stanford infrastructure:
        - Privacy / data requirements
        - Cost
        - Reproducibility
        - Not constrained by API rate limits
    - Local LLM vs. Stanford AI Playground vs. third-party API: when and why? (see [`engine-room.md`](engine-room.md))

4. **Using the GPU partition**
    - Modern LLMs rely on GPUs (graphics processing units)
        - Why? LLM outputs are essentially chained matrix multiplication → it turns out that these numerical operations can be performed particularly quickly on GPUs
    - The Yens have GPUs that facilitate running LLM jobs
    - Understanding different GPU types at a high level
        - And how they map to different Yen nodes (see [`armory.md`](armory.md))
    - **Exercise:** Submitting a simple job to the GPU partition (see [`h200-chamber.md`](h200-chamber.md))
    - **Exercise:** Running an LLM on the Yens (see [`summoning-circle.md`](summoning-circle.md))
    - Choosing between LLMs on the Yens in practice (see [`engine-room.md`](engine-room.md))

5. **LLM failure modes**
    - Rules of thumb for validating LLM outputs (e.g., comparing between models; see [`engine-room.md`](engine-room.md))
        - Make it possible to compare a subset of filings
    - TODO: Re-evaluate the list of failure modes and how to defend against them (see [`trap-garden.md`](trap-garden.md))

6. **Putting it all together** — **Exercise (capstone)** (see [`boss-gate-4.md`](boss-gate-4.md))
    - Running an array job and combining the outputs
        - Using two different LLMs
    - Comparing the outputs
    - Writing a README

7. **Staying in touch** (see [`research-guild.md`](research-guild.md))
