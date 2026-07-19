---
layout: default
title: "Parallelization Basics"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 1
permalink: /day4/parallelization/
---

# Parallelization Basics

<div data-room-id="d4-parallelization"></div>

This is a concept section — no hands-on. Before you scale a job across the cluster, it helps to picture what "in parallel" actually means, when it works, and why it's usually the single biggest speedup available to you.

---

## One Core at a Time

On Day 3 you wrote a script that extracts structured fields from a single SEC filing — pulling out the reporting person, transaction dates, share counts, and so on. It handles one filing from start to finish, then moves on to the next. A single **core** — one worker inside the machine — does all the work, one filing after another.

The canonical way to write this is a **`for` loop** — walk the list of filings and process each in turn:

```python
for filing in filings:          # 100 filings in the list
    result = extract(filing)     # one core does this, start to finish
    save(result)
# the loop can't start filing 2 until filing 1 is done
```

That loop is exactly what the diagram below shows: one worker stepping through the boxes in order.

<svg viewBox="0 0 562 162" role="img" aria-labelledby="serial-title serial-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:560px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="serial-title">Serial processing: one core moves from filing to filing</title>
  <desc id="serial-desc">Six boxes represent filings in a row. A single circle labelled CPU moves along the row, stopping on each filing one at a time, so the total time is the sum of all the filings.</desc>
  <!-- dashed track the core travels along -->
  <line x1="54" y1="34" x2="509" y2="34" stroke="#cdd4e6" stroke-width="2" stroke-dasharray="4 5"/>
  <!-- six filing boxes -->
  <rect x="16"  y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="54"  y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="107" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="145" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="198" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="236" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="289" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="327" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <rect x="380" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="418" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="471" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="509" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <!-- the single core, moving from box to box -->
  <g>
    <path d="M46,54 L62,54 L54,64 Z" fill="#0072B2"/>
    <circle cx="54" cy="34" r="20" fill="#0072B2">
      <animate attributeName="r" values="20;22;20" dur="1s" repeatCount="indefinite"/>
    </circle>
    <text x="54" y="38" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;91,0;91,0;182,0;182,0;273,0;273,0;364,0;364,0;455,0;455,0;0,0"
      keyTimes="0;0.09;0.14;0.23;0.28;0.37;0.42;0.51;0.56;0.65;0.70;0.90;1"
      dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="281" y="147" font-size="12.5" fill="#6a7280" text-anchor="middle">One core visits each filing in turn — total time adds up (≈ 6 × 5s = 30s)</text>
</svg>

If one filing takes 5 seconds, 100 filings take ~500 seconds — and the whole time, the rest of the machine sits idle. A Yen node has dozens of cores; this approach uses exactly one of them.

---

## Many Cores at Once

Here's the key property of *this* task: extracting fields from one filing doesn't require anything from any other filing. The fields pulled from filing 42 don't depend on filing 41, so there's no reason to make them wait in line. (That independence comes from the task, not the filings themselves — a different task *could* interrelate them, say tracking how one insider's holdings build up across their filings over time. Field extraction simply doesn't.)

Because the work is independent, you can hand the filings out across several cores and let those cores run at the same time, each moving on to the next unprocessed filing the moment it finishes one.

<svg viewBox="0 0 562 184" role="img" aria-labelledby="parallel-title parallel-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:560px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="parallel-title">Parallel processing with fewer cores than filings</title>
  <desc id="parallel-desc">Six boxes represent filings in a row. Two coloured circles labelled CPU each process a filing at the same time, then move on to the next unprocessed filing, sweeping across all six filings in three waves.</desc>
  <!-- six filing boxes -->
  <rect x="16"  y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="54"  y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="107" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="145" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="198" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="236" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <rect x="289" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="327" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <rect x="380" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="418" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 5</text>
  <rect x="471" y="64" width="76" height="56" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="509" y="97" font-size="13" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <!-- core 1 (blue): filing 1 → 3 → 5 -->
  <g>
    <path d="M46,54 L62,54 L54,64 Z" fill="#0072B2"/>
    <circle cx="54" cy="34" r="20" fill="#0072B2"><animate attributeName="r" values="20;22;20" dur="1s" repeatCount="indefinite"/></circle>
    <text x="54" y="38" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;182,0;182,0;364,0;364,0;0,0"
      keyTimes="0;0.22;0.30;0.52;0.60;0.82;1"
      dur="6s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <!-- core 2 (orange): filing 2 → 4 → 6 -->
  <g>
    <path d="M137,54 L153,54 L145,64 Z" fill="#E69F00"/>
    <circle cx="145" cy="34" r="20" fill="#E69F00"><animate attributeName="r" values="20;22;20" dur="1s" repeatCount="indefinite"/></circle>
    <text x="145" y="38" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;182,0;182,0;364,0;364,0;0,0"
      keyTimes="0;0.22;0.30;0.52;0.60;0.82;1"
      dur="6s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="281" y="152" font-size="12.5" fill="#6a7280" text-anchor="middle"><tspan x="281" dy="0">Two cores, six filings: each core finishes one, then moves</tspan><tspan x="281" dy="16">to the next free filing — three waves (≈ 3 × 5s = 15s)</tspan></text>
</svg>

Even with just a handful of cores, the batch finishes in a fraction of the serial time: here two cores clear six filings in three waves — about 3 × 5s ≈ **15s of wall-clock time**, versus ~30s running them one at a time. That is parallelization: the same total work, spread across many workers instead of stacked on one.

So far every filing took the same 5 seconds. Real filings aren't so uniform — a dense filing with many transactions can take two or three times as long as a simple one. When task durations are uneven, the cores stop finishing in lockstep:

<svg viewBox="0 0 562 176" role="img" aria-labelledby="imbalance-title imbalance-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:560px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="imbalance-title">Uneven filing durations cause load imbalance</title>
  <desc id="imbalance-desc">A timeline with two rows, one per core, over 30 seconds. Short filings take 5 seconds and long filings take 15 seconds. One core is handed a run of work that finishes at 30 seconds while the other finishes at 20 seconds and then sits idle, so the total time is set by the busiest core.</desc>
  <!-- row labels -->
  <circle cx="16" cy="47" r="6" fill="#0072B2"/>
  <text x="28" y="51" font-size="12" fill="#2c3e50">core 1</text>
  <circle cx="16" cy="91" r="6" fill="#E69F00"/>
  <text x="28" y="95" font-size="12" fill="#2c3e50">core 2</text>
  <!-- core 1 timeline: f1 (5s), f3 (5s), f4 (5s), f5 (15s, long) -->
  <rect x="90"  y="30" width="75"  height="34" fill="#0072B2" stroke="#ffffff" stroke-width="2"/>
  <text x="128" y="51" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f1 · 5s</text>
  <rect x="165" y="30" width="75"  height="34" fill="#0072B2" stroke="#ffffff" stroke-width="2"/>
  <text x="203" y="51" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f3 · 5s</text>
  <rect x="240" y="30" width="75"  height="34" fill="#0072B2" stroke="#ffffff" stroke-width="2"/>
  <text x="278" y="51" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f4 · 5s</text>
  <rect x="315" y="30" width="225" height="34" fill="#0072B2" stroke="#ffffff" stroke-width="2"/>
  <text x="428" y="51" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f5 · 15s (long)</text>
  <!-- core 2 timeline: f2 (15s, long), f6 (5s), then idle -->
  <rect x="90"  y="74" width="225" height="34" fill="#E69F00" stroke="#ffffff" stroke-width="2"/>
  <text x="203" y="95" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f2 · 15s (long)</text>
  <rect x="315" y="74" width="75"  height="34" fill="#E69F00" stroke="#ffffff" stroke-width="2"/>
  <text x="353" y="95" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">f6 · 5s</text>
  <rect x="390" y="74" width="150" height="34" fill="#f3f4f7" stroke="#cdd4e6" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="465" y="95" font-size="11" font-weight="600" fill="#9aa2b1" text-anchor="middle">idle</text>
  <!-- time axis -->
  <line x1="90" y1="118" x2="548" y2="118" stroke="#b8bfcc" stroke-width="1.5"/>
  <path d="M548,114 L556,118 L548,122 Z" fill="#b8bfcc"/>
  <line x1="90"  y1="114" x2="90"  y2="118" stroke="#b8bfcc" stroke-width="1.5"/>
  <line x1="240" y1="114" x2="240" y2="118" stroke="#b8bfcc" stroke-width="1.5"/>
  <line x1="390" y1="114" x2="390" y2="118" stroke="#b8bfcc" stroke-width="1.5"/>
  <line x1="540" y1="114" x2="540" y2="118" stroke="#b8bfcc" stroke-width="1.5"/>
  <text x="90"  y="131" font-size="10.5" fill="#6a7280" text-anchor="middle">0s</text>
  <text x="240" y="131" font-size="10.5" fill="#6a7280" text-anchor="middle">10s</text>
  <text x="390" y="131" font-size="10.5" fill="#6a7280" text-anchor="middle">20s</text>
  <text x="540" y="131" font-size="10.5" fill="#6a7280" text-anchor="middle">30s</text>
  <!-- caption -->
  <text x="281" y="150" font-size="12.5" fill="#6a7280" text-anchor="middle"><tspan x="281" dy="0">A long filing takes 3× a short one, so the cores fall out of step.</tspan><tspan x="281" dy="16">Total time is set by the busiest core (30s); the other sits idle.</tspan></text>
</svg>

Whichever core draws the long filings finishes last, and the total wall-clock time is set by that busiest core — not the average. The quicker cores go idle waiting for it. This is called **load imbalance**, and it's why you can't just divide total work by the number of cores to predict runtime.

---

## More Filings Than Cores (and Vice Versa)

The illustration above already shows the common situation — more filings than cores, cleared in waves. It's worth making both ratios explicit, since they come up constantly.

**More filings than cores — the usual case.** Say you have 100 filings but only 8 cores. The cores work in *waves*: the first 8 filings run at once, and the moment a core finishes it picks up the next filing in line, until all 100 are done. The total time is roughly the number of waves times the per-filing time — about ⌈100 ÷ 8⌉ = 13 waves × 5s ≈ 65s, versus ~500s in serial. You don't manage the waves yourself; the scheduler hands the next filing to whichever core comes free.

**More cores than filings.** Say you have 5 filings but 32 cores available. Only 5 cores can do anything — a single filing can't be split across cores — so the other 27 sit idle. Cores beyond the number of independent tasks buy you nothing, and requesting more than you'll use can mean a longer wait in the queue for resources you never touch.

{: .note }
> **Rule of thumb:** match cores to tasks. Aim for roughly one core per independent task, capped by what's available. Below that, you process in waves and still finish far ahead of serial; above that, the extra cores just sit idle.

---

## When Parallelization Helps

Parallelization only pays off when the pieces of work are **independent** — each can run without waiting on the results of another. When a job splits cleanly into fully independent tasks with no coordination between them, it's called **embarrassingly parallel** — and it's the easiest, highest-payoff kind of work to spread across cores. Extracting fields from a folder of filings is a textbook example.

| Works well in parallel | Does *not* parallelize cleanly |
|---|---|
| Extract fields from 100 separate filings | Step B needs the output of step A |
| Run the same simulation with 50 different seeds | A running total that every task updates |
| Resize 10,000 images | Reading line *n* requires line *n − 1* |

A quick test: if you could hand each task to a different person and never have them talk to each other, it will parallelize. Your extraction job fits perfectly — every filing is its own self-contained task.

{: .note }
> Parallelization doesn't make a single task faster — one filing still takes ~5s. It makes *many* tasks finish sooner by running them at the same time. If your bottleneck is one slow step, parallelizing won't help; you need a faster step (or a GPU — coming later today).

---

<label class="quest-check"><input type="checkbox" data-room="d4-parallelization" data-key="main"> I can explain what parallelization is and when it helps</label>

---

## What You Learned

- You can explain the difference between running tasks sequentially on one core and in parallel across many
- You can tell whether a workload is **independent** enough to parallelize
- You understand that parallelization speeds up *many* tasks, not a single slow one
