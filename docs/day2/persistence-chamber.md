---
layout: default
title: "The Persistence Chamber"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 11
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
