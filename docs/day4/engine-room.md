---
layout: default
title: "The Engine Room"
parent: "Day 4 — The GPU Fortress"
nav_order: 6
permalink: /day4/engine-room/
---

# The Engine Room

<div data-room-id="d4-engine-room"></div>

*Two power lines run into the Engine Room. One is the local generator — Ollama, humming on the H200 down the hall, powered by the cluster you already own. The other snakes out through the fortress wall and into the wider world: Stanford's AI Playground, OpenAI, Anthropic. Both lines light the same bulb. The question is never "which one works?" — it's "which one should I trust with this data, and what will it cost me?"*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Understand the three LLM access patterns available to Stanford researchers — local Ollama, Stanford AI Playground, and third-party APIs — and know which one fits your data, budget, and research context.

This is a concept and demo block.

**The three patterns:**

| | Ollama (local, on Yens) | Stanford AI Playground | Third-party API (OpenAI, Anthropic, etc.) |
|---|---|---|---|
| **Where data goes** | Stays on the Yens cluster | Stays within Stanford perimeter | Leaves Stanford — goes to vendor |
| **Cost** | Free (cluster access you already have) | Budget-capped (Stanford account) | Costs $ per token |
| **Models available** | Whatever fits on the H200 (141 GB VRAM) | GPT-4o, Claude, Llama — vendor-curated list | Most capable, latest models |
| **Good for** | Restricted/sensitive data, large batch jobs | General research, day-to-day LLM work | Work where data restrictions allow |
| **Setup** | `ollama pull` + API already running | API key from aiapi-prod.stanford.edu | API key from vendor |

**The secret that makes this easy:**

All three speak the same OpenAI-compatible API. Your Python code doesn't change — only `base_url` and `api_key` do.

```python
import openai, os

# Pattern 1 — Ollama on the Yens (local, free, data stays on cluster)
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"          # Ollama ignores the key but the client requires one
)

# Pattern 2 — Stanford AI Playground (Stanford perimeter, budget-capped)
client = openai.OpenAI(
    base_url="https://aiapi-prod.stanford.edu/v1",
    api_key=os.getenv("PLAYGROUND_API_KEY")
)

# Pattern 3 — Third-party (OpenAI, Anthropic via OpenAI-compat layer, etc.)
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    # base_url defaults to api.openai.com
)

# The rest of your code is identical across all three
response = client.chat.completions.create(
    model="llama3.2:3b",      # swap model name to match the backend
    messages=[{"role": "user", "content": prompt}]
)
```

**How to choose:**

```
Is the data restricted (Level 2 / confidential / covered by IRB)?
  └── Yes → Ollama only. Data cannot leave the cluster.

Is the data public or low-sensitivity?
  ├── Running a large batch job on the cluster? → Ollama (free, already here)
  ├── Want GPT-4 class models, Stanford-audited? → AI Playground
  └── Need cutting-edge capability, data restrictions allow? → Third-party API

Not sure about your data? → Visit the Grand Hall before you pick.
```

{: .note }
> The 3-bucket data classification rule was covered in [The Crucible](../../day2/human-vs-llm/) on Day 2. If you're unsure which bucket your data belongs to, revisit that room before picking an endpoint.

<label class="quest-check"><input type="checkbox" data-room="d4-engine-room" data-key="main"> Engine Room briefing complete — I know which LLM access pattern fits my data and research context</label>

---

## Discussion — Human vs. LLM: when to trust results at scale

You've run filings through both pipelines. Now the harder question: how much do you trust what came back?

{: .note }
> **Class discussion:** Compare your Playground and Ollama outputs on the same 5 filings:
> - Where do the two models agree? Where do they disagree?
> - When a model returns a confident answer, how would you verify it's correct?
> - If you scaled to 10,000 filings, how would you detect that 5% of extractions are wrong?

**Rules of thumb for validation at scale:**

| Situation | What to do |
|-----------|------------|
| Models agree on all 5 samples | Spot-check 2–5% of the full run; automate a format sanity check |
| Models disagree on 1–2 samples | Read those cases; understand why before scaling |
| Models disagree on 3+ samples | Stop. Rewrite the prompt. Validate on 20 before scaling. |
| High-stakes extraction | Human review on a random 10% sample, no exceptions |

The goal is not to find the "best" model — it's to know your error rate before you commit to a 100-job array.

---

## 🧠 Skills Learned

- You can describe the three LLM access patterns available on the Yens and what distinguishes them: data residency, cost, and model availability
- You know that all three speak the same OpenAI-compatible API — swapping `base_url` is the only code change
- You can apply the decision guide: restricted data forces local Ollama; general research fits the AI Playground; third-party is available when data governance allows
- You understand that the Grand Hall's 3-bucket rule is the prerequisite to this decision — classification first, access pattern second
