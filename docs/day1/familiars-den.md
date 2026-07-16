---
layout: default
title: "Working with Claude Code"
parent: "Day 1 — Foundations"
nav_order: 9
permalink: /day1/familiars-den/
---

# Working with Claude Code

<div data-room-id="d1-familiars-den"></div>

You've set up Git and made your first commit by hand. Claude Code is a tool that can do that kind of work for you — and much more. This section covers what it is, how it works, how to get it through Stanford, and what data you can and can't give it.

---

## Meet Claude Code

In **Version Control with Git** you worked through fork, clone, branch, commit, and push by hand. That was the point: you now know what each step *means*. From here on, you don't have to type it yourself.

**Claude Code** is an AI assistant that lives in your terminal: you describe what you want in plain English, and it does the work — running commands, editing files, and handling git for you.

You just saw *why* keeping your work in GitHub is worth the trouble (see [Version Control with Git](../repository/)) — and those are exactly the habits Claude Code can handle for you. You will **not** memorize the commands for any of it. You say *"log this as an issue"* or *"try this on a branch,"* and Claude Code does it — the right way — because it follows a **skill** we wrote for research (more below).

---

## How Claude Code Works

A few basics — expand any box for more.

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
<summary>Tokens — how Claude reads, and what it costs</summary>

Claude doesn't read letter by letter or word by word — it reads in **tokens**. A token is a chunk of text: very roughly **¾ of a word**, or about **4 characters**. "Repository" is a couple of tokens; a full page of prose is around 500.

Everything is counted this way — the text you send *and* the text Claude sends back. Tokens matter for two reasons: they are **how much Claude can hold at once** (see *Context*, next), and they are **how paid AI services charge** — a fixed price per token. You won't pay by hand inside Claude Code, but the API calls you'll write on Day 2 are billed in exactly these tokens, so "send fewer tokens" comes to mean "spend less."

*Type `/cost` any time to see how many tokens the current session has used.*
</details>

<details markdown="1">
<summary>Context — Claude's working memory, and when to clear it</summary>

The **context** (or *context window*) is everything Claude can see right now: your conversation, any files it has read, and its own replies so far. It's measured in tokens — large, but not infinite.

A long session slowly fills the window. When it's full, or when the conversation has drifted far from the task at hand, the fix is to **start fresh**: `/clear` wipes the slate so the next question gets Claude's full attention. `/context` shows how full the window currently is.

If you're filling up but *don't* want to lose the thread, **`/compact`** is the middle ground: it replaces the long back-and-forth with a short summary, freeing room while keeping what matters. Use `/compact` to keep going on the same task; use `/clear` when you're moving on to a new one.

*Rule of thumb: one focused task per conversation. A clean context beats a cluttered one every time.*
</details>

<details markdown="1">
<summary>Memory — the notebook Claude keeps</summary>

Context is erased the moment you `/clear` or close the terminal. **Memory** is what survives — and it comes in two forms:

- **A `CLAUDE.md` file in your project.** A plain-text note you commit alongside your code, telling Claude how *this* project works — where the data lives, how to run things, conventions to follow. Every future session (yours or a collaborator's) reads the same file, which makes your project easier to pick back up and to reproduce.
- **Personal memory across sessions** — facts about you and how you like to work, remembered from one sitting to the next.

*Start any line with `#` to jot something into memory on the spot. Because `CLAUDE.md` is just a file in your repo, it's version-controlled like everything else you commit.*
</details>

<details markdown="1">
<summary>Skills — standing instructions for how your group works</summary>

A **skill** is a reusable set of instructions that Claude Code pulls in whenever it's relevant — so it follows your group's way of doing things without being told each time. If *memory* is a set of facts, a *skill* is a way of working.

Skills can come from Stanford, from your lab, or ones you write yourself. This course ships one — **github-for-research** — which you'll meet just below.
</details>

{: .tip }
> **See it for yourself — Claude lives in hidden files.** Remember the **dotfiles** from Command Line Basics — names starting with a `.`, invisible to a plain `ls`? That's exactly where Claude Code keeps its settings, skills, and memory. Reveal the hidden folder in your home directory and look inside:
>
> ```bash
> ls -a ~          # spot the hidden .claude folder among the dotfiles
> ls ~/.claude     # settings, skills, and memory — all plain text
> ```
>
> Open one up (`cat ~/.claude/CLAUDE.md` shows your personal memory, if you've saved any). Nothing here is magic — it's ordinary text in hidden files, editable and versionable like anything else you've touched today.

**Terminal vs. the app — where you act, where you think.** Claude Code runs in the **terminal**, right where your files and commands live — ideal for research computing. The **Claude app** (website or desktop) is a chat window: great for questions, writing, and brainstorming, but it can't touch your machine. Same Claude underneath — use the app to *think*, use Claude Code to *act on your project*.

---

## Claude at Stanford

You don't need a personal account. Stanford runs **Claude for Education** — a secure, university-managed environment — and for most people it's **free**.

- **Why go through Stanford?** Your work stays under Stanford's data-governance terms. Claude Code is approved for low-, moderate-, and high-risk research data (health data — known as PHI — needs special handling). For real research data, always use the Stanford route, never a personal account.
- **How to get it.** The **Standard tier is free** for all active faculty, students, postdocs, and staff with a SUNet ID. (A **Premium tier** is available if you have a PTA — a Stanford billing account your lab may hold.) Free still means you request it once, through **ServiceNow** (Stanford's IT request website) — it's a quick approval, not a purchase.
- **What you get.** Claude on the web and in the app, **Claude Code**, and **Skills** — which is how the research skill below reaches you.

### What leaves your machine — and what must not

Claude Code runs in two halves. The **harness** stays on your machine and is the part that actually *does things* — it reads and edits your files, runs shell commands, drives git, and calls other tools. The **model** — the brain that decides *what* to do — runs on **Anthropic's server**.

The two work in a **loop**: the harness sends the model your prompt and whatever it has read; the model sends back its next step (*"read this file," "run that command"*); the harness carries it out on your machine and reports the result; repeat until the task is done. The model never touches your machine directly — but everything the harness feeds it **leaves your machine and travels to that server**.

Here is the part people get wrong: Claude Code does **not** sort safe data from sensitive. It sends whatever you let it read — if you point it at a file full of names, those names go to the server. Nothing keeps personal, restricted, or health data local on its own. **Holding that data back is *your* job** — by not letting Claude read it in the first place.

<svg viewBox="0 0 840 384" role="img" aria-labelledby="cc-arch-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:840px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="cc-arch-title">How Claude Code works: both the harness and the tools it drives — your files, shell, git, and other tools — live on your machine. The harness exchanges with Claude's model on Anthropic's server across the campus perimeter in a loop: it sends your prompt and what it reads, and the model replies with the next step. Public data and your code may cross to the server; PII, restricted, and health data must not, and the harness will not withhold them for you.</title>
  <defs>
    <marker id="ah-green" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2e8b57"/></marker>
    <marker id="ah-slate" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
    <marker id="ah-brown" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#b5761f"/></marker>
  </defs>

  <!-- perimeter -->
  <line x1="606" y1="34" x2="606" y2="300" stroke="#b09668" stroke-width="2" stroke-dasharray="5 5"/>
  <text x="606" y="26" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="0.5" fill="#b09668">CAMPUS PERIMETER</text>

  <!-- your machine: contains BOTH the harness and the tools it drives -->
  <rect x="16" y="48" width="566" height="250" rx="16" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="36" y="78" font-size="14.5" font-weight="700" fill="#2c3e50">💻  Your machine · the Yens</text>
  <text x="36" y="99" font-size="11" fill="#9a8a68">The harness drives these locally:</text>

  <!-- tools list -->
  <text x="36" y="134" font-size="13">📄</text><text x="62" y="134" font-size="12.5" fill="#2c3e50">Your files — read &amp; edit</text>
  <text x="36" y="166" font-size="13">⌨️</text><text x="62" y="166" font-size="12.5" fill="#2c3e50">Shell — run commands</text>
  <text x="36" y="198" font-size="13">🔀</text><text x="62" y="198" font-size="12.5" fill="#2c3e50">Git — commit &amp; push</text>
  <text x="36" y="230" font-size="13">🔌</text><text x="62" y="230" font-size="12.5" fill="#2c3e50">Other tools — MCP, web</text>
  <text x="36" y="262" font-size="10.5" font-style="italic" fill="#a5281c">…and some files hold PII / NDA / PHI.</text>

  <!-- harness box, inside your machine, near the perimeter -->
  <rect x="356" y="150" width="170" height="94" rx="13" fill="#fbe9cf" stroke="#dcae6a" stroke-width="1.75"/>
  <text x="441" y="186" text-anchor="middle" font-size="14" font-weight="700" fill="#2c3e50">⚙️  The harness</text>
  <text x="441" y="207" text-anchor="middle" font-size="11" fill="#8a6d3b">Claude Code — the</text>
  <text x="441" y="222" text-anchor="middle" font-size="11" fill="#8a6d3b">local actor</text>

  <!-- harness drives the tools -->
  <line x1="354" y1="197" x2="292" y2="197" stroke="#b5761f" stroke-width="2.5" marker-end="url(#ah-brown)"/>
  <text x="323" y="188" text-anchor="middle" font-size="10.5" font-weight="600" fill="#95611a">drives</text>

  <!-- model box: anthropic server, across the perimeter -->
  <rect x="652" y="148" width="172" height="108" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="738" y="182" text-anchor="middle" font-size="14" font-weight="700" fill="#2c3e50">🧠  Claude's model</text>
  <text x="738" y="204" text-anchor="middle" font-size="11" fill="#6a7280">Anthropic's server</text>
  <text x="738" y="224" text-anchor="middle" font-size="10.5" fill="#8a94a6">reached via Stanford's</text>
  <text x="738" y="238" text-anchor="middle" font-size="10.5" fill="#8a94a6">governed route</text>

  <!-- up: harness sends context to model -->
  <line x1="526" y1="166" x2="648" y2="168" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#ah-green)"/>
  <text x="587" y="153" text-anchor="middle" font-size="11.5" font-weight="600" fill="#1f6b45">① sends context →</text>

  <!-- down: model replies with the next step -->
  <line x1="648" y1="200" x2="526" y2="202" stroke="#556a95" stroke-width="2.5" marker-end="url(#ah-slate)"/>
  <text x="587" y="220" text-anchor="middle" font-size="11.5" font-weight="600" fill="#3f4f74">② its next step ←</text>
  <text x="587" y="238" text-anchor="middle" font-size="10" fill="#8a94a6">loops until done</text>

  <!-- governance footer -->
  <rect x="16" y="316" width="808" height="52" rx="12" fill="#fbf3f0" stroke="#eccfc9" stroke-width="1.5"/>
  <text x="420" y="339" text-anchor="middle" font-size="12" font-weight="700" fill="#2c3e50">Only what the harness sends leaves the perimeter — public data &amp; your code are fine.</text>
  <text x="420" y="358" text-anchor="middle" font-size="11" fill="#a5281c">PII · NDA · PHI must not cross — Claude won't withhold them; keeping them out is your job.</text>
</svg>

*The harness is the local actor — it drives your files, shell, git, and other tools, and it runs the loop. The model only ever sees what the harness sends across the perimeter to Anthropic's server, reached under Stanford's governed route. Public data and your own code may cross; **PII, restricted, and health data must not — and the tool won't withhold them for you.** Never a personal account for real research data. We map out these categories in full on Day 2.*

{: .note }
> Full details and the request links live at [uit.stanford.edu/service/claude](https://uit.stanford.edu/service/claude). Your instructor can point you to the exact sign-up link in class.

---

## The github-for-research Skill

You just met skills in the abstract; here's the one this course ships. **github-for-research** teaches Claude Code how *our* research group works — so it does the right thing without being told each time:

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

## Optional Practice — Set Up Claude Code

{: .important }
> **Optional practice:** Install Claude Code on your laptop, ask it about a real research repository, then let it drive git for you.

Optional — the Day 1 Challenge only needs the exercise from Version Control with Git. This is extra practice.

### Part A — Install it and take it for a spin

<details markdown="1">
<summary>Show steps</summary>

{: .warning }
> ⚠️ This runs on **your laptop**, not the Yens. Everything before this lived on the cluster; Claude Code you install locally.

**macOS:** open **Terminal** (as you did in Command Line Basics). **Windows:** open **Git Bash** — the same terminal you installed there. Then install Claude Code following the [official instructions](https://docs.claude.com/en/docs/claude-code/overview) and launch it from any project folder:

```bash
claude
```

**Your first run — try each of these once:**

1. **Launch it** — run `claude` in a project folder.
2. **Sign in** with your **SUNet ID** (see *Claude at Stanford* above).
3. **Check your usage** — type `/cost` to see how many tokens this session has used (see the *Tokens* box above).
4. **Switch modes** — press `Shift+Tab` to flip between plan mode and auto mode (see the *Plan mode vs. auto mode* box above).

{: .note }
> Stuck on install or sign-in? This whole section is optional — raise your hand and we'll help, and you won't fall behind. The Day 1 Challenge only needs the exercise from Version Control with Git.

</details>

### Part B — Ask a real research repo questions

<details markdown="1">
<summary>Show steps</summary>

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

</details>

### Part C — Let Claude Code drive git

<details markdown="1">
<summary>Show steps</summary>

Go back to your own course repo and let Claude Code do the git work you just did by hand. Launch `claude` inside `rf-bootcamp-2026` and give it a real, checkable task — put your SUNet ID in a file and have Claude drive the whole git loop:

```
> Create a file called signed_in.txt containing my SUNet ID, commit it on a new branch, and open a pull request.
```

Then confirm it worked: on your fork on GitHub, check that a new **branch** and a **pull request** appeared, and that `signed_in.txt` holds your SUNet ID. For a second task, try:

```
> Log an issue for the outlier I couldn't sort in Bulk File Operations.
```

{: .note }
> Look at what it did: the work went on a **branch**, opened as a **pull request**, and the commit **credits Claude** — the good habits happened automatically, because of the skill.

</details>

<label class="quest-check"><input type="checkbox" data-room="d1-familiars-den" data-key="side1"> Optional practice complete</label>

---

## What You Learned

- How Claude Code works — model vs. harness, models, modes, tokens, context, memory, skills, terminal vs. app
- What a token is, and why context and cost are both measured in tokens
- What leaves your machine on an AI call — and why sensitive data can't go to an external LLM
- How to get Claude through Stanford's managed service
- Interrogate a real research repo with Claude Code
- Let Claude Code drive git via the github-for-research skill
