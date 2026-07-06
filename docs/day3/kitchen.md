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

The best way to understand why the cluster needs a scheduler is to try to cook without one. You're about to run three rounds of a grilled cheese kitchen — with real volunteers, real roles, and a real timer.

{: .important }
> **Quest:** Run three rounds of the grilled cheese kitchen — discover through cooking what parallelism, resource limits, and scheduling feel like.

**The Recipe: Grilled Cheese**

> 1. Collect **one** slice of cheese from the **fridge** (= RAM)
> 2. Collect **two** slices of bread from the **pantry** (= storage)
> 3. Unwrap the cheese and place it between the bread slices
> 4. "Cook" for **30 seconds** — your Chef de Temps calls time
> 5. Plate and serve

Two roles in every round:

| Role | Job |
|------|-----|
| **Chef de Cuisine** | Follow the recipe — make sandwiches |
| **Chef de Temps** | Keep time — alert the Chef de Cuisine when 30 seconds has passed |

---

### Round 1 — Your Laptop (1 burner)

**Volunteers needed:** 1 Chef de Cuisine · 1 Chef de Temps

*Timer: 2 minutes. Go!*

After the round, discuss:
- How many sandwiches did you make?
- What was the bottleneck? Could you do two at once?
- What if you had 100 orders?

{: .note }
> **This is your laptop.** One CPU core = one burner. Your script processes tasks one at a time — sequential, single-threaded. Fine for 1 filing. Painful for 100.

---

### Round 2 — A Bigger Kitchen (3 burners)

**Volunteers needed:** 1 Chef de Cuisine · 3 Chef de Temps *(one timer per burner)*

Same recipe. Three stations are open simultaneously.

*Timer: 2 minutes. Let's cook!*

After the round, discuss:
- How many sandwiches this time?
- Did throughput scale with the number of burners? Why?
- Did the fridge (RAM) or pantry (storage) become a bottleneck?

{: .note }
> **This is the Yens.** More CPU cores = more burners. Independent tasks — like extracting separate filings — can all start at the same time. Wall time stays roughly constant while throughput multiplies.

---

### Round 3 — More Chefs! (5 burners, 3 timers)

**Volunteers needed:** 5 Chef de Cuisine · 3 Chef de Temps — *"Let Them Cook!"*

Five workers, but only three timers. What happens?

*Timer: 2 minutes. Go!*

After the round, discuss:
- Did 5 chefs produce 5× more sandwiches than Round 1?
- What happened to the 2 chefs who had no Chef de Temps?
- What does this tell you about requesting more resources than are available?

{: .note }
> **This is resource contention.** The scheduler assigns what exists. If you request 32 CPUs but the node only has 16 free, your job waits in the queue. The right request — not the biggest request — gets you cooking fastest.

---

## The Kitchen Analogy

Everything that just happened maps directly to SLURM:

| Kitchen | Yens / SLURM |
|---------|--------------|
| Head chef | SLURM scheduler |
| Station (stove) | Compute node |
| Burner | CPU core |
| Fridge | RAM |
| Pantry / warehouse | Shared storage (`/scratch`) |
| Order ticket | Job script (`sbatch`) |
| Tickets on the rail | Job queue (`squeue`) |
| Recipe | Your Python/R/shell script |
| Time limit (Chef de Temps) | `#SBATCH --time` |
| Resource request | `#SBATCH --mem`, `--cpus-per-task` |

You don't walk into the kitchen and start cooking. You hand your recipe to the head chef (`sbatch`), specify what burners, fridge space, and time you need (`#SBATCH` directives), and come back when the meal is done.

---

## See the Real Kitchen

Now look at the actual Yens:

**Your own resource usage on this node:**
```bash
userload          # shows YOUR CPU and memory usage on this interactive Yen node
```

**All processes on this node** (including other users sharing the same machine):
```bash
htop              # press q to quit — spot other users' processes competing for the same cores
```

**All jobs across the whole cluster** (the full ticket rail):
```bash
squeue            # every queued and running SLURM job across the Yens
squeue -u $USER   # just yours
```

{: .note }
> `userload` shows only your usage on the current node — it's not a cluster-wide view. `htop` lets you see other researchers' processes on the same shared machine. `squeue` gives you the full picture across all nodes.

---

## Why SLURM?

The interactive Yens are shared — everyone who SSHs in lands on the same machine. Running a long, CPU-heavy job directly here is like firing up all the burners in a shared kitchen and refusing to leave.

```bash
# Don't do this for long/intensive work:
# python my_big_script.py   ← blocks the shared node for everyone

# Do this instead — sbatch gives you a dedicated compute node:
# sbatch jobs/extract.sh    ← coming up in The Foreman's Desk
```

<label class="quest-check"><input type="checkbox" data-room="d3-kitchen" data-key="main"> Kitchen demo complete — I understand why SLURM exists</label>

---

## 🧠 Skills Learned

- You've felt the difference between serial (1 burner), parallel (3 burners), and resource-constrained (5 chefs, 3 timers) execution — through doing, not just watching
- You can map every SLURM concept to a kitchen equivalent: scheduler, queue, compute node, directives
- You know `userload` shows your own usage on the current node; `htop` shows all processes on the node; `squeue` shows all cluster jobs
- You understand why running heavy jobs on the shared interactive Yens is inconsiderate — and why `sbatch` gives you the isolation you need
