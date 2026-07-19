---
layout: default
title: "Choosing a GPU"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 3
permalink: /day4/armory/
---

# Choosing a GPU

<div data-room-id="d4-armory"></div>

This is a concept section — no hands-on. The goal is to learn the GPU landscape on the Yens: what's available, what each GPU is for, and how to request one.

---

## GPUs on the Yens

| GPU | Node | VRAM | Good for |
|-----|------|------|----------|
| A30 | yen-gpu1, yen-gpu2 | 24 GB | Small model inference, embedding, fine-tuning small models |
| A40 | yen-gpu3 | 48 GB | Medium model inference, training, larger batches |
| H200 | yen-gpu4 | 141 GB | Large model inference, vLLM serving, frontier models |

## Key Concepts

- **VRAM (video RAM):** the GPU's working memory. The model weights must fit here. A 70B parameter model in float16 needs ~140 GB — only the H200 has enough.
- **Compute vs. memory bound:** some tasks are limited by calculation speed (compute bound); others by how fast the GPU can move data to its cores (memory bound). H200's HBM3e memory bandwidth is the reason it's fast for LLM inference, not just its raw FLOPS.
- **Requesting a GPU:** `--gres=gpu:1` in your `#SBATCH` directives; add `--nodelist=yen-gpu4` to target the H200 specifically.

<label class="quest-check"><input type="checkbox" data-room="d4-armory" data-key="main"> I know what GPUs are available and when to use each</label>

---

## What You Learned

- You can identify the three GPU tiers on the Yens (A30 / A40 / H200) and match the right GPU to the job
- You understand VRAM — not CPU RAM or disk — as the binding constraint on model size
- You can request a GPU in any SLURM script with `--gres=gpu:1` and pin to a specific node when you need a particular GPU
- You can judge when a GPU job is worth the queue wait — and when a CPU job will get you there faster
