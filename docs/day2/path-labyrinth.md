---
layout: default
title: "The Path Labyrinth"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/path-labyrinth/
---

# The Path Labyrinth

<div data-room-id="d2-path-labyrinth"></div>

*Corridors fracture in every direction, each passage marked with the same name: "python." You call out and five doors crack open at once — five different Pythons, each certain it is the one you want. The labyrinth does not guess. It follows a strict protocol: check the first corridor, then the second, then the third, until it finds a match and stops. The researcher who understands the order commands the maze. The one who ignores it stumbles through cryptic failures, wrong versions, and errors that appear from nowhere. You are about to learn the order.*

---

## 🗡️ Main Quest

The shell is not magic — it follows a map. That map is `$PATH`, and every command you type is just a race down its list of corridors. Here is how you take control of the race.

{: .important }
> **Quest:** Understand `$PATH` — how the shell finds commands — and debug a "command not found" error by tracing the lookup chain.

**See your current PATH:**
```bash
echo $PATH
# Output: colon-separated list of directories, checked left to right
```

**Find where a command lives:**
```bash
which python3       # which directory's python3 runs when you type python3?
which pip           # which pip?
which module        # is module even a real command?
```

**Load a module and see PATH change:**
```bash
module load python/3.11
echo $PATH          # compare before and after — a new directory was prepended
which python3       # now points to the module version
```

**Activate your venv and see it change again:**
```bash
source .venv/bin/activate
echo $PATH          # .venv/bin is now first
which python3       # now points into .venv
```

The rule: **the first match in PATH wins.** Modules and venvs work by prepending their `bin/` directory to PATH so their commands shadow everything else.

<label class="quest-check"><input type="checkbox" data-room="d2-path-labyrinth" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Hidden in the labyrinth walls is a rune that lets you reshape the corridors themselves — permanently, at login, before you even type a single command. Crack it open.

{: .chest }
> **Side Quest 1 — Profile Rune:** Add a line to `~/.bash_profile` (or `~/.bashrc`) on the Yens that automatically activates your Bootcamp venv whenever you log in. Test it by logging out and back in. Why might this be a bad idea for a shared project, even if it's convenient for solo work?

<label class="quest-check"><input type="checkbox" data-room="d2-path-labyrinth" data-key="side1"> Profile Rune unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Profile Rune** — customize `~/.bash_profile` to set environment variables, load modules, or activate venvs automatically on login; make your shell do the setup work every time.

---

## 🧠 Skills Learned

- You can now read `$PATH` like a map and predict exactly which binary the shell will run when you type any command
- You can now use `which` to expose the precise binary behind any command name — no more guessing
- You can now explain why `module load` and `source venv/bin/activate` both work the same way: they win the race by going first in PATH
- You can now diagnose "command not found" and "wrong version" errors by tracing the PATH lookup chain step by step
