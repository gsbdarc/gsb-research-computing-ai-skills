---
layout: default
title: "The Watchtower of Secrets"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 6
permalink: /day2/watchtower-of-secrets/
---

# The Watchtower of Secrets

<div data-room-id="d2-watchtower-of-secrets"></div>

*You climb the spiral stairs and step out onto the parapet. Wind. Clarity. From up here you can see everything that leaves the dungeon — every scroll launched into the cloud, every question breathed to the Oracle, every invisible HTTP packet slipping past the gate. Most researchers never bother climbing this high. They send their data into the dark and hope for the best. You are not most researchers.*

---

## 🗡️ Main Quest

Before you send a single byte to a cloud model, you need to know exactly what you're handing over — and to whom. Step up to the parapet and read what's written on the wind.

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

## 🧠 Skills Learned

- You can now name exactly what data leaves your machine on every LLM API call — no more black boxes
- You can sort any dataset into its bucket and know instantly whether it's safe to send to a cloud API
- You understand where the Stanford AI Playground's data perimeter ends and your own responsibility begins
- You have a pre-flight checklist burned into your workflow so you never launch a pipeline blind
