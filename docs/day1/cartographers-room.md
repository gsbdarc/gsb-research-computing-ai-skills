---
layout: default
title: "The Cartographer's Room"
parent: "Day 1 — The Gatehouse"
nav_order: 5
permalink: /day1/cartographers-room/
---

# The Cartographer's Room

<div data-room-id="d1-cartographers-room"></div>

*Ancient stone maps cover every wall, carved by researchers who came before you and survived. Glowing veins trace the dungeon's arteries — the deep scratch vaults where raw data floods in, the precious home quarters where your work is sealed and guarded, the shadowy project halls where your PI's treasures are stacked. On the Yens, this knowledge isn't trivia. Blind adventurers who ignore their quota find their pipelines strangled mid-run. Those who can't load a module stand at locked doors rattling the wrong handle. The Cartographer's Room exists to make you neither.*

---

## 🗡️ Main Quest

Before you touch a single data file, you need to know the terrain — what's yours, how much of it you have, and what weapons the cluster has already forged for you.

{: .important }
> **Quest:** Map the Yens file system — find out where your data lives, how much space you have, and what software is available.

**The file system layout:**

```
/home/users/SUNetID/      ← your home directory (limited quota, backed up)
/yen/projects/            ← project storage (backed up, shared with collaborators)
/scratch/shared/SUNetID/  ← scratch space (large, fast, NOT backed up)
```

{: .note }
> **How to organize a research project on the Yens:**
> - Raw data → `/yen/projects/your_project/data/` — shared with your PI, backed up, never overwrite
> - Scripts → your git repo in `/home/users/SUNetID/` or `/yen/projects/`
> - Outputs and scratch work → `/scratch/shared/SUNetID/results/` — fast, but not backed up; copy anything you want to keep
> - Never mix raw data and outputs in the same folder — future-you will not know which is which

**Check your quota:**
```bash
gsbquota                             # shows home and scratch usage for your account
gsbquota /yen/projects/your_project  # append a path to check a project folder's usage
```

**Browse storage in a visual file manager:**
```bash
gsbbrowser                # opens an interactive file size browser in the terminal
# navigate with arrow keys, q to quit
```

**See what software modules are available:**
```bash
module avail              # lists all available software modules
module avail python       # filter by name
module load python/3.11   # load a specific version (adjust to what's available)
python --version          # confirm it loaded
module list               # see what's currently loaded
module unload python/3.11 # unload it
```

<label class="quest-check"><input type="checkbox" data-room="d1-cartographers-room" data-key="main"> Main Quest complete</label>
