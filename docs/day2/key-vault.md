---
layout: default
title: "The Key Vault"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 5
permalink: /day2/key-vault/
---

# The Key Vault

<div data-room-id="d2-key-vault"></div>

*You press your shoulder against a door reinforced with iron bands and Stanford seals. It swings open to reveal a small chamber with a single locked chest. Inside: the key that opens the Stanford AI Playground. These keys are not yours to keep. They belong to Stanford, they are audited, and they do not cross the campus perimeter. Know what that buys you — speed, safety, budget protection — and what it costs you — privacy of prompts — before your fingers touch a single API endpoint.*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Load the Stanford AI Playground API key from a `.env` file, add `.env` to `.gitignore`, and make your first authenticated API call.

---

### Step 1 — Look at the Shared Key

The bootcamp API key lives in a shared file on the Yens. Take a look:

```bash
cat /scratch/shared/rf-bootcamp-2026/.env
```

You'll see something like:

```
OPENAI_API_KEY=sk-stanford-...
OPENAI_BASE_URL=https://aiapi-prod.stanford.edu/v1
```

Do not copy this file anywhere public. Do not commit it to git. You are about to load it safely.

---

### Step 2 — Create Your Own `.env`

In your `day2/` directory:

```bash
cd ~/day2
touch .env
```

Open `.env` and add the values you saw above:

```
OPENAI_API_KEY=sk-stanford-...
OPENAI_BASE_URL=https://aiapi-prod.stanford.edu/v1
```

---

### Step 3 — Add `.env` to `.gitignore`

The `.env` file must never be committed to git. Add it now:

```bash
echo ".env" >> ~/.gitignore
# or, within your bootcamp repo:
echo ".env" >> ~/rf-bootcamp-2026/.gitignore
git -C ~/rf-bootcamp-2026 add .gitignore
git -C ~/rf-bootcamp-2026 commit -m "Ignore .env files"
```

{: .warning }
> **A committed API key is a leaked key.** GitHub indexes public repos. Even if you delete the key in a later commit, it remains in the history and can be found by automated scanners. Add `.env` to `.gitignore` before you ever create the file.

---

### Step 4 — Load in Python

In your JupyterHub notebook (with the Bootcamp 2026 kernel):

```python
from dotenv import load_dotenv
import os

load_dotenv('/path/to/your/day2/.env')   # reads .env, sets environment variables

print(os.getenv("OPENAI_API_KEY"))       # should print your key (keep this cell private)
print(os.getenv("OPENAI_BASE_URL"))
```

Or simply `load_dotenv()` (no path) to load `.env` from the current working directory.

---

### Step 5 — Initialize the Client

```python
import openai

client = openai.OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)
```

Notice: the key never appears in the code. The code is safe to commit. The `.env` file is not.

---

## 🔒 What Leaves Your Machine on Every API Call

Every time you call the API, the following is sent to Stanford's gateway:

- **Prompt text** — verbatim, including any data you paste in
- **API key** — sent as an HTTP header (never put it in the prompt itself)
- **Metadata** — timestamp, model name, token counts, your IP address
- **Model response** — returned and (at Stanford's end) logged

**Three-bucket rule** — before sending any data to an API, classify it:

| Bucket | Examples | Send via Stanford API? |
|--------|----------|----------------------|
| 🟢 **Public** | Published papers, open datasets | Yes |
| 🟡 **Restricted** | Unpublished research, proprietary data, IRB-approved data | Check your DUA/IRB first |
| 🔴 **PII** | Names, SSNs, health records, email addresses | No — never |

When in doubt: anonymize a test subset before sending real data through any API.

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="main"> Main Quest complete</label>

---

## 🧠 Skills Learned

- Load API keys from `.env` using `python-dotenv` — the key stays out of your code and out of git
- `.gitignore` is your first line of defense against accidental credential exposure
- Everything you send through the Stanford AI Playground is logged — classify your data before calling the API
