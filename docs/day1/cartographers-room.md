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

<svg viewBox="0 0 660 200" role="img" aria-labelledby="fs-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="fs-title">The Yens have three main places to keep files. Your home directory is small and backed up. Project storage is shared with your team and backed up. Scratch is huge and fast but NOT backed up, so files there can be deleted — copy out anything you want to keep.</title>
  <text x="14" y="26" font-size="12.5" font-weight="700" letter-spacing="0.4" fill="#8a94a6">📁  WHERE YOUR FILES LIVE ON THE YENS</text>

  <!-- Home: backed up -->
  <rect x="14" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="30" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">🏠  Your home</text>
  <text x="30" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/home/users/SUNetID/</text>
  <rect x="28" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="114" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="30" y="162" font-size="11" fill="#6a7280">personal workspace</text>
  <text x="30" y="180" font-size="11" fill="#6a7280">small quota</text>

  <!-- Projects: backed up -->
  <rect x="230" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="246" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">👥  Project storage</text>
  <text x="246" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/yen/projects/</text>
  <rect x="244" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="330" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="246" y="162" font-size="11" fill="#6a7280">shared with your team</text>
  <text x="246" y="180" font-size="11" fill="#6a7280">space is limited</text>

  <!-- Scratch: NOT backed up -->
  <rect x="446" y="40" width="200" height="150" rx="14" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="462" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">⚡  Scratch space</text>
  <text x="462" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/scratch/shared/SUNetID/</text>
  <rect x="460" y="112" width="172" height="28" rx="8" fill="#fdeceb" stroke="#f0c3bd" stroke-width="1.5"/>
  <text x="546" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#c0392b">✕  NOT backed up</text>
  <text x="462" y="162" font-size="11" fill="#6a7280">huge &amp; fast</text>
  <text x="462" y="180" font-size="11" fill="#6a7280">copy out what you keep</text>
</svg>

*Rule of thumb: keep raw data and scripts in **home** or **projects** — they're backed up — and run big jobs in **scratch** because it's fast, but copy anything you want to keep back to a backed-up folder, since scratch files can be deleted.*

{: .note }
> **How to organize a research project on the Yens:**
> - Raw data → `/yen/projects/your_project/data/` — shared with your PI, backed up, never overwrite
> - Scripts → your git repo in `/home/users/SUNetID/` or `/yen/projects/`
> - Outputs and scratch work → `/scratch/shared/SUNetID/results/` — fast, but not backed up; copy anything you want to keep
> - Never mix raw data and outputs in the same folder — future-you will not know which is which

**Check your quota:**
```bash
gsbquota                             # shows home and scratch usage for your account
gsbquota /yen/projects/your_project  # append a path to check a project folder's usage
```

**Browse storage in a visual file manager:**
```bash
gsbbrowser                # opens an interactive file size browser in the terminal
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
