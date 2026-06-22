---
layout: default
title: "The Path Labyrinth"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 3
permalink: /day2/path-labyrinth/
---

# The Path Labyrinth

<div data-room-id="d2-path-labyrinth"></div>

*Corridors branch endlessly. You shout "python" and five doors open, each leading to a different Python. Which one runs? The labyrinth has rules — it checks the first door, then the second, then the third. Know the order and you control which Python wins. Ignore it and your scripts fail in ways that make no sense.*

---

## Main Quest

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

## Chest

{: .chest }
> **Chest 1 — Profile Rune:** Add a line to `~/.bash_profile` (or `~/.bashrc`) on the Yens that automatically activates your Bootcamp venv whenever you log in. Test it by logging out and back in. Why might this be a bad idea for a shared project, even if it's convenient for solo work?

<label class="quest-check"><input type="checkbox" data-room="d2-path-labyrinth" data-key="chest1"> Profile Rune unlocked</label>

---

## Weapon Earned

{: .weapon }
> **Profile Rune** — customize `~/.bash_profile` to set environment variables, load modules, or activate venvs automatically on login; make your shell do the setup work every time.

---

## Skills Learned

- Understand that `$PATH` is an ordered list of directories searched left-to-right when you type a command
- Use `which` to find exactly which binary runs for any command
- Understand how `module load` and `source venv/bin/activate` both work by prepending to PATH
- Diagnose "command not found" and "wrong version" errors by tracing PATH
