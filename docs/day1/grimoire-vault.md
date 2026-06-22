---
layout: default
title: "The Grimoire Vault"
parent: "Day 1 — The Gatehouse"
nav_order: 3
permalink: /day1/grimoire-vault/
---

# The Grimoire Vault

<div data-room-id="d1-grimoire-vault"></div>

*Ice crystals preserve three hundred scrolls in an enormous, unsorted chamber. Each scroll bears a name in the format `fireball_fire_3_offensive_meteor.spell`. Your task: sort them into order before the frost claims your fingers. The Archmage does not accept "I couldn't find it" as an answer.*

---

## Main Quest

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

## Chests

{: .chest }
> **Chest 1 — Wildcard Wand:** Which element+type combination is rarest in the entire grimoire? Find the answer using only `ls`, pipes, `sort`, and `uniq -c` — no Python.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest1"> Wildcard Wand unlocked</label>

{: .chest }
> **Chest 2 — Find Familiar:** Use `find -exec` to print the first line of every tier-5 offensive spell file across all element subdirectories in a single command.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest2"> Find Familiar unlocked</label>

{: .chest }
> **Chest 3 — Awk Sigil:** Use `awk` to generate a CSV inventory: `element,tier,type,count` — one row per unique combination, sorted by count descending. Redirect it to `inventory.csv`.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="chest3"> Awk Sigil unlocked</label>

---

## Weapons Earned

{: .weapon }
> **Wildcard Wand** — use `*` and `?` patterns to target hundreds of files at once; never click-drag a file batch again.
>
> **Find Familiar** — `find -exec` to run any command on every matching file across an entire directory tree.
>
> **Awk Sigil** — `awk` for on-the-fly text parsing and aggregation; turn filenames and log lines into structured data without opening Python.

---

## Skills Learned

- Use wildcards (`*`, `?`) to match and move hundreds of files in one command
- Understand how the shell expands glob patterns before running the command
- Use `ls | wc -l`, `sort`, and `uniq` to count and summarize file sets
- Think in patterns, not individual files — the researcher's approach to bulk data
