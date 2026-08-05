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

{: .important }
> 💳 **Treat an API key exactly like a credit card number.** The comparison is close enough to be useful in every direction:
>
> | A credit card number | An API key |
> |----------------------|------------|
> | Anyone holding it can spend your money | Anyone holding it can spend your budget |
> | It identifies *you*, so charges trace back to you | It identifies *you*, so every call is logged against you |
> | You don't email it, print it in a report, or read it aloud | You don't commit it, paste it in Slack, or print it in a notebook |
> | Leaked? You cancel it and get a new number | Leaked? You revoke it and request a new key |
>
> You already have solid instincts about credit card numbers. This room is about applying those same instincts to a string of characters that doesn't *look* dangerous.

Before you touch the shared key, a quick gut check. You'll initialize the client the same way you did in the Stanford AI Playground room. What happens if you paste the real key straight into that code?

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-stanford-abc123",   # the real key, pasted right into your code
    base_url="https://aiapi-prod.stanford.edu/v1",
)
```

Ask yourself three questions:

**1. Where does this file go from here?** Almost nothing stays on one machine. This script gets pushed to GitHub, pasted into Slack when you ask a colleague why it's failing, dropped into a Claude Code window for help debugging, copied into a notebook, attached to an email. **The key is inside the file, so it travels everywhere the file travels** — and you stop being able to name everyone who has a copy.

**2. If you delete that line tomorrow, is the key gone?** Not if you already committed it. Git keeps your history on purpose, so the key sits in that old commit for anyone who looks. Deleting it going forward hides it from the current version of the file and from nobody else.

**3. What does a labmate have to change to run this with their own key?** Your source code. They have to edit your program to use their credential, which means the key isn't configuration — it's tangled into the logic, and now there are two slightly different copies of your script in the world.

Every one of those questions should worry you a little. That's the whole reason `.env` files exist: the secret lives in one file, off to the side, that never gets committed, shared, or pasted anywhere. Your code asks for the key by name at runtime. It never contains the key itself.

{: .note }
> **Wait, "environment" again?** In the Venv Forge, you built a **virtual environment**: a folder of isolated Python packages. A `.env` file is a completely different thing: a text file of **environment variables**, key/value pairs like `STANFORD_API_KEY=...`, that your shell or script can read at runtime. Same word, two unrelated ideas. A virtual environment isolates *packages*. An environment variable holds a *value* (usually a secret or config setting) that your code reads without hardcoding it.

---

### Step 2: Look at the Shared Key

The shared API key for this course lives in a file on the Yens. Take a look:

```bash
cat /scratch/shared/gsb-research-computing-ai-skills/.env
```

You'll see something like:

```
STANFORD_API_KEY=sk-stanford-...
```

That file is **shared** — every one of you is looking at the same copy, so leave it exactly as it is. You're about to take your own copy and load it safely.

---

### Step 3: Copy the Key into Your Repo

Your copy goes at the **root of your repo** — one `.env` for the whole project, found by everything you run this week:

```bash
cd ~/gsb-research-computing-ai-skills
cp /scratch/shared/gsb-research-computing-ai-skills/.env .env
```

Copy it rather than retyping it. An API key is 40-odd characters of deliberate gibberish, and a single transposed one gives you a `401 Unauthorized` two rooms from now that looks like a broken pipeline rather than a typo. `cp` cannot misread a character.

{: .note }
> 💡 **Why the root, and not `day2/`?** One key, one place. Notebooks in `day2/`, the scripts you'll run from the repo root in [The Oracle's Chamber](../oracles-chamber/), and the cluster jobs on Day 3 all need this same key. Keeping a copy per folder means keeping a secret in several places at once, and forgetting where they all are. Your `.gitignore` covers `.env` anywhere in the repo, so the root is both the most convenient spot and a safe one.

<details markdown="1">
<summary>Reminder: Confirm It Worked (click to reveal)</summary>

Files that start with a dot are hidden by default from a plain `ls`. This is the same trick from Day 1's Command Spire: add `-a` to reveal hidden files.

```bash
ls -a
```

You should see `.env` in the list. Now check the copy actually landed:

```bash
cat .env
```

You should see the key line: `STANFORD_API_KEY=...`. If the file is missing or empty, check `pwd` to confirm you're in `~/gsb-research-computing-ai-skills` (the repo root, not `day2/`), then redo the `cp`.

</details>

{: .note }
> 💡 **You now hold a copy of a shared secret**, which is the ordinary situation in a lab: one credential, several people, and each of you responsible for your own copy of it. Your copy is yours to protect. If it leaks, it isn't only your budget that gets revoked — it's everyone's, because it's the same key.

{: .note }
> 🟢 **Green sticky** = `.env` sits at my repo root and `cat .env` shows the `STANFORD_API_KEY=` line &nbsp;&nbsp; 🔴 **Red sticky** = the `cp` failed, or `.env` is missing or empty
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

### Step 4: Add `.env` to `.gitignore`

The `.env` file must never be committed to git. Add it now:

```bash
echo ".env" >> ~/.gitignore
# or, within your course repo:
echo ".env" >> ~/gsb-research-computing-ai-skills/.gitignore
git -C ~/gsb-research-computing-ai-skills add .gitignore
git -C ~/gsb-research-computing-ai-skills commit -m "Ignore .env files"
```

{: .warning }
> **A committed key is a leaked key.** Not "at risk of being leaked." Leaked.
>
> The moment you push, assume a stranger has it. Bots scan public commits on GitHub within seconds of them landing, and that is not an exaggeration for effect — it is a running, automated business.
>
> **Deleting the key in a later commit does not fix it.** Git keeps the old commit on purpose; the key is still sitting there in your history for anyone who looks.
>
> There is exactly one fix, and it is not editing a file: **revoke the key and get a new one.** Anything else is hoping nobody noticed.
>
> Which is why `.env` goes in `.gitignore` *before* the file exists — you are not tidying up, you are preventing a thing you cannot undo.

---

### Step 5: Load in Python

In your JupyterHub notebook (with the GSB AI 2026 kernel), running from your `day2/` folder:

```python
from dotenv import load_dotenv
import os

load_dotenv("../.env")   # this notebook lives in day2/, so step up one folder

key = os.getenv("STANFORD_API_KEY")


def mask(secret):
    """Show just enough to confirm it loaded, and nothing more."""
    if not secret:
        return "NOT FOUND — check the path to .env"
    return secret[:6] + "X" * (len(secret) - 6)


print(mask(key))   # sk-staXXXXXXXXXXXXXXXXXXXXXXXX
```

You want to answer one question here — *did the key load?* — and printing the whole thing answers it no better than printing the first six characters. The masked version confirms the plumbing works, tells you the length is plausible, and leaves nothing behind worth stealing.

{: .warning }
> 🖨️ **Never print a secret in a notebook.** A notebook doesn't just *show* you cell output, it **saves that output inside the `.ipynb` file**. So `print(key)` writes your live key into a file on disk — and that file is exactly the sort of thing you commit and push without thinking twice. `.gitignore` won't save you here, because it's your notebook that's leaking, not `.env`.
>
> Two habits that cost you nothing:
>
> - **Mask it**, as above, so the output is safe to save.
> - If you *did* print a secret, clear the evidence: **Cell → Current Outputs → Clear**, or *Kernel → Restart Kernel and Clear All Outputs*, then save. Do that **before** you commit, not after.

**Why `"../.env"` and not just `load_dotenv()`?** Called with no argument, `load_dotenv()` looks in the folder you're running *from*. Your notebook runs from `day2/`, and the `.env` you made is one level up at the repo root — so `../` is how you say "the folder above this one." This is the same `pwd` lesson from [The Path](../the-path/), showing up in Python instead of the shell: a relative path is always relative to where you are standing.

Scripts you run from the repo root need no argument at all, because there the plain `.env` is right beside them. You'll see exactly that in [The Oracle's Chamber](../oracles-chamber/).

{: .note }
> 🟢 **Green sticky** = my masked key printed, so `.env` is loading &nbsp;&nbsp; 🔴 **Red sticky** = I got `NOT FOUND` or an error
>
> Put a sticky note on your laptop lid so instructors can see where you are.

{: .note }
> 💡 **Environment variables aren't only the ones you set.** They're a shared pool of key/value settings that the operating system and your shell fill in automatically so programs know how to behave: `PATH` (where the shell looks for commands), `HOME` (your home directory), `USER`, `LANG`, and dozens more. `load_dotenv()` simply adds your `.env` entries into that same pool for this process, which is why `os.getenv("STANFORD_API_KEY")` now returns a value.
>
> See the pool for yourself — **names only, no values**:
>
> ```python
> sorted(os.environ)   # the names of every variable set in this process
> ```
>
> You'll find far more than you added, `STANFORD_API_KEY` now among them. Notice what that list tells you: the name is safe to look at, and the value is the part you protect. Asking for `dict(os.environ)` instead would print every value, secrets included, straight into your saved notebook — which is the mistake the warning above is about.

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
  <text x="130" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">under Stanford's agreement</text>

  <!-- local model -->
  <rect x="275" y="246" width="210" height="150" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="380" y="276" text-anchor="middle" font-size="14.5" font-weight="700" fill="#2c3e50">💻  a local model</text>
  <text x="380" y="300" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.5" fill="#8a94a6">BASE_URL</text>
  <rect x="285" y="308" width="190" height="26" rx="6" fill="#ffffff" stroke="#bcd4f2" stroke-width="1.2"/>
  <text x="380" y="325" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2f6fb0">localhost:11434/v1</text>
  <text x="380" y="358" text-anchor="middle" font-size="12.5" fill="#6a7280">Ollama, vLLM</text>
  <text x="380" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">runs on the Yens</text>

  <!-- vendor api -->
  <rect x="525" y="246" width="210" height="150" rx="12" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="630" y="276" text-anchor="middle" font-size="14.5" font-weight="700" fill="#2c3e50">🌐  a vendor's API</text>
  <text x="630" y="300" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.5" fill="#8a94a6">BASE_URL</text>
  <rect x="535" y="308" width="190" height="26" rx="6" fill="#ffffff" stroke="#d5d8e2" stroke-width="1.2"/>
  <text x="630" y="325" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">api.openai.com/v1</text>
  <text x="630" y="358" text-anchor="middle" font-size="12.5" fill="#6a7280">GPT, …</text>
  <text x="630" y="380" text-anchor="middle" font-size="11" fill="#8a94a6">commercial terms</text>
</svg>

That is why swapping to a model running locally on the Yens is a one-line change.

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

---

## 🧠 Skills Learned

- Load secrets from `.env` using `python-dotenv`, which keeps them out of your code and out of git
- `.gitignore` is your first line of defense against accidental credential exposure
- Public config (like a `base_url`) can be hardcoded; only true secrets belong in `.env`
- The `openai` client is a de facto standard: point `base_url` at any OpenAI-compatible service and the same code works
