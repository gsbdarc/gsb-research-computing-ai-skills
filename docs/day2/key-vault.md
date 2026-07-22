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

### Step 1 — Why a `.env` File?

Before you touch the shared key, a quick gut check. What happens if you just write this directly in your script?

```python
api_key = "sk-stanford-abc123"
```

Ask yourself:
- Where does this script go next? (A `git push`. A Slack message. A Claude Code chat window you paste code into for help.)
- If you delete this line in your next commit, is the key actually gone?
- If a labmate wants to run your script with their own key, what do they have to edit in your code?

Every one of those questions should worry you a little. That's the whole reason `.env` files exist: the secret lives in one file, off to the side, that never gets committed, shared, or pasted anywhere. Your code asks for the key by name at runtime. It never contains the key itself.

{: .note }
> **Wait, "environment" again?** In the Venv Forge, you built a **virtual environment**: a folder of isolated Python packages. A `.env` file is a completely different thing: a text file of **environment variables**, key/value pairs like `STANFORD_API_KEY=...`, that your shell or script can read at runtime. Same word, two unrelated ideas. A virtual environment isolates *packages*. An environment variable holds a *value* (usually a secret or config setting) that your code reads without hardcoding it.

---

### Step 2 — Look at the Shared Key

The bootcamp API key lives in a shared file on the Yens. Take a look:

```bash
cat /scratch/shared/gsb-research-computing-ai-skills/.env
```

You'll see something like:

```
STANFORD_API_KEY=sk-stanford-...
OPENAI_BASE_URL=https://aiapi-prod.stanford.edu/v1
```

Do not copy this file anywhere public. Do not commit it to git. You are about to load it safely.

---

### Step 3 — Create Your Own `.env`

In your `day2/` directory:

```bash
cd ~/day2
touch .env
```

Open `.env` and add the values you saw above:

```
STANFORD_API_KEY=sk-stanford-...
OPENAI_BASE_URL=https://aiapi-prod.stanford.edu/v1
```

<details markdown="1">
<summary>Reminder: Confirm It Worked (click to reveal)</summary>

Files that start with a dot are hidden by default from a plain `ls`. This is the same trick from Day 1's Command Spire: add `-a` to reveal hidden files.

```bash
ls -a
```

You should see `.env` in the list. Now check the contents actually saved:

```bash
cat .env
```

You should see your two lines: `STANFORD_API_KEY=...` and `OPENAI_BASE_URL=...`. If the file is missing or empty, check `pwd` to confirm you're in `~/day2`, then redo Step 3.

</details>

---

### Step 4 — Add `.env` to `.gitignore`

The `.env` file must never be committed to git. Add it now:

```bash
echo ".env" >> ~/.gitignore
# or, within your bootcamp repo:
echo ".env" >> ~/gsb-research-computing-ai-skills/.gitignore
git -C ~/gsb-research-computing-ai-skills add .gitignore
git -C ~/gsb-research-computing-ai-skills commit -m "Ignore .env files"
```

{: .warning }
> **A committed API key is a leaked key.** GitHub indexes public repos. Even if you delete the key in a later commit, it remains in the history and can be found by automated scanners. Add `.env` to `.gitignore` before you ever create the file.

---

### Step 5 — Load in Python

In your JupyterHub notebook (with the Bootcamp 2026 kernel):

```python
from dotenv import load_dotenv
import os

load_dotenv('/path/to/your/day2/.env')   # reads .env, sets environment variables

print(os.getenv("STANFORD_API_KEY"))       # should print your key (keep this cell private)
print(os.getenv("OPENAI_BASE_URL"))
```

Or simply `load_dotenv()` (no path) to load `.env` from the current working directory.

---

### Step 6 — Initialize the Client

```python
import openai

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],
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

**Classify before you send:** place any data on Stanford's risk scale before it goes to an API.

| Risk level | Examples | Send via Stanford API? |
|------------|----------|------------------------|
| 🟢 **Low** | Published papers, open datasets | Yes |
| 🟡 **Moderate** | Unpublished research, FERPA records, DUA-covered data | Yes, check your DUA/IRB |
| 🔴 **High (incl. PHI)** | SSNs, financial account numbers, health records | Yes, the gateway is approved for it (subject to your DUA) |

The Stanford gateway clears all three levels because it stays inside Stanford's perimeter. A **third-party** API (not Stanford's) is Low-risk or public data only. More on choosing paths in [The Crucible](../human-vs-llm/).

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="main"> Main Quest complete</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Search for Leaked Keys**

The warning above says GitHub indexes public repos and automated scanners find leaked keys. See it for yourself: use [GitHub code search](https://github.com/search) to look up a well-known leaked-key pattern, like `AKIA` (an AWS access key prefix) or a generic `sk-` prefix. Don't open, save, clone, or use anything you find. Just note how many public results come back. This is exactly what those scanners are doing at scale, all day, every day.

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side1"> I searched GitHub for a leaked-key pattern and saw how many public results turned up</label>

**Side quest — Prove Git Never Forgets**

In a throwaway scratch repo (not this one), commit a fake `.env` containing a made-up key like `STANFORD_API_KEY=sk-fake-1234`. Delete the file in a second commit. Now run:

```bash
git log --all --full-history -- .env
git show <first-commit-hash>:.env
```

The key is still there, sitting in the first commit, even though the file is gone from your working directory. Deleting a file removes it from the latest snapshot. It does not remove it from history.

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side2"> I committed a fake key, deleted it, and found it still recoverable from git history</label>

---

## 🧠 Skills Learned

- Load API keys from `.env` using `python-dotenv` — the key stays out of your code and out of git
- `.gitignore` is your first line of defense against accidental credential exposure
- Everything you send through the Stanford AI Playground is logged — classify your data before calling the API
