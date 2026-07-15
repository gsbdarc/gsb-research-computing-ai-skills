---
layout: default
title: "Data Privacy"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/data-privacy/
---

# The Stanford AI Playground

<div data-room-id="d2-stanford-ai-playground"></div>

*Beyond the forge, a corridor opens into a high-vaulted chamber. Banners bearing the Stanford seal line the walls, and where you might expect bare iron, you find polished glass terminals — each one connected not to the open internet, but to a walled garden of approved models maintained by the University. This is not your personal account. It is a shared instrument, governed, audited, and provided to every researcher on campus. Use it wisely.*

---

## 🖊️ What Is Stanford AI Playground?

Stanford AI Playground is a University-hosted gateway to large language models. It gives every Stanford researcher access to the same models (GPT-4o, GPT-4o-mini, and others) without a personal OpenAI account or credit card.

It comes in two forms:

**Web GUI** — a chat interface (like ChatGPT) accessible at:
> [https://aitools.stanford.edu](https://aitools.stanford.edu)

Log in with your SUNet credentials. You can ask questions, draft text, and test prompts — all going through Stanford's infrastructure, not your personal account.

**API gateway** — the same models accessible via code, using an OpenAI-compatible client. The only difference from a personal OpenAI setup is a different `base_url` and a Stanford-issued API key.

---

## 🔰 Try the Web GUI

Open [https://aitools.stanford.edu](https://aitools.stanford.edu) in your browser and log in.

Ask it something:
- *"Summarize what a virtual environment is in one sentence."*
- *"What is the difference between a kernel and a Python interpreter?"*

Notice: the responses come from the same models you'd use via the API. You're already using Stanford AI Playground.

---

## 🖊️ Upsides and Downsides

| | Detail |
|-|--------|
| ✅ **No personal billing** | Budget caps enforced by Stanford — you cannot accidentally run up a $10,000 bill |
| ✅ **Stanford data perimeter** | Covered under Stanford's data processing agreement with OpenAI |
| ✅ **No account required** | Every Stanford researcher has access via SUNet login |
| ⚠️ **Prompts are audited** | Stanford can review usage logs — don't send restricted data or PII through this gateway |
| ⚠️ **Rate limits** | Shared infrastructure means lower throughput than a dedicated paid account |
| ⚠️ **Model selection** | Available models are determined by Stanford's contract, not your preference |

**Personal OpenAI key vs. Stanford key:**

| | Personal key | Stanford key |
|-|-------------|-------------|
| Cost | Your credit card | Covered by Stanford |
| Audit | Not audited | Stanford can see prompts |
| Data governance | OpenAI's standard terms | Stanford's DPA with OpenAI |
| Rate limits | Based on your plan | Shared pool |
| Setup | Create account, enter billing | Already available — use the shared key |

---

## 🖊️ How the API Works

The Stanford AI Playground API is fully OpenAI-compatible. Code that calls the OpenAI API can call Stanford's gateway with two changes:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_STANFORD_KEY",           # Stanford-issued key, not OpenAI key
    base_url="https://aiapi-prod.stanford.edu/v1",  # Stanford gateway, not api.openai.com
)
```

Every model call, prompt, and response flows through `aiapi-prod.stanford.edu` — Stanford's contracted endpoint — instead of directly to OpenAI. Your code looks identical; only the endpoint changes.

In the next room (The Key Vault), you'll load the key securely from a `.env` file rather than hardcoding it.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="main"> Main Quest complete</label>

---

## 🧠 Skills Learned

- Stanford AI Playground gives every researcher access to GPT-4o and other models — no personal account needed
- The web GUI and the API gateway are two interfaces to the same underlying service
- The API is OpenAI-compatible: only `base_url` and the key change; all code is the same
- Prompts sent through Stanford's gateway are subject to audit — classify your data before sending it
