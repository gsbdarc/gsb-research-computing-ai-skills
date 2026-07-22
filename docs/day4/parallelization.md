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

Think back to [the kitchen from Day 3](../../day3/compute-environments/): your machine is a kitchen, and every CPU core is a burner.

Some cooking splits across burners perfectly. Say you want four grilled cheeses: each sandwich is its own pan — get the bread, put on the cheese, grill one side, grill the other — and no sandwich needs anything from the others. Fire up four burners and lunch is ready in a quarter of the time.

But the steps *within* one sandwich don't split at all: you can't grill a side before the cheese is on the bread — each step needs the previous one finished. Put four cooks on a single sandwich and three of them stand around watching. And no matter how many cooks you hire, a sandwich that takes four minutes takes four minutes.

<svg viewBox="0 0 600 534" role="img" aria-labelledby="gc-title gc-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gc-title">Grilled cheese on one burner vs. four burners</title>
  <desc id="gc-desc">Two panels. Top: one burner cooks four grilled cheeses one after another — a single burner box shows the four steps (get bread, put cheese on bread, grill one side, grill the other side) lighting up in sequence, with a note to repeat four times, one sandwich after another. Bottom: four burner boxes side by side each run the same four steps at the same time, cooking all four sandwiches at once.</desc>
  <!-- panel A: one burner, the ×4 repetition shown vertically -->
  <text x="300" y="22" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">One burner, four grilled cheeses</text>
  <rect x="190" y="34" width="220" height="264" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="202" y="50" font-size="10" font-weight="700" fill="#8a93a3">Burner</text>
  <text x="207" y="64" font-size="8.5" font-weight="600" fill="#8a93a3">sandwich 1</text>
  <text x="180" y="87"  font-size="9" fill="#8a93a3" text-anchor="end">t = 1</text>
  <text x="180" y="119" font-size="9" fill="#8a93a3" text-anchor="end">t = 2</text>
  <text x="180" y="151" font-size="9" fill="#8a93a3" text-anchor="end">t = 3</text>
  <text x="180" y="183" font-size="9" fill="#8a93a3" text-anchor="end">t = 4</text>
  <rect x="205" y="70" width="190" height="26" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.06;0.08;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="87" font-size="11" fill="#2c3e50" text-anchor="middle">get bread</text>
  <rect x="205" y="102" width="190" height="26" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.04;0.06;0.12;0.14;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="119" font-size="11" fill="#2c3e50" text-anchor="middle">put cheese on bread</text>
  <rect x="205" y="134" width="190" height="26" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.10;0.12;0.18;0.20;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="151" font-size="11" fill="#2c3e50" text-anchor="middle">grill one side of sandwich</text>
  <rect x="205" y="166" width="190" height="26" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.16;0.18;0.24;0.26;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="183" font-size="11" fill="#2c3e50" text-anchor="middle">grill other side of sandwich</text>
  <!-- sandwiches 2–4: the same four steps, repeated vertically -->
  <text x="180" y="216" font-size="9" fill="#8a93a3" text-anchor="end">t = 5–8</text>
  <text x="180" y="248" font-size="9" fill="#8a93a3" text-anchor="end">t = 9–12</text>
  <text x="180" y="280" font-size="9" fill="#8a93a3" text-anchor="end">t = 13–16</text>
  <rect x="205" y="200" width="190" height="24" rx="6" fill="#f3f5fa" stroke="#cdd4e6" stroke-width="1.2" stroke-dasharray="4 3"><animate attributeName="fill" values="#f3f5fa;#f3f5fa;#fde9c8;#fde9c8;#f3f5fa;#f3f5fa" keyTimes="0;0.22;0.24;0.48;0.50;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="216" font-size="9.5" fill="#8a93a3" text-anchor="middle">sandwich 2 — same four steps</text>
  <rect x="205" y="232" width="190" height="24" rx="6" fill="#f3f5fa" stroke="#cdd4e6" stroke-width="1.2" stroke-dasharray="4 3"><animate attributeName="fill" values="#f3f5fa;#f3f5fa;#fde9c8;#fde9c8;#f3f5fa;#f3f5fa" keyTimes="0;0.46;0.48;0.72;0.74;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="248" font-size="9.5" fill="#8a93a3" text-anchor="middle">sandwich 3 — same four steps</text>
  <rect x="205" y="264" width="190" height="24" rx="6" fill="#f3f5fa" stroke="#cdd4e6" stroke-width="1.2" stroke-dasharray="4 3"><animate attributeName="fill" values="#f3f5fa;#f3f5fa;#fde9c8;#fde9c8;#f3f5fa;#f3f5fa" keyTimes="0;0.70;0.72;0.96;0.98;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="300" y="280" font-size="9.5" fill="#8a93a3" text-anchor="middle">sandwich 4 — same four steps</text>
  <!-- repeat annotation -->
  <text x="490" y="140" font-size="16" font-weight="700" fill="#8a93a3" text-anchor="middle">× 4</text>
  <text x="490" y="158" font-size="10" fill="#8a93a3" text-anchor="middle">one sandwich after another</text>
  <line x1="490" y1="170" x2="490" y2="250" stroke="#b3bccb" stroke-width="1.5"/>
  <polygon points="485,248 495,248 490,258" fill="#b3bccb"/>
  <!-- panel B: four burners -->
  <text x="300" y="330" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">Four burners, four grilled cheeses</text>
  <text x="38" y="378" font-size="9" fill="#8a93a3" text-anchor="end">t = 1</text>
  <text x="38" y="408" font-size="9" fill="#8a93a3" text-anchor="end">t = 2</text>
  <text x="38" y="438" font-size="9" fill="#8a93a3" text-anchor="end">t = 3</text>
  <text x="38" y="468" font-size="9" fill="#8a93a3" text-anchor="end">t = 4</text>
  <rect x="44" y="340" width="128" height="142" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="52" y="354" font-size="8.5" font-weight="700" fill="#8a93a3">Burner 1</text>
  <rect x="50" y="362" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.06;0.08;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="108" y="378" font-size="7.5" fill="#2c3e50" text-anchor="middle">get bread</text>
  <rect x="50" y="392" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.04;0.06;0.12;0.14;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="108" y="408" font-size="7.5" fill="#2c3e50" text-anchor="middle">put cheese on bread</text>
  <rect x="50" y="422" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.10;0.12;0.18;0.20;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="108" y="438" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill one side of sandwich</text>
  <rect x="50" y="452" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.16;0.18;0.24;0.26;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="108" y="468" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill other side of sandwich</text>
  <rect x="182" y="340" width="128" height="142" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="190" y="354" font-size="8.5" font-weight="700" fill="#8a93a3">Burner 2</text>
  <rect x="188" y="362" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.06;0.08;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="246" y="378" font-size="7.5" fill="#2c3e50" text-anchor="middle">get bread</text>
  <rect x="188" y="392" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.04;0.06;0.12;0.14;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="246" y="408" font-size="7.5" fill="#2c3e50" text-anchor="middle">put cheese on bread</text>
  <rect x="188" y="422" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.10;0.12;0.18;0.20;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="246" y="438" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill one side of sandwich</text>
  <rect x="188" y="452" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.16;0.18;0.24;0.26;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="246" y="468" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill other side of sandwich</text>
  <rect x="320" y="340" width="128" height="142" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="328" y="354" font-size="8.5" font-weight="700" fill="#8a93a3">Burner 3</text>
  <rect x="326" y="362" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.06;0.08;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="384" y="378" font-size="7.5" fill="#2c3e50" text-anchor="middle">get bread</text>
  <rect x="326" y="392" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.04;0.06;0.12;0.14;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="384" y="408" font-size="7.5" fill="#2c3e50" text-anchor="middle">put cheese on bread</text>
  <rect x="326" y="422" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.10;0.12;0.18;0.20;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="384" y="438" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill one side of sandwich</text>
  <rect x="326" y="452" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.16;0.18;0.24;0.26;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="384" y="468" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill other side of sandwich</text>
  <rect x="458" y="340" width="128" height="142" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="466" y="354" font-size="8.5" font-weight="700" fill="#8a93a3">Burner 4</text>
  <rect x="464" y="362" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.06;0.08;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="522" y="378" font-size="7.5" fill="#2c3e50" text-anchor="middle">get bread</text>
  <rect x="464" y="392" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.04;0.06;0.12;0.14;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="522" y="408" font-size="7.5" fill="#2c3e50" text-anchor="middle">put cheese on bread</text>
  <rect x="464" y="422" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.10;0.12;0.18;0.20;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="522" y="438" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill one side of sandwich</text>
  <rect x="464" y="452" width="116" height="24" rx="6" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.2"><animate attributeName="fill" values="#eef1f8;#eef1f8;#fde9c8;#fde9c8;#eef1f8;#eef1f8" keyTimes="0;0.16;0.18;0.24;0.26;1" dur="14s" repeatCount="indefinite"/></rect>
  <text x="522" y="468" font-size="7.5" fill="#2c3e50" text-anchor="middle">grill other side of sandwich</text>
  <!-- caption -->
  <text x="300" y="506" font-size="12.5" fill="#6a7280" text-anchor="middle"><tspan x="300" dy="0">The four steps of one sandwich are a sequence — grilling can't start before assembly. But the</tspan><tspan x="300" dy="16">sandwiches are independent: four burners finish at t = 4 what one burner finishes at t = 16.</tspan></text>
</svg>

Code is the same. Parallelization pays off when the pieces of work are **independent** — each can run without waiting on the results of another. When a job splits cleanly into fully independent tasks with no coordination between them, it's called **embarrassingly parallel** — the easiest, highest-payoff kind of work to spread across workers.

A quick test, in kitchen terms: if you could hand each task to a different cook and never have them talk to each other, it will parallelize. Your extraction job fits perfectly — every filing is its own self-contained task.

{: .note }
> Parallelization doesn't make a single task faster — one grilled cheese still takes its four steps. It makes *many* tasks finish sooner by running them at the same time. If your bottleneck is one slow step, parallelizing won't help; you need a faster step (or a GPU — coming later today).

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

So far every filing took the same 5 seconds. Real filings aren't so uniform — a dense filing with many transactions can take two or three times as long as a simple one. Take the same eight filings, but let **filing 3 run 3× long** — mid-row, and in the middle of job 1's chunk in the two-job split below. Now the two dials behave differently.

**Within one job**, the cores share the batch dynamically — each grabs the next free filing the moment it's done. The long filing simply gets absorbed: one core settles into it while the other sweeps up the remaining short filings, and both finish together at **t = 5**:

<svg viewBox="0 0 600 178" role="img" aria-labelledby="lf1-title lf1-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="lf1-title">One job, two cores, one long filing in the middle: the cores rebalance</title>
  <desc id="lf1-desc">A single SLURM job box holds two CPUs and eight filings; the third filing takes three times as long as the others. One CPU settles into the long filing while the other sweeps up the remaining short filings, so both stay busy and finish together at time five.</desc>
  <rect x="6" y="6" width="588" height="136" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="25" font-size="12" font-weight="700" fill="#8a93a3">Job</text>
  <text x="300" y="30" font-size="11" font-weight="600" fill="#009E73" text-anchor="middle" opacity="0">all eight done at t = 5<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.66;0.70;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/></text>
  <rect x="22"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="52"  y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="92"  y="86" width="60" height="48" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="122" y="114" font-size="11" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="162" y="86" width="60" height="48" rx="9" fill="#fdf1e0" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="192" y="104" font-size="11" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <text x="192" y="120" font-size="9" font-weight="600" fill="#b26a00" text-anchor="middle">long ×3</text>
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
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;420,0;420,0;0,0" keyTimes="0;0.115;0.13;0.505;0.52;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <g>
    <path d="M115,75 L129,75 L122,86 Z" fill="#E69F00"/>
    <circle cx="122" cy="58" r="18" fill="#E69F00"><animate attributeName="r" values="18;20;18" dur="1s" repeatCount="indefinite"/></circle>
    <text x="122" y="61" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;140,0;140,0;210,0;210,0;280,0;280,0;420,0;420,0;0,0" keyTimes="0;0.115;0.13;0.245;0.26;0.375;0.39;0.505;0.52;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="164" font-size="12.5" fill="#6a7280" text-anchor="middle">CPU 1 settles into the long filing; CPU 2 sweeps up the rest — everything is done at t = 5.</text>
</svg>

That's the strength of a shared pool of work: as long as anything is left to do, no core waits.

**Across two jobs**, the filings were split into fixed chunks before anything ran — job 1 gets filings 1–4, long one included; job 2 gets 5–8. The chunks can't help each other: job 2 clears its short filings by **t = 4**, finishes, and releases its core back to the cluster, while job 1 grinds on until **t = 6**. The batch is done only when the slowest chunk is — this is **load imbalance**, and fixed chunks have no way to rebalance it:

<svg viewBox="0 0 600 300" role="img" aria-labelledby="lf2-title lf2-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:598px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="lf2-title">Two jobs, one core each, the long filing in job 1's chunk: chunks can't rebalance</title>
  <desc id="lf2-desc">Two stacked SLURM job boxes, each with one CPU and four filings. The long third filing sits in the middle of the first job's chunk: job 1 works until time six, while job 2 clears its four short filings by time four, completes, and releases its core. The whole batch waits on the slowest chunk.</desc>
  <rect x="6" y="6" width="588" height="124" rx="12" fill="#f7f9fd" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="22" y="24" font-size="12" font-weight="700" fill="#8a93a3">Job 1</text>
  <rect x="40"  y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="75"  y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 1</text>
  <rect x="190" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="225" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 2</text>
  <rect x="340" y="80" width="70" height="44" rx="9" fill="#fdf1e0" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="375" y="100" font-size="12" fill="#2c3e50" text-anchor="middle">filing 3</text>
  <text x="375" y="116" font-size="9" font-weight="600" fill="#b26a00" text-anchor="middle">long ×3</text>
  <rect x="490" y="80" width="70" height="44" rx="9" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="525" y="106" font-size="12" fill="#2c3e50" text-anchor="middle">filing 4</text>
  <text x="240" y="58" font-size="11" font-weight="600" fill="#6a7280" text-anchor="middle" opacity="0">done at t = 6<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.78;0.82;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/></text>
  <g>
    <path d="M68,70 L82,70 L75,80 Z" fill="#0072B2"/>
    <circle cx="75" cy="54" r="16" fill="#0072B2"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="57" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 1</text>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;0,0" keyTimes="0;0.115;0.13;0.245;0.26;0.635;0.65;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
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
  <text x="240" y="198" font-size="11" font-weight="600" fill="#009E73" text-anchor="middle" opacity="0">job complete at t = 4 — core released ✓<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.54;0.58;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/></text>
  <g>
    <path d="M68,210 L82,210 L75,220 Z" fill="#E69F00"/>
    <circle cx="75" cy="194" r="16" fill="#E69F00"><animate attributeName="r" values="16;18;16" dur="1s" repeatCount="indefinite"/></circle>
    <text x="75" y="197" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">CPU 2</text>
    <animate attributeName="opacity" values="1;1;0.15;0.15;1" keyTimes="0;0.52;0.56;0.9;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;150,0;150,0;300,0;300,0;450,0;450,0;450,0;0,0" keyTimes="0;0.115;0.13;0.245;0.26;0.375;0.39;0.505;0.88;1" dur="14s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="290" font-size="12.5" fill="#6a7280" text-anchor="middle">Fixed chunks can't share the load: job 1 runs to t = 6 while job 2 finishes at t = 4 and releases its core.</text>
</svg>

Same filings, same cores — different totals. The shared pool finishes at **t = 5**; the fixed chunks finish at **t = 6**, because job 2 can't help with a filing that isn't in its chunk. What the two-job version buys instead is release: job 2's core goes back to the cluster at t = 4, while the one-job version holds both cores until the whole batch ends.

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
- You can distinguish parallelizing **within a job** (more cores) from **across jobs** (a job array) — and the trade-off: a shared pool rebalances around a long task, while separate jobs release their cores as they finish but can't rebalance fixed chunks
- You understand that parallelization speeds up *many* tasks, not a single slow one
