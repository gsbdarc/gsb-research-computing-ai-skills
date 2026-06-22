---
layout: default
title: "The Primer Chamber"
parent: "Day 1 — The Gatehouse"
nav_order: 9
permalink: /day1/primer-chamber/
---

# The Primer Chamber

<div data-room-id="d1-primer-chamber"></div>

*A quiet antechamber before the exit. Four illuminated panels on the wall. No keyboards, no commands — just four pictures drawn together that explain what you will be doing for the rest of this course. The magic ahead is less mysterious once you understand the mechanism.*

---

## Main Quest

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

## Skills Learned

- Understand that LLMs predict tokens, not sentences — and what that means for reliability
- Know what a context window is and why it limits what the model can "remember"
- Understand the difference between a single LLM call and an agent loop
- Have a mental model to stand on when writing prompts and interpreting outputs starting Day 2
