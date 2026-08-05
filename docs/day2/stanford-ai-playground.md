---
layout: default
title: "The Stanford AI Playground"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/stanford-ai-playground/
---

# The Stanford AI Playground

<div data-room-id="d2-stanford-ai-playground"></div>

"Can I analyze this data with AI?" is really three questions at once, and you have to satisfy all three: what risk level is the data, what does your Data Use Agreement allow, and what is the machine you're working on cleared to hold. This room covers those rules, then Stanford's two ways to work under them — the AI Playground, a chat window you log into with your SUNetID, and the AI API Gateway, which reaches the same class of models from your code. Both put every prompt under a University contract instead of a personal account's consumer terms. You'll send your first prompt through the Playground and learn which data you may, and may not, put through it.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Log in to the Stanford AI Playground with your SUNetID credentials, send your first prompt through Stanford's governed gateway, and know which data-risk levels you may (and may not) send through it.

---

## 🖊️ Data Security

Datasets that aren't public come with rules, and those rules are imposed by **three** different entities at once. They are independent of each other, they don't consult each other, and you have to satisfy all three. When they disagree, the **strictest one wins**.

**1. Stanford's data risk classification**

![Stanford Data Risk]({{ "/assets/images/Stanford_data_risk.png" | relative_url }})

*Stanford's data risk classification guidelines.*

<a href="https://uit.stanford.edu/guide/riskclassifications" target="_blank" rel="noopener noreferrer">
  Read Stanford's data risk classification guidance
</a>

**2. Data Use Agreements (DUAs)**

DUAs come from datasets purchased or licensed for faculty use. Stanford's lawyers negotiate these agreements so you can do cutting-edge research, but the terms vary widely, from permissive to restrictive:

| | Example clause |
|-|-----------------|
| 🟢 Permissive | "You may publish no more than 5% of the data publicly" |
| 🟢 Permissive | "You must keep all analysis on Stanford servers" |
| 🔴 Restrictive | "You may not use ANY form of AI on this data" |
| 🔴 Restrictive | "All analysis must be done on company servers with approved libraries" |

**3. The computing system you're working on**

Every system you touch is itself approved up to some maximum risk level, and that ceiling belongs to the **machine**, not to your data or your good intentions. This is the one researchers forget, because nothing stops you: you can copy a restricted file onto a system that isn't cleared for it and everything will appear to work fine. The violation is the copy, not the crash.

| Where you're working | Approved up to |
|----------------------|----------------|
| **<a href="https://rcpedia.stanford.edu/_policies/security/?h=high+risk#data-risk" target="_blank" rel="noopener noreferrer">The Yens</a>** (GSB research computing) | 🟡 Moderate |
| **<a href="https://www.sherlock.stanford.edu/docs/concepts/" target="_blank" rel="noopener noreferrer">Sherlock</a>** (Stanford's shared HPC cluster) | 🟡 Moderate |
| **<a href="https://docs.carina.stanford.edu/" target="_blank" rel="noopener noreferrer">Carina</a>** (secure on-prem cluster for regulated data) | 🔴 High, **including** PHI |
| **<a href="https://nero-docs.stanford.edu/" target="_blank" rel="noopener noreferrer">Nero GCP</a>** (secure cloud platform for regulated data) | 🔴 High, **including** PHI |
| **AI Playground** (chat window) | 🔴 High, but **not** PHI |
| **AI API Gateway** (from your code) | 🔴 High, **including** PHI |
| A personal laptop or consumer AI account | 🟢 Low |

So "can I analyze this data with AI?" is really three questions: *what risk level is the data*, *what does my DUA allow*, and *what is this machine cleared to hold*. High-risk data on the Yens fails the third test even when the first two are satisfied.

{: .note }
> 💡 **Know which machine to reach for.** The Yens are your home for this course and for most GSB research; their data-risk policy is spelled out in <a href="https://rcpedia.stanford.edu/_policies/security/?h=high+risk#data-risk" target="_blank" rel="noopener noreferrer">RCpedia</a>. <a href="https://www.sherlock.stanford.edu/docs/concepts/" target="_blank" rel="noopener noreferrer">**Sherlock**</a> is Stanford's shared HPC cluster, where you go when a job outgrows the Yens — still Moderate, so it is not the answer to a High-Risk problem.
>
> High-Risk work, including anything involving PHI, belongs on a platform built for it, and Stanford runs **two**: <a href="https://docs.carina.stanford.edu/" target="_blank" rel="noopener noreferrer">**Carina**</a> is the on-premises option, run by Stanford Research Computing with the School of Medicine, and it is **Slurm-based** — so the job scripts you write on Day 3 transfer almost unchanged. <a href="https://nero-docs.stanford.edu/" target="_blank" rel="noopener noreferrer">**Nero GCP**</a> is the cloud option, the same idea built on Google Cloud. Both need a PI-led team and go through Stanford's Data Risk Assessment, so neither is something you spin up on a Tuesday afternoon. Sort that out *before* you copy a single file, because the moment restricted data lands on a system that isn't cleared for it, the problem already exists.

You satisfy all three (Stanford's classification, your DUA, and the ceiling of the system you're on) so both you and Stanford stay protected.

{: .warning }
> **Improper use of a dataset can mean lawsuits, and losing access to the data or the tools entirely.**

**🖊️ Exercise: Classify These Five**

For each, is it **Low**, **Moderate**, or **High** Risk under Stanford's definitions above?

1. A published, peer-reviewed journal article
2. Social Security numbers
3. An unreleased internal budget or financial projection
4. Student grades and transcripts
5. De-identified, aggregated survey data

*Discuss as a class: which ones surprised you? Where did opinions differ?*

<details markdown="1">
<summary>💡 Answer key: click to reveal</summary>

| # | Item | Risk | Why |
|---|------|------|-----|
| 1 | Published, peer-reviewed article | 🟢 **Low** | Already public, no restriction on sharing. |
| 2 | Social Security numbers | 🔴 **High** | Regulated personal identifiers; a textbook High-Risk example. |
| 3 | Unreleased internal budget / projection | 🟡 **Moderate** | Confidential business information, but not regulated personal data. |
| 4 | Student grades and transcripts | 🟡 **Moderate** | Education records protected by **FERPA**. |
| 5 | De-identified, aggregated survey data | 🟢 **Low** | De-identification *and* aggregation remove the personal risk. |

A **DUA or IRB protocol can push any of these higher**: de-identified data that can be re-identified, or a budget under a confidentiality agreement, may need stricter handling. Classify by the data **and** its contract.
</details>

---

Since AI is permeating every facet of research, Stanford has worked hard to give you a space to submit AI queries with certain guarantees.

## 🖊️ Stanford's AI Offerings

Stanford builds and runs **two** of its own AI services, two different ways in to the same governed idea:

- **The AI Playground:** a **chat window** in your browser. Point, click, and type; nothing to install. *(This room.)*
- **The AI API Gateway:** **API access** to the same class of models for your *code*, over an OpenAI-compatible endpoint (`aiapi-prod.stanford.edu`). A separate system you call programmatically. You'll wire into it from [The Key Vault](../key-vault/) onward.

{: .note }
> 💡 **Two words before we go further, in case they're new.**
>
> **An API** (Application Programming Interface) is a door into a service built for **programs** rather than for people. The chat window and the API reach the very same models; what differs is who is standing at the door. You type into a chat window and read the reply yourself. Your *code* sends a request to an API and gets structured data back that the rest of your script can use.
>
> Why a researcher should care: reading one SEC filing in a chat window is easy. Reading **ten thousand** of them means a `for` loop, and a loop needs a door that code can open. Same models, same Stanford contract, different door.
>
> **An API key** is the credential that opens that door. A server has no other way to know who is knocking, so your key identifies you and carries your permissions and your budget with it. That leads to the two rules you'll practise next room: keep it **secret**, because anyone holding it can spend against your account, and never let it end up in your code, a screenshot, a chat window, or a commit. [The Key Vault](../key-vault/) is entirely about handling it properly.

Both put every prompt under one of Stanford's enterprise agreements rather than a personal account's consumer terms. The rest of this room walks the **chat window** first, then the **API**.

Stanford also brokers access to a growing list of **third-party** services (each with its own data rules):

| Category | Offering | Provider |
|----------|----------|----------|
| Education accounts | Claude for Education | Anthropic |
| Education accounts | Google Gemini Enterprise | Google |
| Education accounts | OpenAI ChatGPT Edu | OpenAI |
| Education accounts | Microsoft Copilot | Microsoft |
| Cloud AI | AWS Bedrock | Amazon |
| Cloud AI | Azure OpenAI | Microsoft |
| Cloud AI | Google Vertex | Google |

*This list keeps growing. See the <a href="https://uit.stanford.edu/ai/services/explore" target="_blank" rel="noopener noreferrer">full directory</a> for the latest.*

---

## 🖊️ The AI Playground: A Chat Window

The AI Playground is a University-hosted **chat interface** that gives every Stanford researcher one safe, governed space to work with many cutting-edge models. You log in with your SUNetID credentials and chat much as you would with ChatGPT, but every prompt is covered by Stanford's enterprise agreement with the cloud provider instead of consumer terms, and it is cleared for data up to **High Risk, but *not* PHI** (protected health information).

It offers many of the same models you'd reach commercially (Claude Opus 4.8, GPT-5.2, and Gemini 2.5 Flash, among others) with no personal account or credit card. (The exact model ids come from the models endpoint you'll query in [The Oracle's Chamber](../oracles-chamber/).)

### 🔰 Try the AI Playground

Open <a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">https://uit.stanford.edu/aiplayground</a> in your browser and log in with SUNetID.

Ask it something:
- *"Summarize what a virtual environment is in one sentence."*
- *"What is the difference between a kernel and a Python interpreter?"*

Notice: the responses come from the same models you'd reach through the API. You're already using the Stanford AI Playground.

### Upsides and Downsides

| | Detail |
|-|--------|
| ✅ **Free to you** | Stanford covers the cost. No credit card to attach and no per-use charge to keep an eye on, unlike a personal ChatGPT or Claude subscription |
| ✅ **Stanford's agreement applies** | Your prompts fall under Stanford's enterprise contract and data processing agreement, not a consumer account's terms |
| ✅ **No account required** | Every Stanford researcher has access via SUNetID login |
| ⚠️ **Prompts are logged** | Stanford can review usage logs, so it isn't anonymous. The upside: that audited, contracted arrangement is exactly what clears the Playground for sensitive data up to **High Risk, though not PHI** (and always subject to your DUA) |
| ⚠️ **Model selection** | Available models are determined by Stanford's contract, not your preference |

---

## 🖊️ The AI API Gateway: API Access

The Playground's sibling, the Stanford <a href="https://uit.stanford.edu/service/ai-api-gateway" target="_blank" rel="noopener noreferrer"><strong>AI API Gateway</strong></a>, exposes the same class of models to your *code* and is fully OpenAI-compatible. Code that already calls the OpenAI API can call Stanford's gateway with two changes:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_STANFORD_KEY",           # Stanford-issued key, not OpenAI key
    base_url="https://aiapi-prod.stanford.edu/v1",  # Stanford gateway, not api.openai.com
)
```

Here's what happens on the wire when that code runs:

<svg viewBox="0 0 1000 420" role="img" aria-labelledby="api-flow-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:1000px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="api-flow-title">How the Stanford AI API Gateway works: your code sends a request to Stanford's gateway. The gateway authenticates you through SUNetID, applies Stanford's contract, enforces budget caps, and logs the call, then routes it to the model, which is served by an enterprise cloud provider under one of Stanford's enterprise agreements rather than on a personal vendor account. The response returns along the same path.</title>
  <defs>
    <marker id="api-ah-green" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2e8b57"/></marker>
    <marker id="api-ah-slate" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- your code -->
  <rect x="40" y="170" width="230" height="130" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="155" y="214" text-anchor="middle" font-size="21" font-weight="700" fill="#2c3e50">💻  Your code</text>
  <text x="155" y="244" text-anchor="middle" font-size="16" fill="#9a8a68">laptop or the Yens</text>
  <text x="155" y="270" text-anchor="middle" font-size="14.5" fill="#9a8a68">OpenAI-compatible client</text>

  <!-- gateway: the governed door -->
  <rect x="385" y="118" width="250" height="234" rx="16" fill="#fbe9cf" stroke="#dcae6a" stroke-width="2"/>
  <text x="510" y="150" text-anchor="middle" font-size="18" font-weight="700" fill="#2c3e50">🛡️  Stanford AI API Gateway</text>
  <text x="510" y="174" text-anchor="middle" font-size="14" fill="#8a6d3b">aiapi-prod.stanford.edu</text>
  <line x1="410" y1="190" x2="610" y2="190" stroke="#e0c48a" stroke-width="1"/>
  <text x="510" y="222" text-anchor="middle" font-size="15" fill="#6a5326">🪪  authenticates you (SUNetID)</text>
  <text x="510" y="252" text-anchor="middle" font-size="15" fill="#6a5326">🔒  applies Stanford's contract</text>
  <text x="510" y="282" text-anchor="middle" font-size="15" fill="#6a5326">💵  enforces budget caps</text>
  <text x="510" y="312" text-anchor="middle" font-size="15" fill="#6a5326">📋  keeps an audit trail</text>

  <!-- model -->
  <rect x="755" y="170" width="205" height="130" rx="16" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="857" y="214" text-anchor="middle" font-size="21" font-weight="700" fill="#2c3e50">🧠  The model</text>
  <text x="857" y="244" text-anchor="middle" font-size="14.5" fill="#6a7280">served by an enterprise</text>
  <text x="857" y="266" text-anchor="middle" font-size="14.5" fill="#6a7280">cloud provider</text>
  <text x="857" y="288" text-anchor="middle" font-size="12.5" fill="#8a94a6">under Stanford's agreement</text>

  <!-- your code <-> gateway (green) -->
  <line x1="270" y1="205" x2="383" y2="205" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#api-ah-green)"/>
  <text x="326" y="196" text-anchor="middle" font-size="14.5" font-weight="700" fill="#1f6b45" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">① request</text>
  <line x1="383" y1="265" x2="272" y2="265" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#api-ah-green)"/>
  <text x="326" y="284" text-anchor="middle" font-size="14.5" font-weight="700" fill="#1f6b45" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">④ response</text>

  <!-- gateway <-> model (slate) -->
  <line x1="637" y1="205" x2="753" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#api-ah-slate)"/>
  <text x="695" y="196" text-anchor="middle" font-size="14.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">② forward</text>
  <line x1="753" y1="265" x2="639" y2="265" stroke="#556a95" stroke-width="2.5" marker-end="url(#api-ah-slate)"/>
  <text x="695" y="284" text-anchor="middle" font-size="14.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">③ response</text>
</svg>

Every model call, prompt, and response flows through `aiapi-prod.stanford.edu`, Stanford's contracted endpoint, instead of going straight to the provider. Your code looks identical; only the endpoint changes.

### Why Stanford Runs Its Own Server

That gateway is a server Stanford stands up and maintains itself, placed between your code and the model provider on purpose. Owning the middle is what lets the University put every request under its contract with the provider (the **DPA**), authenticate you through **SUNetID**, enforce **budget caps**, and keep an **audit trail**. Send data straight to a vendor on a personal account instead, and none of those protections apply. One governed door for all of campus beats thousands of ungoverned ones.

{: .important }
> **The chat window and the API have different PHI ceilings.** The Playground **chat window** is cleared for data up to High Risk but **not PHI** (protected health information). The **API Gateway** *is* approved for High Risk **including PHI** (always subject to your DUA). So when PHI is involved, reach for the **API path**, not the chat window.

### The API Gateway Is Metered

Here's the other way the two services differ, and it's the one that surprises people. The chat window is **free to you** — type all day, nothing accrues. The API Gateway is **pay-per-use**: every call is billed on the amount of text you send plus the amount the model generates back, at a rate that depends on which model you picked. That's what the budget cap in the diagram is capping.

At the scale of today — a handful of calls on one filing — this is fractions of a cent, and you're spending against a shared course key rather than your own. It starts to matter the moment a `for` loop is involved. Ten thousand filings is ten thousand billable calls, and the difference between the cheapest and most expensive model on the menu is not small.

So two habits, starting now: know that a loop over documents is a loop over charges, and measure the cost on a few records before you launch the full run. [The Crucible](../human-vs-llm/) takes this apart properly later today — what drives the bill, how to estimate one from a sample, and the trap where a model charges you for reasoning you never see.

### Requesting Your Own Key

Today you're using the shared course key. If you or your PI need a personal Stanford AI API Gateway key later, you'll submit a request with:

- **Organization**: Stanford University, Stanford Health Care (SHC), or Stanford Children's Health (SCH)
- **Requester**: yourself, someone else, or your department/service team
- **Model(s)**: which AI model(s) you need access to
- **Key alias**: a short, descriptive, alphanumeric name (20 characters max)
- **Business purpose**: what the key will be used for
- **Budget**: your maximum monthly spend
- **Volume**: approximate number of requests per day
- **Due date**: when you need the key by
- **Billing**: your Project, Task, and Award (the PTA), plus an approver for the billing account if your request requires approval (Ask Your Advisor)

{: .note }
> If your request needs approval, the designated approver gets notified before the key is issued. If you're the designated approver yourself, the request is auto-approved.

In the next room (The Key Vault), you'll load the key securely from a `.env` file rather than hardcoding it.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="main"> Main Quest complete</label>

## Side quests

{: .note }
> Finished early? Try any of these.
>
> 🌐 **All three happen in the <a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">AI Playground</a> chat window in your browser** — the same tab you logged into above. No code, no API key, nothing to install. You're exploring what the chat window can do before you start driving the same models from Python.

**Side quest: Save a Course Context Prompt**

**In the AI Playground**, save a reusable prompt that gives the AI quick background on the class you're taking: what the course is, what you're working on, and what tools you have access to. Paste it in at the top of a new conversation instead of re-explaining yourself every time.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side1"> I saved a reusable course-context prompt in the AI Playground</label>

**Side quest: Compare Two Models**

**In the AI Playground**, use the model picker to ask two different cutting-edge models the same Yen-specific question. Compare the answers: which one do you trust more, and why?

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side2"> I compared two models on the same question in the AI Playground</label>

**Side quest: Customize the System Prompt**

**In the AI Playground**, set the system prompt so the AI knows who you are, your current knowledge level, and how you like to be spoken to. Ask the same question with the system prompt empty versus filled in, and see whether the tone or depth actually changes.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side3"> I customized the system prompt and compared the results in the AI Playground</label>

---

## 🧠 Skills Learned

- Stanford AI Playground gives every researcher access to models such as Claude Opus 4.8, GPT-5.2, and Gemini 2.5 Flash; no personal account needed
- The AI Playground (a **chat window**) and the AI API Gateway (**API access** for code) are two *separate* Stanford services: the chat window is cleared to High Risk but **not PHI**, while the API Gateway handles High Risk **including PHI**
- The chat window is free to you; the API Gateway is **metered per call**, billed on text in plus text out, which is why a loop over 10,000 documents is a budgeting decision and not just a coding one
- The API is OpenAI-compatible: only `base_url` and the key change; all code is the same
- Prompts sent through either service are logged and subject to audit; classify your data before sending it
