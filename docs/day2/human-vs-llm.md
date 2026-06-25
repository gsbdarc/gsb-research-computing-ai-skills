---
layout: default
title: "The Crucible"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 9
permalink: /day2/human-vs-llm/
---

# The Crucible

<div data-room-id="d2-human-vs-llm"></div>

*The room smells of both burnt silicon and human error — because both have been made here in equal measure. Mounted on the wall is a scale: on one side, a glowing terminal prompt; on the other, a stack of human-annotated outputs. Neither side is always right. The Alchemist who reaches for the LLM for every task is as reckless as the one who refuses it entirely. The Crucible is where you develop the judgment to know which is which — and the discipline to always, always look at your data before trusting either.*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Work through the decision framework — when does an LLM help, when does a human win, and when do you need to test carefully before trusting the output at scale?

This is a discussion block. No code. Bring your opinions.

---

### When LLMs shine

- **High-volume repetitive extraction** — process 10,000 filings at the cost of an hour instead of weeks
- **Unstructured → structured** — turn free-form text into typed, validated fields
- **First-pass drafts where a human reviews** — save time on generation, spend it on judgment
- **Good-enough at speed** — when the cost of an error is low and the cost of slowness is high

---

### When humans are better

- **Novel judgment calls** — the LLM generalizes from training data; your domain may have context it doesn't
- **One error is catastrophic** — medical triage, legal interpretation, IRB-governed decisions
- **Small datasets** — manual annotation of 50 records is often faster and cheaper than prompt engineering
- **Documented chain of custody** — some workflows require a human decision-maker on record

---

### When you need to test carefully first

- **Unfamiliar domains** — the model may hallucinate confidently in areas with thin training coverage
- **Invisible failure modes** — plausible-looking wrong answers are harder to catch than obvious errors
- **You're about to scale** — running 10,000 jobs with a broken prompt produces 10,000 broken results
- **The prompt or model changed** — even a small prompt tweak can shift behavior in unexpected ways

---

### Always look at your data

Before you trust any LLM pipeline at scale:

1. **Run it on 10–20 examples and read every output** — not just "does it work," but "does it make sense?"
2. **Look at the failures, not just the successes** — success rate hides where and how the model is wrong
3. **Compare against a human baseline on a small sample** — do you and the model agree? Where don't you?
4. **Ask: what would I miss if this output is wrong?** — the answer tells you how much validation you need

{: .note }
> **Class discussion:** Look at 5 outputs from your Oracle's Chamber run. Read them carefully.
> - Do the extracted names and roles look right?
> - What would it take to verify one of them manually?
> - If you ran this on 5,000 filings, how would you know if 3% were wrong?

---

### A practical rule of thumb

```
Volume × Cost of Error → Validation Depth

Low volume  + low stakes  → skim a few outputs
Low volume  + high stakes → review every output
High volume + low stakes  → spot-check 5%, automate a sanity check
High volume + high stakes → human-in-the-loop; never fully automate
```

<label class="quest-check"><input type="checkbox" data-room="d2-human-vs-llm" data-key="main"> Crucible complete — I can decide when to use an LLM and how much to trust its output</label>

---

## 🧠 Skills Learned

- You can classify any task into: LLM wins / human wins / needs careful testing
- You know that high volume × invisible errors = the most dangerous pipeline failure mode
- You will always spot-check outputs before scaling — not because you distrust the model, but because you've seen what happens when you don't
- You can design a validation step proportional to the stakes of the task
