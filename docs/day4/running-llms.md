---
layout: default
title: "Running LLMs on the Yens"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 5
permalink: /day4/running-llms/
---

# Running LLMs on the Yens

<div data-room-id="d4-running-llms"></div>

The last section covered *why* you'd run a model yourself. This one is the *how*: LLMs need a **GPU**, so you'll request one from the cluster, load an open model onto it, and query that model with the same OpenAI-compatible code you already used for the Playground.

---

## Why LLMs Need a GPU

Running an LLM is, under the hood, an enormous chain of **matrix multiplications** — the same arithmetic repeated across billions of numbers. A CPU does a few of these at a time, whereas a **GPU** (graphics processing unit) has thousands of small cores that do them all at once. Because those billions of multiplications don't depend on each other, spreading them across thousands of cores clears the whole batch far faster — so a model that crawls on a CPU runs at a usable speed on a GPU.

So: "running an LLM on the Yens" really means get your job onto a **GPU node**, where the model can actually run sufficiently quickly.

{: .note }
> The dependence of LLMs on GPUs has made them enormously valuable. Indeed, the surge in the share price of NVIDIA, the dominant GPU maker, tracks the AI boom:
>
> <svg viewBox="0 0 600 278" role="img" aria-labelledby="nvda-title nvda-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:600px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
>   <title id="nvda-title">NVIDIA share price over time</title>
>   <desc id="nvda-desc">A line chart of NVIDIA's split-adjusted year-end share price from 2016 to 2024. It stays low — a few dollars — through 2019, rises through 2021, dips in 2022, then climbs steeply in 2023 and 2024 as demand for AI GPUs surges, reaching about $134 by the end of 2024.</desc>
>   <text x="300" y="20" font-size="13" font-weight="700" fill="#2c3e50" text-anchor="middle">NVIDIA's share price</text>
>   <!-- y gridlines -->
>   <line x1="50" y1="171" x2="585" y2="171" stroke="#eef1f8" stroke-width="1"/>
>   <line x1="50" y1="93"  x2="585" y2="93"  stroke="#eef1f8" stroke-width="1"/>
>   <!-- axes -->
>   <line x1="50" y1="30"  x2="50"  y2="250" stroke="#b8bfcc" stroke-width="1.5"/>
>   <line x1="50" y1="250" x2="585" y2="250" stroke="#b8bfcc" stroke-width="1.5"/>
>   <!-- y labels -->
>   <text x="44" y="254" font-size="10" fill="#6a7280" text-anchor="end">$0</text>
>   <text x="44" y="175" font-size="10" fill="#6a7280" text-anchor="end">$50</text>
>   <text x="44" y="97"  font-size="10" fill="#6a7280" text-anchor="end">$100</text>
>   <!-- price line -->
>   <polyline points="55,246 121,242 186,245 252,241 318,230 383,204 449,227 514,172 580,39" fill="none" stroke="#0072B2" stroke-width="2.5"/>
>   <circle cx="55"  cy="246" r="3" fill="#0072B2"/>
>   <circle cx="121" cy="242" r="3" fill="#0072B2"/>
>   <circle cx="186" cy="245" r="3" fill="#0072B2"/>
>   <circle cx="252" cy="241" r="3" fill="#0072B2"/>
>   <circle cx="318" cy="230" r="3" fill="#0072B2"/>
>   <circle cx="383" cy="204" r="3" fill="#0072B2"/>
>   <circle cx="449" cy="227" r="3" fill="#0072B2"/>
>   <circle cx="514" cy="172" r="3" fill="#0072B2"/>
>   <circle cx="580" cy="39"  r="4" fill="#0072B2"/>
>   <text x="578" y="33" font-size="10" font-weight="700" fill="#0072B2" text-anchor="end">~$134</text>
>   <!-- x labels -->
>   <text x="55"  y="266" font-size="10" fill="#6a7280" text-anchor="middle">2016</text>
>   <text x="121" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2017</text>
>   <text x="186" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2018</text>
>   <text x="252" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2019</text>
>   <text x="318" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2020</text>
>   <text x="383" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2021</text>
>   <text x="449" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2022</text>
>   <text x="514" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2023</text>
>   <text x="580" y="266" font-size="10" fill="#6a7280" text-anchor="middle">2024</text>
> </svg>

---

## GPUs on the Yens

The Yens have several GPU types. For our purposes they differ mainly in one thing: **VRAM** (the GPU's own memory), which sets a ceiling on how big a model you can load.

| GPU type | VRAM | Roughly good for |
|-----|------|------------------|
| A30 | 24 GB | small models, embeddings |
| A40 | 48 GB | mid-size models |
| H200 | 141 GB | large models |

A model's weights have to fit in VRAM, so VRAM — not disk or CPU RAM — is the binding constraint on which models you can run.

You request a GPU the same way you set any other resource in a SLURM script — a directive at the top:

```bash
#SBATCH --partition=gpu       # the GPU partition (confirm the name for your setup)
#SBATCH --gres=gpu:1          # request one GPU
```

Just like the `#SBATCH` directives you wrote on Day 3, this tells the scheduler what your job needs — here, one GPU. Match the partition name (and any specific-node targeting) to your cluster's current setup; ask an instructor if unsure.

<label class="quest-check"><input type="checkbox" data-room="d4-running-llms" data-key="main"> I know why LLMs need a GPU and how to request one on the Yens</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-running-llms.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## Exercise: Run a Model on a GPU

We'll use **[Ollama](https://ollama.com)**, a tool that downloads an open model and serves it behind a local API. Run these on a GPU node (an interactive GPU session, or inside a GPU job).

**Part 1 — Pull and serve an open model:**

```bash
ollama pull llama3.2:3b     # download the weights (cached locally on the cluster)
ollama serve                # start the local model server (keep it running)
```

**Part 2 — Query it from Python.** The interface is **OpenAI-compatible**, so this is the *same* code you used for the Stanford AI Playground on Day 2 — only the `base_url` changes.

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",   # the local Ollama server
    api_key="ollama",                        # ignored, but the client requires a value
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "In one sentence, what is an SEC Form 3 filing?"}],
)
print(response.choices[0].message.content)
```

Switching between a local model, the Playground, and a third-party API is just a matter of changing `base_url` (and `model`/`api_key`) — the rest of your pipeline stays identical.

{: .note }
> The model runs entirely on the Yens — your prompts and data never leave the cluster. That's the privacy point from the last section, made real.

<label class="quest-check"><input type="checkbox" data-room="d4-running-llms" data-key="exercise"> Exercise complete — pulled an open model on a GPU and queried it</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/rf-bootcamp-2026` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-running-llms.exercise` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/rf-bootcamp-2026`), not the class repo `gsbdarc/rf-bootcamp-2026` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- You can explain why LLMs need a GPU: inference is massively parallel matrix multiplication, which GPUs do far faster than CPUs
- You know that **VRAM** sets the ceiling on the model size a given GPU can load, and how the Yen GPUs compare
- You can request a GPU in a SLURM job with `--partition=gpu` and `--gres=gpu:1`
- You ran an open model locally with Ollama and queried it — and you know switching endpoints is just a change of `base_url`
