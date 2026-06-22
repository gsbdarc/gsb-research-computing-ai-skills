---
layout: default
title: "The Kitchen"
parent: "Day 3 — The SLURM Mines"
nav_order: 2
permalink: /day3/kitchen/
---

# The Kitchen

<div data-room-id="d3-kitchen"></div>

*The dungeon's communal kitchen. Right now, at this very moment, seventeen other researchers are using it. Some are running long batch jobs — the equivalent of a slow roast that's been in the oven for six hours. Others are queued, waiting for a burner to free up. Watch the kitchen before you cook. Then you'll understand why SLURM exists.*

---

## Main Quest

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

## Skills Learned

- See live resource contention on the Yens before writing a single SLURM script
- Understand the head chef / kitchen analogy for batch scheduling
- Know the difference between a login node (for submitting work) and a compute node (for running it)
- Understand why running computation on a login node is bad cluster citizenship
