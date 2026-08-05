---
layout: floor
title: "Day 2 — The Alchemist's Lab"
nav_order: 2
has_children: true
permalink: /day2/
floor: 2
---

# Day 2 — The Alchemist's Lab

Day 2 moves from the shell into Python, and from there into calling AI models from your own code. You'll open JupyterHub and run Python on the Yens from your browser, build an isolated virtual environment that anyone can rebuild from a `requirements.txt`, and then work with Stanford's AI API Gateway: loading a key from a `.env` file, extracting structured fields out of real SEC filings, and validating what comes back with Pydantic so bad output fails loudly instead of quietly. The day closes on the judgment that surrounds all of it — which data you're allowed to send where, what a run costs, and which calls a human still has to make.

**Duration:** ~3 hours

<img src="{{ '/assets/images/day2-overview.png' | relative_url }}" alt="An illustrated grimoire open to the Day 2 spread, The Alchemist's Lab, levels 4 to 6. The left page shows a hooded alchemist in a vaulted lab behind a row of flasks labelled Python 3.10, 3.11, and 3.12, with a glowing API Keys vault door behind them. The right page, headed The Keep of Computation, lists the seven rooms in order with their format and focus: The Path (hands-on, open JupyterHub, run a cell, understand notebooks vs scripts), The Venv Forge (hands-on, understand PATH and modules, forge an isolated Python environment), The Stanford AI Playground (concept and demo, the AI Playground chat window vs the API gateway and their data-risk limits), The Key Vault (hands-on, load the API key from .env, add to .gitignore, understand what you're sending), The Oracle's Chamber (hands-on, make your first API call, extract and validate SEC filing data with Pydantic, move code to a script), The Crucible (discussion, AI agents at Stanford, what they send, data privacy rules, and how to stay defensible), and Boss Gate 2 (capstone, the Genre Tribunal, scale a research judgment call with LLM-as-a-judge then route the contested cases to a human)." style="display:block;width:100%;max-width:900px;height:auto;margin:1.5rem auto">

---

## Sections

Work through the sections in order — later ones build on earlier ones, and the Day 2 Challenge draws on everything you've learned.

| Section | Format | What you'll learn |
|------|--------|-----------------|
| [Running Python on the Yens](the-path/) | 💻 Hands-on | How `$PATH` decides which `python3` answers, JupyterHub in your browser, and the three ways to run Python — interpreter, notebook, and script |
| [Python Environments](venv-forge/) | 💻 Hands-on | Build an isolated virtual environment, register it as a JupyterHub kernel, and rebuild any project from its `requirements.txt` |
| [Stanford's AI Services](stanford-ai-playground/) | 🖊️💬 Concept + demo | The AI Playground chat window vs. the AI API Gateway for code, and which data-risk levels each one is cleared for |
| [Managing API Keys](key-vault/) | 💻 Hands-on | Load a key from `.env`, keep it out of git, and know why a committed key is a leaked key |
| [Extracting Data with an LLM API](oracles-chamber/) | 💻 Hands-on | Your first API call, then pulling structured fields out of real SEC filings — validated with Pydantic, and moved from a notebook into a logged script |
| [AI Agents & Data Privacy](human-vs-llm/) | 💬 Discussion | What coding agents send to remote servers, how to classify your data, what each path costs, and how to keep a pipeline defensible |
| [Day 2 Challenge](boss-gate-2/) | 🔑 Capstone | Scale a research judgment call with LLM-as-a-judge: classify, check it with a second model, then route the contested cases to a human |
