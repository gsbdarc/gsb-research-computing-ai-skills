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

**[⬇ Download grimoire.zip](https://drive.google.com/file/d/11ngowIAXgm2VK-_78Q-OdNrtRaHXX4Ej/view?usp=drive_link)**

```bash
mv ~/Downloads/grimoire.zip ~/Desktop/    # move from Downloads to Desktop
cd ~/Desktop                              # go to Desktop
unzip grimoire.zip                        # unzip the archive
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

*Class discussion — how would you organize these files?*

Options to consider:
- Group by **element** (`fire/`, `ice/`, `lightning/`, `earth/`, `wind/`)
- Group by **tier** (`tier1/`, `tier2/`, … `tier5/`)
- Group by **type** (`offensive/`, `defensive/`, `utility/`, `healing/`)

We will go with **element** — it is the most natural grouping for a spell archive and maps cleanly to the filename structure.

---

**Step 4 — Try by hand first**

Before using the terminal, open **Finder** (Mac) or **File Explorer** (Windows). Navigate to `Desktop/grimoire/`. Create a `fire/` folder and try moving 10 fire spells into it by clicking and dragging.

Now imagine doing that for all 300 files across 5 elements. How long would it take? What happens when you get 10,000 files next year?

That is exactly what the terminal solves.

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

---

**Step 6 — Verify**

```bash
ls fire/ | wc -l      # count fire spells
ls ice/ | wc -l       # count ice spells
# all 5 counts should sum to ~300
```

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
