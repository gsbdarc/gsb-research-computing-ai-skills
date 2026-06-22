---
layout: default
title: "The Venv Forge"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 2
permalink: /day2/venv-forge/
---

# The Venv Forge

<div data-room-id="d2-venv-forge"></div>

*Deep in the Alchemist's Lab, the forge blazes with a fierce, contained light. Every serious project demands its own crucible — a sealed vessel where dependencies are bound to one purpose and one purpose only. Pour the wrong reagent into the wrong crucible and the contamination cascades, poisoning every experiment downstream. The Forge was built to stop that. Step inside, heat your crucible, and pour your ingredients with precision. One project. One environment. No exceptions.*

---

## 🗡️ Main Quest

Step up to the forge and claim your isolated environment — this is the foundation every reproducible research project is built on.

{: .important }
> **Quest:** Create a virtual environment for your research project, activate it, install packages, and connect it to JupyterHub as a kernel.

**On the Yens:**

```bash
# Create a venv in your project directory
cd ~/rf_bootcamp_2026
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Your prompt should now show (.venv) — you're inside the environment
which python       # should point inside .venv, not /usr/bin/python

# Install packages
pip install requests pydantic python-dotenv ipykernel

# Register the venv as a Jupyter kernel
python -m ipykernel install --user --name bootcamp --display-name "Bootcamp 2026"
```

**In JupyterHub:**

Refresh the page. When you create a new notebook, select **"Bootcamp 2026"** as the kernel. Packages you installed into `.venv` are now available.

**Deactivate when done:**
```bash
deactivate
```

{: .note }
> 💡 The `.venv` directory lives inside your project. It is never committed to git — add `.venv/` to your `.gitignore`. The `requirements.txt` file (Chest 1) is what you commit instead.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Three hidden caches are sealed behind this forge's walls — crack them open and you'll walk away with tools that set you apart from every researcher still fighting dependency chaos.

{: .chest }
> **Side Quest 1 — Freeze Flask:** Export your environment to `requirements.txt` using `pip freeze`. Then create a new empty venv, install from the requirements file, and verify the packages are the same.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side1"> Freeze Flask unlocked</label>

Inside Chest 2 lies the secret that turns active development from a reinstall nightmare into pure flow — change your code, run it, see it work, instantly.

{: .chest }
> **Side Quest 2 — Editable Elixir:** Install a local Python package in "editable" mode (`pip install -e .`) so that changes to the source code take effect immediately without reinstalling. When is this useful for research code you're actively developing?

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side2"> Editable Elixir unlocked</label>

Chest 3 holds a potion that grants mastery over Python itself — not just packages, but the very interpreter version your project runs on.

{: .chest }
> **Side Quest 3 — Pyenv Potion:** Look up `pyenv` — a tool for managing multiple Python versions on one machine. What problem does it solve that `module load python` doesn't? When would you need it on the Yens?

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side3"> Pyenv Potion unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Freeze Flask** — `pip freeze > requirements.txt` to snapshot your exact environment; anyone can reproduce it with `pip install -r requirements.txt`.
>
> **Editable Elixir** — `pip install -e .` for packages you're actively developing; changes take effect without reinstalling.
>
> **Pyenv Potion** — `pyenv` to manage multiple Python versions per-project; the right tool when `module load` isn't flexible enough.

---

## 🧠 Skills Learned

- You can now forge an isolated virtual environment and explain exactly why every serious project demands its own
- You can activate and deactivate a venv at will — and you know precisely what shifts in your shell the moment you do
- You can install any package into a sealed environment, leaving the system Python completely untouched
- You can wire a venv directly into JupyterHub as a named kernel, so your notebooks always run the right stack
- You know that `requirements.txt` is the artifact you share with the world — not the `.venv` directory itself
