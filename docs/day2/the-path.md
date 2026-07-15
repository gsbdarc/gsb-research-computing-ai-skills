---
layout: default
title: "The Path"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 1
permalink: /day2/the-path/
---

# The Path and The Way 

<div data-room-id="d2-arcane-notebook"></div>

You awake with a start as if from a bad dream. You were sleeping so peacefully, what was that dream about. As the fresh air hits your face you remember what you were dreaming about...

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

You should see your home directory and the `rf-bootcamp-2026` folder you cloned yesterday.

---

## 🗡️ Main Quest - The Path 

{: .important }
> **Quest:** Follow the sacred Path, Learn about JupyterHub, command AI to do your bidding

---

## Step 1

### Who are you

``` bash 
whoami  
```
### Where are you?
```bash
pwd
```
### What is the Path?
```bash
echo $PATH
echo $PATH | tr ':' '\n' #For a cleaner view
```

This list is like a checklist for the shell

```bash
/home/users/jeffott/.local/bin #The middle section should be your SUNet
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/sbin
/bin
/usr/games
/usr/local/games
/snap/bin
/zfs/tools/darc/bin
```


Each directory is part of the PATH environment variable. When you type a command, the shell checks these directories from top to bottom until it finds an executable file with that command’s exact name.

{: .chest }
> **Exercise:** Using the skills you learned for yesterday go find python3.

<details> <summary>Hint (click to reveal)</summary>

Run <code>which python3</code> and look at the beginning of the path.
</details>



For example, when you type:
```bash
python3
```
the shell effectively checks for:

```bash
/home/users/jeffott/.local/bin/python3
/usr/local/sbin/python3
/usr/local/bin/python3
/usr/sbin/python3
/usr/bin/python3
/sbin/python3
/bin/python3
/usr/games/python3
/usr/local/games/python3
/snap/bin/python3
/zfs/tools/darc/bin/python3 
```

So when you do something like 

```bash 
module load python
echo $PATH | tr ':' '\n' 
```

You may notice a
```bash
/software/free/python/3.10.5/bin:
```
at the front of your path. 

This means that when you type 
```bash 
which python3
```
 You will get a much different answer. 


## Step 2 - Running Standalone Python Code


Example Code


```python 
import matplotlib.pyplot as plt #Plotting Library
import numpy as np  # Scientific computing library


fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("My First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
fig.savefig("my_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig)
```

<details>
<summary>Hint (click to reveal)</summary>

Run `pip install matplotlib numpy` in the same Python environment you are using. This installs the libraries for that environment so you can import them in your notebook or script.

</details>


Now you if you look into your files with `ls` you should have a my_plot.png. If you "look" (`cat`) This will not look like your graph but 

```text
�PNG
IHDR....IDATx...��KѐP....
```
What is this **incantation** this is not the clean graph from the code you ran?? If this all the Yens has to offer what are you doing here. Why did you take this perilous journey? 


### Step 3 — Summon JupyterHub

JupyterHub is a browser-based interface to the Yens. Choose any node:

| Node | URL |
|------|-----|
| Yen1 | [yen1.stanford.edu/jupyter/hub/home](https://yen1.stanford.edu/jupyter/hub/home) |
| Yen2 | [yen2.stanford.edu/jupyter/hub/home](https://yen2.stanford.edu/jupyter/hub/home) |
| Yen3 | [yen3.stanford.edu/jupyter/hub/home](https://yen3.stanford.edu/jupyter/hub/home) |
| Yen4 | [yen4.stanford.edu/jupyter/hub/home](https://yen4.stanford.edu/jupyter/hub/home) |
| Yen5 | [yen5.stanford.edu/jupyter/hub/home](https://yen5.stanford.edu/jupyter/hub/home) |

Log in with your SUNet credentials. You should see the same files as your home directory on the Yens. Along with a `my_plot.png`

---

### Step 4 — Start a Notebook and a Terminal

- Click the **blue "+"** to open the Launcher
- Start a **Python 3** notebook
- Also open a **Terminal** tab — you'll switch between the two throughout Day 2

---

### Step 5 — Run a Cell

Type this into a cell and run with **Shift+Enter**:

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

Expected output: `15`

---


Now plug in the above code to 


```python
import matplotlib.pyplot as plt #Plotting Library
import numpy as np  # Scientific computing library


fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("My First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
fig.savefig("my_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print('plotting finished')

```

### Step 4 — Run the Same Code as a Script

1. Make a new python file called plotting_code.py
2. In jupyterHub open the python file
3. Paste the plotting code inside

in the Jupyter terminal run python 


Same output, different workflow. Notebooks are good for exploration; scripts are what you submit to the cluster. For the rest of Day 2, you will write scripts.

<label class="quest-check"><input type="checkbox" data-room="d2-arcane-notebook" data-key="main"> Main Quest complete</label>

---

## 🧠 Skills Learned

- You can open JupyterHub on the Yens and run Python from any browser
- You know the difference between a notebook cell and a script — and when each is useful
- You can run a `.py` script from the terminal, which is how cluster jobs work
