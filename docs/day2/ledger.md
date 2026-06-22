---
layout: default
title: "The Ledger"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 9
permalink: /day2/ledger/
---

# The Ledger

<div data-room-id="d2-ledger"></div>

*The Oracle does not work for free. Every whispered answer drains a pouch of gold tokens — and the Alchemist's Ledger hangs on the wall as a reminder: the greatest researchers are not those who summon the Oracle most often, but those who know exactly when a humble `grep` blade is all they ever needed. Before you spend, you calculate. Before you cast, you ask: is this a spell — or just a pattern?*

---

## 🗡️ Main Quest

Before you unleash the Oracle on your dataset, step up to the Ledger. Every number on this parchment is a decision you get to make consciously rather than discover on your invoice.

{: .important }
> **Quest:** Develop intuition for LLM token costs and learn the decision rule for when to use an LLM vs. a simpler tool.

This is a discussion block. Work through the numbers together.

**Token cost basics:**

A token is roughly 0.75 words. The Stanford AI Playground shows costs per 1,000 input tokens and 1,000 output tokens for each model. Sample rates (check your Playground dashboard for current pricing):

| Model | Input / 1K tokens | Output / 1K tokens |
|-------|-------------------|---------------------|
| gpt-4o-mini | ~$0.00015 | ~$0.0006 |
| gpt-4o | ~$0.005 | ~$0.015 |
| claude-3-5-sonnet | ~$0.003 | ~$0.015 |

**The math for your pipeline:**

- 100 SEC filings, each ~2,000 words ≈ 2,700 tokens
- 100 filings × 2,700 tokens = 270,000 input tokens
- At gpt-4o-mini pricing: 270 × $0.00015 ≈ **$0.04**
- At gpt-4o pricing: 270 × $0.005 ≈ **$1.35**
- At 10,000 filings: **$4 vs. $135**

**The decision rule:**

> Use `grep` (or regex) first. Use an LLM only when the task requires understanding, not just pattern matching.

| Task | Right tool |
|------|-----------|
| Find all lines containing "Director" | `grep` |
| Extract a structured name from messy prose | LLM |
| Count files by extension | `ls \| wc -l` |
| Summarize a paragraph | LLM |
| Parse a consistent CSV column | Python/pandas |
| Extract a date from "as of the third Tuesday of last month" | LLM |

<label class="quest-check"><input type="checkbox" data-room="d2-ledger" data-key="main"> Ledger reviewed — I can estimate API cost for a dataset before running it</label>

---

## 🧠 Skills Learned

- You can now **estimate API cost for any dataset** before a single token is spent — tokens × rate × count, no surprises on the invoice
- You can **apply the "regex first, LLM second" rule** with confidence, reaching for the right tool instead of the most impressive one
- You know that **cheap models often match expensive ones** on structured extraction — power isn't always the answer
- You understand that **cost scales with both input length and dataset size**, so you calculate before you batch, every time
