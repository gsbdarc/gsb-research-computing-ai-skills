---
layout: default
title: "The Arcane Notebook"
parent: "Day 1 — The Gatehouse"
nav_order: 7
permalink: /day1/arcane-notebook/
---

# The Arcane Notebook

<div data-room-id="d1-arcane-notebook"></div>

*You push open a heavy oak door and step into a firelit study. The shelves stretch floor-to-ceiling, stacked with glowing notebooks that hum with quiet power — each one running not on your laptop, but on the dungeon's own iron engines deep below. Every page is a cell. Every cell is a spell: conjure charts, interrogate data, summon results from thousands of rows in a breath. The warmth in the air comes from the Yens. You're just the one holding the quill.*

---

## 🗡️ Main Quest

The notebook is open. The kernel is live. All that's left is to prove you're the one casting the spells — not your laptop.

{: .important }
> **Quest:** Open JupyterHub on the Yens, start a notebook, and run a cell — all from your browser.

**Open JupyterHub:**

Navigate to [https://jupyter.yen.stanford.edu](https://jupyter.yen.stanford.edu) in your browser and log in with your SUNet credentials. Start a server if prompted.

**Create a notebook:**

- Click **New → Python 3** (or select an existing kernel)
- In the first cell, type and run:

```python
import os
print("Running on:", os.uname().nodename)
print("Python location:", os.sys.executable)
```

- Press **Shift+Enter** to run the cell. The output should show a Yens hostname — not your laptop.

**Understand the kernel:**

The kernel is the Python process running your code. When you close the browser, the kernel keeps running on the Yens. Your code's state (variables, imports) lives in the kernel, not the file.

```python
x = 42          # assign in one cell
print(x)        # run in a later cell — it still works (same kernel)
```

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Hidden in the study's locked drawers are tools that separate the apprentice from the archmage — crack them open.

{: .chest }
> **Side Quest 1 — Magic Scroll:** Learn three keyboard shortcuts that will save you hours: run-and-advance, insert cell below, and interrupt kernel. Then use `%time` to measure how long a cell takes to run.

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="side1"> Magic Scroll unlocked</label>

The second side quest glows with a terminal's green light — the notebook and the shell, fused into one fearsome tool.

{: .chest }
> **Side Quest 2 — Shell Tome:** Run a shell command directly inside a Jupyter cell using `%%bash`. Use it to list your grimoire directory on the Yens. Then run `!hostname` (single `!`) in a Python cell. What's the difference between `%%bash` and `!`?

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="side2"> Shell Tome unlocked</label>

The third side quest is engraved with ancient runes that speed your hands across every cell without ever reaching for the mouse.

{: .chest }
> **Side Quest 3 — Vim Sigil:** Enable Vim keybindings in JupyterHub (Settings → Keyboard shortcuts or the Vim extension). Navigate between cells in command mode using `j`/`k`. Why might a researcher bother learning this?

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="side3"> Vim Sigil unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Magic Scroll** — keyboard shortcuts for Jupyter that cut cell management time in half; `%time` and `%timeit` to measure performance without writing a timer.
>
> **Shell Tome** — `%%bash` magic cell to run shell commands inside Jupyter; mix Python and shell in a single notebook workflow.
>
> **Vim Sigil** — Vim keybindings in Jupyter; navigate and edit notebooks without leaving the home row.

---

## 🧠 Skills Learned

- You can now open JupyterHub and run Python on Yens hardware from any browser — no SSH, no setup, no excuses
- You understand what a kernel is: the persistent Python process that outlives your browser tab and remembers everything
- You know the kernel keeps running after you close the browser — a superpower when used wisely, a trap when forgotten
- You can tell the difference between running code on your laptop and running it on the cluster — and you know why it matters
