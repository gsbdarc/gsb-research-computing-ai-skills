---
layout: default
title: "The Kitchen"
parent: "Day 3 — The SLURM Mines"
nav_order: 2
permalink: /day3/kitchen/
---

# The Kitchen

<div data-room-id="d3-kitchen"></div>

*Steam hangs in the air. Seventeen other researchers are already in here — one has a slow roast that's been in the oven for six hours, two more are fighting over the last open burner, and somewhere in the back a job has been queued so long it's practically fossilized. This is the Yens cluster at peak hours, rendered in cast iron and fire. Watch it breathe before you even think about striking a match. Once you see the chaos, SLURM stops being bureaucracy and starts being salvation.*

---

## 🗡️ Main Quest

Before you touch a single `sbatch` flag, you need to see the beast with your own eyes.

{: .important }
> **Quest:** Watch the Yens live — see resource contention in real time, then understand the kitchen analogy for SLURM.

This is a 20-minute live demo. Follow along with what's on the projector.

**Step 1 — See who's using the Yens right now:**

```bash
userload          # shows current CPU/memory usage per user across all login nodes
htop              # interactive process viewer — press q to quit
```

Look at `userload`. Every row is a researcher. Some are using thousands of CPU-hours. Now imagine you try to run a 32-core job from the command line — you'd be competing with all of them for the same shared hardware.

**Step 2 — The kitchen analogy:**

| Kitchen | Yens cluster |
|---------|-------------|
| Head chef | SLURM scheduler |
| Line cooks | Compute nodes |
| Orders | Job scripts (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Pantry | Shared storage (`/scratch`) |
| Recipe | Your Python/R/shell script |
| Reservation (dietary restriction) | `#SBATCH` resource request |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef (`sbatch`), specify what ingredients and burners you need (`#SBATCH` directives), and come back when the meal is done.

**Step 3 — Why login nodes are not for cooking:**

```bash
# Never run this on a login node — you're sharing it with everyone
# python my_big_script.py   ← wrong
# Instead, use sbatch (we'll get there in The Foreman's Desk)
```

Login nodes are for editing, submitting, and checking jobs — not running them.

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> Kitchen demo complete — I understand why SLURM exists</label>

---

## 🧠 Skills Learned

- You can read live resource contention on the Yens and know exactly who is eating the cluster's lunch
- You can map every piece of SLURM vocabulary to a kitchen equivalent — scheduler, queue, compute node, and all
- You can instantly distinguish a login node (the pass-through window) from a compute node (the actual stove) and use each correctly
- You know that running heavy computation on a login node is the cluster equivalent of blocking the fire exit — and you will never do it
