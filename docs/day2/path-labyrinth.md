---
layout: default
title: "The Path Labyrinth"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 4
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

**How PATH lookup works:**

Your tools (programs) live in folders. $PATH is the list of folders the shell searches, in order. A tool can be *installed* on the system and still be invisible to the shell if its folder isn't in $PATH.

```
  You have tools installed in different folders:

  /usr/bin/             python3  (system python)
  /apps/python/3.11/   python3  (module version)  ← not in PATH yet
  .venv/bin/            python3  (your venv)       ← not in PATH yet

  ──────────────────────────────────────────────────────────────
  Situation 1 — default shell (only /usr/bin/ in PATH):

  $ python3  →  shell finds /usr/bin/python3  →  runs system version

  ──────────────────────────────────────────────────────────────
  Situation 2 — after  module load python/3.11:
                adds /apps/python/3.11/ to the FRONT of PATH

  $ python3  →  shell finds /apps/python/3.11/python3 FIRST  ✓
                (never even looks in /usr/bin/)

  ──────────────────────────────────────────────────────────────
  Situation 3 — after  source .venv/bin/activate:
                adds .venv/bin/ to the FRONT of PATH

  $ python3  →  shell finds .venv/bin/python3 FIRST  ✓
                (module and system versions are shadowed)
```

Both `module load` and `source .venv/bin/activate` work the same way: they win by going first. The tool that's at the front of PATH is the one that runs.

```
  $PATH (left to right, first match wins):

  [.venv/bin] → [/apps/python/3.11/] → [/usr/local/bin] → [/usr/bin] → ...
       ↑
   venv wins — everything else shadowed
```

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

<label class="quest-check"><input type="checkbox" data-room="d2-path-labyrinth" data-key="main"> Main Quest complete</label>
