---
layout: default
title: "The Cartographer's Room"
parent: "Day 1 — The Gatehouse"
nav_order: 5
permalink: /day1/cartographers-room/
---

# The Cartographer's Room

<div data-room-id="d1-cartographers-room"></div>

*Stone maps line every wall. This room belongs to whoever learned the dungeon's layout — where the storage vaults are, how full they're getting, which exits are passable. On the Yens, this knowledge is not optional. Run out of quota or load a module that doesn't exist, and your research stops.*

---

## Main Quest

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

## Chest

{: .chest }
> **Chest 1 — Module Lens:** Use `module spider` to find a module that isn't listed obviously in `module avail` — one that requires loading a prerequisite first. What is the prerequisite, and why does the system require it?

<label class="quest-check"><input type="checkbox" data-room="d1-cartographers-room" data-key="chest1"> Module Lens unlocked</label>

---

## Weapon Earned

{: .weapon }
> **Module Lens** — `module spider <name>` to locate any software on the cluster and understand its dependency chain; never wonder again why `module load` failed.

---

## Skills Learned

- Understand the Yens file system: home (backed up, limited) vs. scratch (large, not backed up)
- Check disk quota before starting a large job — avoid running out mid-pipeline
- Use `gsbbrowser` to see where disk space is being consumed
- Load and unload software modules; understand why the same command might not exist in a fresh shell
