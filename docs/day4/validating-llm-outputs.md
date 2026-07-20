---
layout: default
title: "Validating LLM Outputs"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 6
permalink: /day4/validating-llm-outputs/
---

# Validating LLM Outputs

LLMs are remarkable tools — but they are also **brittle**. Even the best models get things wrong, often confidently, and often enough to matter. Before you trust an LLM's output — especially at scale (thousands of filings, for example) — you need a way to check it.

How brittle? Look at how the frontier models do on a genuinely hard benchmark.

---

## Even the Best Models Fail

[**Humanity's Last Exam**](https://artificialanalysis.ai/evaluations/humanitys-last-exam) is a 3,000-question benchmark built from expert questions that frontier models *can't* answer. Even the best model tops out around **53%** — the strongest AI available still gets about half of them wrong.

![Bar chart of Humanity's Last Exam scores by model: the top model scores about 53%, most frontier models sit in the 40s, and many score far lower.]({{ site.baseurl }}/assets/images/humanitys-last-exam.png)

*Source: [Artificial Analysis — Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam).*

Capability is also uneven — the same models score about **94%** on GPQA Diamond (graduate-level science). But even 94% is a **6% failure rate**: fine for some uses, catastrophic for others (a commercial aircraft must fail far less often). The question isn't "is the model accurate?" but "accurate enough *for this*?" — which you can only answer by measuring your own error rate.

Your extraction job isn't an exam, but the lesson holds: across a batch of filings, the model will nail most and quietly get some wrong. The rest of this section is how to catch those.

---

## LLM Failure Modes

LLMs fail in a handful of characteristic ways. The one you're most likely to hit:

### Hallucination

The most notorious failure mode is **hallucination**: the model produces fluent, confident, plausible-looking output that is simply false — and nothing in the output itself flags it.

{: .note }
> It isn't malfunctioning: a [2025 analysis from OpenAI](https://arxiv.org/abs/2509.04664) argues models hallucinate because training and evaluation reward *guessing* over admitting uncertainty — so a confident wrong answer tends to score better than "I don't know."

The textbook symptom is **fabricated citations** — references with plausible authors, titles, journals, even DOIs, that simply don't exist. A memorable real-world case: in late 2024, Stanford misinformation expert **Jeff Hancock** filed an expert declaration defending Minnesota's deepfake law that cited journal articles which don't exist — invented by ChatGPT. The court [rejected his testimony](https://minnesotareformer.com/2024/12/02/misinformation-expert-used-ai-to-draft-testimony-containing-misinformation-about-ai/), the judge noting the irony that an AI expert was undone by the very technology he studies. (Lawyers have been sanctioned for the same thing.)

For your work the lesson is concrete: ask an LLM to extract a value and it may hand back a confident, well-formatted answer that's wrong — with no error and no warning. That's precisely what validation is for.

---

<p style="color:#cc0000; font-weight:700; margin:1.5rem 0;">🚧 TODO: add the validation rules of thumb (spot-checking, comparing across models, format sanity checks) and the remaining LLM failure modes — drawing on the OWASP Top 10 for LLMs (2025); see the mapping in <code>TODO.md</code>.</p>
