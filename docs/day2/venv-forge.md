---
layout: default
title: "The Venv Forge"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 2
permalink: /day2/venv-forge/
---

# The Venv Forge

<div data-room-id="d2-venv-forge"></div>

A virtual environment is a sealed Python of your own: its own interpreter and its own installed packages, isolated so one project's dependencies never collide with another's. You'll forge one with `python3 -m venv`, then **activate** it — which simply prepends its `bin/` to your `$PATH`, the same trick `module load` played in The Path — install the packages this bootcamp needs, and register it as a named **kernel** so JupyterHub notebooks can use it. Finally you'll capture the whole environment as a `requirements.txt` recipe: the one file that lets a collaborator, or future you, rebuild your exact setup and reproduce your results on any machine. One project, one environment.

---

## 🗡️ Main Quest

{: .important }
> **Quest:** Create a Python virtual environment on the Yens, **activate** it, install packages, and connect it to JupyterHub as a named kernel.

---

## 🖊️ There Has Been a Switch Up

By now you should have **two terminals** open: a **JupyterHub terminal** and your **login (SSH) shell**. They look identical. Are they running the *same* Python?

### Practical Exercise

In your **JupyterHub terminal**, install a package:

```bash
pip install seaborn
```

Then start Python in that same terminal and import it:

```bash
python
```

```python
import seaborn   # this works, seaborn is installed here
```

Now try the exact same thing in your **login shell**. This time `import seaborn` fails with `ModuleNotFoundError`.

**❓ Same command, same package name — so why would `import seaborn` work in one terminal but not the other?** Think it through before you reveal the answer.

<details markdown="1">
<summary>💡 Answer — click to reveal</summary>

The two terminals are using **different Pythons**, each with its own set of installed packages. `pip install seaborn` in the JupyterHub terminal installed it for *that* Python only — your login shell runs a different Python that never got it. That is the problem this room solves: stop leaving your environment to chance and forge one you control.
</details>

## Step 1: Create a Working Directory and Venv

In your **Jupyter terminal** (or SSH terminal), move into your cloned repo and make a folder for today's work:

```bash
cd ~/gsb-research-computing-ai-skills
mkdir -p day2
```

Now forge the virtual environment at the repo root, using the system Python:

```bash
/usr/bin/python3 -m venv .venv
```

{: .note }
> 💡 This single `.venv` at `~/gsb-research-computing-ai-skills/.venv` is the crucible you'll use for the rest of the bootcamp, and it's the exact path Days 3 and 4 **activate**. (Potion Brawl in Step 6 is a *separate* project, so it gets its own venv, which is the "one project, one crucible" rule in action.)


---

## Step 2: Activate and Explore the PATH Change

```bash
source ~/gsb-research-computing-ai-skills/.venv/bin/activate
```

Your prompt now shows `(.venv)`, meaning you are inside the environment. Check what changed:

```bash
echo $PATH          # .venv/bin is now at the front
which python3       # now points inside .venv/
```

Try **deactivating** and checking again:

```bash
deactivate
which python3       # back to system python
echo $PATH
```

**Reactivate:**

```bash
source ~/gsb-research-computing-ai-skills/.venv/bin/activate
```

{: .note }
> 💡 The `activate` script works by prepending `.venv/bin/` to your `$PATH`, the same mechanism as `module load` from The Path. **Deactivating** removes it.

{: .note }
> 🟢 **Green sticky** = my environment is up and running (my prompt shows `(.venv)`) &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## Step 3: Install Packages

With the venv **active**, install the packages you'll need for Day 2:

```bash
pip install python-dotenv ipykernel openai pydantic
```

These packages are installed only inside this venv, not for anyone else on the cluster.

Verify by testing in the venv terminal:

```bash
python3 -c "import dotenv; print('dotenv ok')"
```

Now **deactivate** and try the same import:

```bash
deactivate
python3 -c "import dotenv"    # should fail: not installed in system python
```

**Reactivate** when done testing.

---

## Step 4: Register as a Jupyter Kernel

With the venv **active**, register it as a kernel JupyterHub can use:

```bash
python -m ipykernel install --user --name=bootcamp-2026 --display-name "Bootcamp 2026"
```

Now go to JupyterHub:
- Open your `day2/` folder in the file browser
- Create a new notebook and name it `venv_check.ipynb`
- Select **"Bootcamp 2026"** as the kernel from the kernel menu

In the notebook, confirm the environment is **active** — that the packages you installed in Step 3 are importable from this kernel:

```python
import dotenv
import openai
print("dotenv and openai are available!")
```

If this runs without error, your venv is correctly connected.

{: .note }
> 💡 Never commit a venv to git: it holds hundreds of megabytes of packages and machine-specific paths. The repo's `.gitignore` already lists `.venv/`, so yours is covered.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="main"> Main Quest complete</label>

---

## Step 5: Share the Recipe, Not the Crucible

You may need to share an environment with a collaborator or recreate it on another machine. Do not copy the venv folder itself: virtual environments contain machine-specific paths and can break when moved.

Instead, save a `requirements.txt` file. This is the recipe for your environment: a list of the packages and versions needed to run your code.

With your virtual environment **activated**, create the recipe:

```bash
python -m pip freeze > requirements.txt
```

Commit `requirements.txt` to your repository, but keep `.venv/` out of git (it's already in `.gitignore`).

To recreate the environment elsewhere:

```bash
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

{: .note }
> `requirements.txt` recreates installed packages. It does not copy data files, API keys, notebooks, or Python itself.

---

## Step 6: Rebuild a Complex Brew from the Scroll

Everything so far was an *empty* crucible: you installed a handful of packages you chose yourself. The real power of a venv shows up when you inherit **someone else's complex project** and have to make it run: no guessing which packages, no "but it works on my machine." Just the code and the recipe scroll.

Your cloned repo already ships one: **Potion Brawl**, a little physics spectacle where three enchanted potions brawl rock-paper-scissors style until one floods the lab. It leans on a whole shelf of reagents: `numpy`, `scipy`, `matplotlib`, `plotly`, `networkx`, and more.

Move into it and read the scroll:

```bash
cd ~/gsb-research-computing-ai-skills/data/potion_brawl
cat requirements.txt
```

That's **13 pinned reagents**. Nobody memorises that list, and nobody should have to. The scroll *is* the memory.

### Forge a crucible just for this brew

Potion Brawl gets its **own** environment, separate from the one you built above. That is the whole discipline: one project, one crucible.

```bash
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

One command rebuilds the entire shelf (exact packages, exact versions) from the scroll alone.

{: .note }
> `.venv/` and the brew's `output/` folder are already in the repo's `.gitignore`, so you'll never accidentally commit hundreds of megabytes of packages or generated artifacts.

### Brew it

```bash
python potion_brawl.py
```

You'll get a `POTION BRAWL` banner, a progress bar, a populations table, and a fresh `output/` folder:

| file | what it is |
|------|------------|
| `brawl.gif` | top-down animation of the bouncing brawl |
| `populations.png` | stacked-area chart of the war over time |
| `law_of_the_brawl.png` | the 3-potion cycle diagram |
| `victor.txt` | the tick count and final tally |
| `lab_journal.pkl` | the **save state**: positions, velocities, and the random-number generator |

### The punchline: reproducibility you can *see*

Run it again:

```bash
python potion_brawl.py
```

It finds the lab journal and **resumes the exact same brawl**. Because the journal restored the random-number generator's state, the continuation is *bit-for-bit identical* to a brawl that never paused. Copy the folder (code + `requirements.txt` + `output/lab_journal.pkl`) to a brand-new directory, or a different machine entirely, rebuild the venv from the scroll, and the brew picks up precisely where it left off.

That is the point of this entire room. In research it's the difference between:

- **"It ran last spring on my laptop"**, and nobody, including future-you, can reproduce the number in the paper; and
- **"Here's the code and `requirements.txt`"**, and a collaborator, a reviewer, or the cluster rebuilds your exact environment and gets your exact result.

The recipe scroll + your code = the same brew, any alchemist, any lab.

{: .note }
> Prefer the story with pictures? With `.venv` **active**, register it as a kernel and open the notebook:
> ```bash
> python -m ipykernel install --user --name potion-brawl --display-name "Potion Brawl (venv)"
> ```
> Then open **`the_alchemists_lab.ipynb`** in JupyterHub, choose the **"Potion Brawl (venv)"** kernel, and *Kernel → Restart & Run All*.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side1"> Rebuilt and brewed Potion Brawl</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Find Where Kernels Live**

A kernel is just a folder on disk. Track yours down:

```bash
jupyter kernelspec list
```

This prints every registered kernel and its path (a `--user` install like yours lands in `~/.local/share/jupyter/kernels/`). `ls` the **Bootcamp 2026** kernel's folder and open its `kernel.json`. Notice it points straight at your venv's Python. That link is the whole trick behind connecting a venv to JupyterHub, and it's why deleting a venv leaves a broken kernel behind until you remove its folder too.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side2"> I found where my kernels live and read a kernel.json</label>

**Side quest — Why You Can't Copy a Crucible**

Step 5 said never to copy a venv folder. See for yourself why. Peek inside your crucible:

```bash
ls -l ~/gsb-research-computing-ai-skills/.venv/bin/python
cat ~/gsb-research-computing-ai-skills/.venv/pyvenv.cfg
```

The `python` inside a venv is just a **symlink** back to one specific system Python, and `pyvenv.cfg` hardcodes that interpreter's path. Move or copy the folder to another machine (or another user's account) and those paths point at nothing. That is exactly why you rebuild from `requirements.txt` instead of copying the crucible.

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="side3"> I inspected the venv's python symlink and pyvenv.cfg</label>

---

## 🧠 Skills Learned

- A virtual environment is an isolated Python installation: packages installed in one venv don't affect any other project
- `source .venv/bin/activate` prepends `.venv/bin/` to `$PATH`, making the venv's Python the first match
- JupyterHub kernels are just named Python environments: you can have one per project
- Never commit `.venv/` to git: it's too large and machine-specific
- A `requirements.txt` lets anyone rebuild a complex environment (exact packages and versions) from a single command, which is what makes your research reproducible
