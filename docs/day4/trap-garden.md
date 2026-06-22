---
layout: default
title: "The Trap Garden"
parent: "Day 4 — The GPU Fortress"
nav_order: 7
permalink: /day4/trap-garden/
---

# The Trap Garden

<div data-room-id="d4-trap-garden"></div>

*A garden that looks harmless. Each flower is a feature: "the agent can browse the web," "the agent can edit files," "the agent can run code." Pick the wrong flower and the agent runs in a loop for three hours, bills you $400, and deletes the output directory. The Trap Garden teaches you to name the risks before you build.*

---

## Main Quest

{: .important }
> **Quest:** Name four LLM agent failure modes and a concrete defense for each — before they appear in your research pipeline.

This is a discussion block. No hands-on.

---

**Failure Mode 1 — Hallucination at Scale**

A single LLM call might hallucinate a number, a citation, or a fact. An agent loop running 10,000 times propagates that error 10,000 times. Your output CSV looks complete and plausible — and 12% of the entries are fabricated.

**Defense:** Spot-check 5% of outputs manually. For high-stakes extractions, use Pydantic validation and require the model to cite the exact quote that supports its answer.

---

**Failure Mode 2 — Runaway Loops**

An agent that retries on failure with no cap will retry until it times out — or until it exhausts your API budget. A pipeline that calls itself recursively with no base case can fork exponentially.

**Defense:** Every loop gets a `max_retries` limit. Every agent gets a budget cap. Log every iteration. If a job runs longer than 2× the expected time, cancel it and investigate.

---

**Failure Mode 3 — Prompt Injection**

An adversarial string in your input data — a document that contains "Ignore all previous instructions and…" — can redirect an agent's behavior. Public web data is especially risky.

**Defense:** Never concatenate untrusted input directly into a system prompt. Use a separate user message. For public data: treat the model's output as untrusted until validated.

---

**Failure Mode 4 — Irreversibility**

An agent that writes to a database, sends emails, or deletes files takes actions that cannot be undone. LLMs make mistakes. Mistakes that modify state are the most expensive kind.

**Defense:** Prefer read-only operations in automated pipelines. For write operations: log first, act second, verify before committing. Build a dry-run mode that prints actions without executing them.

<label class="quest-check"><input type="checkbox" data-room="d4-trap-garden" data-key="main"> Trap Garden complete — I can name 4 agent failure modes and their defenses</label>

---

## Skills Learned

- Name the four main LLM agent failure modes: hallucination at scale, runaway loops, prompt injection, irreversibility
- Apply a concrete defense to each before starting a new agentic pipeline
- Understand why automated pipelines require more defensive design than single-call scripts
- Know when a pipeline is "agentic" and therefore needs these extra considerations
