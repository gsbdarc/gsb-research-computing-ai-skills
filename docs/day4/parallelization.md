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

<svg viewBox="0 0 600 178" role="img" aria-labelledby="imbalance-title imbalance-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="imbalance-title">A long filing causes load imbalance</title>
  <desc id="imbalance-desc">Six filings in a row; the last filing takes three times as long as the others. Two cores process the filings two at a time. When the short filings run out, one core moves to the end of the line and waits idle while the other core finishes the long final filing, which sets the total time.</desc>
  <!-- filing boxes: the last one (filing 6) is long and tinted -->
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
  <rect x="471" y="64" width="76" height="56" rx="10" fill="#fdf1e0" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="509" y="90" font-size="13" fill="#2c3e50" text-anchor="middle">filing 6</text>
  <text x="509" y="107" font-size="10" font-weight="600" fill="#b26a00" text-anchor="middle">long ×3</text>
  <!-- core 1 (blue): filings 1, 3, 5 — then waits idle at the end of the line -->
  <g>
    <path d="M46,54 L62,54 L54,64 Z" fill="#0072B2"/>
    <circle cx="54" cy="34" r="20" fill="#0072B2"/>
    <text x="54" y="38" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <text x="54" y="9" font-size="10" font-weight="600" fill="#9aa2b1" text-anchor="middle" opacity="0">idle<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.5833;0.60;0.8667;1" dur="8s" repeatCount="indefinite" calcMode="linear"/></text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;182,0;182,0;364,0;364,0;524,0;524,0;0,0"
      keyTimes="0;0.1667;0.1833;0.35;0.3667;0.5333;0.5833;0.8667;1"
      dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <!-- core 2 (orange): filings 2, 4, then the long filing 6 — the straggler -->
  <g>
    <path d="M137,54 L153,54 L145,64 Z" fill="#E69F00"/>
    <circle cx="145" cy="34" r="20" fill="#E69F00"/>
    <text x="145" y="38" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">CPU</text>
    <animateTransform attributeName="transform" type="translate"
      values="0,0;0,0;182,0;182,0;364,0;364,0;0,0"
      keyTimes="0;0.1667;0.1833;0.35;0.3667;0.8667;1"
      dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="150" font-size="12.5" fill="#6a7280" text-anchor="middle"><tspan x="300" dy="0">Filing 6 runs 3× longer, so core 2 is still busy when core 1 runs out of work.</tspan><tspan x="300" dy="16">Core 1 waits idle at the end of the line; the straggler sets the total time.</tspan></text>
</svg>

The core that draws a long filing keeps working after the others have run out, and the total wall-clock time is set by that straggler — not the average. The cores that finish early sit idle waiting for it. This is called **load imbalance**, and it's why you can't just divide total work by the number of cores to predict runtime.

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
