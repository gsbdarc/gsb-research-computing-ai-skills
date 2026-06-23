---
layout: default
title: "The AI Scribe"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 7
permalink: /day2/ai-scribe/
---

# The AI Scribe

<div data-room-id="d2-ai-scribe"></div>

*In the deepest alcove of the Alchemist's Lab hovers a luminous quill — the AI Scribe. It writes faster than any mortal hand, conjuring functions and logic from plain words alone. But the Scribe is a powerful ally, not an oracle: it has invented SLURM flags that do not exist, returned Python functions that almost work, and confidently explained code that does the wrong thing. The researcher who wields it is not a passive passenger — they are the commander who directs the quill and the judge who catches its errors before they detonate.*

---

## 🗡️ Main Quest

You step up to the Scribe's pedestal. The quill hovers, waiting. Your task: summon it, command it, and keep your eyes open.

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
> ⚠️ **The one security rule:** Never paste API keys, restricted dataset samples, or PII into a Claude Code prompt. Claude Code sends your prompt to Anthropic's servers. The same rules as any other cloud API apply.

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Two side quests await — each one rewards a sharper, more dangerous command of the Scribe.

{: .chest }
> **Side Quest 1 — Prompt Blade:** The generated script has at least one thing you'd write differently. Identify it and write a better prompt that produces a cleaner result. What made the second prompt better?

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="side1"> Prompt Blade unlocked</label>

The second side quest holds the secret that separates novices from true Scribe commanders: give the Scribe context and it transforms from a guesser into a collaborator.

{: .chest }
> **Side Quest 2 — Context Tome:** Feed Claude Code your Day 3 SLURM job script (from yesterday's hypothetical) and ask it to explain each `#SBATCH` directive and suggest two improvements. Verify whether each suggestion is correct before accepting it.

<label class="quest-check"><input type="checkbox" data-room="d2-ai-scribe" data-key="side2"> Context Tome unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Prompt Blade** — write precise coding prompts that specify inputs, outputs, error handling, and constraints; get useful output from AI tools instead of plausible-looking boilerplate.
>
> **Context Tome** — feed AI tools existing code for explanation and improvement; use AI as a code reviewer, not just a writer.

---

## 🧠 Skills Learned

- 💡 You can now summon Claude Code on the Yens and put it to work on real research code
- 💡 You can now run the "direct, then verify" workflow — AI drafts, you judge, nothing executes unseen
- 💡 You can now enforce the security rule: keys, restricted data, and PII never leave your terminal in a prompt
- 💡 You can now craft prompts that specify inputs, outputs, edge cases, and constraints — so the Scribe delivers signal, not noise
