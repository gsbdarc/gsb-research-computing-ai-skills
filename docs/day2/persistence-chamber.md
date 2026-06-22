---
layout: default
title: "The Persistence Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 10
permalink: /day2/persistence-chamber/
---

# The Persistence Chamber

<div data-room-id="d2-persistence-chamber"></div>

*The dungeon has a rule: if you leave, your work stops. Your SSH session is a torch — close it and the flame dies. The Persistence Chamber holds torches that don't go out. Start a `screen` session here and your script will still be running when you come back tomorrow.*

---

## Main Quest

{: .important }
> **Quest:** Start a long-running script inside a `screen` session, detach from it, close your terminal, reattach, and verify it's still running.

**Start a screen session:**

```bash
screen -S my_pipeline      # start a named session called "my_pipeline"
```

Inside the session, run something that takes a while:

```bash
# Simulate a long pipeline
python3 -c "
import time
for i in range(100):
    print(f'Processing filing {i+1}/100...')
    time.sleep(2)
"
```

**Detach — without stopping the script:**

Press **Ctrl-A**, then **D** (hold Ctrl, press A, release, press D). You will see `[detached]` and return to your regular terminal. The script keeps running.

**Close your terminal completely.** Reopen it. SSH back onto the same Yens node (use `hostname` to confirm you're on the same one). Reattach:

```bash
screen -ls                 # list running sessions
screen -r my_pipeline      # reattach to your session
```

You should see the script still printing output.

**Exit the session when done:**

```bash
# Inside the screen session:
exit                       # or Ctrl-D
```

{: .note }
> You must reconnect to the **same login node** (yen1, yen2, etc.) to reattach. If you SSH to `yen.stanford.edu` and land on a different node, your `screen` session won't be there. Use `ssh yen1.stanford.edu` explicitly if needed. The SSH Sigil from Day 1 helps here.

<label class="quest-check"><input type="checkbox" data-room="d2-persistence-chamber" data-key="main"> Main Quest complete</label>

---

## Chest

{: .chest }
> **Chest 1 — Screen Scroll:** Configure `~/.screenrc` to show a status bar at the bottom with the session name, hostname, and time. Then create a session with two horizontal panes (Ctrl-A, ") and run a script in one while monitoring with `htop` in the other.

<label class="quest-check"><input type="checkbox" data-room="d2-persistence-chamber" data-key="chest1"> Screen Scroll unlocked</label>

---

## Weapon Earned

{: .weapon }
> **Screen Scroll** — configure `~/.screenrc` for a persistent status bar and multi-pane layout; run code in one pane, monitor resources in another, all within a single detachable session.

---

## Skills Learned

- Use `screen` to create sessions that survive SSH disconnections
- Detach with Ctrl-A D and reattach with `screen -r` on the same login node
- Understand why you must reconnect to the same node where the session was started
- Know when to use `screen` (interactive scripts, long local runs) vs. SLURM (batch jobs — Day 3)
