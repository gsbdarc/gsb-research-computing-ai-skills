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
cd ~/rf-bootcamp-2026
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
