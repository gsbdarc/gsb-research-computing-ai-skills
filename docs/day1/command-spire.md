---
layout: default
title: "The Command Spire"
parent: "Day 1 — The Gatehouse"
nav_order: 2
permalink: /day1/command-spire/
---

# The Command Spire

<div data-room-id="d1-command-spire"></div>

*Lightning splits the air between rune-carved obsidian columns, and the smell of ozone hangs like a dare. The walls themselves are covered in commands — chiseled by every researcher who came before you, each one who clawed their way to the top floor and never looked back. The inscriptions look almost too simple. That's how you know they're powerful. Master what's written here and no Unix system on earth — no cluster, no remote server, no black-screened HPC node — will ever feel foreign again.*

---

## 🖊️ Why the Terminal

Before you type a single command, understand why the command line exists.

Researchers use the terminal — not GUIs, not file browsers — for three reasons:

```
        GUI (Finder / Explorer)              CLI (Terminal)
   ─────────────────────────────      ──────────────────────────────────
   click → drag → drop                $ mv *_fire_*.spell fire/
   one file at a time                 300 files sorted in one second

   no record of what you did          save as a script, run it again
   breaks on a remote server          runs on laptop, Yens, any Linux
```

The terminal also reaches further. After SSH (later this morning), every command you practice right now will work identically on the Yens cluster:

```
  Your laptop (now)                  Stanford Yens (later this morning)
  ┌───────────────────────────┐      ┌───────────────────────────────────┐
  │ $ ls grimoire/            │      │ $ ls grimoire/                    │
  │ $ mv *.spell …            │─ssh─►│ $ mv *.spell …                    │
  │                           │      │                                   │
  │ ~8–16 cores               │      │ 256 cores per node · 5 nodes      │
  │ ~8–32 GB RAM              │      │ ~1 TB RAM per node                │
  └───────────────────────────┘      └───────────────────────────────────┘
  your machine                         remote server — same commands
```

**Open your terminal now:**

- **Mac:** Press `Cmd+Space`, type `Terminal`, press Enter. (iTerm2 also works if installed.)
- **Windows:** Open the Start menu, search for `Ubuntu` — this is WSL (Windows Subsystem for Linux). If it isn't installed, [Git Bash](https://git-scm.com/downloads) is a good alternative — download and install it, then open "Git Bash" from the Start menu.

You should see a blinking cursor waiting for a command. That cursor is the entrance to the dungeon.

---

## 🗡️ Main Quest

Every hero needs to know where they stand. Your terminal is open — now claim your footing.

{: .important }
> **Quest:** Use the command line to navigate your file system and reorganize a directory of files — without touching a mouse.

Work through each command below:

**Where are you?**
```bash
pwd           # print working directory — your current location
ls            # list files and directories here
ls -la        # -l = long format (size, date, permissions), -a = include hidden files (dotfiles)
```

{: .tip }
> **Tab completion:** Start typing a filename and press `Tab` — the shell completes it. If nothing happens, press `Tab` twice to see all matches. This works for commands, paths, and flags. Use it constantly; it saves time and prevents typos.

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
> ⚠️ `rm` is permanent. There is no undo. Double-check your path before you run it.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Three side quests wait behind the columns, each sealed with a different cipher. Complete them and claim weapons that will serve you for years.

{: .chest }
> **Side Quest 1 — Grep Blade:** Your dungeon contains 300 spell files. Find every `fire` spell that is also `offensive`, and count how many there are — using only pipes and no loops.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="side1"> Grep Blade unlocked</label>

The second side quest hums with strange energy — it wants you to rename things in bulk, the kind of task that would take an hour by hand and ten seconds in a loop.

{: .chest }
> **Side Quest 2 — Shell Rune:** Write a `for` loop that renames every `.txt` file in the current directory by appending `_archive` before the extension. (e.g. `quest.txt` → `quest_archive.txt`)

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="side2"> Shell Rune unlocked</label>

The third side quest is the hardest — and the most valuable. Inside is the power to turn any trick you learn today into a tool you can call anytime.

{: .chest }
> **Side Quest 3 — Arcane Blade:** Write a reusable shell script `organize.sh` that takes a directory as its first argument (`$1`) and prints a count of files per extension. Run it on the grimoire directory.

<label class="quest-check"><input type="checkbox" data-room="d1-command-spire" data-key="side3"> Arcane Blade unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Grep Blade** — search any file or stream for a pattern; chain with pipes to filter, sort, and count without writing a single line of Python.
>
> **Shell Rune** — automate repetitive file operations with `sed` and `for` loops; rename, reformat, and transform at the command line.
>
> **Arcane Blade** — write shell scripts that accept arguments; turn any one-off command into a reusable research tool.

---

## 🧠 Skills Learned

- You can drop into any Unix terminal on any machine — cluster, cloud, or borrowed laptop — and navigate with total confidence
- You know the difference between absolute and relative paths and can use both without thinking twice
- You can conjure, copy, move, and destroy files and directories without ever reaching for a mouse
- You understand that `rm` is permanent — there is no recycle bin on a cluster, and you will never be caught off guard by that again
