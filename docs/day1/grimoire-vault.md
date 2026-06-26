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

Three hundred spell files. No order. No organization. A real research dataset looks exactly like this — files from a vendor, a scrape, an instrument dump. Your job before any analysis is to understand what you have and impose structure on it.

{: .important }
> **Quest:** Organize 300 spell files into a clean directory structure using the explore → plan → execute → document framework.

**Step 1 — Download and unzip**

Run this in your terminal (Git Bash on Windows, Terminal on Mac):

```bash
cd ~/Desktop
curl -L https://raw.githubusercontent.com/gsbdarc/rf-bootcamp-2026/main/docs/assets/data/grimoire.zip -o grimoire.zip
unzip grimoire.zip
```

---

**Step 2 — Explore: look at what you have**

Before touching anything, understand the data:

```bash
ls grimoire/             # see the files
ls grimoire/ | wc -l     # how many are there?
ls grimoire/ | head -20  # look at the first 20 names
```

The filename format is: `name_ELEMENT_tier_type_mastery.spell`

What elements do you see? What patterns are there? What would make a logical organization?

---

**Step 3 — Plan: decide on a strategy**

*Class discussion — how would you organize these files? Raise your hand.*

<details markdown="1">
<summary>Options to consider (expand after discussion)</summary>

- Group by **element** (`fire/`, `ice/`, `lightning/`, `earth/`, `wind/`)
- Group by **tier** (`tier1/`, `tier2/`, … `tier5/`)
- Group by **type** (`offensive/`, `defensive/`, `utility/`, `healing/`)

We will go with **element** — it is the most natural grouping for a spell archive and maps cleanly to the filename structure.

</details>

---

**Step 4 — Try by hand first**

Before using the terminal, open **Finder** (Mac) or **File Explorer** (Windows). Navigate to `Desktop/grimoire/`. Create a `fire/` folder and try moving 10 fire spells into it by clicking and dragging.

Now imagine doing that for all 300 files across 5 elements. How long would it take? What happens when you get 10,000 files next year?

That is exactly what the terminal solves. This is the first skill you will use in real research — and you will reach for it again every time a new dataset arrives.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

**Step 5 — Execute: sort with wildcards**

The `*` wildcard matches any characters. `*_fire_*` matches every filename that has `_fire_` anywhere in it — all 60 fire spells at once:

```bash
cd ~/Desktop/grimoire
mkdir fire ice lightning earth wind

mv *_fire_*.spell fire/
mv *_ice_*.spell ice/
mv *_lightning_*.spell lightning/
mv *_earth_*.spell earth/
mv *_wind_*.spell wind/
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

**Challenge — now try it by type**

Your spells are sorted into element folders. But a researcher might also want to find all offensive spells across every element at once.

Using `cp` (not `mv`) — so files stay in their element folders — organize the spells by type into `offensive/`, `defensive/`, `utility/`, `healing/` folders.

*Think before you type: what wildcard would match all offensive spells regardless of which element folder they are in?*

<details markdown="1">
<summary>Solution (expand after trying)</summary>

```bash
mkdir offensive defensive utility healing

cp */*_offensive_*.spell offensive/
cp */*_defensive_*.spell defensive/
cp */*_utility_*.spell utility/
cp */*_healing_*.spell healing/
```

`*/*` reaches into every immediate subdirectory at once — so `*/*_offensive_*` matches offensive spells inside fire/, ice/, lightning/, earth/, and wind/ all in one command. Using `cp` instead of `mv` means each spell now lives in two places simultaneously: its element folder and its type folder.

</details>

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

**Step 6 — Verify**

The `|` character is called a **pipe**. It takes the output of one command and feeds it as input to the next. `wc -l` counts lines — so `ls fire/ | wc -l` asks: *list the files in fire/, then count how many lines that produces.*

```bash
ls fire/ | wc -l      # count fire spells
ls ice/ | wc -l       # count ice spells
ls lightning/ | wc -l
ls earth/ | wc -l
ls wind/ | wc -l
# all 5 counts should sum to 300
```

You can also count everything at once:

```bash
ls */*.spell | wc -l  # total spells across all element folders
```

---

**Task: Keeping Track**

Create a file listing the names of all tier-3 spells in the grimoire.

The `grep` command searches for a pattern in input. Combined with `ls` and a pipe, you can filter filenames by any part of their name:

```bash
ls */*.spell | grep "_3_"          # list all tier-3 spells
ls */*.spell | grep "_3_" > tier3_spells.txt   # save the list to a file
```

The `>` operator redirects output to a file instead of printing it to the screen. If the file already exists it is overwritten; use `>>` to append instead.

The `cat` command displays the contents of a file:

```bash
cat tier3_spells.txt               # view the file you just created
wc -l tier3_spells.txt             # how many tier-3 spells are there?
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

**Step 7 — Document: write a README**

Always leave a note explaining what you did and why. Create a `README.md` in the grimoire folder:

```bash
nano ~/Desktop/grimoire/README.md
```

Write something like:

```
# Grimoire Archive

300 spell files sorted by element into subdirectories:
fire/, ice/, lightning/, earth/, wind/

Each filename follows the format:
  name_element_tier_type_mastery.spell

Organized: [today's date]
```

Save with `Ctrl+O`, exit with `Ctrl+X`.

This habit — documenting your organization decisions while they are fresh — is one of the highest-leverage things you can do for your research career. You will thank yourself in six months.

{: .note }
> You will transfer your sorted grimoire to the Yens in [The Scroll Transfer](../scroll-transfer/) room. Keep this directory — you need it there.

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quest

**Find the Rarest Combination**

The filename format is `name_element_tier_type_mastery.spell`. Find the least common element + type combination across all 300 spells.

The `cut` command splits each line on a delimiter and extracts specific fields. `sort` sorts lines alphabetically. `uniq -c` counts consecutive identical lines (so sort first). `sort -n` sorts numerically.

```bash
ls */*.spell | cut -d'_' -f2,4 | sort | uniq -c | sort -n
```

- `cut -d'_' -f2,4` — split on `_`, keep fields 2 (element) and 4 (type)
- `sort` — group identical combos together
- `uniq -c` — count each group
- `sort -n` — sort by count, smallest first

The rarest combinations appear at the top. What do you find?

<label class="quest-check"><input type="checkbox" data-room="d1-grimoire-vault" data-key="side1"> Side Quest complete</label>
