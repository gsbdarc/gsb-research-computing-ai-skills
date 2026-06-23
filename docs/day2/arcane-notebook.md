---
layout: default
title: "The Arcane Notebook"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/arcane-notebook/
---

# The Arcane Notebook

<div data-room-id="d2-arcane-notebook"></div>

*You push open a heavy oak door and step into a firelit study. The shelves stretch floor-to-ceiling, stacked with glowing notebooks that hum with quiet power — each one running not on your laptop, but on the dungeon's own iron engines deep below. Every page is a cell. Every cell is a spell: conjure charts, interrogate data, summon results from thousands of rows in a breath. The warmth in the air comes from the Yens. You're just the one holding the quill.*

---

## 🗡️ Main Quest

The notebook is open. The kernel is live. All that's left is to prove you're the one casting the spells — not your laptop.

{: .important }
> **Quest:** Open JupyterHub on the Yens, start a notebook, run a cell — then connect the venv you just built as a kernel.

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

**Connect your venv as a kernel:**

After completing the Venv Forge, your virtual environment can be selected as a kernel in JupyterHub. Pick it from the kernel menu — your notebook will now run with your project's exact dependencies.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

*Additional side quests coming soon.*

---

## 🧠 Skills Learned

- You can now open JupyterHub and run Python on Yens hardware from any browser — no SSH required
- You understand what a kernel is: the persistent Python process that outlives your browser tab and remembers everything
- You know the kernel keeps running after you close the browser — a superpower when used wisely, a trap when forgotten
- You can connect a virtual environment as a JupyterHub kernel, ensuring your notebook uses the right dependencies
