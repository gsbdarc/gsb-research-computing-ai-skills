---
layout: default
title: "The Stanford AI Playground"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/stanford-ai-playground/
---

# The Stanford AI Playground

<div data-room-id="d2-stanford-ai-playground"></div>

*Beyond the forge, a corridor opens into a high-vaulted chamber. Banners bearing the Stanford seal line the walls, and where you might expect bare iron, you find polished glass terminals, each one connected not to the open internet, but to a walled garden of approved models maintained by the University. This is not your personal account. It is a shared instrument, governed, audited, and provided to every researcher on campus. Use it wisely.*

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

You follow both systems (Stanford's classification and your DUA) so Stanford stays protected. Improper use of a dataset can mean lawsuits and losing access to the data, or the tools, entirely.

**🖊️ Quick Check: Classify These Five**

For each, is it **Low**, **Moderate**, or **High** Risk under Stanford's definitions above?

1. A published, peer-reviewed journal article
2. Social Security numbers
3. An unreleased internal budget or financial projection
4. Student grades and transcripts
5. De-identified, aggregated survey data

*Discuss as a class: which ones surprised you? Where did opinions differ?*

---

Since AI is permeating every facet of research, Stanford has worked hard to give you a space to submit AI queries with certain guarantees.

## 🖊️ The AI Offerings at Stanford

*This list keeps growing. See the [full directory](https://uit.stanford.edu/ai/services/explore) for the latest.*

| Category | Offering | Provider |
|----------|----------|----------|
| Stanford-built | The AI Playground (chat UI) | Stanford |
| Stanford-built | The AI API Gateway | Stanford |
| Education accounts | Claude for Education | Anthropic |
| Education accounts | Google Gemini Enterprise | Google |
| Education accounts | OpenAI ChatGPT Edu | OpenAI |
| Education accounts | Microsoft Copilot | Microsoft |
| Cloud AI | AWS Bedrock | Amazon |
| Cloud AI | Azure OpenAI | Microsoft |
| Cloud AI | Google Vertex | Google |


## 🖊️ What Is Stanford AI Playground?


Stanford AI Playground is a University-hosted gateway to large language models. It gives every Stanford researcher access to the same models (Claude-Opus-4-8, GPT-5.2, gemini-3.5-flash, and others) without a personal OpenAI account or credit card.

It comes in two forms:

**Web GUI**: a chat interface (like ChatGPT) accessible at:
> <a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">https://uit.stanford.edu/aiplayground</a>

Log in with your SUNet credentials. You can ask questions, draft text, and test prompts, all going through Stanford's infrastructure, not your personal account.

**API gateway**: the same models accessible via code, using an OpenAI-compatible client. The only difference from a personal OpenAI setup is a different `base_url` and a Stanford-issued API key.

---

## 🔰 Try the Web GUI

Open <a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">https://uit.stanford.edu/aiplayground</a> in your browser and log in.

Ask it something:
- *"Summarize what a virtual environment is in one sentence."*
- *"What is the difference between a kernel and a Python interpreter?"*

Notice: the responses come from the same models you'd use via the API. You're already using Stanford AI Playground.

---

## 🖊️ Upsides and Downsides {#upsides-and-downsides}

| | Detail |
|-|--------|
| ✅ **No personal billing** | Budget caps enforced by Stanford; you cannot accidentally run up a $10,000 bill |
| ✅ **Stanford data perimeter** | Covered under Stanford's data processing agreement with the model provider |
| ✅ **No account required** | Every Stanford researcher has access via SUNet login |
| ⚠️ **Prompts are logged** | Stanford can review usage logs, so it isn't anonymous. The upside: that audited, contracted perimeter is exactly what lets the gateway handle sensitive data up to High Risk, including PHI (subject to your DUA) |
| ⚠️ **Model selection** | Available models are determined by Stanford's contract, not your preference |


## 🖊️ How the API Works

The Stanford [**AI API Gateway**](https://uit.stanford.edu/service/ai-api-gateway) is fully OpenAI-compatible. Code that calls the OpenAI API can call Stanford's gateway with two changes:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_STANFORD_KEY",           # Stanford-issued key, not OpenAI key
    base_url="https://aiapi-prod.stanford.edu/v1",  # Stanford gateway, not api.openai.com
)
```

Here's what happens on the wire when that code runs:

```text
┌─────────────────┐              ┌─────────────────┐              ┌─────────────────┐
│    Your Code    │─1. request──►│     Gateway     │─2. forward──►│      Model      │
│ (laptop / Yens) │◄─4. response─│   (Stanford)    │◄─3. response─│   (executes)    │
└─────────────────┘              └─────────────────┘              └─────────────────┘
```

Every model call, prompt, and response flows through `aiapi-prod.stanford.edu`, Stanford's contracted endpoint, instead of going straight to the provider. Your code looks identical; only the endpoint changes.

**Why Stanford Runs Its Own Server**

That gateway is a server Stanford stands up and maintains itself, placed between your code and the model provider on purpose. Owning the middle is what lets the University put every request under its contract with the provider (the **DPA**), authenticate you through **SUNet**, enforce **budget caps**, and keep an **audit trail**. Send data straight to a vendor on a personal account instead, and none of those protections apply. One governed door for all of campus beats thousands of ungoverned ones.

**Requesting Your Own Key**

Today you're using the shared bootcamp key. If you or your PI need a personal Stanford AI Playground key later, you'll submit a request with:

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

## 📦 Side Quests

**Side Quest: Save a Course Context Prompt**

Save a reusable prompt that gives the AI quick background on the class you're taking: what the course is, what you're working on, and what tools you have access to. Paste it in at the top of a new conversation instead of re-explaining yourself every time.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side1"> I saved a reusable course-context prompt</label>

**Side Quest: Compare Two Models**

Ask two different cutting-edge models the same Yen-specific question. Compare the answers: which one do you trust more, and why?

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side2"> I compared two models on the same question</label>

**Side Quest: Customize the System Prompt**

Set the system prompt so the AI knows who you are, your current knowledge level, and how you like to be spoken to. Ask the same question with the system prompt empty versus filled in, and see whether the tone or depth actually changes.

<label class="quest-check"><input type="checkbox" data-room="d2-stanford-ai-playground" data-key="side3"> I customized the system prompt and compared the results</label>

---

## 🧠 Skills Learned

- Stanford AI Playground gives every researcher access to Claude-Opus-4-8, GPT-5.2, and other models; no personal account needed
- The web GUI and the API gateway are two interfaces to the same underlying service
- The API is OpenAI-compatible: only `base_url` and the key change; all code is the same
- Prompts sent through Stanford's gateway are subject to audit; classify your data before sending it
