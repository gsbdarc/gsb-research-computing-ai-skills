---
layout: default
title: "Version Control with Git"
parent: "Day 1 — Foundations"
nav_order: 8
permalink: /day1/repository/
---

# Version Control with Git

<div data-room-id="d1-repository"></div>

Version control tracks every change you make to a project — who changed what, when, and why — so nothing is ever lost and you can roll back to any earlier state. In this course, your version history is also how you submit your work. This section sets up Git and GitHub and walks through the core workflow.

---

## Git and GitHub

**Git** is version control software that runs on your machine (or the Yens). It tracks every change you make to a project — who, what, and when — and lets you roll back to any previous state.

**GitHub** is a website that hosts git repositories in the cloud. It's where you share, back up, and submit your work.

<svg viewBox="0 0 660 176" role="img" aria-labelledby="gd1-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gd1-title">Git saves snapshots on your machine; GitHub stores them in the cloud. You push commits up to your fork and pull updates back down.</title>
  <defs>
    <marker id="gd1-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <rect x="14" y="30" width="276" height="116" rx="14" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="34" y="63" font-size="15" font-weight="700" fill="#2c3e50">💻  Your machine · the Yens</text>
  <text x="34" y="92" font-size="12.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#c0561a">git add · git commit</text>
  <text x="34" y="117" font-size="12.5" fill="#6a7280">saves snapshots locally</text>
  <rect x="370" y="30" width="276" height="116" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="390" y="63" font-size="15" font-weight="700" fill="#2c3e50">☁️  GitHub · the cloud</text>
  <text x="390" y="92" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#33415c">YOUR_USERNAME/rf-bootcamp-2026</text>
  <text x="390" y="117" font-size="12.5" fill="#6a7280">your fork — backup &amp; submission</text>
  <line x1="294" y1="76" x2="364" y2="76" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd1-ah)"/>
  <text x="330" y="66" text-anchor="middle" font-size="12.5" font-weight="600" fill="#b3611a">push</text>
  <line x1="366" y1="100" x2="296" y2="100" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd1-ah)"/>
  <text x="330" y="118" text-anchor="middle" font-size="12.5" font-weight="600" fill="#b3611a">pull</text>
</svg>

The workflow for this course:

<svg viewBox="0 0 680 392" role="img" aria-labelledby="gd2-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gd2-title">Three steps. Step 1, fork the shared course repo to your own GitHub account. Step 2, clone your fork down to the Yens, where you work. Step 3, push your finished work back up to your fork.</title>
  <defs>
    <marker id="gd2-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <!-- GitHub band -->
  <rect x="12" y="40" width="656" height="138" rx="16" fill="#f7f9fc" stroke="#d3ddec" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="32" y="66" font-size="12" font-weight="700" letter-spacing="0.6" fill="#8a94a6">☁️  ON GITHUB · THE CLOUD</text>
  <rect x="30" y="82" width="250" height="80" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="50" y="116" font-size="15" font-weight="700" fill="#2c3e50">Course repo</text>
  <text x="50" y="142" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">gsbdarc/rf-bootcamp-2026</text>
  <rect x="404" y="82" width="250" height="80" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="424" y="116" font-size="15" font-weight="700" fill="#2c3e50">Your fork</text>
  <text x="424" y="142" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">YOUR_USERNAME/rf-bootcamp-2026</text>
  <line x1="288" y1="122" x2="398" y2="122" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="343" y="111" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">① fork</text>
  <!-- Yens band -->
  <rect x="336" y="250" width="332" height="126" rx="16" fill="#fffaf2" stroke="#ecdcc0" stroke-width="1.5" stroke-dasharray="5 4"/>
  <rect x="404" y="262" width="250" height="76" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="424" y="294" font-size="15" font-weight="700" fill="#2c3e50">Your working copy</text>
  <text x="424" y="320" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#b5561f">edit → git add → git commit</text>
  <text x="356" y="362" font-size="12" font-weight="700" letter-spacing="0.6" fill="#b09668">💻  ON THE YENS · WHERE YOU WORK</text>
  <line x1="560" y1="164" x2="560" y2="260" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="597" y="219" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">② clone</text>
  <line x1="458" y1="260" x2="458" y2="164" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="423" y="219" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">③ push</text>
</svg>

*Three numbered steps: **① fork** — make your own copy of the course repo on GitHub · **② clone** — download that copy to the Yens, where you actually work · **③ push** — send your finished work back up to your fork.*

Each day's challenge is submitted with a `git push` to your fork as proof of work. No push, no submission.

Beyond `commit` and `push`, three GitHub features come up constantly — you'll use them later in the course, so it's worth knowing the words now:

- **Branch** — a separate line of work inside your repo. You make changes on a branch so your experiments never disturb the main, working version. When the work is ready, it gets merged back in.
- **Issue** — a written note attached to the repo: a task to do, a bug you hit, a question to revisit. Issues are timestamped and searchable, so they become a running record of what happened and why.
- **Pull request (PR)** — a proposal to merge one branch into another. It shows exactly what changed and lets you (or a collaborator) review the changes before they become part of the main version.

Version control isn't just bookkeeping — for research it's a real advantage:

{: .tip }
> **Why GitHub is worth it for research:**
> - **Nothing is ever lost.** Every version is recoverable — roll a broken analysis back to last week's working one.
> - **Issues are your research record.** Log a data problem the moment you spot it, even if you fix it in five minutes. At paper-writing time, you can reconstruct *what happened and why*.
> - **Branches let you experiment safely.** Try a risky reanalysis without touching your working results. A failed experiment is a finding, not a mistake to delete.
> - **Reproducible and credited.** Commit your environment so a collaborator — or a reviewer — can rerun everything.

---

## Exercise

Your work in this course is tracked in your version history. Set up your copy of the course repo and make your first commit now.

{: .important }
> **Exercise:** Fork the course repo, clone it to the Yens, create a branch, commit a file, and push it back to your fork.

**Step 1 — Fork the course repo, and build your site**

A **fork** is your own copy of the course repo, living under your GitHub account. Go to the [course repo on GitHub](https://github.com/gsbdarc/rf-bootcamp-2026) and click **Fork** in the top-right corner to create it.

Now turn your fork into your personal course site:

- **Enable GitHub Pages:** on your fork, go to **Settings → Pages → Source → GitHub Actions → Save**.
- **Open your site:** `https://YOUR-USERNAME.github.io/rf-bootcamp-2026/`

This is now *your* course site, where your progress and leaderboard position are tracked from here on. (It may take a minute to appear the first time.)

**Step 2 — Clone to the Yens**

**Cloning** downloads your fork onto the machine you're working on — here, the Yens.

```bash
cd ~
git clone https://github.com/YOUR_GITHUB_USERNAME/rf-bootcamp-2026.git
cd rf-bootcamp-2026
```

**Step 3 — Create a branch**

A **branch** is a safe, separate workspace, so your experiments never disturb the main version of your work.

```bash
git checkout -b day1-work
```

**Step 4 — Make a change and commit**

`add` chooses which changes go into your next snapshot; `commit` saves that snapshot with a message describing what changed and why.

```bash
echo "Hello from Day 1" > my_first_commit.txt
git add my_first_commit.txt
git commit -m "Add my first commit from Day 1"
```

**Step 5 — Push to your fork**

**Pushing** sends your saved snapshots up to your fork on GitHub — where your site updates and, later, your submitted work can be checked.

```bash
git push -u origin day1-work
```

{: .important }
> Every day's challenge is submitted the same way — a `git push` to your fork. Come back to these steps whenever you need to submit work.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="main"> Exercise complete</label>

---

## What You Learned

- Fork, clone, branch, commit, and push with git — version-control every project from day one

---

*Next: set up Claude Code and learn what data it can and can't be given — see **[Working with Claude Code](../familiars-den/)**.*
