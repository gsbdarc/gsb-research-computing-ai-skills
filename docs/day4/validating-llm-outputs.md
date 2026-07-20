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

[**Humanity's Last Exam**](https://artificialanalysis.ai/evaluations/humanitys-last-exam) is a 3,000-question benchmark built from expert questions that frontier models *can't* answer. Even the best model tops out around 53% — the strongest AI available still gets about half of them wrong.

![Bar chart of Humanity's Last Exam scores by model: the top model scores about 53%, most frontier models sit in the 40s, and many score far lower.]({{ site.baseurl }}/assets/images/humanitys-last-exam.png)

*Source: [Artificial Analysis — Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam).*

Capability is also uneven — the same models score about 94% on GPQA Diamond (graduate-level science). But even 94% is a 6% failure rate: fine for some uses, catastrophic for others. The question isn't "is the model accurate?" but "accurate enough *for this*?" — which you can only answer by measuring your own error rate.

Your extraction job isn't an exam, but the lesson holds: across a batch of filings, the model will nail most and quietly get some wrong. The rest of this page walks through some typical failure modes — and how to build in checks and resilience to try to catch them before they reach your results.

---

## LLM Failure Modes

LLMs fail in a handful of characteristic ways. A few you'll want to watch for:

### 1. Hallucination

The most notorious failure mode is **hallucination**: the model produces fluent, confident, plausible-looking output that is simply false — and nothing in the output itself flags it. In high-stakes settings, that can be professionally consequential.

{: .note }
> **Real-world case:** in 2024, Stanford misinformation expert Jeff Hancock submitted expert testimony citing journal articles that ChatGPT had invented, and the court [threw it out](https://minnesotareformer.com/2024/12/02/misinformation-expert-used-ai-to-draft-testimony-containing-misinformation-about-ai/). (Lawyers have been sanctioned for the same thing.)
>
> ![Minnesota Reformer headline: "Misinformation expert used AI to draft testimony containing misinformation about AI"]({{ site.baseurl }}/assets/images/hancock-ai-testimony-headline.png)
>
> *Source: [Minnesota Reformer](https://minnesotareformer.com/2024/12/02/misinformation-expert-used-ai-to-draft-testimony-containing-misinformation-about-ai/).*

For your work the lesson is concrete: ask an LLM to extract a value and it may hand back a confident, well-formatted answer that's wrong — with no error and no warning. That's precisely what validation is for.

**Guarding against it:** don't take outputs at face value — spot-check a sample against the source documents, add format/type checks (e.g. Pydantic) to catch malformed answers, and for high-stakes fields have the model quote the exact text that supports each answer so you can verify it.

### 2. Irreversibility {#irreversibility}

The stakes rise sharply when an LLM's output *drives an action* — writing to a database, sending emails, deleting files. LLMs make mistakes, and mistakes that change state are the most expensive kind: you often can't undo them.

Recall from [Day 1](../../day1/command-spire/) that `rm` deletes permanently — no trash, no undo; an agent runs the same commands, just without a human pausing to reconsider. Agents run with *your* full permissions, so "clean up this folder" can reach anything you can.

{: .note }
> **Real-world case:** in early 2026 a user asked Claude to organize a desktop, and it deleted a folder holding roughly 15 years of family photos — thousands of files — with terminal commands that bypassed the Trash entirely.
>
> ![Futurism headline: Blundering Husband Asks Claude AI to Organize Wife's PC, Accidentally Erases Her Cherished Family Photos]({{ site.baseurl }}/assets/images/claude-family-photos-headline.png)
>
> *Source: [Futurism](https://futurism.com/artificial-intelligence/claude-wife-photos).*

**Guarding against it:** the reliable defense is "least privilege": giving the agent only the access it truly needs (read-only where possible; scoped, minimal credentials), and requiring confirmation for anything that changes state. Keep automated pipelines read-only where you can; for writes, log the intended action first, act second, and verify before committing — and build a **dry-run mode** that prints what *would* happen without doing it.

### 3. Prompt Injection

Your input data isn't always trustworthy. A document you feed the model can contain adversarial text — for example, "Ignore all previous instructions and…" — that hijacks its behavior, making it do something other than the task you intended. Data scraped from the public web is especially risky.

**Guarding against it:** keeping your instructions in the system message and untrusted data in a separate user message helps — models are trained to prioritize system instructions — but it's a *partial* mitigation, not a hard boundary: to the model it's all just text, and a determined injection can still get through. So lean on the real backstops: **validate the output** before you rely on it, and apply least privilege (see [Irreversibility](#irreversibility) above) — assume the model can be manipulated, and make sure it simply *can't* take a harmful action.

### 4. Runaway Loops

An automated pipeline that retries on failure with no cap can retry forever — until it times out or burns through your API budget. A step that calls itself with no stopping condition can fan out exponentially.

**Guarding against it:** cap everything — a `max_retries` on each retry loop, a spend/budget limit on the whole job, and a sanity timeout. Log each iteration, and if a job runs well past its expected time, kill it and investigate.

---

<p style="color:#cc0000; font-weight:700; margin:1.5rem 0;">🚧 TODO: add the validation rules of thumb (spot-checking, comparing across models, format sanity checks); see the OWASP mapping in <code>TODO.md</code> for any further failure modes.</p>
