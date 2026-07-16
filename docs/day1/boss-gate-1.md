---
layout: default
title: "Day 1 Challenge"
parent: "Day 1 — Foundations"
nav_order: 10
permalink: /day1/boss-gate-1/
---

# Day 1 Challenge

<div data-room-id="d1-boss-gate-1"></div>

This challenge combines everything from Day 1: moving around the file system, sorting files in bulk, connecting over SSH, and committing your work with Git.

A shared directory contains fifty-one files. Fifty belong to five known categories. One does not. Your task is to find that outlier, read the value stored inside it, and push the proof to your GitHub fork.

---

## The Challenge

{: .important }
> **Task:** Go to the shared directory, sort the files by category, find the file that doesn't fit, read the value inside it, and push the proof to your GitHub fork.

---

### Step 1 — Create your workspace in scratch

You are already SSH'd onto the Yens. Create a personal working directory and copy the shared files into it:

```bash
mkdir /scratch/shared/$USER/boss1
cp -r /scratch/shared/rf-bootcamp-2026/boss1/ /scratch/shared/$USER/boss1/
```

`-r` means recursive — copies the entire directory, just like `scp -r` in the Transferring Files (scp) room.

Navigate in and count what you have:

```bash
cd /scratch/shared/$USER/boss1
ls | wc -l          # how many files are there?
ls | head -10       # look at the naming pattern
```

---

### Step 2 — Sort the files by category

The filename format is `name_CATEGORY_tier_type_level.spell`. Create directories for the five standard categories and move the files into them:

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

Now check what is still in the working directory — what the wildcards could not sort:

```bash
ls *.spell
```

One file does not belong to any of the five categories. That is the file you are looking for.

---

### Step 4 — Read the file

```bash
cat <the-remaining-filename>.spell
```

`cat` displays the contents of a file. The file contains a line beginning with `SIGNATURE:` — copy that string exactly.

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
Signature: <the-signature-string-from-the-file>
```

Save with `Ctrl+O`, exit with `Ctrl+X`.

---

### Step 6 — Push to your fork

```bash
git add signature_spell.txt
git commit -m "Day 1 Challenge: signature found"
git push
```

Open your GitHub fork in a browser and confirm `signature_spell.txt` appears. That commit is your submission.

{: .note }
> If `git push` asks for credentials, your token may not be cached on the Yens. Ask an instructor.

---

## What You Learned

| Skill | Where you learned it |
|-------|---------------------|
| `ssh` to a remote server | Connecting to a Cluster |
| `mkdir` to create directories | Command Line Basics |
| `cd` to navigate the file system | Command Line Basics |
| `cp -r` to copy a directory | Command Line Basics (cp) + Transferring Files (scp) (-r flag) |
| `ls \| wc -l` to count files | Bulk File Operations |
| `mv *_category_*` wildcard sorting | Bulk File Operations |
| `cat` to read a file's contents | (new — but you know `ls` and `head`) |
| `git add / commit / push` | Version Control with Git |

<label class="quest-check"><input type="checkbox" data-room="d1-boss-gate-1" data-key="main"> Day 1 Challenge complete</label>
