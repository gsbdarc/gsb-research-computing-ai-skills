---
layout: default
title: "The AI Scribe"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 6
permalink: /day2/ai-scribe/
---

# The AI Scribe

<div data-room-id="d2-ai-scribe"></div>

*A quill that writes on your behalf — but only if you guide it precisely. The Scribe is fast and usually right. It has also, on occasion, invented a SLURM flag that does not exist and written a Python function that almost works. The researcher's job is to direct, then verify.*

---

## Main Quest

{: .important }
> **Quest:** Install Claude Code, configure it for the Yens, and use it to write a Python script that you verify before running.

**Install Claude Code** (on the Yens, inside your venv):

```bash
source .venv/bin/activate
pip install claude-code   # or follow the official install instructions your instructor provides
```

**Configure:**

Claude Code runs in your terminal. It can read your project files and write code, but you review everything before it executes. Never paste your Stanford AI Playground key or any restricted data into the Claude Code prompt.

**Use it to write a script:**

```bash
claude "Write a Python script that reads all .spell files from a directory passed as the first argument and prints a count of files per element. Save it as count_spells.py"
```

Review the generated script before running it:
- Does it handle the case where the directory doesn't exist?
- Does it correctly parse the filename format `name_element_tier_type_mastery.spell`?
- Would you be comfortable submitting this as your own work?

Run it:
```bash
python count_spells.py ~/grimoire/
```

{: .warning }
> **The one security rule:** Never paste API keys, restricted dataset samples, or PII into a Claude Code prompt. Claude Code sends your prompt to Anthropic's servers. The same rules as any other cloud API apply.

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Prompt Blade:** The generated script has at least one thing you'd write differently. Identify it and write a better prompt that produces a cleaner result. What made the second prompt better?

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="chest1"> Prompt Blade unlocked</label>

{: .chest }
> **Chest 2 — Context Tome:** Feed Claude Code your Day 3 SLURM job script (from yesterday's hypothetical) and ask it to explain each `#SBATCH` directive and suggest two improvements. Verify whether each suggestion is correct before accepting it.

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="chest2"> Context Tome unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Prompt Blade** — write precise coding prompts that specify inputs, outputs, error handling, and constraints; get useful output from AI tools instead of plausible-looking boilerplate.
>
> **Context Tome** — feed AI tools existing code for explanation and improvement; use AI as a code reviewer, not just a writer.

---

## Skills Learned

- Install and use Claude Code as a research coding tool on the Yens
- Understand the "direct, then verify" workflow: AI writes a draft, you check it before running
- Apply the security rule: no keys, no restricted data, no PII in AI prompts
- Write better prompts that specify the exact behavior you need
