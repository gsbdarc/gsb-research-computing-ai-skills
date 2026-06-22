---
layout: default
title: "The Armory"
parent: "Day 4 — The GPU Fortress"
nav_order: 2
permalink: /day4/armory/
---

# The Armory

<div data-room-id="d4-armory"></div>

*The weapons vault of the GPU Fortress. Three rows of hardware — each row faster, larger, and more expensive than the last. A30s for the everyday work. A40s for more demanding inference. H200s for the frontier. Choosing the wrong weapon wastes your time and the cluster's resources. Choose deliberately.*

---

## Main Quest

{: .important }
> **Quest:** Learn the GPU landscape on the Yens — what's available, what each GPU is for, and how to request one.

This is a concept block. Follow the whiteboard.

**GPUs on the Yens:**

| GPU | Node | VRAM | Good for |
|-----|------|------|----------|
| A30 | yen-gpu1, yen-gpu2 | 24 GB | Small model inference, embedding, fine-tuning small models |
| A40 | yen-gpu3 | 48 GB | Medium model inference, training, larger batches |
| H200 | yen-gpu4 | 141 GB | Large model inference, vLLM serving, frontier models |

**Key concepts:**

- **VRAM (video RAM):** the GPU's working memory. The model weights must fit here. A 70B parameter model in float16 needs ~140 GB — only the H200 has enough.
- **Compute vs. memory bound:** some tasks are limited by calculation speed (compute bound); others by how fast the GPU can move data to its cores (memory bound). H200's HBM3e memory bandwidth is the reason it's fast for LLM inference, not just its raw FLOPS.
- **Requesting a GPU:** `--gres=gpu:1` in your `#SBATCH` directives; add `--nodelist=yen-gpu4` to target the H200 specifically.

<label class="quest-check"><input type="checkbox" data-room="d4-armory" data-key="main"> Armory briefing complete — I know what GPUs are available and when to use each</label>

---

## Skills Learned

- Know the three GPU tiers on the Yens (A30 / A40 / H200) and what each is suited for
- Understand VRAM as the binding constraint for model size — not CPU RAM
- Know how to request a GPU in a SLURM script with `--gres=gpu:1`
- Understand when a GPU job is worth the queue wait vs. CPU-based processing
