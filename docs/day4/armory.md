---
layout: default
title: "The Armory"
parent: "Day 4 — The GPU Fortress"
nav_order: 2
permalink: /day4/armory/
---

# The Armory

<div data-room-id="d4-armory"></div>

*Torchlight catches the glint of silicon and copper as you step into the GPU Fortress's most sacred chamber. Three rows of weapons line the walls — each tier heavier, faster, and hungrier than the last. The A30s hum with quiet readiness, battle-tested workhorses for daily inference. The A40s pulse with more menace, built for models that would crush lesser hardware. And at the far end, draped in shadow, the H200 waits — 141 gigabytes of video RAM, enough to swallow a 70-billion-parameter giant whole. Every adventurer who has tried to force a massive model onto the wrong GPU has paid for that mistake in wasted hours and failed jobs. Study the arsenal. Choose deliberately.*

---

## 🗡️ Main Quest

The GPU landscape is your map — without it, you're swinging blind. Take a moment at the whiteboard before you draw a weapon.

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

## 🧠 Skills Learned

- You can now identify the three GPU tiers on the Yens (A30 / A40 / H200) and match the right weapon to the right job
- You understand VRAM as the true binding constraint for model size — not CPU RAM, not disk, VRAM
- You can request a GPU in any SLURM script with `--gres=gpu:1` and pin to a specific node when you need the big iron
- You can judge when a GPU job is worth the queue wait — and when a CPU job will get you there faster
