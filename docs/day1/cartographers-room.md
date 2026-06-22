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
/scratch/SUNetID/         ← scratch space (large, fast, NOT backed up)
/zfs/projects/            ← group/project storage (ask your PI)
```

**Check your quota:**
```bash
gsbquota                  # shows home and scratch usage for your account
```

**Browse storage in a visual file manager:**
```bash
gsbbrowser                # opens a ncurses-style file size browser
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

---

## 📦 Chests

Hidden in this room is a lens that lets you see past the obvious — software that's buried deeper than the main index, waiting to be claimed by someone who knows where to look.

{: .chest }
> **Chest 1 — Module Lens:** Use `module spider` to find a module that isn't listed obviously in `module avail` — one that requires loading a prerequisite first. What is the prerequisite, and why does the system require it?

<label class="quest-check"><input type="checkbox" data-room="d1-cartographers-room" data-key="chest1"> Module Lens unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Module Lens** — `module spider <name>` to locate any software on the cluster and understand its dependency chain; never wonder again why `module load` failed.

---

## 🧠 Skills Learned

- You can now read the Yens file system like a map — home is your fortified base (backed up, limited space), scratch is your war camp (vast, fast, no safety net)
- You can check your disk quota before launching a long job, so a full disk never kills your pipeline at 3 AM
- You can navigate `gsbbrowser` to hunt down whatever is eating your storage and reclaim the space
- You can load, swap, and unload software modules — and you understand why a fresh shell might act like your tools never existed
