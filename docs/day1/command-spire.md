---
layout: default
title: "The Command Spire"
parent: "Day 1 — The Gatehouse"
nav_order: 2
permalink: /day1/command-spire/
---

# The Command Spire

<div data-room-id="d1-command-spire"></div>

*Lightning crackles between the rune-carved columns. Every researcher who reached the top floor passed through here first. The commands etched into the walls are simple — deceptively so. Master them and you can navigate any Unix system, anywhere, forever.*

---

## Main Quest

{: .important }
> **Quest:** Use the command line to navigate your file system and reorganize a directory of files — without touching a mouse.

Open your terminal (Mac: Terminal or iTerm; Windows: WSL Ubuntu terminal). Work through each command below:

**Where are you?**
```bash
pwd           # print working directory — your current location
ls            # list files and directories here
ls -la        # long format, including hidden files (dotfiles)
```

**Move around:**
```bash
mkdir dungeon                  # create a directory
cd dungeon                     # enter it
cd ..                          # go up one level
cd ~                           # go home (your home directory)
```

**Create, copy, move, remove:**
```bash
touch quest.txt                # create an empty file
cp quest.txt quest_backup.txt  # copy it
mv quest_backup.txt old/       # move into a subdirectory (create old/ first)
rm quest.txt                   # delete — no trash, gone forever
rm -r old/                     # delete a directory and everything in it
```

{: .warning }
> `rm` is permanent. There is no undo. Double-check your path before you run it.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="main"> Main Quest complete</label>

---

## Chests

{: .chest }
> **Chest 1 — Grep Blade:** Your dungeon contains 300 spell files. Find every `fire` spell that is also `offensive`, and count how many there are — using only pipes and no loops.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="chest1"> Grep Blade unlocked</label>

{: .chest }
> **Chest 2 — Shell Rune:** Write a `for` loop that renames every `.txt` file in the current directory by appending `_archive` before the extension. (e.g. `quest.txt` → `quest_archive.txt`)

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="chest2"> Shell Rune unlocked</label>

{: .chest }
> **Chest 3 — Arcane Blade:** Write a reusable shell script `organize.sh` that takes a directory as its first argument (`$1`) and prints a count of files per extension. Run it on the grimoire directory.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="chest3"> Arcane Blade unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Grep Blade** — search any file or stream for a pattern; chain with pipes to filter, sort, and count without writing a single line of Python.
>
> **Shell Rune** — automate repetitive file operations with `sed` and `for` loops; rename, reformat, and transform at the command line.
>
> **Arcane Blade** — write shell scripts that accept arguments; turn any one-off command into a reusable research tool.

---

## Skills Learned

- Navigate the Unix file system with confidence from any terminal on any machine
- Understand absolute vs. relative paths
- Create, copy, move, and delete files and directories without a GUI
- Know that `rm` is permanent — no recycle bin on a cluster
