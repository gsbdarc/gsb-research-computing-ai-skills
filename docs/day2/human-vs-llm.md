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
> **Quest:** Understand how AI coding agents work at Stanford - What is the current working state of LLMs, How people are using them and How they handle your data

This is a discussion block. No code. Bring your questions.

---


### Models

A model reads language (and, increasingly, images) as **tokens**. A token is a chunk of text a little smaller than a word: as a rule of thumb, ~750 words (a short blog post or article) is about **1,000 tokens**, so one word is roughly 1.3 tokens. Models these days have context windows of a million tokens or more.

The **context window** is the maximum amount of context you can fit into the model at once. Whenever you ask a model something, its answer is shaped by two things: what it learned during training, and whatever is in the context window right now.

```text
   prompt + files + images
              │
              ▼   tokenized  (~750 words ≈ 1,000 tokens)
   ┌──────────────────────────────────┐
   │  CONTEXT WINDOW                   │
   │  up to ~1,000,000 tokens          │
   └──────────────────────────────────┘
              │
              ▼   + training knowledge (frozen when the model was built)
              │
              ▼
            answer
```

### What are AI coding agents?

AI coding tools (Claude Code, GitHub Copilot, Cursor, and similar) are **harnesses** wrapped around a model. They give the model the ability to read your files, run commands, and use other tools on your behalf, though the exact powers vary by tool. To do any of that, the harness gathers **context** from your machine, sends it to a remote model, and returns suggestions.

Here's the catch. In [The Oracle's Chamber](../oracles-chamber/) you built the `messages` yourself: you wrote the system prompt and the user prompt, so you knew *exactly* what the model received. A coding agent is not that tidy. It assembles the context for you, and that context can include:

- The file you're editing
- Nearby files the tool has indexed
- Your chat history in the current session
- Sometimes terminal output, error messages, or clipboard contents

You didn't hand-pick any of it. That context leaves your machine on each request (and, for autocomplete tools, as you pause while typing) and travels to the model provider's servers, often without you seeing exactly what was sent.

---

### AI services at Stanford

Stanford runs a growing catalog of AI services: chat interfaces, the API gateway you used today, cloud AI (AWS Bedrock, Azure OpenAI, Google Vertex), and locally hosted models. The list keeps changing, so browse the current one rather than memorize it: [Stanford AI Services](https://uit.stanford.edu/ai/services).

Before you pick one, separate two very different jobs. The data risk is not the same for each.

**Job 1: Using an LLM to analyze your data.** Your data *is* the input: you deliberately put it in the prompt, the way you fed filing text to the model in [The Oracle's Chamber](../oracles-chamber/). The question is direct: *is this data allowed to go where this model runs?* Classify the data on Stanford's risk scale, then choose the path:

- **Stanford AI Playground / API gateway:** approved for **every** Stanford risk level, Low, Moderate, and High Risk *including PHI*, because it runs inside Stanford's contracted perimeter. For real research data this is your default path. (A restrictive DUA can still narrow what you may send, so check yours.)
- **A local model on the Yens:** keeps everything on the cluster. Reach for it when a DUA says the data may not leave your own systems, or when you want no external dependency at all (you'll do this on Day 4).
- **A third-party tool or API** (ChatGPT, Claude direct to Anthropic, Copilot): *outside* Stanford's perimeter, so public or low-risk data only, unless it is separately approved.

The Stanford gateway is built to take all of it. The risk usually isn't the data, it's reaching for a convenient tool that sits outside Stanford's walls.

**Job 2: Using an LLM to build your pipeline.** Here a coding agent (Claude Code, Copilot, Cursor) writes code *with* you. Your data is not meant to be the input, but it can slip into the agent's context anyway: a data file left open, a hardcoded path or key, a comment quoting a real record. The risk isn't the dataset you chose to send; it's what the harness sweeps up around it, the context problem from the *What are AI coding agents?* section above. The next section keeps it in check.

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
- The same data rules apply: a coding agent that calls a third-party endpoint (Claude Code to Anthropic, Copilot to GitHub) sits outside Stanford's perimeter, so keep Moderate and High Risk data out of its context
- "I'm just asking for coding help" doesn't change where your data goes if it's in the context

---

### Data governance: know your data before you pick your tool

Every prompt you send leaves your machine unless the model runs locally. Classify your data on Stanford's risk scale first, then pick the tool.

| Risk level | Examples | Stanford AI Gateway | Local model (Yens) | Third-party tool/API |
|------------|----------|---------------------|--------------------|----------------------|
| 🟢 **Low** | Published papers, SEC filings, open datasets | ✅ | ✅ | ✅ |
| 🟡 **Moderate** | Unpublished research, FERPA records, DUA-covered data | ✅ | ✅ | ❌ unless separately approved |
| 🔴 **High (incl. PHI)** | SSNs, financial account numbers, health records, credentials | ✅ | ✅* | ❌ |

<small>*Running a local model adds no new exposure, but the data must already be permitted to live on the Yens.</small>

**Why the Stanford gateway clears every row:** it runs inside Stanford's contracted perimeter, under agreements that cover even PHI, so your prompt is handled under Stanford's terms rather than a vendor's consumer terms. That is exactly why Stanford stood it up.

**What each path does with your data:**
- **Stanford AI Gateway** → the prompt flows through Stanford's contracted perimeter and is logged. Approved across every risk level.
- **Local model (Yens)** → nothing leaves the cluster; the weights run on the H200. No new exposure beyond wherever the data already lives.
- **Third-party tool/API** → the prompt reaches the vendor under standard commercial terms. Low-risk or public data only, unless separately covered.

**DUA and IRB still govern.** A data use agreement or IRB protocol can be stricter than Stanford's classification (for example, "data may not leave these specific systems"). Read yours; when a DUA restricts where data can be processed, the local path on the Yens is the safe default.

{: .note }
> **Class discussion:** The SEC filings you're processing today, which risk level? They can clearly go through the Stanford gateway, but what changes if you switch to a third-party tool like ChatGPT? And if the filings contained unreported insider PII, which paths would still be allowed?

---

### Designing defensible research pipelines

A pipeline is defensible when a skeptical colleague can audit it end-to-end. Before you scale:

1. **Classify your data** — which risk level? Which tool?
2. **Validate your outputs** — Pydantic schema + manual spot-check on 10–20 examples
3. **Document your decisions** — README: what the pipeline does, what model, what prompt version, what validation was run
4. **Keep humans in the loop for high-stakes steps** — extraction is fine to automate; acting on that extraction may not be

<label class="quest-check"><input type="checkbox" data-room="d2-human-vs-llm" data-key="main"> Crucible complete — I understand what AI coding agents send, how to classify my data, and how to design a defensible pipeline</label>

---

## 🧠 Skills Learned

- You can describe what AI coding agents send to remote servers and what that means for research data
- You know how to configure AI tools to exclude sensitive data from their context
- You can classify any dataset by Stanford's risk level and choose the right tool without guessing
- You can design a validation step proportional to the stakes of the task
- You can write a pipeline that a skeptical colleague could audit: classified data, documented decisions, outputs you actually read
