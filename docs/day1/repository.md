---
layout: default
title: "The Repository"
parent: "Day 1 — The Gatehouse"
nav_order: 8
permalink: /day1/repository/
---

# The Repository

<div data-room-id="d1-repository"></div>

*The archive hall. Stone tablets record every change ever made to every scroll — who changed what, when, and why. Nothing is ever lost. Every version is recoverable. The Archmage demands one thing from all who pass through: your work must live here. Every Boss Gate requires a commit.*

---

## Main Quest

{: .important }
> **Quest:** Fork the course repo, clone it to the Yens, create a branch, commit a file, and push it back to your fork.

**Step 1 — Fork the course repo**

Go to the course repo on GitHub (your instructor will share the link). Click **Fork** to create your own copy under your GitHub account.

**Step 2 — Clone to the Yens**

On the Yens:
```bash
cd ~
git clone https://github.com/YOUR_GITHUB_USERNAME/rf_bootcamp_2026.git
cd rf_bootcamp_2026
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

---

## Chests

{: .chest }
> **Chest 1 — History Lens:** Use `git log --oneline`, `git diff HEAD~1`, and `git status` to answer: what was the last commit, what changed, and are there uncommitted modifications right now?

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="chest1"> History Lens unlocked</label>

{: .chest }
> **Chest 2 — Stash Spell:** Start editing a file, then realize you need to switch branches before finishing. Use `git stash` to park your changes, switch branches, then `git stash pop` to bring them back.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="chest2"> Stash Spell unlocked</label>

{: .chest }
> **Chest 3 — Blame Blade:** Run `git blame` on a file in the course repo. What information does each line show? When would a researcher use this on their own project?

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="chest3"> Blame Blade unlocked</label>

---

## Weapons Earned

{: .weapon }
> **History Lens** — `git log`, `git diff`, `git status` to understand your project's history and current state at a glance; never lose work or wonder what changed.
>
> **Stash Spell** — `git stash` to set aside work-in-progress without committing it; context-switch cleanly between branches.
>
> **Blame Blade** — `git blame` to trace every line to its author and commit; understand who changed what and why in any collaborative project.

---

## Skills Learned

- Fork a repo on GitHub and clone it to the Yens
- Create a branch, commit changes, and push to your fork
- Understand the fork → branch → commit → push → pull request workflow
- Know why version control is non-negotiable for reproducible research: you can always return to a working state, share your exact pipeline, and see exactly what changed between runs
