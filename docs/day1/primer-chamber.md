---
layout: default
title: "The Primer Chamber"
parent: "Day 1 — The Gatehouse"
nav_order: 9
permalink: /day1/primer-chamber/
---

# The Primer Chamber

<div data-room-id="d1-primer-chamber"></div>

*A hushed antechamber glows with four stone panels, each etched with a diagram that pulses with soft blue light. No terminal, no keyboard — only four pictures carved into the dungeon wall, the blueprint behind every LLM tool you will wield this week. The dragons ahead breathe fire you can predict, if you understand what fire actually is.*

---

## 🗡️ Main Quest

Sharpen your mental blade before you draw it — these four pictures are the hidden blueprint behind every LLM tool you'll wield this week.

{: .important }
> **Quest:** Build a working mental model of how LLMs work — four diagrams, four concepts.

This is a concept block — there is no hands-on exercise.

---

**Picture 1 — Token**

Text is not fed into a model as characters. It is split into **tokens** — subword chunks. "Grimoire" might be one token. "Counterintuitive" might be three. The model never sees letters; it sees numbers.

```
Your text:  "Grimoire has 300 spells"
                 │
                 ▼  tokenizer splits into subword chunks
Tokens:     ["Grim", "oire", " has", " 300", " spells"]
                 │
                 ▼  each token maps to a number
Numbers:    [  4821,   892,   318,   2318,    805  ]
                 │
                 ▼  this sequence of numbers is what the model reads
```

---

**Picture 2 — Context Window**

The model reads all tokens at once — but only up to a fixed limit. When the window fills, the model can no longer see the beginning of the conversation.

```
┌──────────────────────── context window (e.g. 200,000 tokens) ─────────────────────────┐
│  [system prompt]  [your messages]  [model replies so far]  [← predicting next token]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
   Everything inside: model can see it.
   Anything pushed out the left side: gone — the model has no memory of it.
```

---

**Picture 3 — Prompt → Completion**

The model predicts the most likely next token, then the next, then the next — until it decides to stop. No lookup, no understanding. Just: *given all tokens so far, what comes next?*

```
Prompt:  "Extract the insider's name from this SEC filing: ..."
              │
              ▼  model predicts next token, then next, then next
  Step 1:  "John"      ← highest probability next token
  Step 2:  " Smith"    ← highest probability given "John"
  Step 3:  "\n"        ← sentence complete
  Step 4:  [stop]      ← model decides to stop
              │
              ▼
Completion:  "John Smith"
```

---

**Picture 4 — Agent**

An **agent** is a loop: prompt → response → (optional) tool call → result feeds back into the next prompt → repeat. The "AI that can browse the web and write code" is this loop, run many times.

```
  ┌─────────────────────────────────┐
  │  Prompt                         │
  │  (system prompt + history       │◄──────────────┐
  │   + new input + tool results)   │               │ tool result
  └────────────────┬────────────────┘               │
                   │                                 │
                   ▼                                 │
            ┌──────────────┐                         │
            │    Model     │                         │
            └──────┬───────┘                         │
                   │ response                        │
                   ▼                                 │
        ┌──────────────────────┐                     │
        │  Tool call?          │── yes → run tool ───┘
        │  (read file, grep,   │
        │   API call, search)  │── no  → final answer → done
        └──────────────────────┘
```

Your Day 3 SLURM pipeline and Day 4 Ollama pipeline are both Picture 4.

{: .note }
> The course bot you can open in the corner of this page is an example of Picture 4. It has a system prompt, access to the course content as context, and returns completions. Nothing more.

<label class="quest-check"><input type="checkbox" data-room="d1-primer-chamber" data-key="main"> Primer complete — I have a mental model of tokens, context windows, completions, and agents</label>

---

## 🧠 Skills Learned

- You can now explain why an LLM sometimes fumbles — it predicts tokens, not sentences, and probability is not truth
- You can now reason about context windows: you know why the model "forgets" and how to work with that limit, not against it
- You can now tell a single LLM call apart from an agent loop — and recognize which one you're looking at in the wild
- You now carry a mental map that makes every prompt you write starting Day 2 a deliberate act, not a guess
