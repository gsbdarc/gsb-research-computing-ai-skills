---
layout: default
title: "Boss Gate 1"
parent: "Day 1 — The Gatehouse"
nav_order: 10
permalink: /day1/boss-gate-1/
---

# Boss Gate 1: The Archmage's Seal

<div data-room-id="d1-boss-gate-1"></div>

*Iron doors. A glowing crest — the Archmage's seal — pulses cold blue across the stone.*

*"You have learned to move. You have learned to sort. You have learned to reach across the wire into machines far more powerful than your own. Now prove it."*

*In the Archmage's staging vault, fifty-one spell files lie unsorted. Fifty belong to the five known elements. One does not. It bears a seal. Find it. Read it. Commit the proof. The gate does not open until your push lands.*

---

## 🔑 The Challenge

{: .important }
> **Quest:** Navigate to the vault, sort the spells by element, find the outlier, read its seal, and push the proof to your GitHub fork.

---

### Step 1 — Create your workspace in scratch

You are already SSH'd onto the Yens. Create a personal working directory and copy the vault into it:

```bash
mkdir /scratch/shared/$USER/boss1
cp -r /scratch/shared/rf-bootcamp-2026/boss1/ /scratch/shared/$USER/boss1/
```

`-r` means recursive — copies the entire directory, just like `scp -r` in the Scroll Transfer room.

Navigate in and count what you have:

```bash
cd /scratch/shared/$USER/boss1
ls | wc -l          # how many spell files are there?
ls | head -10       # look at the naming pattern
```

---

### Step 2 — Sort the vault by element

The filename format is `name_ELEMENT_tier_type_mastery.spell`. Create directories for the five standard elements and move the spells into them:

```bash
mkdir fire ice lightning earth wind

mv *_fire_*.spell fire/
mv *_ice_*.spell ice/
mv *_lightning_*.spell lightning/
mv *_earth_*.spell earth/
mv *_wind_*.spell wind/
```

---

### Step 3 — Count and find what remains

Verify your work:

```bash
ls fire/ | wc -l
ls ice/ | wc -l
ls lightning/ | wc -l
ls earth/ | wc -l
ls wind/ | wc -l
```

Now check what is still in the working directory — what wildcards could not sort:

```bash
ls *.spell
```

One file does not belong to any of the five elements. That is the Archmage's signature spell.

---

### Step 4 — Read the seal

```bash
cat <the-remaining-filename>.spell
```

`cat` displays the contents of a file. The file contains a line beginning with `SIGNATURE:` — that string is the Archmage's seal. Copy it exactly.

---

### Step 5 — Record the proof in your repo

Navigate to your cloned repository on the Yens:

```bash
cd ~/rf-bootcamp-2026/
```

Create a file called `signature_spell.txt` with two lines:

```bash
nano signature_spell.txt
```

Write exactly:

```
Spell found: <the-filename-you-found>.spell
Signature: <the-seal-string-from-the-file>
```

Save with `Ctrl+O`, exit with `Ctrl+X`.

---

### Step 6 — Push to your fork

```bash
git add signature_spell.txt
git commit -m "Boss Gate 1: Archmage signature found"
git push
```

Open your GitHub fork in a browser and confirm `signature_spell.txt` appears. That commit is your key.

{: .note }
> If `git push` asks for credentials, your token may not be cached on the Yens. Ask an instructor.

---

## 🧠 Skills This Gate Tests

| Skill | Where you learned it |
|-------|---------------------|
| `ssh` to a remote server | The SSH Gate |
| `mkdir` to create directories | The Command Spire |
| `cd` to navigate the file system | The Command Spire |
| `cp -r` to copy a directory | The Command Spire (cp) + Scroll Transfer (-r flag) |
| `ls \| wc -l` to count files | The Grimoire Vault |
| `mv *_element_*` wildcard sorting | The Grimoire Vault |
| `cat` to read a file's contents | (new — but you know `ls` and `head`) |
| `git add / commit / push` | The Repository |

<label class="quest-check"><input type="checkbox" data-room="d1-boss-gate-1" data-key="main"> Boss Gate 1 complete</label>

---

## 📊 End of Day 1 — Sync Your Progress

Let your instructor see where you landed today. Takes 2 minutes.

**Step 1 — Export your quest log**

Click **"📤 Sync to leaderboard"** in the bottom-left corner of this page. A file called `quest_log.json` downloads to your laptop.

**Step 2 — Upload it to your fork**

Go to your fork on GitHub (`github.com/YOUR_USERNAME/rf-bootcamp-2026`) → **Add file → Upload files** → drag `quest_log.json` in → **Commit changes** to `main`.

The leaderboard updates within 2 minutes. Your instructor can see how many quests you completed and whether you cleared the Boss Gate.
