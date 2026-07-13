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

Every Boss Gate in this dungeon requires a `git push` as proof of work. No push, no gate.

---

## 🗡️ Main Quest

Your journey through the dungeon leaves a trail — and that trail is your version history. Carve your name into the Archive now.

{: .important }
> **Quest:** Fork the course repo, clone it to the Yens, create a branch, commit a file, and push it back to your fork.

**Step 1 — Fork the course repo, and build your site**

A **fork** is your own copy of the course repo, living under your GitHub account. Go to the [course repo on GitHub](https://github.com/gsbdarc/rf-bootcamp-2026) and click **Fork** in the top-right corner to create it.

Now turn your fork into your personal dungeon site:

- **Enable GitHub Pages:** on your fork, go to **Settings → Pages → Source → GitHub Actions → Save**.
- **Open your site:** `https://YOUR-USERNAME.github.io/rf-bootcamp-2026/`

This is now *your* quest-log site — your leaderboard rank and floor unlocks live here from now on. (It may take a minute to appear the first time.)

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
echo "Hello from the Repository" > my_first_commit.txt
git add my_first_commit.txt
git commit -m "Add my first commit from Day 1"
```

**Step 5 — Push to your fork**

**Pushing** sends your saved snapshots up to your fork on GitHub — where your site updates and, later, the Boss Gate grader can see your work.

```bash
git push -u origin day1-work
```

{: .important }
> **Every Boss Gate** requires a `git push` to your fork as the submission mechanism. Return to this room's steps whenever you need to submit work. This is the unlock pattern for every floor exit.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="main"> Main Quest complete</label>

---

## 🤖 Meet Claude Code

*You just performed the git ritual by hand — fork, clone, branch, commit, push. Every archmage learns the motions once. But no archmage repeats them by rote forever; they summon a familiar to carry the lantern.*

You now know what each git step *means* — and doing it once by hand is the point. From here on, you don't have to type it. **Claude Code** is an AI assistant that lives in your terminal: you describe what you want in plain English, and it does the work — running commands, editing files, and handling git for you.

Before we summon it, a quick word on *why* keeping your work in GitHub is worth the trouble — because these are exactly the things Claude Code will handle for you.

{: .tip }
> **Why GitHub is worth it for research:**
> - **Nothing is ever lost.** Every version is recoverable — roll a broken analysis back to last week's working one.
> - **Issues are your research record.** Log a data problem the moment you spot it, even if you fix it in five minutes. At paper-writing time, you can reconstruct *what happened and why*.
> - **Branches let you experiment safely.** Try a risky reanalysis without touching your working results. A failed experiment is a finding, not a mistake to delete.
> - **Reproducible and credited.** Commit your environment so a collaborator — or a reviewer — can rerun everything.

You will **not** memorize the commands for any of that. You say *"log this as an issue"* or *"try this on a branch,"* and Claude Code does it — the right way — because it follows a **skill** we wrote for research (more below).

---

## 🧭 How Claude Code Works

*Know your familiar before you summon it.* A few basics — expand any box for more.

**The model and the harness — the brain and the hands.** *Claude* is the **LLM** (large language model — the AI "brain" itself): it reads, reasons, and writes. On its own, it can only talk. **Claude Code** is the *harness* around that brain — it hands Claude real tools: read your files, run commands, edit code, use git. The model is the expert; the harness is the desk, the tools, and permission to act.

<details markdown="1">
<summary>The models — and how to switch them</summary>

Claude comes as a family, trading speed for power:

| Model | Best for |
|-------|----------|
| **Opus** | The most capable — deep reasoning, hard problems |
| **Sonnet** | Balanced — great for everyday work |
| **Haiku** | Fastest and lightest — quick, simple tasks |

Switch anytime with the `/model` command. Default to a capable model; drop to a faster one when the task is small.
</details>

<details markdown="1">
<summary>Plan mode vs. auto mode — look vs. act</summary>

- **Plan mode:** Claude Code investigates and proposes a plan but changes *nothing* until you approve. Perfect when you want to see the approach first.
- **Auto mode:** Claude Code carries the work out — editing files and running commands as it goes.

Press `Shift+Tab` to cycle between them. *Plan mode when you want a proposal; auto mode when you trust it to go.*
</details>

<details markdown="1">
<summary>Memory — so you don't repeat yourself</summary>

Claude Code can remember things across sessions: facts about your project, your preferences, how your group works. Think of it as a notebook Claude keeps for your project, so you don't re-explain everything each time you sit down.
</details>

**Terminal vs. the app — where you act, where you think.** Claude Code runs in the **terminal**, right where your files and commands live — ideal for research computing. The **Claude app** (website or desktop) is a chat window: great for questions, writing, and brainstorming, but it can't touch your machine. Same Claude underneath — use the app to *think*, use Claude Code to *act on your project*.

---

## 🔐 Claude at Stanford

You don't need a personal account. Stanford runs **Claude for Education** — a secure, university-managed environment — and for most people it's **free**.

- **Why go through Stanford?** Your work stays under Stanford's data-governance terms. Claude Code is approved for low-, moderate-, and high-risk research data (health data — known as PHI — needs special handling). For real research data, always use the Stanford route, never a personal account.
- **How to get it.** The **Standard tier is free** for all active faculty, students, postdocs, and staff with a SUNet ID. (A **Premium tier** is available if you have a PTA — a Stanford billing account your lab may hold.) Free still means you request it once, through **ServiceNow** (Stanford's IT request website) — it's a quick approval, not a purchase.
- **What you get.** Claude on the web and in the app, **Claude Code**, and **Skills** — which is how the research skill below reaches you.

{: .note }
> Full details and the request links live at [uit.stanford.edu/service/claude](https://uit.stanford.edu/service/claude). Your instructor can point you to the exact sign-up link in class.

---

## 📜 The github-for-research Skill

A **skill** is a set of standing instructions that teaches Claude Code how *our* research group works — so it does the right thing without being told each time:

- Do new work on a **branch**, never straight on `main`.
- **Log problems as issues** — even ones you fix immediately.
- **Never quietly change raw data**; always validate processed data.
- **Credit Claude** on every commit, and keep the environment **reproducible**.

It's already prepared for the course. If it isn't installed yet, one command sets it up (an instructor may have done this already):

```bash
bash scripts/install_github_for_research_skill.sh
```

{: .note }
> This is a one-time setup. Not sure if it's already installed? Just ask Claude Code — `> do you have the github-for-research skill?` — or run the command again; it's safe to re-run. The skill's home is `gsbdarc/claude-skill-github-for-research`.

---

## 📦 Side Quest — Summon the Familiar

{: .important }
> **Side Quest:** Install Claude Code on your laptop, interrogate a real research repository, then let the Familiar drive git for you. Complete this to earn your first **Weapon** and climb the leaderboard.

Optional — the Main Quest above is all the Boss Gate requires. But this is where the top of the leaderboard is decided.

### Part A — Summon it (on your laptop)

{: .warning }
> ⚠️ This Side Quest runs on **your laptop**, not the Yens. Everything before this lived on the cluster; Claude Code you install locally.

<details markdown="1">
<summary>💻 macOS</summary>

Open **Terminal** (as you did in The Command Spire), install Claude Code following the [official instructions](https://docs.claude.com/en/docs/claude-code/overview), then launch it from any project folder:

```bash
claude
```
</details>

<details markdown="1">
<summary>🪟 Windows</summary>

Open **Git Bash** — the same terminal you installed in The Command Spire — install Claude Code following the [official instructions](https://docs.claude.com/en/docs/claude-code/overview), then launch it from any project folder:

```bash
claude
```
</details>

When Claude Code starts, sign in with your **SUNet ID** (see *Claude at Stanford* above).

{: .note }
> Stuck on install or sign-in? This whole Side Quest is optional — raise your hand and we'll help, and you won't fall behind. The Boss Gate only needs the Main Quest above.

### Part B — Interrogate a real research repo

Here is the payoff of a well-kept repository: you can *ask it questions*. We'll use a real Stanford project — an analysis of whether San Francisco's graffiti 311 reports fell during COVID.

Clone it and open Claude Code inside it:

```bash
git clone https://github.com/gsbdarc/sf311.git
cd sf311
claude
```

Now ask, in plain English:

```
> What research question does this project answer?
> How was the raw 311 data cleaned, and where is that checked?
> Walk me through how to reproduce the main finding.
> Are there any open issues or things left to do?
```

{: .tip }
> Notice how Claude reads the README, the scripts, and the issue history to answer. That structure exists *because* someone kept the repo the way the skill describes — good practice is what makes a project answerable.

### Part C — Let the Familiar drive git

Go back to your own course repo and let Claude Code do the git work you just did by hand. Launch `claude` inside `rf-bootcamp-2026` and try:

```
> Commit my work on a new branch and open a pull request.
> Log an issue for the outlier spell I couldn't sort in the Grimoire Vault.
```

{: .note }
> Look at what it did: the work went on a **branch**, opened as a **pull request**, and the commit **credits Claude** — the good habits happened automatically, because of the skill.

<label class="quest-check"><input type="checkbox" data-room="d1-repository" data-key="side1"> Side Quest complete — 🗡️ Weapon earned: <strong>The Familiar</strong></label>

---

## 🧠 Skills Learned

- Fork, clone, branch, commit, and push with git
- How Claude Code works — model vs. harness, models, modes, memory, terminal vs. app
- How to get Claude through Stanford's managed service
- Interrogate a real research repo with Claude Code
- Let Claude Code drive git via the github-for-research skill
