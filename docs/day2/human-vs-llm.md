---
layout: default
title: "The Crucible"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 7
permalink: /day2/human-vs-llm/
---

# The Crucible

<div data-room-id="d2-human-vs-llm"></div>

Everything you built today assumed you knew what was leaving your machine. With AI coding agents (Claude Code, Copilot, Cursor) that assumption stops holding: they gather context for you, and at Stanford that comes with terms of service, data residency, and IRB implications most tutorials skip. This room makes it explicit: what these tools send, where it goes, and when the right answer is "not with this data."

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Understand how AI coding agents work at Stanford: where LLMs currently stand, how researchers are actually using them, and what happens to your data when you do.

This is a discussion block. No code. Bring your questions.

---

### Models

A model reads language (and increasingly images) as **tokens**, chunks a little smaller than a word. Rule of thumb: ~750 words is about **1,000 tokens**.

The **context window** is how much you can fit in at once, now a million tokens or more. Every answer is shaped by exactly two things: what the model learned in training, and what's in that window right now.

<svg viewBox="0 0 980 490" role="img" aria-labelledby="ctx-window-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:980px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="ctx-window-title">How a model produces an answer. What you send (your prompt, files, and images) is broken into tokens and placed in the context window, which holds up to about one million tokens, roughly 750,000 words. Today's 4,000-character SEC filing is about 1,000 tokens, a sliver of that capacity. The model reads the context window and combines it with training knowledge learned once when the model was built and never updated on its own. The answer is shaped by both.</title>
  <defs>
    <marker id="ctx-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- what you send -->
  <rect x="20" y="155" width="180" height="190" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="110" y="188" text-anchor="middle" font-size="15.5" font-weight="700" fill="#2c3e50">what you send</text>
  <text x="110" y="228" text-anchor="middle" font-size="14.5" fill="#6a5326">📝  your prompt</text>
  <text x="110" y="262" text-anchor="middle" font-size="14.5" fill="#6a5326">📄  files</text>
  <text x="110" y="296" text-anchor="middle" font-size="14.5" fill="#6a5326">🖼️  images</text>
  <text x="110" y="330" text-anchor="middle" font-size="11.5" fill="#9a8a68">you pick every piece</text>

  <!-- tokenize arrow -->
  <line x1="202" y1="250" x2="296" y2="250" stroke="#556a95" stroke-width="2.5" marker-end="url(#ctx-ah)"/>
  <text x="249" y="240" text-anchor="middle" font-size="13" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">tokenized</text>

  <!-- context window -->
  <rect x="300" y="125" width="290" height="250" rx="16" fill="#fbe9cf" stroke="#dcae6a" stroke-width="2"/>
  <text x="445" y="164" text-anchor="middle" font-size="18.5" font-weight="700" letter-spacing="0.5" fill="#2c3e50">CONTEXT WINDOW</text>
  <text x="445" y="188" text-anchor="middle" font-size="13" fill="#8a6d3b">everything the model can see, right now</text>
  <line x1="322" y1="206" x2="568" y2="206" stroke="#e0c48a" stroke-width="1"/>

  <!-- capacity bar: the filing is a hairline against 1M tokens -->
  <text x="568" y="228" text-anchor="end" font-size="11.5" fill="#8a94a6">capacity ~1,000,000 tokens</text>
  <rect x="322" y="236" width="246" height="26" rx="6" fill="#ffffff" stroke="#dcae6a" stroke-width="1.2"/>
  <rect x="323" y="237" width="4" height="24" fill="#b3611a"/>
  <text x="322" y="282" text-anchor="start" font-size="11.5" fill="#b3611a">▲ today's filing, ~1,000 tokens</text>

  <text x="445" y="314" text-anchor="middle" font-size="13" fill="#6a5326">~750 words ≈ 1,000 tokens</text>
  <text x="445" y="343" text-anchor="middle" font-size="12.5" font-style="italic" fill="#9a8a68">nothing outside this box exists to the model</text>

  <!-- read arrow -->
  <line x1="592" y1="250" x2="656" y2="250" stroke="#556a95" stroke-width="2.5" marker-end="url(#ctx-ah)"/>
  <text x="624" y="240" text-anchor="middle" font-size="13" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">reads</text>

  <!-- training knowledge -->
  <rect x="660" y="35" width="300" height="110" rx="14" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5"/>
  <text x="810" y="72" text-anchor="middle" font-size="15.5" font-weight="700" fill="#2c3e50">📚  training knowledge</text>
  <text x="810" y="100" text-anchor="middle" font-size="13" fill="#6a7280">learned once, when the model was built</text>
  <text x="810" y="124" text-anchor="middle" font-size="12.5" font-style="italic" fill="#8a94a6">never updates on its own</text>
  <line x1="810" y1="147" x2="810" y2="196" stroke="#556a95" stroke-width="2.5" marker-end="url(#ctx-ah)"/>

  <!-- the model -->
  <rect x="660" y="200" width="300" height="100" rx="16" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="810" y="240" text-anchor="middle" font-size="18" font-weight="700" fill="#2c3e50">🧠  the model</text>
  <text x="810" y="270" text-anchor="middle" font-size="13" fill="#6a7280">combines both sources</text>
  <line x1="810" y1="302" x2="810" y2="356" stroke="#556a95" stroke-width="2.5" marker-end="url(#ctx-ah)"/>

  <!-- answer -->
  <rect x="660" y="360" width="300" height="90" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="810" y="398" text-anchor="middle" font-size="18" font-weight="700" fill="#2c3e50">💬  answer</text>
  <text x="810" y="426" text-anchor="middle" font-size="13" fill="#9a8a68">shaped by both, nothing else</text>
</svg>

### What are AI coding agents?

AI coding tools (Claude Code, Copilot, Cursor) are **harnesses** wrapped around a model. They let it read your files, run commands, and use tools on your behalf. To do that, the harness gathers **context** from your machine and sends it to a remote model.

Look back at the diagram: *you pick every piece.* That was true in [The Oracle's Chamber](../oracles-chamber/), where you wrote both prompts yourself and knew exactly what the model received. A coding agent fills that window for you, with:

- The file you're editing
- Nearby files the tool has indexed
- Your chat history this session
- Sometimes terminal output, error messages, or clipboard contents

You hand-picked none of it, and it leaves your machine on every request (for autocomplete tools, every time you pause typing), often without your seeing what was sent.

---

### How researchers are actually using this

Three patterns dominate at Stanford right now. Two treat AI as an **instrument**; the third treats it as the **object of study**.

**1. Reading unstructured text at scale.** The most common by far. A researcher has thousands of dense documents (filings, earnings calls, court opinions, contracts, clinical notes, news archives, open-ended survey responses) holding evidence that no structured dataset captures. The model reads them and returns fields you can actually analyze.

The important nuance: this usually isn't a fishing expedition. The researcher already has a hypothesis from their study, and the model is how they **test and validate it** across a corpus too large to hand-code. That reframes the work. You aren't asking a model what to think, you're asking it to apply your coding scheme consistently across 10,000 documents, which is also why validation matters so much: an inconsistent coder silently corrupts your result. Today's Form 3 room is that pattern at a scale of one, and the [Day 2 Challenge](../boss-gate-2/) builds the checking half, where a second model reviews each call and the genuinely contested ones get routed back to you.

**2. Building and automating the pipeline.** Researchers use coding agents to write the plumbing around pattern 1: the batch loop, the retry logic, the SLURM script, the plots. The researcher stays the designer and reviewer; the agent handles the parts that are tedious rather than intellectual. You'll do exactly this on Day 3 when you have Claude Code write a SLURM job.

**3. Studying AI itself.** A growing body of work here treats the model as the subject: how humans interact with AI systems, whether people over-trust or under-trust them, and how AI is reshaping the workforce, tasks, and labor markets. If your research is *about* AI rather than *assisted by* AI, the governance picture flips. Your participants are human subjects again, so IRB and consent come back to the front, and the data you protect is theirs, not the model's.

{: .note }
> **Class discussion:** Which of the three is closest to your own work? For pattern 1, what would a wrong extraction cost you: a noisy estimate, or a retracted claim? That answer determines how much validation is enough.

---

### AI services at Stanford

Stanford runs a growing catalog: chat interfaces, the API gateway you used today, cloud AI (AWS Bedrock, Azure OpenAI, Google Vertex), and locally hosted models. The list changes, so browse it rather than memorize it: [Stanford AI Services](https://uit.stanford.edu/ai/services).

Two very different jobs hide behind "using AI," and they carry different risks.

**Job 1: an LLM analyzes your data.** Your data *is* the input, the way you fed filing text to the model in [The Oracle's Chamber](../oracles-chamber/). One question decides everything: *is this data allowed to go where this model runs?*

| Risk level | Examples | Stanford API Gateway | Local model (Yens) | Third-party tool/API |
|------------|----------|---------------------|--------------------|----------------------|
| 🟢 **Low** | Published papers, SEC filings, open datasets | ✅ | ✅ | ✅ |
| 🟡 **Moderate** | Unpublished research, FERPA records, DUA-covered data | ✅ | ✅ | ❌ unless approved |
| 🔴 **High (incl. PHI)** | SSNs, account numbers, health records, credentials | ✅† | ❌* | ❌ |

<small>*<strong>The Yens are approved for Low and Moderate risk data, not High.</strong> Running the model locally keeps your data on the machine, but that only helps if the data is allowed on that machine in the first place — and High Risk data isn't allowed on the Yens at all. High Risk work belongs on a system cleared for it, which at Stanford means <a href="https://docs.carina.stanford.edu/" target="_blank" rel="noopener noreferrer">Carina</a> (on-premises, Slurm-based) or <a href="https://nero-docs.stanford.edu/" target="_blank" rel="noopener noreferrer">Nero GCP</a> (secure Google Cloud) rather than the Yens; sort that out before you copy anything anywhere.</small><br>
<small>†API Gateway only. The **Playground chat window** runs under the same Stanford contract but stops short of PHI, so when PHI is involved reach for the API, not the chat box.</small>

{: .warning }
> **Two separate questions, and people routinely collapse them into one.** *Is this data allowed on this machine?* and *is this data allowed to go to this model?* A local model on the Yens answers the second question well and says nothing at all about the first. The Yens are a Moderate-risk environment, so "I'll just run it locally" is not a way to work with High Risk data — it's a way to put High Risk data somewhere it shouldn't be.

The gateway clears every row because it runs under Stanford's contract rather than a vendor's consumer terms. The risk usually isn't your data, it's reaching for a convenient tool outside Stanford's walls.

**DUA and IRB still govern.** Either can be stricter than Stanford's classification, for example "data may not leave these systems." Read yours; when a DUA restricts where data is processed, the local path on the Yens is the safe default.

**Job 2: an LLM helps you build the pipeline.** Pattern 2 above. Your data isn't meant to be the input, but it slips in anyway: a data file left open, a hardcoded path, a comment quoting a real record. The risk isn't what you chose to send, it's what the harness sweeps up around it, and the next section keeps it in check.

**The practical rule:** if you wouldn't paste it into a Google Doc, don't paste it into an agent's context.

{: .note }
> **Class discussion:** The SEC filings you processed today, which risk level? What changes if you switch to ChatGPT? And if the filings contained unreported insider PII, which paths would still be allowed?

---

### Keeping data out of agent context

- Never hardcode secrets, keys, or paths containing PII in files open in an AI tool
- Keep credentials in `.env`, and `.env` in `.gitignore`
- Close files containing restricted data before using a coding assistant
- Exclude `data/` and `results/` from the tool's workspace or project settings, which control what gets indexed
- A coding agent calling a third-party endpoint (Claude Code to Anthropic, Copilot to GitHub) is not covered by Stanford's agreements, so the same rules apply. "I'm just asking for coding help" doesn't change where your data goes.

{: .note }
> **Class discussion:** You're using Claude Code to write a SLURM script. It references a path to a data file. Does the model see the data? What if the script has a hardcoded API key? What about a comment mentioning a patient's condition?

---

### What it costs

Risk decides what you *may* send. Cost decides what you can afford to send at scale.

You met the headline in [The Stanford AI Playground](../stanford-ai-playground/): the chat window is free, the API Gateway is metered. Here is where the meter actually runs.

<svg viewBox="0 0 1000 400" role="img" aria-labelledby="cost-flow-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:1000px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="cost-flow-title">Where the money goes in a single API call. Everything you send — your prompt, the filing text, the schema — is billed as input tokens. Inside the model, a reasoning model may generate hidden thinking that is billed as output tokens even though it is never shown to you. Everything you read back is billed as output tokens as well. Output is priced higher than input, and both rates depend on which model you chose. The meter runs three times per call, and only one of those three is visible in the reply you read.</title>
  <defs>
    <marker id="cost-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- what you send -->
  <rect x="20" y="118" width="205" height="140" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="122" y="158" text-anchor="middle" font-size="17" font-weight="700" fill="#2c3e50">📤  what you send</text>
  <text x="122" y="190" text-anchor="middle" font-size="14" fill="#9a8a68">your prompt</text>
  <text x="122" y="214" text-anchor="middle" font-size="14" fill="#9a8a68">the filing text</text>
  <text x="122" y="238" text-anchor="middle" font-size="14" fill="#9a8a68">the schema</text>

  <!-- arrow 1 + meter badge -->
  <line x1="228" y1="188" x2="384" y2="188" stroke="#556a95" stroke-width="2.5" marker-end="url(#cost-ah)"/>
  <rect x="244" y="136" width="126" height="30" rx="8" fill="#fff6e5" stroke="#dcae6a" stroke-width="1.4"/>
  <text x="307" y="156" text-anchor="middle" font-size="14" font-weight="700" fill="#b3611a">💰 input</text>

  <!-- the model -->
  <rect x="388" y="95" width="240" height="205" rx="16" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.8"/>
  <text x="508" y="130" text-anchor="middle" font-size="17" font-weight="700" fill="#2c3e50">🧠  the model</text>
  <rect x="402" y="152" width="212" height="88" rx="10" fill="#ffffff" stroke="#9db8d8" stroke-width="1.4" stroke-dasharray="6 5"/>
  <text x="508" y="180" text-anchor="middle" font-size="14.5" font-weight="700" fill="#3f4f74">thinking you never see</text>
  <text x="508" y="203" text-anchor="middle" font-size="12.5" fill="#6a7280">some models reason first</text>
  <text x="508" y="226" text-anchor="middle" font-size="12.5" font-weight="700" fill="#b3611a">💰 billed as output</text>
  <text x="508" y="272" text-anchor="middle" font-size="12.5" font-style="italic" fill="#8a94a6">invisible on your screen</text>

  <!-- arrow 2 + meter badge -->
  <line x1="631" y1="188" x2="787" y2="188" stroke="#556a95" stroke-width="2.5" marker-end="url(#cost-ah)"/>
  <rect x="638" y="136" width="142" height="30" rx="8" fill="#fff6e5" stroke="#dcae6a" stroke-width="1.4"/>
  <text x="709" y="156" text-anchor="middle" font-size="14" font-weight="700" fill="#b3611a">💰💰 output</text>

  <!-- what you read -->
  <rect x="790" y="118" width="190" height="140" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="885" y="158" text-anchor="middle" font-size="17" font-weight="700" fill="#2c3e50">📥  what you read</text>
  <text x="885" y="192" text-anchor="middle" font-size="14" fill="#9a8a68">the reply</text>
  <text x="885" y="222" text-anchor="middle" font-size="12.5" font-style="italic" fill="#8a94a6">the only part</text>
  <text x="885" y="242" text-anchor="middle" font-size="12.5" font-style="italic" fill="#8a94a6">you actually see</text>

  <!-- summary band -->
  <line x1="60" y1="330" x2="940" y2="330" stroke="#e6cfa8" stroke-width="1"/>
  <text x="500" y="362" text-anchor="middle" font-size="15.5" font-weight="700" fill="#2c3e50">The meter runs three times. You see one of them.</text>
  <text x="500" y="386" text-anchor="middle" font-size="13.5" fill="#6a7280">Output is priced higher than input, and both rates depend on the model you picked.</text>
</svg>

Three levers, then, before you scale a run:

| Lever | The decision you're making |
|---|---|
| **How much you send** | The `[:4000]` slice in The Oracle's Chamber was a cost decision as much as a context-limit one |
| **Which model** | The cheapest and most expensive ids on the gateway are not close |
| **Whether it reasons** | A three-word answer can cost thousands of output tokens you never see |

Rates change, so look them up rather than trusting a number in a slide deck: **<a href="https://uit.stanford.edu/service/ai-api-gateway/rates" target="_blank" rel="noopener noreferrer">AI API Gateway rates</a>**.

#### AI coding agents: a plan, not a meter

There's no meter on this side at all. Claude Code, Copilot, and the rest are **licensed**, and everyday use is **free to you** as a Stanford affiliate; need more than the standard allowance and your **PI requests an upgraded plan** — a fixed cost paid up front, not a per-keystroke charge.

| | API Gateway | Coding agent |
|---|---|---|
| **Billing** | Per token, per model | Flat plan; standard tier free |
| **A runaway loop** | Spends real money, immediately | Burns your allowance, then stops |
| **Scaling up** | Costs more, in proportion | Needs a request through your PI |
| **What to plan** | Measure on a sample, then multiply | Ask early; approval takes time |

Neither is "the cheap one." The gateway is nearly free for a small job and expensive for a careless one; an agent plan costs the same whether you lean on it or never log in.

#### Same answer, 22× the bill

Models such as `o1`, `o3-mini`, `deepseek-r1`, and the `gpt-5` family reason internally before answering. One trick question, three models, all three correct in about forty words — here is what each one charged:

<svg viewBox="0 0 1000 320" role="img" aria-labelledby="tok-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:1000px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="tok-title">Output tokens billed for the same one-line answer, by model. gemini-2.5-flash-lite was billed 27 output tokens, all of them the reply you can read. o3-mini was billed 236, of which it reported 192 as hidden reasoning — 81 percent of the charge for text never shown to the user. deepseek-r1 was billed 595 output tokens, 22 times gemini's total; it reported no breakdown, but its visible reply is only about 47 tokens, so roughly 548 of them must have been reasoning. The length of the visible reply is no guide to what a call costs.</title>

  <!-- legend -->
  <rect x="190" y="20" width="12" height="12" rx="2" fill="#b3611a"/>
  <text x="209" y="31" font-size="13.5" fill="#6a7280">output you can read</text>
  <rect x="352" y="20" width="12" height="12" rx="2" fill="#3f4f74"/>
  <text x="371" y="31" font-size="13.5" fill="#6a7280">reasoning, reported</text>
  <rect x="512" y="20" width="12" height="12" rx="2" fill="#3f4f74" stroke="#ffffff" stroke-width="1.4" stroke-dasharray="3 2"/>
  <text x="531" y="31" font-size="13.5" fill="#6a7280">reasoning, inferred</text>

  <!-- baseline -->
  <line x1="189" y1="52" x2="189" y2="234" stroke="#e6cfa8" stroke-width="1"/>

  <!-- gemini-2.5-flash-lite : 27 output, no reasoning -->
  <text x="178" y="83" text-anchor="end" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">gemini-2.5-flash-lite</text>
  <path d="M190,62 H209 Q213,62 213,66 V90 Q213,94 209,94 H190 Z" fill="#b3611a"/>
  <text x="223" y="83" font-size="14" font-weight="700" fill="#2c3e50">27</text>

  <!-- o3-mini : 236 = 44 shown + 192 reported reasoning -->
  <text x="178" y="147" text-anchor="end" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">o3-mini</text>
  <rect x="190" y="126" width="38" height="32" fill="#b3611a"/>
  <path d="M230,126 H391 Q395,126 395,130 V154 Q395,158 391,158 H230 Z" fill="#3f4f74"/>
  <text x="312" y="147" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">192 reported</text>
  <text x="405" y="147" font-size="14" font-weight="700" fill="#2c3e50">236<tspan font-weight="400" fill="#8a94a6"> — 81% of it hidden</tspan></text>

  <!-- deepseek-r1 : 595, no breakdown reported; ~47 visible so ~548 inferred -->
  <text x="178" y="211" text-anchor="end" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2c3e50">deepseek-r1</text>
  <rect x="190" y="190" width="39" height="32" fill="#b3611a"/>
  <path d="M231,190 H698 Q702,190 702,194 V218 Q702,222 698,222 H231 Z" fill="#3f4f74" stroke="#ffffff" stroke-width="1.6" stroke-dasharray="6 5"/>
  <text x="466" y="211" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">≈548 inferred — it reported nothing</text>
  <text x="712" y="211" font-size="14" font-weight="700" fill="#2c3e50">595<tspan font-weight="400" fill="#8a94a6"> — 92% of it hidden</tspan></text>

  <!-- caption -->
  <text x="500" y="272" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">Same question. Same answer. 22× the bill.</text>
  <text x="500" y="296" text-anchor="middle" font-size="12.5" fill="#8a94a6">deepseek-r1 reported no breakdown — but its visible reply is ~47 tokens, so the other ~548 went somewhere.</text>
</svg>

Nothing is broken here; that's how these models work. The trap is reading cost off the length of the reply, so read `usage` instead. If you want to watch it happen on a live call, the *Pay for Thinking You Never See* side quest in [The Oracle's Chamber](../oracles-chamber/) runs exactly this comparison.

{: .note }
> **Class discussion:** You budget a 10,000-filing run by timing 10 filings and multiplying. What could make the real bill come in far higher? (Think: a longer filing, a model swap, a retry loop, a reasoning model.) Which of those would you catch before spending the money, and how? Now ask the same question about a semester of Claude Code use, where the failure isn't an invoice but running out of allowance the week before a deadline.

---

### Designing defensible research pipelines

A pipeline is defensible when a skeptical colleague can audit it end-to-end. Before you scale:

1. **Classify your data.** Which risk level? Which tool does that allow?
2. **Cost it on a sample.** Measure `usage` on a handful of real records, then multiply, before you launch the full run.
3. **Validate your outputs.** A Pydantic schema plus a manual spot-check on 10 to 20 examples.
4. **Document your decisions.** A README covering what the pipeline does, what model, what prompt version, and what validation was run.
5. **Keep humans in the loop for high-stakes steps.** Extraction is fine to automate; acting on that extraction may not be.

<label class="quest-check"><input type="checkbox" data-room="d2-human-vs-llm" data-key="main"> Crucible complete: I understand what AI coding agents send, how to classify my data, what it costs, and how to design a defensible pipeline</label>

---

## 🧠 Skills Learned

- You can describe what AI coding agents send to remote servers and what that means for research data
- You know how to configure AI tools to exclude sensitive data from their context
- You can classify any dataset by Stanford's risk level and choose the right tool without guessing
- You can tell the two billing models apart: the API Gateway meters you per token, while coding agents run on a plan, and you know which failure each one sets you up for
- You know that reasoning models charge for output you never see, so the length of a reply is no guide to its cost
- You can place your own work among the ways researchers use AI, and say whether the model is your instrument or your subject
- You can design a validation step proportional to the stakes of the task
- You can write a pipeline that a skeptical colleague could audit: classified data, documented decisions, outputs you actually read
