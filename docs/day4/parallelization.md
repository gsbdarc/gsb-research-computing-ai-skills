---
layout: default
title: "Parallelization Basics"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 1
permalink: /day4/parallelization/
---

# Parallelization Basics

<div data-room-id="d4-parallelization"></div>

Before you scale a job across the cluster, it helps to picture what "in parallel" actually means, when it works, and why it's usually the single biggest speedup available to you.

---

## When Parallelization Helps

Think back to [the kitchen from Day 3](../../day3/compute-environments/): your machine is a kitchen, and every CPU core is a burner. Some cooking splits across burners perfectly — eight identical dishes, one pan each, no pan needing anything from the others. Fire up more burners and dinner is ready in a fraction of the time. Other cooking doesn't split at all: a risotto is one pot and one sequence — sauté, add stock, stir, reduce — and each step needs the previous one finished. Put four cooks on one risotto and three of them stand around watching. And no matter how many cooks you hire, a roast that needs three hours needs three hours.

Code is the same. Parallelization pays off when the pieces of work are **independent** — each can run without waiting on the results of another. When a job splits cleanly into fully independent tasks with no coordination between them, it's called **embarrassingly parallel** — the easiest, highest-payoff kind of work to spread across workers. Extracting fields from a folder of filings is a textbook example: filing 42 needs nothing from filing 41, so no filing has to wait in line for another.

| Works well in parallel | Does *not* parallelize cleanly |
|---|---|
| Extract fields from 100 separate filings | Step B needs the output of step A |
| Run the same simulation with 50 different seeds | Reading line *n* requires line *n − 1* |

A quick test, in kitchen terms: if you could hand each task to a different cook and never have them talk to each other, it will parallelize. Your extraction job fits perfectly — every filing is its own self-contained task.

{: .note }
> Parallelization doesn't make a single task faster — one filing still takes ~5s, just as the three-hour roast still takes three hours. It makes *many* tasks finish sooner by running them at the same time. If your bottleneck is one slow step, parallelizing won't help; you need a faster step (or a GPU — coming later today).

---

## Cores, Jobs, or Both

Everything you run on the cluster happens inside a **SLURM job** — a request the scheduler fills by reserving cores (and memory, and time) on a node. That leaves you two independent dials for going faster, and you can turn either one or both.

Your Day 3 script turned neither — **one job, one core**, a `for` loop walking the filings in sequence:

```python
for filing in filings:          # 100 filings in the list
    result = extract(filing)     # one core does this, start to finish
    save(result)
# the loop can't start filing 2 until filing 1 is done
```

<svg viewBox="0 0 600 178" role="img" aria-labelledby="jc1-title jc1-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="jc1-title">One job, one core</title>
  <desc id="jc1-desc">A single SLURM job box holds one CPU and eight filings in a row. The CPU moves from filing to filing one at a time.</desc>
  <rect x="6" y="6" width="588" height="136" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="25" font-size="12" font-weight="700" fill="#8a93a3">Job</text>
  <rect x="22"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="52"  y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="92"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="122" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="162" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="192" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="232" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="262" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <rect x="302" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="332" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="372" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="402" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="442" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="472" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="512" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="542" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <g>
    <path d="M45,75 L59,75 L52,86 Z" fill="#0072B2"/>
    <circle cx="52" cy="58" r="18" fill="#0072B2"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="52" y="62" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;70,0;70,0;140,0;140,0;210,0;210,0;280,0;280,0;350,0;350,0;420,0;420,0;490,0;490,0;0,0"
      keyTimes="0;0.07;0.12;0.19;0.24;0.31;0.36;0.43;0.48;0.55;0.60;0.67;0.72;0.79;0.84;0.91;1"
      dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="164" font-size="12.5" fill="#6a7280" text-anchor="middle">One job, one core — the filings are processed one after another.</text>
</svg>

If one filing takes 5 seconds, 100 filings take ~500 seconds — and the whole time the rest of the node sits idle. A Yen node has dozens of cores; this approach uses exactly one of them.

**Parallelize _within_ a job — one job, many cores.** Ask the same job for several cores (`--cpus-per-task`) and split the filings across them in your code (with `multiprocessing`, `joblib`, or GNU `parallel`). The cores share the node's memory, so coordinating them is cheap — but you're capped at the cores on a single machine:

<svg viewBox="0 0 600 178" role="img" aria-labelledby="jc2-title jc2-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="jc2-title">One job, many cores</title>
  <desc id="jc2-desc">A single SLURM job box holds two CPUs and eight filings. The two CPUs work different filings at the same time, sweeping the row in four waves.</desc>
  <rect x="6" y="6" width="588" height="136" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="25" font-size="12" font-weight="700" fill="#8a93a3">Job</text>
  <rect x="22"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="52"  y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="92"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="122" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="162" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="192" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="232" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="262" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <rect x="302" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="332" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="372" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="402" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="442" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="472" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="512" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="542" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <g>
    <path d="M45,75 L59,75 L52,86 Z" fill="#0072B2"/>
    <circle cx="52" cy="58" r="18" fill="#0072B2"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="52" y="61" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;280,0;280,0;420,0;420,0;0,0" keyTimes="0;0.14;0.20;0.34;0.40;0.54;0.60;0.74;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <g>
    <path d="M115,75 L129,75 L122,86 Z" fill="#E69F00"/>
    <circle cx="122" cy="58" r="18" fill="#E69F00"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="122" y="61" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;280,0;280,0;420,0;420,0;0,0" keyTimes="0;0.14;0.20;0.34;0.40;0.54;0.60;0.74;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="164" font-size="12.5" fill="#6a7280" text-anchor="middle">One job, two cores — they split the filings and finish in waves.</text>
</svg>

Two cores clear the eight filings in four waves — ≈ 4 × 5s = 20s of wall-clock, versus ~40s one at a time. Same total work, spread across two workers.

**Parallelize _across_ jobs — many jobs, one core each.** Submit a **job array**: the scheduler launches many near-identical jobs at once, each an independent task on (possibly) a different node, each working its own slice of the filings. This scales past a single machine, and because every task stands alone, a failure costs you only that task. It's the workhorse for the rest of Day 4 — the [next page](../slurm-arrays/) builds one step by step:

<svg viewBox="0 0 600 300" role="img" aria-labelledby="jc3-title jc3-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="jc3-title">Many jobs, one core each</title>
  <desc id="jc3-desc">Two separate SLURM job boxes stacked vertically, each with its own CPU. The first job's CPU processes filings 1 to 4; the second job's CPU processes filings 5 to 8, both at the same time.</desc>
  <rect x="6" y="6" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="24" font-size="12" font-weight="700" fill="#8a93a3">Job 1</text>
  <rect x="40"  y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="190" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="340" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="490" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <g>
    <path d="M68,70 L82,70 L75,80 Z" fill="#0072B2"/>
    <circle cx="75" cy="54" r="16" fill="#0072B2"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="57" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;0,0" keyTimes="0;0.14;0.20;0.34;0.40;0.54;0.60;0.74;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <rect x="6" y="146" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="164" font-size="12" font-weight="700" fill="#8a93a3">Job 2</text>
  <rect x="40"  y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="190" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="340" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="490" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <g>
    <path d="M68,210 L82,210 L75,220 Z" fill="#E69F00"/>
    <circle cx="75" cy="194" r="16" fill="#E69F00"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="197" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;0,0" keyTimes="0;0.14;0.20;0.34;0.40;0.54;0.60;0.74;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="290" font-size="12.5" fill="#6a7280" text-anchor="middle">Two jobs, one core each — each job works its own slice of filings, in parallel.</text>
</svg>

**Do both — many jobs, many cores.** Nothing stops an array task from itself requesting several cores. Reach for this when one dial isn't enough: many jobs to spread across nodes, several cores inside each to chew through a big slice:

<svg viewBox="0 0 600 300" role="img" aria-labelledby="jc4-title jc4-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="jc4-title">Many jobs, many cores</title>
  <desc id="jc4-desc">Two stacked SLURM job boxes, each holding two CPUs and four filings. In each job the two CPUs split the four filings two-and-two, and the two jobs run at the same time.</desc>
  <rect x="6" y="6" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="24" font-size="12" font-weight="700" fill="#8a93a3">Job 1</text>
  <rect x="40"  y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="190" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="340" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="490" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <g>
    <path d="M68,70 L82,70 L75,80 Z" fill="#0072B2"/>
    <circle cx="75" cy="54" r="16" fill="#0072B2"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="57" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;300,0;300,0;0,0" keyTimes="0;0.30;0.42;0.72;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <g>
    <path d="M218,70 L232,70 L225,80 Z" fill="#E69F00"/>
    <circle cx="225" cy="54" r="16" fill="#E69F00"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="225" y="57" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;300,0;300,0;0,0" keyTimes="0;0.30;0.42;0.72;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <rect x="6" y="146" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="164" font-size="12" font-weight="700" fill="#8a93a3">Job 2</text>
  <rect x="40"  y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="190" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="340" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="490" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <g>
    <path d="M68,210 L82,210 L75,220 Z" fill="#009E73"/>
    <circle cx="75" cy="194" r="16" fill="#009E73"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="197" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 3</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;300,0;300,0;0,0" keyTimes="0;0.30;0.42;0.72;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <g>
    <path d="M218,210 L232,210 L225,220 Z" fill="#D55E00"/>
    <circle cx="225" cy="194" r="16" fill="#D55E00"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="225" y="197" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 4</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;300,0;300,0;0,0" keyTimes="0;0.30;0.42;0.72;1" dur="12s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="290" font-size="12.5" fill="#6a7280" text-anchor="middle">Two jobs, two cores each — both dials at once.</text>
</svg>

---

## When One Filing Runs Long

So far every filing took the same 5 seconds. Real filings aren't so uniform — a dense filing with many transactions can take two or three times as long as a simple one. Take the same eight filings, but let **filing 8 run 3× long**. What happens depends on which dial you turned.

**Within one job**, the cores share the batch dynamically — each grabs the next free filing the moment it's done. That works until the work runs out: one core ends up on the long filing while the other finishes everything else and then has nothing left to do. It sits **idle** — and because it belongs to the job, the job keeps holding that reserved core the whole time:

<svg viewBox="0 0 600 178" role="img" aria-labelledby="lf1-title lf1-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="lf1-title">One job, two cores, one long filing: a core ends up idle</title>
  <desc id="lf1-desc">A single SLURM job box holds two CPUs and eight filings; the eighth filing takes three times as long as the others. The two CPUs sweep the row together, but the long final filing goes to one CPU while the other runs out of work and waits idle inside the job.</desc>
  <rect x="6" y="6" width="588" height="136" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="25" font-size="12" font-weight="700" fill="#8a93a3">Job</text>
  <rect x="22"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="52"  y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="92"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="122" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="162" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="192" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="232" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="262" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <rect x="302" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="332" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="372" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="402" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="442" y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="472" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="512" y="86" width="60" height="48" rx="9" fill="#fdf1e0" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="542" y="104" font-size="11" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <text x="542" y="120" font-size="9" font-weight="600" fill="#b26a00" text-anchor="middle">long ×3</text>
  <g>
    <path d="M45,75 L59,75 L52,86 Z" fill="#0072B2"/>
    <circle cx="52" cy="58" r="18" fill="#0072B2"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="52" y="61" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <text x="52" y="34" font-size="10" font-weight="600" fill="#9aa2b1" text-anchor="middle" opacity="0">idle<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.58;0.61;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/></text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;280,0;280,0;420,0;420,0;420,0;0,0" keyTimes="0;0.13;0.15;0.28;0.30;0.43;0.45;0.58;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <g>
    <path d="M115,75 L129,75 L122,86 Z" fill="#E69F00"/>
    <circle cx="122" cy="58" r="18" fill="#E69F00"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="122" y="61" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;280,0;280,0;420,0;420,0;0,0" keyTimes="0;0.13;0.15;0.28;0.30;0.43;0.45;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="164" font-size="12.5" fill="#6a7280" text-anchor="middle">The long filing lands last: CPU 1 runs out of work and idles while the job still holds both cores.</text>
</svg>

The total wall-clock time is set by the straggler, not the average — this is called **load imbalance**. Worse, the early finisher's core isn't returned to the cluster: it stays reserved, doing nothing, until the whole job ends.

**Across two jobs**, the same eight filings split into two independent chunks. The job that drew only short filings simply *finishes* — and releases its core back to the cluster for the next user (or your next task). Nothing sits idle; the long filing just keeps its own job running a little longer:

<svg viewBox="0 0 600 300" role="img" aria-labelledby="lf2-title lf2-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="lf2-title">Two jobs, one core each, one long filing: the finished job releases its core</title>
  <desc id="lf2-desc">Two stacked SLURM job boxes, each with one CPU and four filings; the eighth filing, in the second job, takes three times as long. The first job's CPU finishes its four short filings, the job completes, and its core is released. The second job's CPU keeps working the long filing. No core sits idle.</desc>
  <rect x="6" y="6" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="24" font-size="12" font-weight="700" fill="#8a93a3">Job 1</text>
  <rect x="40"  y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="190" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="340" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="490" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <text x="240" y="58" font-size="11" font-weight="600" fill="#009E73" text-anchor="middle" opacity="0">job complete — core released ✓<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.60;0.64;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/></text>
  <g>
    <path d="M68,70 L82,70 L75,80 Z" fill="#0072B2"/>
    <circle cx="75" cy="54" r="16" fill="#0072B2"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="57" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <animate attributeName="opacity" values="1;1;0.15;0.15;1" keyTimes="0;0.58;0.63;0.9;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;450,0;0,0" keyTimes="0;0.13;0.15;0.28;0.30;0.43;0.45;0.58;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <rect x="6" y="146" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="164" font-size="12" font-weight="700" fill="#8a93a3">Job 2</text>
  <rect x="40"  y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="190" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <rect x="340" y="220" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="375" y="246" font-size="12" fill="#2c3e50" text-anchor="middle">filing 7</text>
  <rect x="490" y="220" width="70" height="44" rx="9" fill="#fdf1e0" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="525" y="240" font-size="12" fill="#2c3e50" text-anchor="middle">filing 8</text>
  <text x="525" y="256" font-size="9" font-weight="600" fill="#b26a00" text-anchor="middle">long ×3</text>
  <g>
    <path d="M68,210 L82,210 L75,220 Z" fill="#E69F00"/>
    <circle cx="75" cy="194" r="16" fill="#E69F00"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="197" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;0,0" keyTimes="0;0.13;0.15;0.28;0.30;0.43;0.45;0.84;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="290" font-size="12.5" fill="#6a7280" text-anchor="middle">Job 1 finishes and releases its core; job 2 keeps working the long filing. No reserved core sits idle.</text>
</svg>

The long filing takes the same wall-clock time either way — no arrangement makes a single slow task faster. The difference is waste: within one job, early finishers idle on reserved cores; across jobs, a finished task hands its core straight back.

{: .tip }
> **If you can order the work, run the longest tasks first.** Load imbalance bites hardest when a long task starts *late* — the other cores finish and sit idle waiting for it. Start the longest tasks first and the short ones backfill around them, so the cores finish close together. This is the "longest processing time first" rule, and it's provably within a third of the best-possible finish time. It does need a rough sense of which tasks are long, but a cheap proxy often works — e.g. sort the filings by file size (bigger ≈ slower) and process the biggest first.

---

## More Filings Than Cores (and Vice Versa)

The illustrations above show a tidy few-filings-per-worker picture. In practice the ratios vary, and both directions come up constantly.

**More filings than cores — the usual case.** Say you have 100 filings but only 8 cores. The cores work in *waves*: the first 8 filings run at once, and the moment a worker finishes it picks up the next filing in line, until all 100 are done. The total time is roughly the number of waves times the per-filing time — about ⌈100 ÷ 8⌉ = 13 waves × 5s ≈ 65s, versus ~500s in serial. You don't manage the waves yourself: within a job your code hands out the next filing; across array jobs, the scheduler does.

**More cores than filings.** Say you have 5 filings but 32 cores available. Only 5 cores can do anything — a single filing can't be split across cores — so the other 27 sit idle. Cores beyond the number of independent tasks buy you nothing, and requesting more than you'll use can mean a longer wait in the queue for resources you never touch.

{: .note }
> **Rule of thumb:** match cores to tasks. Aim for roughly one core per independent task, capped by what's available. Below that, you process in waves and still finish far ahead of serial; above that, the extra cores just sit idle.

---

<label class="quest-check"><input type="checkbox" data-room="d4-parallelization" data-key="main"> I can explain what parallelization is and when it helps</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-parallelization.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- You can explain the difference between running tasks sequentially on one core and in parallel across many
- You can tell whether a workload is **independent** enough to parallelize
- You can distinguish parallelizing **within a job** (more cores) from **across jobs** (a job array) — and know that a finished job releases its core, while an idle core inside a running job stays reserved
- You understand that parallelization speeds up *many* tasks, not a single slow one
