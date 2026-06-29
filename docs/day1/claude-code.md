---
layout: default
title: "The Archmage's Counsel"
parent: "Day 1 — The Gatehouse"
nav_order: 9
permalink: /day1/claude-code/
---

# The Archmage's Counsel

<div data-room-id="d1-claude-code"></div>

*At the top of the Repository tower, before the Boss Gate seals behind you, the Archmage is waiting. Not to give you the answer — to give you the question. "You have learned to move through the dungeon," he says. "Now I will show you the tool every researcher in this tower uses. It writes code fast. It reads your errors. It will save you hours." He pauses. "It will also fail you completely, if you forget who you are."*

---

## 🖊️ What Is Claude Code?

Claude Code is an AI coding assistant that runs in your terminal. Unlike a chat window in a browser, Claude Code works inside your actual project: it reads your files, sees your error messages, and can run commands in your repo directory.

At Stanford, **Claude Code is now officially approved for research use** as part of the Claude for Education program (launching June 30, 2026). All faculty, students, postdocs, and staff have access with a Stanford SUNet ID.

**Where can you run it?**
- **Locally** (your laptop) — the most common way; Claude Code sees your local files and any SSH sessions you have open
- **On the Yens** — SSH in, then run `claude` directly on the cluster; useful for files that live there and shouldn't leave
- **In VSCode** — VSCode with the SSH extension lets you edit files on the Yens in a proper IDE; Claude Code works inside VSCode's terminal too

**What it sends:** Every prompt you send — the files open in your session, recent terminal output, your chat — is transmitted to Anthropic's servers. This matters for research data.

| Data | Claude Code OK? |
|------|----------------|
| 🟢 Public (SEC filings, open datasets, published papers) | ✅ Yes |
| 🟡 Restricted (DUA-covered, unpublished research) | Check your DUA |
| 🔴 PHI | Requires Stanford AI API Gateway routing |

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Run Claude Code in your bootcamp repo and then discuss: what is your role vs the tool's role?

### Step 1 — Open Your Repo

On your local machine, navigate to your forked repo (the one you set up in The Repository):

```bash
cd rf-bootcamp-2026
```

### Step 2 — Run Claude Code locally

If Claude Code is installed (`claude --version` to check):

```bash
claude
```

Ask it something simple: *"What files are in this repo and what does each one do?"*

If you don't have it installed yet, open [claude.ai](https://claude.ai) and paste the same question with a file listing. Both work for today.

{: .note }
> **Install (Mac):** `npm install -g @anthropic-ai/claude-code` — you'll need Node.js first (`brew install node`).

---

### Step 3 — Run Claude Code on the Yens

Claude Code can also run directly on the cluster — useful when your data lives there and you don't want it leaving the Yens perimeter.

SSH in (if you aren't already), then:

```bash
claude
```

Ask it: *"What processes am I running on this server?"* or *"What is the output of `userload` telling me?"*

{: .note }
> Claude Code on the Yens sends your prompts to Anthropic servers over the internet — the compute runs remotely, not locally. For data that must stay within Stanford systems, use the Stanford AI API Gateway or Ollama (Day 4).

---

### Step 4 — Security: what to keep out of Claude's context

Before you use Claude Code habitually, internalize one rule:

**If the file is open in your session, Claude Code can see it.**

- Never open `.env` files or files with API keys in the same session you're using Claude Code
- Exclude `data/` and `results/` directories from Claude's context when working with restricted data
- Public data (SEC filings, published papers) → fine
- Restricted or PII data → use Ollama locally on the Yens (Day 4) or route through the Stanford AI API Gateway

The full data governance discussion happens in [The Crucible](/day2/human-vs-llm/) on Day 2.

---

### Step 5 — Class Discussion: Your Role vs the Tool's Role

*No typing. Put your hands in your lap.*

Claude Code is fast at syntax, boilerplate, and looking things up. What it cannot do:

- Decide whether your research question is well-posed
- Know if the output is correct for your specific data
- Catch when a pipeline produces plausible-but-wrong results at scale
- Defend your methodology to a reviewer

**The test:** If you can't explain what a piece of code does, you cannot trust the result. Running 10,000 filings through a pipeline you don't understand is how wrong numbers end up in a thesis.

**What makes you irreplaceable:**
- Domain knowledge — you know what the SEC filing is supposed to say
- Research judgment — you know when a result looks wrong
- The right question — Claude Code is only as good as what you ask it
- Validation — you are the one who checks 20 examples before scaling to 10,000

**Use Claude Code to move faster on the parts you understand — not to skip the understanding.**

{: .note }
> **Class discussion prompts:**
> - You ask Claude Code to write a SLURM job script. It writes one. How do you know it's correct?
> - Your extraction script produces 9,847 results out of 10,000 filings. Claude Code says "looks good." What do you do?
> - A colleague asks to reproduce your analysis. What does Claude Code know about your intent?

<label class="quest-check"><input type="checkbox" data-room="d1-claude-code" data-key="main"> Archmage's Counsel complete — I know what Claude Code sends, the Stanford data rules, and my role vs the tool's</label>

---

## 🧠 Skills Learned

- You know what Claude Code is and how to run it locally, in VSCode, and on the Yens
- You understand what context it sends and when that matters for research data
- You know what to keep out of Claude's session when working with restricted data
- You can articulate the boundary between what the tool does and what the researcher does — and why that boundary matters when results go to scale
