---
layout: default
title: "The Arcane Notebook"
parent: "Day 1 — The Gatehouse"
nav_order: 7
permalink: /day1/arcane-notebook/
---

# The Arcane Notebook

<div data-room-id="d1-arcane-notebook"></div>

*A firelit study, its shelves lined with glowing notebooks that run on the dungeon's own engines — not your laptop. Each page is a cell. Each cell can cast spells in Python, draw charts, query data, and print results. The fire comes from the Yens; you're just holding the quill.*

---

## Main Quest

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

## Chests

{: .chest }
> **Chest 1 — Magic Scroll:** Learn three keyboard shortcuts that will save you hours: run-and-advance, insert cell below, and interrupt kernel. Then use `%time` to measure how long a cell takes to run.

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="chest1"> Magic Scroll unlocked</label>

{: .chest }
> **Chest 2 — Shell Tome:** Run a shell command directly inside a Jupyter cell using `%%bash`. Use it to list your grimoire directory on the Yens. Then run `!hostname` (single `!`) in a Python cell. What's the difference between `%%bash` and `!`?

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="chest2"> Shell Tome unlocked</label>

{: .chest }
> **Chest 3 — Vim Sigil:** Enable Vim keybindings in JupyterHub (Settings → Keyboard shortcuts or the Vim extension). Navigate between cells in command mode using `j`/`k`. Why might a researcher bother learning this?

<label class="quest-check"><input type="checkbox" data-room="d1-arcane-notebook" data-key="chest3"> Vim Sigil unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Magic Scroll** — keyboard shortcuts for Jupyter that cut cell management time in half; `%time` and `%timeit` to measure performance without writing a timer.
>
> **Shell Tome** — `%%bash` magic cell to run shell commands inside Jupyter; mix Python and shell in a single notebook workflow.
>
> **Vim Sigil** — Vim keybindings in Jupyter; navigate and edit notebooks without leaving the home row.

---

## Skills Learned

- Open and use JupyterHub to run Python on Yens hardware from a browser
- Understand what a kernel is: the live Python process behind the notebook
- Know that the kernel persists when the browser closes — and that this is both useful and dangerous
- Distinguish between running code on your laptop vs. on the cluster
