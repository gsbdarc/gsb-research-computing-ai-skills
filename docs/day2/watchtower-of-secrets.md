---
layout: default
title: "The Watchtower of Secrets"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 5
permalink: /day2/watchtower-of-secrets/
---

# The Watchtower of Secrets

<div data-room-id="d2-watchtower-of-secrets"></div>

*From the top of the tower you can see everything that leaves the dungeon. Every scroll sent out, every question whispered to the Oracle — it all passes through this parapet. Most researchers never climb up here. They should.*

---

## Main Quest

{: .important }
> **Quest:** Work through the security checklist as a class — no keyboard needed. Understand what leaves your machine every time you make an API call, and what the Stanford AI Playground guarantees vs. what it doesn't.

This is a discussion block. Follow along and annotate your own checklist.

**What leaves your machine on every API call:**

Every request to a cloud LLM includes:
- Your prompt text (verbatim)
- Your API key (in the HTTP header — never in the prompt)
- Metadata: timestamp, model name, token counts, your IP address
- The model's response

The API provider logs all of this. Stanford's agreement with OpenAI covers what they can do with it — but the data still leaves Stanford's infrastructure.

**The three-bucket rule (preview — we go deeper on Day 4):**

| Bucket | Examples | Can it go to a cloud API? |
|--------|----------|--------------------------|
| **Public** | Published papers, public filings, open datasets | Yes, freely |
| **Restricted** | Unpublished research data, proprietary datasets, IRB data | Check your DUA / IRB protocol |
| **PII** | Names, emails, SSNs, health data, anything that identifies a person | No — stop, consult your IRB |

**Pre-flight checklist — run through this before every new dataset:**

- [ ] Do I know which bucket this data belongs to?
- [ ] If restricted: does my DUA or IRB protocol allow sending it to a third-party API?
- [ ] If in doubt: can I anonymize or synthesize a safe test version first?
- [ ] Is my API key in `.env`, not in the script?
- [ ] Is `.env` in `.gitignore`?

<label class="quest-check"><input type="checkbox" data-room="d2-watchtower" data-key="main"> Security checklist reviewed</label>

---

## Skills Learned

- Know exactly what data leaves your machine on every LLM API call
- Apply the three-bucket rule to classify any dataset before sending it to a cloud API
- Understand what the Stanford AI Playground's data perimeter guarantees — and what it doesn't
- Have a pre-flight checklist to run before starting any new LLM-based research pipeline
