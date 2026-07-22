---
layout: default
title: "The Stanford AI Playground"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/stanford-ai-playground/
---

# The Stanford AI Playground

<div data-room-id="d2-stanford-ai-playground"></div>

*Beyond the forge, a corridor opens into a high-vaulted chamber where a single door is held by many locks at once. Stanford's data-risk tiers turn one ward; your Data Use Agreement turns another; an IRB protocol a third; the model provider's contract a fourth. No single key opens the door — every contingency must align together, or the data stays where it is. The Playground is the one instrument on campus built so all of them can line up at once: governed, audited, contracted on your behalf. Learn which locks apply to your data before you reach for the handle.*

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Log in to the Stanford AI Playground with your SUNet credentials, send your first prompt through Stanford's governed gateway, and know which data-risk levels you may (and may not) send through it.

---

## 🖊️ Data Security

Datasets that aren't public come with rules, imposed by multiple entities. Two systems matter most for your research.

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

You follow both systems (Stanford's classification and your DUA) so Stanford stays protected.

{: .warning }
> **Improper use of a dataset can mean lawsuits — and losing access to the data, or the tools, entirely.**

**🖊️ Quick Check: Classify These Five**

For each, is it **Low**, **Moderate**, or **High** Risk under Stanford's definitions above?

1. A published, peer-reviewed journal article
2. Social Security numbers
3. An unreleased internal budget or financial projection
4. Student grades and transcripts
5. De-identified, aggregated survey data

*Discuss as a class: which ones surprised you? Where did opinions differ?*

<details markdown="1">
<summary>💡 Answer key — click to reveal</summary>

| # | Item | Risk | Why |
|---|------|------|-----|
| 1 | Published, peer-reviewed article | 🟢 **Low** | Already public — no restriction on sharing. |
| 2 | Social Security numbers | 🔴 **High** | Regulated personal identifiers; a textbook High-Risk example. |
| 3 | Unreleased internal budget / projection | 🟡 **Moderate** | Confidential business information, but not regulated personal data. |
| 4 | Student grades and transcripts | 🟡 **Moderate** | Education records protected by **FERPA**. |
| 5 | De-identified, aggregated survey data | 🟢 **Low** | De-identification *and* aggregation remove the personal risk. |

A **DUA or IRB protocol can push any of these higher** — de-identified data that can be re-identified, or a budget under a confidentiality agreement, may need stricter handling. Classify by the data **and** its contract.
</details>

---

Since AI is permeating every facet of research, Stanford has worked hard to give you a space to submit AI queries with certain guarantees.

## 🖊️ Stanford's AI Offerings

Stanford builds and runs **two** of its own AI services — two different ways in to the same governed idea:

- **The AI Playground** — a **chat window** in your browser, built on the open-source **LibreChat** platform. Point, click, and type; nothing to install. *(This room.)*
- **The AI API Gateway** — **API access** to the same class of models for your *code*, over an OpenAI-compatible endpoint (`aiapi-prod.stanford.edu`). A separate system you call programmatically. You'll wire into it from [The Key Vault](../key-vault/) onward.

Both keep every prompt inside Stanford's contracted perimeter. The rest of this room walks the **chat window** first, then the **API**.

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

## 🖊️ The AI Playground — a Chat Window

The AI Playground is a University-hosted **chat interface**, built on the open-source **LibreChat** platform, that gives every Stanford researcher one safe, governed space to work with many cutting-edge models. You log in with your SUNet credentials and chat much as you would with ChatGPT — but every prompt stays inside Stanford's contracted perimeter, and it is cleared for data up to **High Risk — but *not* PHI** (protected health information).

It offers many of the same models you'd reach commercially — such as Claude Opus 4.8, GPT-5.2, and Gemini 2.5 Flash, among others — with no personal account or credit card. (The exact model ids come from the models endpoint you'll query in [The Oracle's Chamber](../oracles-chamber/).)

### 🔰 Try the AI Playground

Open <a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">https://uit.stanford.edu/aiplayground</a> in your browser and log in with SUNet.

Ask it something:
- *"Summarize what a virtual environment is in one sentence."*
- *"What is the difference between a kernel and a Python interpreter?"*

Notice: the responses come from the same models you'd reach through the API. You're already using the Stanford AI Playground.

### Upsides and Downsides

| | Detail |
|-|--------|
| ✅ **No personal billing** | Budget caps enforced by Stanford; you cannot accidentally run up a $10,000 bill |
| ✅ **Stanford data perimeter** | Covered under Stanford's data processing agreement with the model provider |
| ✅ **No account required** | Every Stanford researcher has access via SUNet login |
| ⚠️ **Prompts are logged** | Stanford can review usage logs, so it isn't anonymous. The upside: that audited, contracted perimeter is exactly what clears the Playground for sensitive data up to **High Risk — though not PHI** (and always subject to your DUA) |
| ⚠️ **Model selection** | Available models are determined by Stanford's contract, not your preference |

---

## 🖊️ The AI API Gateway — API Access

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
  <title id="api-flow-title">How the Stanford AI API Gateway works: your code sends a request to Stanford's gateway, which sits inside the campus perimeter. The gateway authenticates you through SUNet, applies Stanford's contract with the provider, enforces budget caps, and logs the call, then forwards it across the perimeter to the model provider and returns the response back along the same path.</title>
  <defs>
    <marker id="api-ah-green" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2e8b57"/></marker>
    <marker id="api-ah-slate" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- perimeter: gateway is inside Stanford, the provider is outside -->
  <line x1="700" y1="55" x2="700" y2="380" stroke="#b09668" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="700" y="42" text-anchor="middle" font-size="15" font-weight="700" letter-spacing="0.5" fill="#b09668">STANFORD PERIMETER</text>

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
  <text x="510" y="222" text-anchor="middle" font-size="15" fill="#6a5326">🪪  authenticates you (SUNet)</text>
  <text x="510" y="252" text-anchor="middle" font-size="15" fill="#6a5326">🔒  applies Stanford's contract</text>
  <text x="510" y="282" text-anchor="middle" font-size="15" fill="#6a5326">💵  enforces budget caps</text>
  <text x="510" y="312" text-anchor="middle" font-size="15" fill="#6a5326">📋  keeps an audit trail</text>

  <!-- model -->
  <rect x="755" y="170" width="205" height="130" rx="16" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="857" y="216" text-anchor="middle" font-size="21" font-weight="700" fill="#2c3e50">🧠  The model</text>
  <text x="857" y="246" text-anchor="middle" font-size="16" fill="#6a7280">provider executes</text>
  <text x="857" y="272" text-anchor="middle" font-size="14.5" fill="#8a94a6">outside the perimeter</text>

  <!-- your code <-> gateway (green) -->
  <line x1="270" y1="205" x2="383" y2="205" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#api-ah-green)"/>
  <text x="326" y="196" text-anchor="middle" font-size="14.5" font-weight="700" fill="#1f6b45" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">① request</text>
  <line x1="383" y1="265" x2="272" y2="265" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#api-ah-green)"/>
  <text x="326" y="284" text-anchor="middle" font-size="14.5" font-weight="700" fill="#1f6b45" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">④ response</text>

  <!-- gateway <-> model (slate), crossing the perimeter -->
  <line x1="637" y1="205" x2="753" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#api-ah-slate)"/>
  <text x="695" y="196" text-anchor="middle" font-size="14.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">② forward</text>
  <line x1="753" y1="265" x2="639" y2="265" stroke="#556a95" stroke-width="2.5" marker-end="url(#api-ah-slate)"/>
  <text x="695" y="284" text-anchor="middle" font-size="14.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">③ response</text>
</svg>

Every model call, prompt, and response flows through `aiapi-prod.stanford.edu`, Stanford's contracted endpoint, instead of going straight to the provider. Your code looks identical; only the endpoint changes.

### Why Stanford Runs Its Own Server

That gateway is a server Stanford stands up and maintains itself, placed between your code and the model provider on purpose. Owning the middle is what lets the University put every request under its contract with the provider (the **DPA**), authenticate you through **SUNet**, enforce **budget caps**, and keep an **audit trail**. Send data straight to a vendor on a personal account instead, and none of those protections apply. One governed door for all of campus beats thousands of ungoverned ones.

{: .important }
> **The chat window and the API have different PHI ceilings.** The Playground **chat window** is cleared for data up to High Risk but **not PHI** (protected health information). The **API Gateway** *is* approved for High Risk **including PHI** (always subject to your DUA). So when PHI is involved, reach for the **API path**, not the chat window.

### Requesting Your Own Key

Today you're using the shared bootcamp key. If you or your PI need a personal Stanford AI API Gateway key later, you'll submit a request with:

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

**Side quest — Save a Course Context Prompt**

Save a reusable prompt that gives the AI quick background on the class you're taking: what the course is, what you're working on, and what tools you have access to. Paste it in at the top of a new conversation instead of re-explaining yourself every time.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side1"> I saved a reusable course-context prompt</label>

**Side quest — Compare Two Models**

Ask two different cutting-edge models the same Yen-specific question. Compare the answers: which one do you trust more, and why?

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side2"> I compared two models on the same question</label>

**Side quest — Customize the System Prompt**

Set the system prompt so the AI knows who you are, your current knowledge level, and how you like to be spoken to. Ask the same question with the system prompt empty versus filled in, and see whether the tone or depth actually changes.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side3"> I customized the system prompt and compared the results</label>

---

## 🧠 Skills Learned

- Stanford AI Playground gives every researcher access to models such as Claude Opus 4.8, GPT-5.2, and Gemini 2.5 Flash; no personal account needed
- The AI Playground (a LibreChat **chat window**) and the AI API Gateway (**API access** for code) are two *separate* Stanford services — the chat window is cleared to High Risk but **not PHI**, while the API Gateway handles High Risk **including PHI**
- The API is OpenAI-compatible: only `base_url` and the key change; all code is the same
- Prompts sent through either service are logged and subject to audit; classify your data before sending it
