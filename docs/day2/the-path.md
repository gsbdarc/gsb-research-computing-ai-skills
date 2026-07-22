---
layout: default
title: "The Path"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 1
permalink: /day2/the-path/
---

# The Path and The Way

<div data-room-id="d2-arcane-notebook"></div>

Every command you type is a name, and the shell must find who answers. The Path ($PATH) is the ranked list of directories it searches, top to bottom, until the first match wins, which is why loading a module can change which python responds. But a bare terminal can draw a plot without ever showing it, so the Path leads to JupyterHub: your window into the cluster, where code runs on the Yens' hardware but appears in your browser. There you'll run Python three ways, line-by-line in the interpreter, cell-by-cell in a notebook, and start-to-finish as a script, the form you submit to the cluster.

---

## 🗡️ Main Quest: The Path

{: .important }
> **Quest:** Follow the sacred Path, Learn about JupyterHub, command AI to do your bidding

---

## Review

Before opening any notebooks, confirm you're on the Yens.

```bash
ssh SUNetID@yen.stanford.edu
```

Once connected:

```bash
hostname          # which Yen did you land on?
ls                # do you see files from Day 1?
module avail      # Remember these?
```

You should see your home directory and the `gsb-research-computing-ai-skills` folder you cloned yesterday.

---

## Step 1: Who and Where Are You?

Get your bearings before walking the Path:

```bash
whoami                     # who am I logged in as?
pwd                        # where am I?
echo $PATH | tr ':' '\n'   # what is the Path? (one entry per line)
```

`pwd` should show your home directory, `/home/users/<SUNet>`. If you're somewhere else, run `cd` on its own to return home before continuing.

`$PATH` is the shell's **search checklist**. It is a list of directories, roughly:

```text
/home/users/<SUNet>/.local/bin      # your SUNet goes here
/usr/local/sbin
/usr/local/bin
/usr/bin
...
/zfs/tools/darc/bin
```

When you type a command, the shell walks these directories top to bottom and runs the **first** matching executable it finds.

{: .chest }
> **Exercise:** Using yesterday's skills, find `python3`.

<details> <summary>💡 Hint — click to reveal</summary>

Run <code>which python3</code> and look at the front of the Path.
</details>

So typing `python3` checks `.local/bin/python3`, then `/usr/local/sbin/python3`, and so on, stopping at the first hit.

### Loading a Module Changes the Path

```bash
module load python
echo $PATH | tr ':' '\n'
```

A new directory jumps to the **front** of the list:

```text
/software/free/python/3.10.5/bin
```

Now `which python3` points *there* instead. The module put its own Python first.


### Undo the Change: Deactivating a Module

Loading a module is reversible. Unload it and your `$PATH` snaps back to where it started:

```bash
module unload python        # or: module purge  (unloads everything at once)
echo $PATH | tr ':' '\n'    # the python module's bin/ is gone from the front
which python3               # back to the system python3 again
```

{: .note }
> 💡 This load / unload of `$PATH` is the exact same mechanism you'll meet in [The Venv Forge](../venv-forge/): **activating** an environment prepends a directory to the front of your PATH, and **deactivating** removes it.

---

## Step 2: Running Standalone Python Code

You do not need a file to run Python. The **interactive interpreter** lets you type code straight into the terminal and run it immediately, one line at a time.

In the terminal you opened during the Review, start Python:

```bash
python3
```

The prompt changes to `>>>`. You are now *inside* Python. Type (or paste) this code:

```python
import matplotlib.pyplot as plt   # plotting library
import numpy as np                # scientific computing library

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("My First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
fig.savefig("my_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig)
```

When you are done, leave the interpreter and return to the shell:

```python
exit()
```

{: .note }
> 💡 `plt.show()` would normally pop open a window, but a terminal has no screen to draw on, so nothing appears. That is why we also call `fig.savefig(...)`: it writes the plot to `my_plot.png` in your current directory.

<details> <summary>💡 Hint: got a ModuleNotFoundError? — click to reveal</summary>

Leave Python with <code>exit()</code>, run <code>pip install matplotlib numpy</code> in the same environment, then start <code>python3</code> again.
</details>

### Look at What You Made

Back at the normal shell prompt:

```bash
ls                # you should now see my_plot.png
cat my_plot.png   # try to "read" the image
```

`cat` spills something like:

```text
�PNG
IHDR....IDATx...��KѐP....
```
What is this **incantation?** A terminal can *run* the code that draws an image, but it cannot *show* you the image itself. If this is all the Yens has to offer, why did you take this perilous journey? For that, you need a window into the cluster: **JupyterHub**.


## Step 3: Summon JupyterHub

JupyterHub is the development environment we offer on the Yens. It runs in your browser, but your code executes on the cluster's hardware, not your laptop. Instead of the bare command line from Step 2, you get an interactive workspace: write and run code in notebooks, edit files, open a terminal, and see plots and tables right on the screen.

Choose any node to log in:

| Node | URL |
|------|-----|
| Yen1 | [yen1.stanford.edu/jupyter/hub/home](https://yen1.stanford.edu/jupyter/hub/home) |
| Yen2 | [yen2.stanford.edu/jupyter/hub/home](https://yen2.stanford.edu/jupyter/hub/home) |
| Yen3 | [yen3.stanford.edu/jupyter/hub/home](https://yen3.stanford.edu/jupyter/hub/home) |
| Yen4 | [yen4.stanford.edu/jupyter/hub/home](https://yen4.stanford.edu/jupyter/hub/home) |
| Yen5 | [yen5.stanford.edu/jupyter/hub/home](https://yen5.stanford.edu/jupyter/hub/home) |

Log in with your SUNet credentials. You should see the same files as your home directory on the Yens. Along with a `my_plot.png`

---

## Step 4: Start a Notebook and a Terminal

- Click the **blue "+"** to open the Launcher
- Start a **Python 3** notebook
- Open a **Terminal** tab as well

A **notebook** runs code in *cells* you execute one at a time, with the results (text, tables, even images) appearing right below each cell. The **Terminal** is a shell similar to the one you used in Step 2, though not identical. You will dig into that difference in [The Venv Forge](../venv-forge/). You'll switch between the two throughout Day 2.

---

## Step 5: Run a Cell

Type this into the first cell and run it with **Shift+Enter**:

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

Expected output: `15`

Now for the payoff. Remember the "incantation" from Step 2, the plot your terminal could make but not show? Paste the **same code** into a new cell and run it:

```python
import matplotlib.pyplot as plt   # plotting library
import numpy as np                # scientific computing library

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("My First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
```

This time the graph appears **right below the cell**. That is what JupyterHub buys you: in a notebook, `plt.show()` draws the plot inline instead of needing a screen of its own.

{: .note }
> 💡 In a notebook you don't even need `fig.savefig(...)` just to *see* a plot. You still save it when you want a file to keep, share, or hand to the cluster.

---

## Step 6: Run the Same Code as a Script

You have now run Python two ways: the interactive interpreter (Step 2) and a notebook (Step 5). The third way is a **script**, a `.py` file that runs start to finish on its own. This is what you submit to the cluster.

1. In the Launcher, open a **Text File** (or run `nano plotting_code.py` in the Terminal) and name it `plotting_code.py`.
2. Paste in the plotting code from Step 2, keeping the `fig.savefig("my_plot.png", ...)` and `plt.close(fig)` lines so it writes the image to a file.
3. Run it from the Terminal:

```bash
python3 plotting_code.py
```

Same output, different workflow. Notebooks are good for exploration; scripts are what you submit to the cluster. For the rest of Day 2, you will write scripts.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="main"> Main Quest complete</label>

---

## Side quests

{: .note }
> Finished early? Try any of these.

**Side quest — Behold the Incantation**

The terminal could only show you `my_plot.png` as gibberish. JupyterHub can do better. In the **file browser** on the left, find `my_plot.png` and **double-click** it. It opens in an image viewer, and the plot you drew finally reveals itself, the same file, now readable because you have the right tool to look at it.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="side1"> I opened my_plot.png in JupyterHub and saw the graph</label>

**Side quest — Enchant the Plot**

A plot is never finished. Back in your notebook, edit the plotting cell to make it your own, then re-run it with **Shift+Enter** and watch it change:

- Plot a second line, e.g. `ax.plot([1, 2, 3, 4], [2, 3, 1, 4], label="second run")`
- Give each line a `label=...` and add `ax.legend()` to name them
- Change a line's colour with `color="crimson"` (or `"teal"`, `"goldenrod"`)

**Now command the AI to do your bidding.** First save your notebook with a name you'll recognise (**File → Save Notebook As…**, e.g. `plotting.ipynb`). Then open a **Terminal** in JupyterHub and summon Claude Code, exactly as you did in [Working with Claude Code](../../day1/familiars-den/):

```bash
cd ~                 # or wherever you saved the notebook
module load claude
claude
```

Then describe the plot you want — no matplotlib to memorise, just say it:

```text
> Make the plot in plotting.ipynb as exciting as you can — bold colours, several
> lines, a dramatic title, annotations, gridlines, whatever looks great. Then leave
> the notebook so I can re-run it.
```

Claude edits the `.ipynb` **file on disk**. Switch back to the notebook tab — JupyterHub will notice the file changed and offer to **reload** it (click *Reload*) — then **Kernel → Restart Kernel and Run All Cells** to see your enchanted plot.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="side2"> I modified the plot — by hand and with Claude Code — and re-ran the cell to see it update</label>

---

## 🧠 Skills Learned

- You can open JupyterHub on the Yens and run Python from any browser
- You know the difference between a notebook cell and a script, and you know when each is useful
- You can run a `.py` script from the terminal, which is how cluster jobs work
