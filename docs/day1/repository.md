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

Every Boss Gate in this dungeon is submitted with a `git push` — that's how your work lands on your fork and shows up on the leaderboard.

---

## 🗡️ Main Quest

Your journey through the dungeon leaves a trail — and that trail is your version history. Carve your name into the Archive now.

{: .important }
> **Quest:** Fork the course repo, configure three settings on GitHub, clone it to the Yens, commit a file, and push it back to your fork on `main`.

---

**Step 1 — Fork the course repo**

Go to the course repo on GitHub (your instructor will share the link). Click **Fork** → **Create fork**.

---

**Step 2 — Two required settings on your fork**

After forking, do these two things on GitHub before anything else. Each one is needed for the dungeon to work.

**a) Enable GitHub Actions**

Your personal dungeon site is built by a GitHub Actions workflow every time you push to `main`. On forks, GitHub requires you to opt in manually.

*Actions tab → "I understand my workflows, go ahead and enable them"*

**b) Enable GitHub Pages**

This deploys your personal copy of the dungeon website — your quest checkboxes and leaderboard progress are tied to your own site, not the instructor's.

*Settings → Pages → Source: Deploy from a branch → Branch: `main` / `docs` → Save*

After a minute or two, your site will be live at:
```
https://YOUR_GITHUB_USERNAME.github.io/rf-bootcamp-2026/
```

---

**Step 3 — Clone to the Yens**

```bash
cd ~
git clone https://github.com/YOUR_GITHUB_USERNAME/rf-bootcamp-2026.git
cd rf-bootcamp-2026
```

**Step 4 — Make a change and commit**

```bash
echo "Hello from the Repository" > my_first_commit.txt
git add my_first_commit.txt
git commit -m "Add my first commit from Day 1"
```

**Step 5 — Push to `main`**

```bash
git push
```

GitHub Actions will now rebuild your site on your fork. Check the **Actions tab** on GitHub — you should see a green checkmark within a minute.

{: .important }
> **Every Boss Gate** works the same way: make your changes, `git add`, `git commit`, `git push`. Every floor is unlocked from the start — pushing just saves your work and keeps your site and leaderboard current. You always push to `main` — no branch switching needed.

---

## 🤖 Claude + Git Hands-On

Claude Code and git are a natural pair — Claude can explain what happened, draft commit messages, and help you understand diffs before you push.

**Ask Claude to explain your history:**
```bash
git log --oneline   # see your commits
claude              # open Claude Code, then ask:
```
*"Explain the last 3 commits in this repo in plain English."*

**Ask Claude to write a commit message:**

Make a small change — edit your `my_first_commit.txt` file. Then:
```bash
git diff            # show what changed
```
Ask Claude: *"Write a concise git commit message for this change."*

Then commit it:
```bash
git add my_first_commit.txt
git commit -m "your message here"
git push
```

{: .note }
> Claude Code sees your git history, staged files, and diffs — all of that is context it sends to Anthropic's servers. For this repo (public course material), that's fine. For a repo with research data, be deliberate about what you have staged.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="main"> Main Quest complete</label>
