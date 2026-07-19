---
layout: default
title: "LLM Failure Modes"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 7
permalink: /day4/trap-garden/
---

# LLM Failure Modes

<div data-room-id="d4-trap-garden"></div>

This is a discussion section — no hands-on. The goal is to name four LLM failure modes and a concrete defense for each, before they appear in your research pipeline.

---

**Failure Mode 1 — Hallucination at Scale**

A single LLM call might hallucinate a number, a citation, or a fact. A loop running 10,000 times propagates that error 10,000 times. Your output CSV looks complete and plausible — and 12% of the entries are fabricated.

**Defense:** Spot-check 5% of outputs manually. For high-stakes extractions, use Pydantic validation and require the model to cite the exact quote that supports its answer.

---

**Failure Mode 2 — Runaway Loops**

A pipeline that retries on failure with no cap will retry until it times out — or until it exhausts your API budget. A pipeline that calls itself recursively with no base case can fork exponentially.

**Defense:** Every loop gets a `max_retries` limit. Every job gets a budget cap. Log every iteration. If a job runs longer than 2× the expected time, cancel it and investigate.

---

**Failure Mode 3 — Prompt Injection**

An adversarial string in your input data — a document that contains "Ignore all previous instructions and…" — can redirect the model's behavior. Public web data is especially risky.

**Defense:** Never concatenate untrusted input directly into a system prompt. Use a separate user message. For public data: treat the model's output as untrusted until validated.

---

**Failure Mode 4 — Irreversibility**

A pipeline that writes to a database, sends emails, or deletes files takes actions that cannot be undone. LLMs make mistakes. Mistakes that modify state are the most expensive kind.

**Defense:** Prefer read-only operations in automated pipelines. For write operations: log first, act second, verify before committing. Build a dry-run mode that prints actions without executing them.

<label class="quest-check"><input type="checkbox" data-room="d4-trap-garden" data-key="main"> I can name 4 LLM failure modes and their defenses</label>

---

## What You Learned

- You can identify all four LLM failure modes — hallucination at scale, runaway loops, prompt injection, and irreversibility — before they appear in your pipeline
- You can pair each failure mode with a concrete, implementable defense you could add to a pipeline today
- You understand why automated pipelines demand more defensive design than one-off LLM calls
- You can recognize when a pipeline has crossed into automated territory — and know what extra safeguards that demands
