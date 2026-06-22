---
layout: default
title: "The Key Vault"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 4
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
cd ~/rf_bootcamp_2026
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

---

## 📦 Side Quests

Two rewards are hidden in this vault — one teaches you how to undo a mistake before it goes public, the other hands you a more secure way to carry credentials altogether.

{: .chest }
> **Side Quest 1 — Shield of `.gitignore`:** You committed `.gitignore` above. Now practice a harder case: accidentally stage a `.env` file, then remove it from staging without deleting the file. Use `git rm --cached .env`. Why is this important to know if you're working in a public repo?

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side1"> Shield of .gitignore unlocked</label>

This side quest holds something even craftier — a way to keep your secrets off the filesystem entirely.

{: .chest }
> **Side Quest 2 — Keyring Knife:** Use Python's `keyring` library to store and retrieve the API key from the OS keychain instead of a `.env` file. What is the security trade-off between the two approaches?

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side2"> Keyring Knife unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Shield of `.gitignore`** — keep secrets, large data files, and environment-specific config out of your git history; know how to un-stage an accidentally added secret before pushing.
>
> **Keyring Knife** — store credentials in the OS keychain for scripts that run interactively; avoid `.env` files entirely when the platform supports it.

---

## 🧠 Skills Learned

- You can explain what the Stanford AI Playground is and why it is different from a personal API account — audited, budget-capped, and perimeter-bound
- You can load credentials from a `.env` file at runtime using `python-dotenv`, with zero hardcoding in your source
- You can protect a secret before it ever touches git history — and rescue one that almost slipped through with `git rm --cached`
- You can articulate what "data governance" means for AI APIs: your prompts are data, and Stanford can read them
