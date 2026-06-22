---
layout: default
title: "The Grimoire Vault"
parent: "Day 1 — The Gatehouse"
nav_order: 3
permalink: /day1/grimoire-vault/
---

# The Grimoire Vault

<div data-room-id="d1-grimoire-vault"></div>

*The vault breathes cold. Frost coats the stone walls and three hundred spell scrolls lie scattered across the chamber floor in total chaos — each one named in a cryptic cipher like `fireball_fire_3_offensive_meteor.spell`. The Archmage's voice echoes from somewhere above: "Sorted. Now. Before the ice takes your hands." You have no loops. You have no Python. You have the shell — and that is enough.*

---

## 🗡️ Main Quest

The vault won't organize itself. One wildcard pattern can move sixty files in the time it would take you to drag-and-drop three. Here's how you become the archivist legends speak of.

{: .important }
> **Quest:** Download the grimoire archive, then sort all 300 spell files into element subdirectories using wildcards — no loops, no Python.

**Step 1 — Download the grimoire**

Your instructor will provide a download link. Save `grimoire.zip` to your laptop and unzip it:

```bash
unzip grimoire.zip
ls grimoire/          # should show ~300 .spell files in no order
```

**Step 2 — Sort by element**

Each filename contains the element as the second field: `name_ELEMENT_tier_type_mastery.spell`. Use wildcards to move all spells of each element into a subdirectory:

```bash
cd grimoire
mkdir fire ice lightning earth wind

mv *_fire_*.spell fire/
mv *_ice_*.spell ice/
mv *_lightning_*.spell lightning/
mv *_earth_*.spell earth/
mv *_wind_*.spell wind/
```

**Step 3 — Verify**

```bash
ls fire/ | wc -l      # count fire spells
ls ice/ | wc -l       # count ice spells
# all 5 element counts should sum to ~300
```

{: .note }
> You will transfer your sorted grimoire to the Yens in [The Scroll Transfer](../scroll-transfer/) room. Keep this directory — you need it there.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="main"> Main Quest complete</label>

---

## 📦 Chests

Hidden deeper in the vault, three locked chests glow with a faint arcane light. Each one rewards a researcher bold enough to go beyond the basics.

{: .chest }
> **Chest 1 — Wildcard Wand:** Which element+type combination is rarest in the entire grimoire? Find the answer using only `ls`, pipes, `sort`, and `uniq -c` — no Python.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest1"> Wildcard Wand unlocked</label>

The second chest is sealed by a riddle only `find` can answer — pierce every subdirectory in a single breath.

{: .chest }
> **Chest 2 — Find Familiar:** Use `find -exec` to print the first line of every tier-5 offensive spell file across all element subdirectories in a single command.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest2"> Find Familiar unlocked</label>

The third chest holds the most powerful relic in the vault — a tool that transforms raw filenames into structured intelligence.

{: .chest }
> **Chest 3 — Awk Sigil:** Use `awk` to generate a CSV inventory: `element,tier,type,count` — one row per unique combination, sorted by count descending. Redirect it to `inventory.csv`.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest3"> Awk Sigil unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Wildcard Wand** — use `*` and `?` patterns to target hundreds of files at once; never click-drag a file batch again.
>
> **Find Familiar** — `find -exec` to run any command on every matching file across an entire directory tree.
>
> **Awk Sigil** — `awk` for on-the-fly text parsing and aggregation; turn filenames and log lines into structured data without opening Python.

---

## 🧠 Skills Learned

- You can now move hundreds of files in a single command using wildcards (`*`, `?`) — no loops, no scripts, no drama
- You understand how the shell expands glob patterns *before* the command ever runs, giving you precise, predictable control
- You can count, rank, and summarize entire file collections with `ls | wc -l`, `sort`, and `uniq` in seconds
- You think in patterns rather than individual files — the hallmark of a researcher who works at scale
