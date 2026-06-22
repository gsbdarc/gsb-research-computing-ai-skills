---
layout: default
title: "The Grand Hall"
parent: "Day 4 — The GPU Fortress"
nav_order: 6
permalink: /day4/grand-hall/
---

# The Grand Hall

<div data-room-id="d4-grand-hall"></div>

*The throne room of the fortress. Here, the laws of the dungeon are etched into stone. Not arbitrary laws — practical ones. Every dataset you will ever work with belongs to one of three buckets. Misplace it and the research is compromised. Place it correctly and you can build anything on top of it, confidently.*

---

## Main Quest

{: .important }
> **Quest:** Apply the three-bucket privacy rule to a set of real research scenarios, then classify your own Day 3 pipeline's data.

This is a discussion block with a short exercise.

**The three-bucket rule (full depth — Day 2 was the preview):**

| Bucket | Definition | Can it go to a cloud LLM? | Can it go to Ollama? |
|--------|-----------|--------------------------|----------------------|
| **Public** | Published papers, public SEC filings, open-source datasets, anything already on the web | Yes, freely | Yes |
| **Restricted** | Unpublished research, proprietary data, licensed datasets with DUAs, financial data under NDA | Check your DUA — often no | Usually yes, confirm with your PI |
| **PII** | Names, emails, SSNs, dates of birth, medical records, anything that can identify a specific person | No — full stop | Depends on IRB protocol — ask |

**What leaves the Yens:**

- Stanford AI Playground → stays within Stanford's contracted perimeter with OpenAI
- Ollama (local) → nothing leaves the Yens at all
- Any other cloud API → your prompt text reaches that company's servers

**IRB and DUA considerations:**

- IRB protocols sometimes explicitly permit or prohibit sharing data with specific vendors — check yours
- Data Use Agreements often restrict where data can be processed — "Stanford systems" may or may not include cloud APIs
- When in doubt: local Ollama is always safe; ask your IRB coordinator before sending to any cloud API

**Exercise — classify your Day 3 dataset:**

The SEC Form 3 filings you processed were:
- Downloaded from EDGAR (the SEC's public database)
- Names and roles of corporate insiders, publicly filed
- Bucket: **Public** → cloud LLM: ✅

Now classify two of your own datasets from your research. For each: which bucket? which tool?

<label class="quest-check"><input type="checkbox" data-room="d4-grand-hall" data-key="main"> Grand Hall complete — I can apply the 3-bucket rule to my own research data</label>

---

## Skills Learned

- Apply the three-bucket classification (public / restricted / PII) to any dataset
- Understand the difference between "Stanford data perimeter" and "local on the Yens"
- Know when Ollama is required instead of the Playground (restricted data, PII under some protocols)
- Know to check your IRB protocol and DUA before building any LLM pipeline on research data
