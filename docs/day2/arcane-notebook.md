---
layout: default
title: "The Arcane Notebook"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 2
permalink: /day2/arcane-notebook/
---

# The Arcane Notebook

<div data-room-id="d2-arcane-notebook"></div>

*You push open a heavy oak door and step into a firelit study. The shelves stretch floor-to-ceiling, stacked with glowing notebooks that hum with quiet power — each one running not on your laptop, but on the dungeon's own iron engines deep below. Every page is a cell. Every cell is a spell: conjure charts, interrogate data, summon results from thousands of rows in a breath. The warmth in the air comes from the Yens. You're just the one holding the quill.*

---

## 🔰 Warm-Up: SSH Check

Before opening any notebooks, confirm you're on the Yens.

```bash
ssh SUNetID@yen.stanford.edu
```

Once connected:

```bash
hostname          # which Yen did you land on?
whoami            # are you logged in as yourself?
pwd               # what directory are you in?
ls                # do you see files from Day 1?
```

You should see your home directory and the `rf-bootcamp-2026` folder you cloned yesterday.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Open JupyterHub on the Yens, run a Python cell in a notebook, then run the same code as a script from the terminal.

---

### Step 1 — Open JupyterHub

JupyterHub is a browser-based interface to the Yens. Choose any node:

| Node | URL |
|------|-----|
| Yen1 | [yen1.stanford.edu/jupyter/hub/home](https://yen1.stanford.edu/jupyter/hub/home) |
| Yen2 | [yen2.stanford.edu/jupyter/hub/home](https://yen2.stanford.edu/jupyter/hub/home) |
| Yen3 | [yen3.stanford.edu/jupyter/hub/home](https://yen3.stanford.edu/jupyter/hub/home) |
| Yen4 | [yen4.stanford.edu/jupyter/hub/home](https://yen4.stanford.edu/jupyter/hub/home) |
| Yen5 | [yen5.stanford.edu/jupyter/hub/home](https://yen5.stanford.edu/jupyter/hub/home) |

Log in with your SUNet credentials. You should see the same files as your home directory on the Yens.

---

### Step 2 — Start a Notebook and a Terminal

- Click the **blue "+"** to open the Launcher
- Start a **Python 3** notebook
- Also open a **Terminal** tab — you'll switch between the two throughout Day 2

---

### Step 3 — Run a Cell

Type this into a cell and run with **Shift+Enter**:

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

Expected output: `15`

---

### Step 4 — Run the Same Code as a Script

In the **terminal tab**, create a file and paste the same code:

```bash
echo "numbers = [1, 2, 3, 4, 5]" > test.py
echo "print(sum(numbers))" >> test.py
python3 test.py
```

Same output, different workflow. Notebooks are good for exploration; scripts are what you submit to the cluster. For the rest of Day 2, you will write scripts.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="main"> Main Quest complete</label>

---

## 🧠 Skills Learned

- You can open JupyterHub on the Yens and run Python from any browser
- You know the difference between a notebook cell and a script — and when each is useful
- You can run a `.py` script from the terminal, which is how cluster jobs work
