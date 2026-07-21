---
layout: default
title: "Handling LLM Failure Modes"
parent: "Day 4 — Parallelization & GPUs"
nav_order: 6
permalink: /day4/validating-llm-outputs/
---

# Handling LLM Failure Modes

<div data-room-id="d4-failure-modes"></div>

LLMs are remarkable tools — but they are also **brittle**. Even the best models get things wrong, often confidently, and often enough to matter. Before you trust an LLM's output — especially at scale (thousands of filings, for example) — you need a way to check it.

How brittle? Look at how the frontier models do on a genuinely hard benchmark.

---

## Even the Best Models Fail

[**Humanity's Last Exam**](https://artificialanalysis.ai/evaluations/humanitys-last-exam) is a 3,000-question benchmark built from expert questions that frontier models *can't* answer. Even the best model tops out around 53% — the strongest AI available still gets about half of them wrong.

![Bar chart of Humanity's Last Exam scores by model: the top model scores about 53%, most frontier models sit in the 40s, and many score far lower.]({{ site.baseurl }}/assets/images/humanitys-last-exam.png)

*Source: [Artificial Analysis — Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam).*

Capability is also uneven — the same models score about 94% on GPQA Diamond (graduate-level science). But even 94% is a 6% failure rate: fine for some uses, catastrophic for others. The question isn't "is the model accurate?" but "accurate enough *for this*?" — which you can only answer by measuring your own error rate.

Your extraction job isn't an exam, but the lesson holds: across a batch of filings, the model will nail most and quietly get some wrong. The rest of this page covers the failure modes to watch for, and how to build in checks to catch them before they reach your results.

---

## Hallucination

The most notorious failure mode is **hallucination**: the model produces fluent, confident, plausible-looking output that is simply false — and nothing in the output itself flags it. In high-stakes settings, that can be professionally consequential.

{: .note }
> **Real-world case:** in 2024, Stanford misinformation expert Jeff Hancock submitted expert testimony citing journal articles that ChatGPT had invented, and the court [threw it out](https://minnesotareformer.com/2024/12/02/misinformation-expert-used-ai-to-draft-testimony-containing-misinformation-about-ai/). (Lawyers have been sanctioned for the same thing.)
>
> ![Minnesota Reformer headline: "Misinformation expert used AI to draft testimony containing misinformation about AI"]({{ site.baseurl }}/assets/images/hancock-ai-testimony-headline.png)
>
> *Source: [Minnesota Reformer](https://minnesotareformer.com/2024/12/02/misinformation-expert-used-ai-to-draft-testimony-containing-misinformation-about-ai/).*

The deeper issue is "calibration": the model doesn't reliably signal when it's unsure, so a confident tone tells you nothing about whether the answer is right. You usually have to gauge that uncertainty *externally* — which is what the next section is about.

For your work the lesson is concrete: ask an LLM to extract a value and it may hand back a confident, well-formatted answer that's wrong — with no error and no warning.

---

## Validating Outputs at Scale

Because the model won't flag its own mistakes, you have to check correctness *externally* — cheaply enough to do it across a whole batch. A few complementary techniques:

- **Spot-check a sample against the source.** Pull a random handful of outputs, compare them to the original filings by hand, and estimate your error rate. That number — not a benchmark headline — tells you whether the pipeline is accurate enough for your use.
- **Add format and sanity checks.** Cheap, automatic guards catch a surprising share of errors: validate structure and types (e.g. with Pydantic), and check ranges and formats — a date that isn't a date, a CIK with the wrong number of digits, a negative share count.
- **Ground high-stakes fields.** For values that really matter, have the model quote the exact source text supporting each answer, so you — or a reviewer — can check it against the document.
- **Compare across models.** Run the same inputs through two different models and look at where they *disagree* — disagreement is a cheap flag for "this item is uncertain," pointing you to the cases worth reviewing.

{: .tip }
> **Swapping in a second model is a one-line change.** The Stanford AI Playground, a local model served by Ollama, and third-party APIs all speak the same OpenAI-compatible API — so running the same prompt through another model just means a different `base_url` (and `model`/`api_key`). The rest of your code is identical:
>
> ```python
> import os
> from openai import OpenAI
>
> # Model A — Stanford AI Playground
> playground = OpenAI(base_url="https://aiapi-prod.stanford.edu/v1", api_key=os.getenv("STANFORD_API_KEY"))
>
> # Model B — a local model served by Ollama on the Yens
> local = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
>
> # Model C — a third-party provider (e.g. OpenAI); base_url defaults to the provider
> thirdparty = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
>
> # same call for each — only the client and model name change
> answer_a = playground.chat.completions.create(model="gpt-4o-mini", messages=messages)
> answer_b = local.chat.completions.create(model="llama3.2:3b", messages=messages)
> answer_c = thirdparty.chat.completions.create(model="gpt-5.6", messages=messages)
> ```

---

## Failure Modes in Automated Pipelines

Validation catches wrong *outputs*. A different class of failure appears once you run LLMs *unattended* — in an automated pipeline or agent that reads, writes, and loops on your behalf, with no human watching each step. These need architectural guards, not validation.

### Irreversibility {#irreversibility}

The stakes rise sharply when an LLM's output drives an action — writing to a database, sending emails, deleting files. LLMs make mistakes, and mistakes that change state are the most expensive kind: you often can't undo them.

Recall from [Day 1](../../day1/command-spire/) that `rm` deletes permanently — no trash, no undo; an agent runs the same commands, just without a human pausing to reconsider. Agents run with *your* full permissions, so "clean up this folder" can reach anything you can.

{: .note }
> **Real-world case:** in early 2026 a user asked Claude to organize a desktop, and it deleted a folder holding roughly 15 years of family photos — thousands of files — with terminal commands that bypassed the Trash entirely.
>
> ![Futurism headline: Blundering Husband Asks Claude AI to Organize Wife's PC, Accidentally Erases Her Cherished Family Photos]({{ site.baseurl }}/assets/images/claude-family-photos-headline.png)
>
> *Source: [Futurism](https://futurism.com/artificial-intelligence/claude-wife-photos).*

**Guarding against it:** the reliable defense is "least privilege": giving the agent only the access it truly needs (read-only where possible; scoped, minimal credentials), and requiring confirmation for anything that changes state. Keep automated pipelines read-only where you can; for writes, log the intended action first, act second, and verify before committing — and build a **dry-run mode** that prints what *would* happen without doing it.

### Prompt Injection

Your input data isn't always trustworthy. A document you feed the model can contain adversarial text — for example, "Ignore all previous instructions and…" — that hijacks its behavior, making it do something other than the task you intended. Data scraped from the public web is especially risky.

**Guarding against it:** keeping your instructions in the system message and untrusted data in a separate user message helps — models are trained to prioritize system instructions — but it's a *partial* mitigation, not a hard boundary: to the model it's all just text, and a determined injection can still get through. So lean on the real backstops: validate the output before you rely on it, and apply least privilege (see [Irreversibility](#irreversibility) above) — assume the model can be manipulated, and make sure it simply *can't* take a harmful action.

### Runaway Loops

An automated pipeline that retries on failure with no cap can retry forever — until it times out or burns through your API budget. A step that calls itself with no stopping condition can fan out exponentially.

**Guarding against it:** cap everything — a `max_retries` on each retry loop, a spend/budget limit on the whole job, and a sanity timeout. Log each iteration, and if a job runs well past its expected time, kill it and investigate.

<label class="quest-check"><input type="checkbox" data-room="d4-failure-modes" data-key="main"> I can name the main LLM failure modes and how to guard against each</label>

{: .note }
> 🔄 **Keep the leaderboard live.** In your terminal on the Yens, inside `~/gsb-research-computing-ai-skills` — start Claude Code with `claude` if it isn't already running — tell it: "Set `d4-failure-modes.main` to `true` in `quest_log.json` at my repo root (create it if missing). Before pushing, run `git remote -v` and confirm `origin` is my own fork (`{{ site.data.site_meta.github_owner }}/gsb-research-computing-ai-skills`), not the class repo `gsbdarc/gsb-research-computing-ai-skills` — if it points to the class repo, stop and tell me. Then commit and push to `main`." Claude runs the `git add`/`commit`/`push` for you — same `main` branch you've been pushing to all along.

---

## What You Learned

- Even frontier models are brittle and unevenly capable — you can't assume an output is correct, so you measure your own error rate rather than trust a benchmark headline
- Hallucination is the core correctness failure: the model isn't well calibrated, so a confident tone tells you nothing about whether an answer is right
- You can validate outputs at scale — spot-checking against the source, format/type sanity checks, grounding high-stakes fields, and comparing across models (a one-line `base_url` swap)
- You can name the failure modes that appear once LLMs run unattended — irreversibility, prompt injection, and runaway loops — and their architectural guards: least privilege, separating instructions from untrusted data, and caps/timeouts
