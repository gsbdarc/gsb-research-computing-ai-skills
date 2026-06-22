---
layout: default
title: "The Ledger"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 9
permalink: /day2/ledger/
---

# The Ledger

<div data-room-id="d2-ledger"></div>

*Every Oracle consultation has a price. The Ledger records what was spent, what was gained, and whether the expense was justified. Most researchers reach for the Oracle when `grep` would have answered in a millisecond for free. The Ledger asks: did you need magic, or did you just want it?*

---

## Main Quest

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

## Skills Learned

- Estimate API cost for any dataset size before running (tokens × rate × count)
- Apply the "regex first, LLM second" decision rule
- Understand that cheap models are often good enough for structured extraction tasks
- Know that cost scales with both input length and dataset size — always calculate before you batch
