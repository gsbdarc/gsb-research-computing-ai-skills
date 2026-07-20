---
layout: default
title: "Why Run LLMs on the Yens?"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 4
permalink: /day4/why-local-llms/
---

# Why Run LLMs on the Yens?

<div data-room-id="d4-why-local-llms"></div>

This is a concept section. Since Day 2, every LLM call you've made — to the Stanford AI Playground, or any third-party model — has gone to an **API** (application programming interface): your prompt and your data travel to someone else's server, the model runs there, and the answer comes back. This section asks the opposite question: when should you run the model **yourself**, on Stanford's own hardware (the Yens)?

---

## What an API Call Actually Does

When you call an LLM API, three things happen outside your control:

- **Your data leaves.** The filing text — and whatever else is in your prompt — is sent over the network to the model provider.
- **The compute is theirs.** The model runs on the *model provider's* machines, not yours.
- **The model can change.** You get whatever weights the model provider is serving that day.

<svg viewBox="0 0 600 164" role="img" aria-labelledby="api-title api-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:600px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="api-title">Calling an LLM API sends your data to a remote server and back</title>
  <desc id="api-desc">Your code on the left sends a packet labelled "prompt plus data" across the internet to the model provider's server on the right, which runs the model and sends a "response" packet back.</desc>
  <!-- network link -->
  <line x1="170" y1="98" x2="430" y2="98" stroke="#cbd3e0" stroke-width="2" stroke-dasharray="4 5"/>
  <!-- left node: your code -->
  <rect x="20" y="66" width="150" height="64" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="95" y="90" font-size="13" font-weight="700" fill="#2c3e50" text-anchor="middle">Your code</text>
  <text x="95" y="105" font-size="10.5" fill="#6a7280" text-anchor="middle">(on your or</text>
  <text x="95" y="118" font-size="10.5" fill="#6a7280" text-anchor="middle">Stanford's machines)</text>
  <!-- right node: model provider -->
  <rect x="430" y="66" width="150" height="64" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="505" y="90" font-size="13" font-weight="700" fill="#2c3e50" text-anchor="middle">Model provider</text>
  <text x="505" y="105" font-size="10.5" fill="#6a7280" text-anchor="middle">(in the cloud)</text>
  <!-- outbound packet: prompt + data -->
  <g>
    <rect x="176" y="85" width="120" height="26" rx="8" fill="#E69F00"/>
    <text x="236" y="102" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">prompt + data ▶</text>
    <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.06;0.44;0.5;1" dur="5s" repeatCount="indefinite"/>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;130,0;130,0" keyTimes="0;0.06;0.44;1" dur="5s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <!-- inbound packet: response -->
  <g>
    <rect x="304" y="85" width="120" height="26" rx="8" fill="#0072B2"/>
    <text x="364" y="102" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">◀ response</text>
    <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.5;0.56;0.94;1" dur="5s" repeatCount="indefinite"/>
    <animateTransform attributeName="transform" type="translate" values="0,0;0,0;-130,0;-130,0" keyTimes="0;0.56;0.94;1" dur="5s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <!-- caption -->
  <text x="300" y="150" font-size="12.5" fill="#6a7280" text-anchor="middle">Your prompt and data go to the model provider's servers, and the response comes back.</text>
</svg>

---

## Why Run It Yourself?

**1. Privacy & data requirements — often a hard rule, not a preference.** Restricted, confidential, or IRB-governed data may not leave Stanford's perimeter. Run the model locally and your prompts and documents never leave the cluster — nothing goes to an outside model provider. (Which bucket your data falls in was covered in [the data classification section](../../day2/human-vs-llm/) on Day 2.)

**2. Cost at scale.** No per-token bill. You already have cluster access, so local "inference" (querying an LLM) is effectively free at the margin. A run over 100,000 filings that would rack up a real bill on a metered API costs nothing extra on the Yens.

**3. Reproducibility.** Versioning proprietary models is complicated — the provider can change the model behind a given name, and old versions eventually get retired. An open model is always reproducible: you control the weights, so the exact model is fixed and a reviewer (or future you) can rerun the identical pipeline years later.

**4. No API rate limits.** Model providers cap requests and tokens per minute, which throttles a big parallel job array. Locally you're bounded only by your own compute allocation on the cluster, so a thousand-task array isn't held back by someone else's quota.

---

## Open vs. Proprietary Models

There's a catch to "run it yourself": you can only run models whose **weights you can download**. The frontier models from OpenAI (GPT-5.6) and Anthropic (Claude Fable 5) are **proprietary** — the companies never release the weights, so those models exist *only* behind their cloud APIs. There is no way to run them on the Yens.

Running locally therefore means using **open-weight** models — ones whose parameters are published for anyone to download and serve, such as Llama (Meta), Mistral, Qwen, or DeepSeek. These are the kind of models you'll run on the Yens later today.

So the real choice isn't "any model, local or cloud." It's: a **proprietary model in the cloud**, or an **open-weight model you run yourself**.

---

## When the API Is Still the Right Call

Running locally isn't always the answer. The honest tradeoffs:

- **Capability** — the strongest models (GPT-5.6, Claude Fable 5) are proprietary and cloud-only, and often outperform the open models you can run locally. For the hardest tasks, the API wins.
- **Convenience** — an API key and one line of code: no cluster job to submit, no model server to start, no queue wait.
- **Elastic scale** — a hosted API scales on demand; the capacity you can run on the Yens is finite, so very large models or very high volume can exceed it.

---

## The Three Options at a Glance

| | Local on the Yens | Stanford AI Playground | Third-party API |
|---|---|---|---|
| **Where your data goes** | Stays on the cluster | In the cloud, but regulated and approved by Stanford | Leaves Stanford → model provider |
| **Cost** | Free at the margin | Budget-capped Stanford account | Per-token billing |
| **Models** | Whatever you can run on the Yens | Provider-curated, Stanford-audited | Latest, most capable |
| **Best for** | Restricted data, large batch jobs | Everyday research | Hardest tasks where data rules allow |

For the Stanford AI Playground's tradeoffs in more depth, see the [Upsides and Downsides table](../../day2/stanford-ai-playground/#upsides-and-downsides) from Day 2.

---

## Rule of Thumb

**Restricted data → run it locally, no exceptions.** Otherwise, weigh cost, reproducibility, and throughput (which favor local) against capability and convenience (which favor the API). You'll make this call in practice — and compare a model you run yourself against the Playground — in the sections that follow.

<label class="quest-check"><input type="checkbox" data-room="d4-why-local-llms" data-key="main"> I can explain when to run an LLM on the Yens instead of calling an API</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-why-local-llms.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- You know an API call sends your data to a model provider's servers and returns a response — the computation runs on their machines, not yours
- You can give the main reasons to run an LLM on the Yens instead: data privacy, cost at scale, reproducibility, and freedom from API rate limits
- You can name the honest counterweights — capability, convenience, elastic scale — where a hosted API is the better choice
- You can apply the rule of thumb: restricted data forces local; otherwise weigh the tradeoffs
