---
layout: default
title: "The Engine Room"
parent: "Day 4 — The GPU Fortress"
nav_order: 5
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
| **Setup** | `ollama pull` + API already running | API key from playground.stanford.edu | API key from vendor |

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
    base_url="https://playground.stanford.edu/api/v1",
    api_key=os.getenv("PLAYGROUND_API_KEY")
)

# Pattern 3 — Third-party (OpenAI, Anthropic via OpenAI-compat layer, etc.)
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    # base_url defaults to api.openai.com
)

# The rest of your code is identical across all three
response = client.chat.completions.create(
    model="llama3.2",         # swap model name to match the backend
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
> The [Grand Hall](../grand-hall/) covers Stanford's 3-bucket data classification rule. If you don't know which bucket your data is in, that room comes before this decision — not after.

<label class="quest-check"><input type="checkbox" data-room="d4-engine-room" data-key="main"> Engine Room briefing complete — I know which LLM access pattern fits my data and research context</label>

---

## 🧠 Skills Learned

- You can describe the three LLM access patterns available on the Yens and what distinguishes them: data residency, cost, and model availability
- You know that all three speak the same OpenAI-compatible API — swapping `base_url` is the only code change
- You can apply the decision guide: restricted data forces local Ollama; general research fits the AI Playground; third-party is available when data governance allows
- You understand that the Grand Hall's 3-bucket rule is the prerequisite to this decision — classification first, access pattern second
