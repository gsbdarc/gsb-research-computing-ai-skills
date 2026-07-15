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

## 🖊️ There has been a switch up. 

At this point in the process should should have both a JupyterHub terminal and Shell terminal open. 

Are these the same python?

What does this mean?

### Practical Exercise
In your **JupyterHub Terminal** run the following command `pip install seaborn` 

Then in the very same terminal run `python`

```python
import seaborn
```

Now in the Shell terminal try the the same thing.

If everything is working at intended this will not import as expected.


## 🗡️ Main Quest

{: .important }
> **Quest:** Create a Python virtual environment on the Yens, activate it, install packages, and connect it to JupyterHub as a named kernel.

---

### Step 1 — Create a Working Directory and Venv (Learn to Cast Protective Dome)

In your **Jupyter terminal** (or SSH terminal):

```bash
mkdir day2
cd day2
```

Create the virtual environment using the system Python:

```bash
/usr/bin/python3 -m venv venv
```


---

### Step 2 — Activate and Explore the PATH Change

```bash
source venv/bin/activate
```

Your prompt now shows `(venv)` — you're inside the environment. Check what changed:

```bash
echo $PATH          # venv/bin is now at the front
which python3       # now points inside venv/
```

Try deactivating and checking again:

```bash
deactivate
which python3       # back to system python
echo $PATH
```

Reactivate:

```bash
source venv/bin/activate
```

{: .note }
> 💡 The `venv/bin/activate` script works by prepending `venv/bin/` to your `$PATH` — the same mechanism as `module load`. Deactivating removes it.

---

### Step 3 — Install Packages

With the venv active, install the packages you'll need for Day 2:

```bash
pip install python-dotenv ipykernel openai pydantic
```

These packages are installed only inside this venv — not for anyone else on the cluster.

Verify by testing in the venv terminal:

```bash
python3 -c "import dotenv; print('dotenv ok')"
```

Now deactivate and try the same import:

```bash
deactivate
python3 -c "import dotenv"    # should fail — not installed in system python
```

Reactivate when done testing.

---

### Step 4 — Register as a Jupyter Kernel

With the venv active, register it as a kernel JupyterHub can use:

```bash
python -m ipykernel install --user --name=bootcamp-2026 --display-name "Bootcamp 2026"
```

Now go to JupyterHub:
- Open your `day2/` folder in the file browser
- Create a new notebook
- Select **"Bootcamp 2026"** as the kernel from the kernel menu

In the notebook, confirm the environment is active:

```python
import dotenv
print("dotenv is available!")
```

If this runs without error, your venv is correctly connected.

{: .note }
> 💡 Never commit the `venv/` directory to git — it's hundreds of megabytes of installed packages. Add it to `.gitignore`:
> ```bash
> echo "venv/" >> ~/rf-bootcamp-2026/.gitignore
> ```

<label class="quest-check"><input type="checkbox" data-room="d2-venv-forge" data-key="main"> Main Quest complete</label>

---

### Step 5 — Share the Recipe, Not the Crucible

You may need to share an environment with a collaborator or recreate it on another machine. Do not copy the `venv/` folder itself: virtual environments contain machine-specific paths and can break when moved.

Instead, save a `requirements.txt` file. This is the recipe for your environment: a list of the packages and versions needed to run your code.

With your virtual environment activated, create the recipe:

```bash
python -m pip freeze > requirements.txt
```

Commit `requirements.txt` to your repository, but keep `venv/` in `.gitignore`.

To recreate the environment elsewhere:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

{: .note }
> `requirements.txt` recreates installed packages. It does not copy data files, API keys, notebooks, or Python itself.


### Step 6 - Why this matters.

## 🧠 Skills Learned

- A virtual environment is an isolated Python installation — packages installed in one venv don't affect any other project
- `source venv/bin/activate` prepends `venv/bin/` to `$PATH`, making the venv's Python the first match
- JupyterHub kernels are just named Python environments — you can have one per project
- Never commit `venv/` to git — it's too large and machine-specific
