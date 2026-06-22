---
layout: default
title: "The Primer Chamber"
parent: "Day 1 — The Gatehouse"
nav_order: 9
permalink: /day1/primer-chamber/
---

# The Primer Chamber

<div data-room-id="d1-primer-chamber"></div>

*A hushed antechamber glows with four stone panels, each etched with a diagram that pulses with soft blue light. No terminal, no keyboard — only chalk and a whiteboard standing between you and the secret the whole course runs on. The dragons ahead breathe fire you can predict, if you understand what fire actually is.*

---

## 🗡️ Main Quest

Sharpen your mental blade before you draw it — these four pictures are the hidden blueprint behind every LLM tool you'll wield this week.

{: .important }
> **Quest:** Build a working mental model of how LLMs work by drawing four pictures together with the class.

This is a concept block — there is no hands-on exercise. Follow along with the whiteboard.

**Picture 1 — Token**

Text is not fed into a model as characters. It is split into **tokens** — subword chunks. "Grimoire" might be one token. "Counterintuitive" might be three. The model never sees the letter `G`; it sees a number representing the token `Grim`.

**Picture 2 — Context Window**

The model reads all tokens in the **context window** at once — everything in the prompt plus everything generated so far. There is a maximum length. When context fills up, the model can no longer "see" earlier parts of the conversation.

**Picture 3 — Prompt → Completion**

The model takes a prompt (your input tokens) and predicts the most likely next token, then the next, then the next — until it decides to stop. That sequence of predicted tokens is the **completion**. There is no understanding, no memory between calls — just prediction.

**Picture 4 — Agent**

An **agent** is a loop: prompt the model → get a response → (optionally) call a tool → feed the result back into the next prompt → repeat. The "AI that can browse the web and write code" is this loop run many times. Your research pipelines on Day 3 and Day 4 will be agents.

{: .note }
> The course bot you can open in the corner of this page is an example of Picture 4. It has a system prompt, access to the course content as context, and returns completions. Nothing more.

<label class="quest-check"><input type="checkbox" data-room="d1-primer-chamber" data-key="main"> Primer complete — I have a mental model of tokens, context windows, completions, and agents</label>

---

## 🧠 Skills Learned

- You can now explain why an LLM sometimes fumbles — it predicts tokens, not sentences, and probability is not truth
- You can now reason about context windows: you know why the model "forgets" and how to work with that limit, not against it
- You can now tell a single LLM call apart from an agent loop — and recognize which one you're looking at in the wild
- You now carry a mental map that makes every prompt you write starting Day 2 a deliberate act, not a guess
