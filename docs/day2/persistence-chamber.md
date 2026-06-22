---
layout: default
title: "The Persistence Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 10
permalink: /day2/persistence-chamber/
---

# The Persistence Chamber

<div data-room-id="d2-persistence-chamber"></div>

*The dungeon enforces a brutal law: when you leave, your work dies. Every SSH session is a lit torch — the moment you close the connection, the flame snuffs out and your script vanishes into the dark. The Persistence Chamber breaks that curse. Here, you forge torches that burn on without you — start a `screen` session and walk away knowing your pipeline is still churning through data long after you've closed your laptop.*

---

## 🗡️ Main Quest

Your mission: prove that your work can outlast the connection. Start a long-running script inside `screen`, vanish without a trace, and return to find it still alive.

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
> ⚠️ You must reconnect to the **same login node** (yen1, yen2, etc.) to reattach. If you SSH to `yen.stanford.edu` and land on a different node, your `screen` session won't be there. Use `ssh yen1.stanford.edu` explicitly if needed. The SSH Sigil from Day 1 helps here.

<label class="quest-check"><input type="checkbox" data-room="d2-persistence-chamber" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Crack open this side quest and your terminal becomes a battle station: multiple live panes, a status bar that never lets you forget where you are, all within a single indestructible session.

{: .chest }
> **Side Quest 1 — Screen Scroll:** Configure `~/.screenrc` to show a status bar at the bottom with the session name, hostname, and time. Then create a session with two horizontal panes (Ctrl-A, ") and run a script in one while monitoring with `htop` in the other.

<label class="quest-check"><input type="checkbox" data-room="d2-persistence-chamber" data-key="side1"> Screen Scroll unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Screen Scroll** — configure `~/.screenrc` for a persistent status bar and multi-pane layout; run code in one pane, monitor resources in another, all within a single detachable session.

---

## 🧠 Skills Learned

- You can now spawn `screen` sessions that keep running even after you close your terminal and walk away
- You can detach instantly with Ctrl-A D and reattach with `screen -r` — picking up exactly where you left off
- You know why the same login node matters, and how to target it directly so your session is always findable
- You can judge when `screen` is the right tool (interactive scripts, long local runs) versus when to reach for SLURM (batch jobs — Day 3)
