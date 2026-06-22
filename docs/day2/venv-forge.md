---
layout: default
title: "The Venv Forge"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 2
permalink: /day2/venv-forge/
---

# The Venv Forge

<div data-room-id="d2-venv-forge"></div>

*The forge glows red. Each project gets its own crucible — its own isolated set of dependencies, sealed from every other project in the dungeon. Pour the wrong ingredient into the wrong crucible and the contamination spreads. The Forge prevents that. One project, one environment, always.*

---

## Main Quest

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
> The `.venv` directory lives inside your project. It is never committed to git — add `.venv/` to your `.gitignore`. The `requirements.txt` file (Chest 1) is what you commit instead.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Freeze Flask:** Export your environment to `requirements.txt` using `pip freeze`. Then create a new empty venv, install from the requirements file, and verify the packages are the same.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="chest1"> Freeze Flask unlocked</label>

{: .chest }
> **Chest 2 — Editable Elixir:** Install a local Python package in "editable" mode (`pip install -e .`) so that changes to the source code take effect immediately without reinstalling. When is this useful for research code you're actively developing?

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="chest2"> Editable Elixir unlocked</label>

{: .chest }
> **Chest 3 — Pyenv Potion:** Look up `pyenv` — a tool for managing multiple Python versions on one machine. What problem does it solve that `module load python` doesn't? When would you need it on the Yens?

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="chest3"> Pyenv Potion unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Freeze Flask** — `pip freeze > requirements.txt` to snapshot your exact environment; anyone can reproduce it with `pip install -r requirements.txt`.
>
> **Editable Elixir** — `pip install -e .` for packages you're actively developing; changes take effect without reinstalling.
>
> **Pyenv Potion** — `pyenv` to manage multiple Python versions per-project; the right tool when `module load` isn't flexible enough.

---

## Skills Learned

- Create a virtual environment and understand why one is necessary per project
- Activate and deactivate a venv; know what changes in your shell when you do
- Install packages into an isolated environment without affecting the system Python
- Connect a venv to JupyterHub as a named kernel
- Understand that `requirements.txt` is what you share, not the `.venv` directory
