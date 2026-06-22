---
layout: default
title: "The Grand Hall"
parent: "Day 4 — The GPU Fortress"
nav_order: 6
permalink: /day4/grand-hall/
---

# The Grand Hall

<div data-room-id="d4-grand-hall"></div>

*The throne room of the fortress. Iron torches line walls carved with warnings and permissions. Three great stone tablets dominate the far end of the chamber — each one a verdict on every dataset you will ever touch. These are not bureaucratic suggestions. They are load-bearing laws. Misplace a dataset and your entire pipeline is built on cracked ground. Place it correctly and you can construct anything — fast, fearless, and defensible.*

---

## 🗡️ Main Quest

Every quest in this hall begins with one question: what kind of data are you carrying?

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

## 🧠 Skills Learned

- You can instantly classify any dataset into the three buckets — public, restricted, or PII — and choose the right tool without second-guessing yourself
- You can explain exactly what leaves the Yens and when, so no data ever moves somewhere it shouldn't
- You know when Ollama is the only safe choice — and why that's a feature, not a compromise
- You can read your IRB protocol and DUA with a critical eye and catch any clause that would block a cloud LLM pipeline before you build it
