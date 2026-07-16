---
layout: default
title: "The Crucible"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 7
permalink: /day2/human-vs-llm/
---

# The Crucible

<div data-room-id="d2-human-vs-llm"></div>

*The room glows with the light of a dozen open terminals — some running Claude Code, some GitHub Copilot, some a local Ollama instance that doesn't know the internet exists. AI coding agents are everywhere now. At Stanford, they come with terms of service, data residency questions, and IRB implications that most tutorials never mention. The Crucible is where you build the judgment to use these tools well: knowing what they send, where it goes, and when the answer is "not with this data."*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Understand how AI coding agents work at Stanford — what they send, where it goes, and how to use them without compromising your research data.

This is a discussion block. No code. Bring your questions.

---

### What are AI coding agents?

AI coding tools — Claude Code, GitHub Copilot, Cursor, and similar — work by sending context from your editor to a remote model and returning suggestions. "Context" means:

- The file you're editing
- Nearby files the tool has indexed
- Your chat history in the current session
- Sometimes: terminal output, error messages, or clipboard content

That context leaves your machine on every keystroke or request, transmitted to the model provider's servers.

---

### AI coding tools at Stanford

Stanford's guidance on AI tools for research:

| Tool | Data leaves Stanford? | Appropriate for research data? |
|------|-----------------------|-------------------------------|
| Claude Code (Anthropic API) | Yes — to Anthropic servers | Public data only unless your DUA allows |
| GitHub Copilot (Stanford-licensed) | Yes — to GitHub/Azure | Check your DUA; disabled by default for private repos |
| Stanford AI Playground API | Stanford perimeter (contracted vendor) | Check your DUA; generally OK for non-PII research |
| Ollama (local, on Yens) | No — stays on the cluster | Safe for restricted data and PII |

**The practical rule:** If you wouldn't paste your data into a Google Doc, don't paste it into an AI coding agent context.

{: .note }
> **Class discussion:** You're using Claude Code to help write your SLURM job script. Your script references a path to a data file. Does the model see the data? What if your script has a hardcoded API key? What about a comment that mentions a patient's condition?

---

### Best practices for research

**Keep sensitive data out of agent context:**
- Never hardcode secrets, API keys, or file paths containing PII in files open in an AI tool
- Use `.env` files for credentials — and keep `.env` in `.gitignore`
- If a file contains restricted data, close it before using an AI coding assistant

**Be deliberate about what you index:**
- Most tools have a "workspace" or "project" setting that controls which files get indexed
- Exclude `data/`, `results/`, and any directory containing raw research data from the AI tool's workspace

**Model your agent use after your API use:**
- Same 3-bucket rule applies: public data → most tools fine; restricted data → local Ollama; PII → local only
- "I'm just asking for coding help" doesn't change where your data goes if it's in the context

---

### Data governance — know your data before you pick your tool

Every prompt you send leaves your machine. Know where it's going.

| Bucket | Examples | Stanford AI Playground | Ollama (local) | Third-party API |
|--------|----------|----------------------|----------------|-----------------|
| 🟢 **Public** | Published papers, SEC filings, open datasets | ✅ | ✅ | ✅ |
| 🟡 **Restricted** | Unpublished research, proprietary data, DUA-covered datasets | Check your DUA | Usually ✅ | Usually ❌ |
| 🔴 **PII** | Names, SSNs, health records, email addresses | ❌ — never | Depends on IRB | ❌ — never |

**What leaves the cluster on every API call:**
- **Stanford AI Playground** → prompt text flows through Stanford's contracted perimeter with the vendor. Logged. Do not send PII.
- **Ollama (local)** → nothing leaves the Yens. Weights run on the H200. Safe for restricted data.
- **Third-party API** → prompt text reaches the vendor's servers. Standard commercial terms apply.

**IRB and DUA:** Some data use agreements explicitly restrict where data can be processed. "Stanford systems" may or may not include cloud APIs — read yours before sending anything restricted. When in doubt: local Ollama is always the safe default.

{: .note }
> **Class discussion:** The SEC filings you're processing today — which bucket? Can they go to the Stanford AI Playground? What would change if they contained unreported insider PII?

---

### Designing defensible research pipelines

A pipeline is defensible when a skeptical colleague can audit it end-to-end. Before you scale:

1. **Classify your data** — which bucket? Which tool?
2. **Validate your outputs** — Pydantic schema + manual spot-check on 10–20 examples
3. **Document your decisions** — README: what the pipeline does, what model, what prompt version, what validation was run
4. **Keep humans in the loop for high-stakes steps** — extraction is fine to automate; acting on that extraction may not be

<label class="quest-check"><input type="checkbox" data-room="d2-human-vs-llm" data-key="main"> Crucible complete — I understand what AI coding agents send, how to classify my data, and how to design a defensible pipeline</label>

---

## 🧠 Skills Learned

- You can describe what AI coding agents send to remote servers and what that means for research data
- You know how to configure AI tools to exclude sensitive data from their context
- You can classify any dataset into the three buckets and choose the right tool without guessing
- You can design a validation step proportional to the stakes of the task
- You can write a pipeline that a skeptical colleague could audit: classified data, documented decisions, outputs you actually read
