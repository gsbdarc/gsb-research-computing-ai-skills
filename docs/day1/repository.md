---
layout: default
title: "The Repository"
parent: "Day 1 — The Gatehouse"
nav_order: 8
permalink: /day1/repository/
---

# The Repository

<div data-room-id="d1-repository"></div>

*Torchlight flickers across the Archive Hall, where floor-to-ceiling shelves hold stone tablets etched with every change ever made to every scroll — who touched what, when, and why. Nothing is ever lost here. No experiment vanishes, no breakthrough is accidentally overwritten, no "working version" is buried under desperate saves. The Archmage's law is absolute: your work must live in the Repository. Every Boss Gate is sealed until you commit.*

---

## 🖊️ Git and GitHub

**Git** is version control software that runs on your machine (or the Yens). It tracks every change you make to a project — who, what, and when — and lets you roll back to any previous state.

**GitHub** is a website that hosts git repositories in the cloud. It's where you share, back up, and submit your work.

```
  Your Yens                         GitHub (cloud)
  ─────────────────────────         ──────────────────────────
  git add / git commit              your fork
  (saves a snapshot locally)   ──push──►  YOUR_USERNAME/rf-bootcamp-2026
                               ◄──pull──
```

The workflow for this course:

```
  gsbdarc/rf-bootcamp-2026  ──fork──►  YOUR_USERNAME/rf-bootcamp-2026
                                                │
                                           git clone
                                                │
                                                ▼
                                         Yens: ~/rf-bootcamp-2026/
                                         (edit → add → commit → push)
```

Every Boss Gate in this dungeon requires a `git push` as proof of work. No push, no gate.

---

## 🗡️ Main Quest

Your journey through the dungeon leaves a trail — and that trail is your version history. Carve your name into the Archive now.

{: .important }
> **Quest:** Fork the course repo, clone it to the Yens, create a branch, commit a file, and push it back to your fork.

**Step 1 — Fork the course repo**

Go to the course repo on GitHub (your instructor will share the link). Click **Fork** to create your own copy under your GitHub account.

**Step 2 — Clone to the Yens**

On the Yens:
```bash
cd ~
git clone https://github.com/YOUR_GITHUB_USERNAME/rf-bootcamp-2026.git
cd rf-bootcamp-2026
```

**Step 3 — Create a branch**
```bash
git checkout -b day1-work
```

**Step 4 — Make a change and commit**
```bash
echo "Hello from the Repository" > my_first_commit.txt
git add my_first_commit.txt
git commit -m "Add my first commit from Day 1"
```

**Step 5 — Push to your fork**
```bash
git push -u origin day1-work
```

{: .important }
> **Every Boss Gate** requires a `git push` to your fork as the submission mechanism. Return to this room's steps whenever you need to submit work. This is the unlock pattern for every floor exit.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="main"> Main Quest complete</label>
