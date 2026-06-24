---
layout: default
title: "The Key Vault"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 5
permalink: /day2/key-vault/
---

# The Key Vault

<div data-room-id="d2-key-vault"></div>

*You press your shoulder against a door reinforced with iron bands and Stanford seals. It swings open to reveal the AI Playground — a walled garden carved out of the University's own infrastructure, humming with approved models and institutional eyes. These keys are not yours to keep. They belong to Stanford, they are audited, and they do not cross the campus perimeter. Know what that buys you — speed, safety, budget protection — and what it costs you — privacy of prompts — before your fingers touch a single API endpoint.*

---

## 🗡️ Main Quest

You are standing at the threshold. The vault holds models that could accelerate your research by months. The only thing between you and them is a properly loaded key.

{: .important }
> **Quest:** Load a Stanford AI Playground API key from a `.env` file using `python-dotenv`, and make your first authenticated request to confirm the key works.

**The Stanford AI Playground**

Stanford's AI Playground provides access to approved LLMs (GPT-4o, Claude, and others) through an OpenAI-compatible API. It differs from a personal OpenAI account in three critical ways:

1. **Stanford data perimeter** — data stays within Stanford's contracted perimeter, subject to the University's data agreements
2. **Budget caps** — spending is controlled; you cannot accidentally run up a $10,000 bill
3. **Audit logs** — Stanford can see what was sent (prompts + responses); act accordingly

**Step 1 — Create `.env`**

```bash
cd ~/rf-bootcamp-2026
touch .env
```

Edit `.env` (never commit this file):
```
OPENAI_API_KEY=your-playground-api-key-here
OPENAI_BASE_URL=https://api.stanford.edu/openai/v1
```

Your instructor will provide the Playground API key and correct base URL for your cohort.

**Step 2 — Add `.env` to `.gitignore`**

```bash
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Ignore .env files"
```

**Step 3 — Load and use in Python**

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv()   # reads .env, sets environment variables

client = openai.OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say 'The vault is open' and nothing else."}]
)
print(response.choices[0].message.content)
```

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="main"> Main Quest complete</label>
