---
layout: default
title: "The Key Vault"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 5
permalink: /day2/key-vault/
---

# The Key Vault

<div data-room-id="d2-key-vault"></div>

An API key is a credential, and a credential left in the open is a liability. Scribbled into a script, committed to a repo, or pasted into a chat, it can be copied by anyone who finds it and used to spend your budget or act in your name. This vault teaches the discipline that prevents that: load Stanford's AI API Gateway key from a `.env` file, keep that file out of git, and know exactly what each call sends before you make your first authenticated request.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Load the Stanford AI API Gateway key from a `.env` file, add `.env` to `.gitignore`, and make your first authenticated API call.

---

### Step 1: Why a `.env` File?

Before you touch the shared key, a quick gut check. You'll initialize the client the same way you did in the Stanford AI Playground room. What happens if you paste the real key straight into that code?

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-stanford-abc123",   # the real key, pasted right into your code
    base_url="https://aiapi-prod.stanford.edu/v1",
)
```

Ask yourself:
- Where does this script go next? (A `git push`. A Slack message. A Claude Code chat window you paste code into for help.)
- If you delete that `api_key` line in your next commit, is the key actually gone?
- If a labmate wants to run your script with their own key, what do they have to edit in your code?

Every one of those questions should worry you a little. That's the whole reason `.env` files exist: the secret lives in one file, off to the side, that never gets committed, shared, or pasted anywhere. Your code asks for the key by name at runtime. It never contains the key itself.

{: .note }
> **Wait, "environment" again?** In the Venv Forge, you built a **virtual environment**: a folder of isolated Python packages. A `.env` file is a completely different thing: a text file of **environment variables**, key/value pairs like `STANFORD_API_KEY=...`, that your shell or script can read at runtime. Same word, two unrelated ideas. A virtual environment isolates *packages*. An environment variable holds a *value* (usually a secret or config setting) that your code reads without hardcoding it.

---

### Step 2: Look at the Shared Key

The bootcamp API key lives in a shared file on the Yens. Take a look:

```bash
cat /scratch/shared/gsb-research-computing-ai-skills/.env
```

You'll see something like:

```
STANFORD_API_KEY=sk-stanford-...
```

Do not copy this file anywhere public. Do not commit it to git. You are about to load it safely.

---

### Step 3: Create Your Own `.env`

In your `day2/` directory:

```bash
cd ~/gsb-research-computing-ai-skills/day2
touch .env
```

Open `.env` and add the key you saw above:

```
STANFORD_API_KEY=sk-stanford-...
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

You should see your key line: `STANFORD_API_KEY=...`. If the file is missing or empty, check `pwd` to confirm you're in `~/gsb-research-computing-ai-skills/day2`, then redo Step 3.

</details>

---

### Step 4: Add `.env` to `.gitignore`

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

### Step 5: Load in Python

In your JupyterHub notebook (with the Bootcamp 2026 kernel), running from your `day2/` folder:

```python
from dotenv import load_dotenv
import os

load_dotenv()   # reads .env from the current folder, sets environment variables

print(os.getenv("STANFORD_API_KEY"))   # should print your key (keep this cell private)
```

`load_dotenv()` looks in the current working directory, so run the notebook from `day2/` where you created `.env`. To load one elsewhere, pass a relative path, e.g. `load_dotenv("../.env")`.

{: .note }
> 💡 **Environment variables aren't only the ones you set.** They're a shared pool of key/value settings that the operating system and your shell fill in automatically so programs know how to behave: `PATH` (where the shell looks for commands), `HOME` (your home directory), `USER`, `LANG`, and dozens more. `load_dotenv()` simply adds your `.env` entries into that same pool for this process, which is why `os.getenv("STANFORD_API_KEY")` now returns a value.
>
> See the whole pool for yourself:
>
> ```python
> dict(os.environ)   # every variable currently set in this process
> ```
>
> You'll find far more than you added, including the `STANFORD_API_KEY` you just loaded. That is also the caution: this output contains secrets and machine paths, so keep the cell private, and never paste it into a chat or commit it.

---

### Step 6: Initialize the Client

```python
import openai

client = openai.OpenAI(
    api_key=os.environ["STANFORD_API_KEY"],          # the secret, loaded from .env
    base_url="https://aiapi-prod.stanford.edu/v1",   # public endpoint, safe to hardcode
)
```

Notice: only the secret key comes from `.env`. The base URL is public, so it's fine to hardcode. The key never appears in the code, so your code is safe to commit; the `.env` file is not.

**The standard OpenAI created.** OpenAI's Python SDK (the `openai` package) is built around one request/response shape: you send a `model` and a list of `messages`, and get back `choices[0].message.content`. Because OpenAI's API arrived early and caught on, most other providers now implement that *same* shape, an "OpenAI-compatible" endpoint. The single setting that decides *which* service you're talking to is the **`base_url`**: the web address the client sends every request to. Point it at a different endpoint and the same code talks to a different service. You swap the `api_key` (and sometimes the `model`) to match, but your prompts and parsing never change.

<svg viewBox="0 0 760 420" role="img" aria-labelledby="sdk-std-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:760px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="sdk-std-title">One OpenAI-compatible client reaches many services. The same client.chat.completions.create call routes to the Stanford gateway, a local model on the Yens, or a commercial vendor's API. The base_url is the address that decides which service; changing it, plus the key and model, is the only difference.</title>
  <defs>
    <marker id="sdk-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- client -->
  <rect x="150" y="18" width="460" height="86" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="380" y="50" text-anchor="middle" font-size="16" font-weight="700" fill="#2c3e50">🧩  one openai client, one request shape</text>
  <text x="380" y="78" text-anchor="middle" font-size="12.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">client.chat.completions.create(model=…, messages=…)</text>

  <!-- fan-out -->
  <line x1="380" y1="104" x2="380" y2="176" stroke="#556a95" stroke-width="2.5"/>
  <text x="380" y="130" text-anchor="middle" font-size="13" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">the <tspan fill="#b3611a">base_url</tspan> chooses the service</text>
  <line x1="130" y1="176" x2="630" y2="176" stroke="#556a95" stroke-width="2.5"/>
  <line x1="130" y1="176" x2="130" y2="244" stroke="#556a95" stroke-width="2.5" marker-end="url(#sdk-ah)"/>
  <line x1="380" y1="176" x2="380" y2="244" stroke="#556a95" stroke-width="2.5" marker-end="url(#sdk-ah)"/>
  <line x1="630" y1="176" x2="630" y2="244" stroke="#556a95" stroke-width="2.5" marker-end="url(#sdk-ah)"/>

  <!-- Stanford gateway -->
  <rect x="25" y="246" width="210" height="150" rx="12" fill="#fbe9cf" stroke="#dcae6a" stroke-width="1.5"/>
  <text x="130" y="276" text-anchor="middle" font-size="14.5" font-weight="700" fill="#2c3e50">🛡️  Stanford gateway</text>
  <text x="130" y="300" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.5" fill="#8a94a6">BASE_URL</text>
  <rect x="35" y="308" width="190" height="26" rx="6" fill="#ffffff" stroke="#dcae6a" stroke-width="1.2"/>
  <text x="130" y="325" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#b3611a">aiapi-prod.stanford.edu/v1</text>
  <text x="130" y="358" text-anchor="middle" font-size="12.5" fill="#6a7280">Gemini, Claude, …</text>
  <text x="130" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">inside Stanford's perimeter</text>

  <!-- local model -->
  <rect x="275" y="246" width="210" height="150" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="380" y="276" text-anchor="middle" font-size="14.5" font-weight="700" fill="#2c3e50">💻  a local model</text>
  <text x="380" y="300" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.5" fill="#8a94a6">BASE_URL</text>
  <rect x="285" y="308" width="190" height="26" rx="6" fill="#ffffff" stroke="#bcd4f2" stroke-width="1.2"/>
  <text x="380" y="325" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2f6fb0">localhost:11434/v1</text>
  <text x="380" y="358" text-anchor="middle" font-size="12.5" fill="#6a7280">Ollama, vLLM</text>
  <text x="380" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">runs on the Yens (Day 4)</text>

  <!-- vendor api -->
  <rect x="525" y="246" width="210" height="150" rx="12" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="630" y="276" text-anchor="middle" font-size="14.5" font-weight="700" fill="#2c3e50">🌐  a vendor's API</text>
  <text x="630" y="300" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.5" fill="#8a94a6">BASE_URL</text>
  <rect x="535" y="308" width="190" height="26" rx="6" fill="#ffffff" stroke="#d5d8e2" stroke-width="1.2"/>
  <text x="630" y="325" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">api.openai.com/v1</text>
  <text x="630" y="358" text-anchor="middle" font-size="12.5" fill="#6a7280">GPT, …</text>
  <text x="630" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">commercial terms</text>
</svg>

That is why swapping to a local model on Day 4 is a one-line change.

---

## 💬 Class Brainstorm: What Else Goes in a `.env`?

You just used `.env` for one secret: your API key. But the pattern fits anything you don't want hardcoded, committed, or pasted around. As a class, brainstorm what else you might keep in a `.env` for your own research, and why each one belongs there instead of in your code.

<details markdown="1">
<summary>Starter ideas</summary>

- Other **API keys and tokens** (a second model provider, a data vendor, a GitHub token)
- **Database credentials** (host, user, password) for a lab database
- **Cloud credentials** (AWS or GCP keys) for storage or compute
- **Machine-specific paths** (where your data lives on the Yens versus on your laptop)
- **Config that changes per environment** (a `DEBUG` flag, a batch size, an output directory)

</details>

*(What each API call sends, and how to classify the data you send, is the whole focus of [The Crucible](../human-vs-llm/) later today.)*

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="main"> Main Quest complete</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest: Search for Leaked Keys**

The warning above says GitHub indexes public repos and automated scanners find leaked keys. See it for yourself: use [GitHub code search](https://github.com/search) to look up a well-known leaked-key pattern, like `AKIA` (an AWS access key prefix) or a generic `sk-` prefix. Don't open, save, clone, or use anything you find. Just note how many public results come back. This is exactly what those scanners are doing at scale, all day, every day.

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side1"> I searched GitHub for a leaked-key pattern and saw how many public results turned up</label>

**Side quest: Prove Git Never Forgets**

In a throwaway scratch repo (not this one), commit a fake `.env` containing a made-up key like `STANFORD_API_KEY=sk-fake-1234`. Delete the file in a second commit. Now run:

```bash
git log --all --full-history -- .env
git show <first-commit-hash>:.env
```

The key is still there, sitting in the first commit, even though the file is gone from your working directory. Deleting a file removes it from the latest snapshot. It does not remove it from history.

<label class="quest-check"><input type="checkbox" data-room="d2-key-vault" data-key="side2"> I committed a fake key, deleted it, and found it still recoverable from git history</label>

---

## 🧠 Skills Learned

- Load secrets from `.env` using `python-dotenv`, which keeps them out of your code and out of git
- `.gitignore` is your first line of defense against accidental credential exposure
- Public config (like a `base_url`) can be hardcoded; only true secrets belong in `.env`
- The `openai` client is a de facto standard: point `base_url` at any OpenAI-compatible service and the same code works
