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

<svg viewBox="0 0 760 176" role="img" aria-labelledby="gd1-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gd1-title">Git saves snapshots on your machine; GitHub stores them in the cloud. You push commits up to your fork and pull updates back down.</title>
  <defs>
    <marker id="gd1-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <rect x="14" y="30" width="330" height="116" rx="14" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="34" y="63" font-size="15" font-weight="700" fill="#2c3e50">💻  Your machine · the Yens</text>
  <text x="34" y="92" font-size="12.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#c0561a">git add · git commit</text>
  <text x="34" y="117" font-size="12.5" fill="#6a7280">saves snapshots locally</text>
  <rect x="416" y="30" width="330" height="116" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <g transform="translate(436,50) scale(1.05)"><path fill="#2c3e50" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></g>
  <text x="460" y="63" font-size="15" font-weight="700" fill="#2c3e50">GitHub · the cloud</text>
  <text x="436" y="92" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#33415c">YOUR_USERNAME/gsb-research-computing-ai-skills</text>
  <text x="436" y="117" font-size="12.5" fill="#6a7280">your fork — backup &amp; submission</text>
  <line x1="348" y1="76" x2="412" y2="76" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd1-ah)"/>
  <text x="380" y="66" text-anchor="middle" font-size="12.5" font-weight="600" fill="#b3611a">push</text>
  <line x1="414" y1="100" x2="350" y2="100" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd1-ah)"/>
  <text x="380" y="118" text-anchor="middle" font-size="12.5" font-weight="600" fill="#b3611a">pull</text>
</svg>

Git saves your work as **commits** — snapshots of your whole project at a moment in time, each with a short message describing what changed. Your history is a chain of these snapshots, and you can return to any earlier one at any time.

<svg viewBox="0 0 660 130" role="img" aria-labelledby="gc-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gc-title">A commit is a snapshot of your project. Your history is a chain of commits, oldest on the left, newest on the right.</title>
  <defs>
    <marker id="gc-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#b0b8c4"/></marker>
  </defs>
  <text x="20" y="62" font-size="13" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">main</text>
  <line x1="110" y1="58" x2="530" y2="58" stroke="#e0c9a6" stroke-width="3"/>
  <line x1="552" y1="58" x2="614" y2="58" stroke="#c2cad4" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#gc-ah)"/>
  <text x="612" y="44" text-anchor="end" font-size="10.5" fill="#9aa4b0">time →</text>
  <circle cx="110" cy="58" r="13" fill="#fff" stroke="#e67e22" stroke-width="3"/>
  <text x="110" y="94" text-anchor="middle" font-size="11" fill="#5b6472">init project</text>
  <circle cx="250" cy="58" r="13" fill="#fff" stroke="#e67e22" stroke-width="3"/>
  <text x="250" y="94" text-anchor="middle" font-size="11" fill="#5b6472">add raw data</text>
  <circle cx="390" cy="58" r="13" fill="#fff" stroke="#e67e22" stroke-width="3"/>
  <text x="390" y="94" text-anchor="middle" font-size="11" fill="#5b6472">clean data</text>
  <circle cx="530" cy="58" r="13" fill="#e67e22" stroke="#e67e22" stroke-width="3"/>
  <text x="530" y="94" text-anchor="middle" font-size="11" fill="#5b6472">first results</text>
  <text x="530" y="112" text-anchor="middle" font-size="10" font-weight="700" fill="#b3611a">latest</text>
</svg>

*Each dot is one commit — a saved snapshot. The chain runs oldest (left) to newest (right).*

A **branch** is a **git** feature that lets you build a *separate* line of commits without disturbing your main work. You branch off, commit there, and merge back when the work is ready — so a risky experiment never touches your working version.

<svg viewBox="0 0 660 200" role="img" aria-labelledby="gb-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gb-title">A branch is a separate line of commits. You branch off main, make commits on the branch, then merge them back — main stays intact until you do.</title>
  <text x="20" y="64" font-size="13" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">main</text>
  <line x1="110" y1="60" x2="580" y2="60" stroke="#c2cad4" stroke-width="3"/>
  <path d="M230,60 C275,60 288,140 330,140" fill="none" stroke="#e67e22" stroke-width="3"/>
  <line x1="330" y1="140" x2="450" y2="140" stroke="#e67e22" stroke-width="3"/>
  <path d="M450,140 C505,140 518,60 560,60" fill="none" stroke="#e67e22" stroke-width="3"/>
  <circle cx="120" cy="60" r="12" fill="#fff" stroke="#5b6472" stroke-width="3"/>
  <circle cx="230" cy="60" r="12" fill="#fff" stroke="#5b6472" stroke-width="3"/>
  <circle cx="560" cy="60" r="12" fill="#5b6472" stroke="#5b6472" stroke-width="3"/>
  <circle cx="330" cy="140" r="12" fill="#fff" stroke="#e67e22" stroke-width="3"/>
  <circle cx="450" cy="140" r="12" fill="#fff" stroke="#e67e22" stroke-width="3"/>
  <text x="230" y="38" text-anchor="middle" font-size="10.5" fill="#9aa4b0">branch off</text>
  <text x="560" y="38" text-anchor="middle" font-size="10.5" fill="#9aa4b0">merge back</text>
  <text x="390" y="172" text-anchor="middle" font-size="13" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#b3611a">experiment</text>
</svg>

*You branch off `main`, make commits on `experiment`, then merge them back. `main` stays intact until you do.*

The workflow for this course:

<svg viewBox="0 0 786 392" role="img" aria-labelledby="gd2-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="gd2-title">Three steps. Step 1, fork the shared course repo to your own GitHub account. Step 2, clone your fork down to the Yens, where you work. Step 3, push your finished work back up to your fork.</title>
  <defs>
    <marker id="gd2-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>
  <!-- GitHub band -->
  <rect x="8" y="40" width="770" height="138" rx="16" fill="#f7f9fc" stroke="#d3ddec" stroke-width="1.5" stroke-dasharray="5 4"/>
  <g transform="translate(28,56) scale(0.82)"><path fill="#8a94a6" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></g>
  <text x="46" y="66" font-size="12" font-weight="700" letter-spacing="0.6" fill="#8a94a6">ON GITHUB · THE CLOUD</text>
  <rect x="24" y="82" width="332" height="80" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="44" y="116" font-size="15" font-weight="700" fill="#2c3e50">Course repo</text>
  <text x="44" y="142" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">gsbdarc/gsb-research-computing-ai-skills</text>
  <rect x="430" y="82" width="332" height="80" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="450" y="116" font-size="15" font-weight="700" fill="#2c3e50">Your fork</text>
  <text x="450" y="142" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">YOUR_USERNAME/gsb-research-computing-ai-skills</text>
  <line x1="364" y1="122" x2="424" y2="122" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="393" y="111" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">① fork</text>
  <!-- Yens band -->
  <rect x="360" y="250" width="418" height="126" rx="16" fill="#fffaf2" stroke="#ecdcc0" stroke-width="1.5" stroke-dasharray="5 4"/>
  <rect x="430" y="262" width="332" height="76" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="450" y="294" font-size="15" font-weight="700" fill="#2c3e50">Your working copy</text>
  <text x="450" y="320" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#b5561f">edit → git add → git commit</text>
  <text x="382" y="362" font-size="12" font-weight="700" letter-spacing="0.6" fill="#b09668">💻  ON THE YENS · WHERE YOU WORK</text>
  <line x1="662" y1="164" x2="662" y2="260" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="699" y="219" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">② clone</text>
  <line x1="530" y1="260" x2="530" y2="164" stroke="#e67e22" stroke-width="2.5" marker-end="url(#gd2-ah)"/>
  <text x="493" y="219" text-anchor="middle" font-size="13" font-weight="700" fill="#b3611a">③ push</text>
</svg>

*Three numbered steps: **① fork** — make your own copy of the course repo on GitHub · **② clone** — download that copy to the Yens, where you actually work · **③ push** — send your finished work back up to your fork.*

Each day's challenge is submitted with a `git push` to your fork as proof of work. No push, no submission.

You've now met the two core **git** ideas — commits and branches. Two more features come from **GitHub** (the hosting side) and show up later in the course:

- **Issue** — a written note attached to the repo: a task to do, a bug you hit, a question to revisit. Issues are timestamped and searchable, so they can serve as a running log if you choose to use them that way.
- **Pull request (PR)** — a proposal to merge one branch into another. It shows exactly what changed and lets you (or a collaborator) review the changes before they become part of the main version.

Version control isn't just bookkeeping — it offers a few concrete advantages for research:

{: .tip }
> **Why version control helps research:**
> - **A readable history of what changed and why.** Every commit carries a short message. Instead of guessing what a file used to hold, you scroll its history and read *"clean data: drop 3 duplicate rows"* right next to the exact lines that changed.
> - **No more filename soup.** You don't need `analysis_final_v2_USETHIS_edited.R` to keep track of versions. There's one `analysis.R`, and its history holds every past version with an explanation of each change. The filename says *what the file is*; the history says *how it got there*.
> - **Experiment safely on a branch.** Try a risky reanalysis without touching your working results. If it doesn't pan out, the branch is a record of what you tried rather than a mess to clean up.
> - **Project management, even if you barely write code.** GitHub's issues and pull requests aren't only for software teams — you can use issues to track to-dos, data questions, or bugs, and pull requests to review a change before it's merged into your main version.
> - **Backed up and shareable.** Every version is recoverable, and pushing to GitHub backs your work up and lets a collaborator — or your future self — pick it up.

Version control is powerful, but it isn't a cure-all. A few honest caveats:

{: .warning }
> **Caveats:**
> - **Git has a steep learning curve.** It's genuinely confusing for newcomers — expect to lean on notes, cheatsheets, and AI tools at first.
> - **GitHub is a commercial product.** It's owned by Microsoft, not a community-run open project. Convenient and widely used, but not neutral infrastructure.
> - **Git is a poor fit for versioning data.** It's built to track line-by-line changes in text and code; large or binary data files make the repository slow and bloated.
> - **GitHub is not for datasets** — especially large ones. It enforces file-size limits and isn't meant for data storage. Keep data on the cluster (`/yen/projects`, `/scratch`) or in a data repository, not in your GitHub repo.

---

## Exercise

Your work in this course is tracked in your version history. Set up your copy of the course repo and make your first commit now.

{: .important }
> **Exercise:** Fork the course repo, clone it to the Yens, authenticate with GitHub, create a branch, commit a file, and push it back to your fork.

**Step 1 — Fork the course repo, and build your site**

A **fork** is your own copy of the course repo, living under your GitHub account. Go to the [course repo on GitHub](https://github.com/gsbdarc/gsb-research-computing-ai-skills) and click **Fork** in the top-right corner to create it.

Now turn your fork into your personal course site:

- **Enable GitHub Pages:** on your fork, go to **Settings → Pages → Source → GitHub Actions → Save**.
- **Open your site:** `https://YOUR-USERNAME.github.io/gsb-research-computing-ai-skills/`

This is now *your* course site, where your progress and leaderboard position are tracked from here on. (It may take a minute to appear the first time.)

**Step 2 — Clone to the Yens**

**Cloning** downloads your fork onto the machine you're working on — here, the Yens.

```bash
cd ~
git clone https://github.com/YOUR_GITHUB_USERNAME/gsb-research-computing-ai-skills.git
cd gsb-research-computing-ai-skills
```

**Step 3 — Authenticate with GitHub (one time)**

Pushing to your fork has to prove it's really you. The **GitHub CLI** (`gh`) sets this up once, and then git just works. On the Yens, load it and sign in:

```bash
module load gh     # make gh available on the Yens
gh auth login      # answer: GitHub.com → HTTPS → Authenticate Git? Yes → Login with a web browser
```

`gh` prints a **one-time code**. On your **laptop**, open [github.com/login/device](https://github.com/login/device), enter the code, and approve — the Yens have no browser, so you do this part from your laptop. That's it: `gh` configures git to use your GitHub login, so every `git push` from now on works without asking for a password.

<details markdown="1">
<summary>Setting up <code>gh</code> on your own laptop</summary>

You'll want `gh` on your laptop too (for the Claude Code work later). Install it, then run the same `gh auth login`:

- **macOS** (Homebrew): `brew install gh`
- **Windows** (in PowerShell — then it's usable from Git Bash too): `winget install --id GitHub.cli`
- **Linux** / other: see the [official instructions](https://github.com/cli/cli#installation)

```bash
gh auth login    # GitHub.com → HTTPS → Login with a web browser
```

On a laptop `gh` can open the browser for you automatically.

</details>

**Step 4 — Create a branch**

A **branch** is a safe, separate workspace, so your experiments never disturb the main version of your work.

```bash
git checkout -b experiment
```

**Step 5 — Make a change and commit**

`add` chooses which changes go into your next snapshot; `commit` saves that snapshot with a message describing what changed and why.

```bash
echo "Hello from Day 1" > my_first_commit.txt
git add my_first_commit.txt
git commit -m "Add my first commit from Day 1"
```

**Step 6 — Push to your fork**

**Pushing** sends your saved snapshots up to your fork on GitHub — where your site updates and, later, your submitted work can be checked.

```bash
git push -u origin experiment
```

{: .important }
> Every day's challenge is submitted the same way — a `git push` to your fork. Come back to these steps whenever you need to submit work.

**Step 7 — Ready your spell-caster (one time)**

Your fork ships with a small program called `cast` — your spell-caster for recording quest progress to the leaderboard. Make it executable and give it a short name you can run from anywhere on the Yens (run this from inside your repo):

```bash
chmod +x scripts/cast
echo "alias cast=\"$PWD/scripts/cast\"" >> ~/.bash_profile
source ~/.bash_profile
```

From now on, whenever you finish a quest, the site shows a **🔮 Cast to the leaderboard** button with a one-line spell — copy it and run `cast <spell>` here to update your standing.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="main"> Exercise complete</label>

---

## What You Learned

- Fork, clone, branch, commit, and push with git — version-control every project from day one

---

*Next: set up Claude Code and learn what data it can and can't be given — see **[Working with Claude Code](../familiars-den/)**.*
