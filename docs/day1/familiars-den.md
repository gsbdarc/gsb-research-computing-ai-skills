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

A few basics worth knowing before you start.

**The model and the harness — the brain and the hands.** *Claude* is the **LLM** (large language model — the AI "brain" itself): it reads, reasons, and writes. On its own, it can only talk. **Claude Code** is the *harness* around that brain — it hands Claude real tools: read your files, run commands, edit code, use git. The model is the expert; the harness is the desk, the tools, and permission to act.

### The models — and how to switch them

Claude comes as a family, trading speed for power:

| Model | Best for |
|-------|----------|
| **Opus** | The most capable — deep reasoning, hard problems |
| **Sonnet** | Balanced — great for everyday work |
| **Haiku** | Fastest and lightest — quick, simple tasks |

Switch anytime with the `/model` command. Default to a capable model; drop to a faster one when the task is small.

### Plan mode vs. auto mode — look vs. act

- **Plan mode:** Claude Code investigates and proposes a plan but changes *nothing* until you approve. Perfect when you want to see the approach first.
- **Auto mode:** Claude Code carries the work out — editing files and running commands as it goes.

Press `Shift+Tab` to cycle between them. *Plan mode when you want a proposal; auto mode when you trust it to go.*

### Tokens — how Claude reads, and what it costs

Claude doesn't read letter by letter or word by word — it reads in **tokens**. A token is a chunk of text: very roughly **¾ of a word**, or about **4 characters**. "Repository" is a couple of tokens; a full page of prose is around 500.

Everything is counted this way — the text you send *and* the text Claude sends back. Tokens matter for two reasons: they are **how much Claude can hold at once** (see *Context*, next), and they are **how paid AI services charge** — a fixed price per token. You won't pay by hand inside Claude Code, but the API calls you'll write on Day 2 are billed in exactly these tokens, so "send fewer tokens" comes to mean "spend less."

*Type `/cost` any time to see how many tokens the current session has used.*

{: .important }
> **Run out of usage and you wait — you can't pay for more.** Stanford gives you Claude on a **managed plan with a usage limit**, not the pay-per-token billing a personal account would have. When you use up your allowance, Claude Code **pauses until your limit resets after a set time** — there is no "just charge me for more tokens" button. To make your usage last: switch to a lighter model with `/model` (Haiku and Sonnet cost far less than Opus), keep each session to one focused task, and use `/clear` or `/compact` so you're not re-sending a large context every turn.

### Context — Claude's working memory, and when to clear it

The **context** (or *context window*) is everything Claude can see right now: your conversation, any files it has read, and its own replies so far. It's measured in tokens — large, but not infinite.

A long session slowly fills the window. When it's full, or when the conversation has drifted far from the task at hand, the fix is to **start fresh**: `/clear` wipes the slate so the next question gets Claude's full attention. `/context` shows how full the window currently is.

If you're filling up but *don't* want to lose the thread, **`/compact`** is the middle ground: it replaces the long back-and-forth with a short summary, freeing room while keeping what matters. Use `/compact` to keep going on the same task; use `/clear` when you're moving on to a new one.

*Rule of thumb: one focused task per conversation. A clean context beats a cluttered one every time.*

### Memory — the notebook Claude keeps

Context is erased the moment you `/clear` or close the terminal. **Memory** is what survives — and it comes in two forms:

- **A `CLAUDE.md` file in your project.** A plain-text note you commit alongside your code, telling Claude how *this* project works — where the data lives, how to run things, conventions to follow. Every future session (yours or a collaborator's) reads the same file, which makes your project easier to pick back up and to reproduce.
- **Personal memory across sessions** — facts about you and how you like to work, remembered from one sitting to the next.

*To save something to memory, just ask — tell Claude "remember that…" and it stores the note. Use the `/memory` command to review or edit what's saved, or open `CLAUDE.md` directly. Because `CLAUDE.md` is just a file in your repo, it's version-controlled like everything else you commit.*

### Skills — standing instructions for how your group works

A **skill** is a reusable set of instructions that Claude Code pulls in whenever it's relevant — so it follows your group's way of doing things without being told each time. If *memory* is a set of facts, a *skill* is a way of working.

Skills can come from Stanford, from your lab, or ones you write yourself. This course ships one — **github-for-research** — which you'll meet just below.

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

Claude Code does **not** sort safe data from sensitive. It sends whatever you let it read — if you point it at a file full of names, those names go to the server. Nothing keeps personal, restricted, or health data local on its own. **Holding that data back is *your* job** — by not letting Claude read it in the first place.

<svg viewBox="0 0 1000 560" role="img" aria-labelledby="cc-arch-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:1000px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="cc-arch-title">How Claude Code works: on your machine you give the harness instructions and point it at your data — check before sharing. The harness acts as you (editing files, running commands, driving git, calling tools) and loops those results back to itself. It exchanges context with Claude's model on Anthropic's server, across the campus perimeter, reached via Stanford's governed route.</title>
  <defs>
    <marker id="ah-green" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2e8b57"/></marker>
    <marker id="ah-slate" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
    <marker id="ah-brown" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#b5761f"/></marker>
  </defs>

  <!-- perimeter -->
  <line x1="700" y1="40" x2="700" y2="536" stroke="#b09668" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="700" y="30" text-anchor="middle" font-size="15" font-weight="700" letter-spacing="0.5" fill="#b09668">CAMPUS PERIMETER</text>

  <!-- your machine -->
  <rect x="16" y="56" width="628" height="488" rx="18" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="40" y="94" font-size="24" font-weight="700" fill="#2c3e50">💻  Your machine · the Yens</text>
  <text x="40" y="122" font-size="16" fill="#9a8a68">You direct Claude — it reads what you allow, and acts as you.</text>

  <!-- your data panel (what it reads) -->
  <rect x="32" y="142" width="300" height="262" rx="12" fill="#ffffff" stroke="#e6cfa8" stroke-width="1.25"/>
  <text x="50" y="174" font-size="19" font-weight="700" fill="#2c3e50">Your data</text>
  <text x="50" y="202" font-size="16" font-weight="700" fill="#b5761f">⚠️  Check before sharing</text>
  <circle cx="56" cy="232" r="5" fill="#37a06a"/><text x="72" y="238" font-size="16" fill="#2c3e50">Public data (e.g. SEC filings)</text>
  <circle cx="56" cy="264" r="5" fill="#37a06a"/><text x="72" y="270" font-size="16" fill="#2c3e50">Your own code &amp; scripts</text>
  <line x1="50" y1="290" x2="314" y2="290" stroke="#eee2cf" stroke-width="1"/>
  <circle cx="56" cy="318" r="5" fill="#c0392b"/><text x="72" y="324" font-size="16" fill="#7a2018">Personal info (PII)</text>
  <circle cx="56" cy="350" r="5" fill="#c0392b"/><text x="72" y="356" font-size="16" fill="#7a2018">Data under an NDA / license</text>
  <circle cx="56" cy="382" r="5" fill="#c0392b"/><text x="72" y="388" font-size="16" fill="#7a2018">Health data (PHI)</text>

  <!-- your instructions -->
  <rect x="360" y="142" width="280" height="88" rx="12" fill="#ffffff" stroke="#e6cfa8" stroke-width="1.25"/>
  <text x="500" y="180" text-anchor="middle" font-size="20" font-weight="700" fill="#2c3e50">🗨️  Your instructions</text>
  <text x="500" y="210" text-anchor="middle" font-size="15.5" fill="#7a6a48">what you ask it · your CLAUDE.md</text>

  <!-- harness -->
  <rect x="402" y="270" width="196" height="112" rx="14" fill="#fbe9cf" stroke="#dcae6a" stroke-width="1.75"/>
  <text x="500" y="318" text-anchor="middle" font-size="22" font-weight="700" fill="#2c3e50">⚙️  Claude Code</text>
  <text x="500" y="350" text-anchor="middle" font-size="16" fill="#8a6d3b">the model harness</text>

  <!-- your inputs (green): you direct it, and it reads what you allow -->
  <line x1="500" y1="230" x2="500" y2="266" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#ah-green)"/>
  <text x="512" y="254" text-anchor="start" font-size="15" font-weight="700" fill="#1f6b45">you direct it</text>

  <line x1="332" y1="326" x2="398" y2="326" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#ah-green)"/>
  <text x="365" y="316" text-anchor="middle" font-size="15" font-weight="700" fill="#1f6b45">reads</text>

  <!-- local acting loop (brown): acts on your machine, results return -->
  <line x1="478" y1="382" x2="478" y2="416" stroke="#b5761f" stroke-width="2.5" marker-end="url(#ah-brown)"/>
  <text x="468" y="404" text-anchor="end" font-size="15" font-weight="700" fill="#95611a">acts as you</text>
  <line x1="522" y1="416" x2="522" y2="384" stroke="#b5761f" stroke-width="2.5" marker-end="url(#ah-brown)"/>
  <text x="532" y="404" text-anchor="start" font-size="15" font-weight="700" fill="#95611a">results</text>

  <rect x="360" y="418" width="280" height="110" rx="12" fill="#fdf0d8" stroke="#e0c48a" stroke-width="1.25"/>
  <text x="500" y="450" text-anchor="middle" font-size="16.5" font-weight="700" fill="#8a5a12">On your machine, as you:</text>
  <text x="500" y="480" text-anchor="middle" font-size="15.5" fill="#6a5326">edit files · run commands</text>
  <text x="500" y="504" text-anchor="middle" font-size="15.5" fill="#6a5326">drive git · call tools</text>

  <!-- model -->
  <rect x="772" y="250" width="212" height="150" rx="16" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="878" y="298" text-anchor="middle" font-size="21" font-weight="700" fill="#2c3e50">🧠  Claude's model</text>
  <text x="878" y="330" text-anchor="middle" font-size="17" fill="#6a7280">Anthropic's server</text>
  <text x="878" y="362" text-anchor="middle" font-size="15" fill="#8a94a6">reached via Stanford's</text>
  <text x="878" y="382" text-anchor="middle" font-size="15" fill="#8a94a6">governed route</text>

  <!-- remote model loop (slate): harness sends context; model replies -->
  <line x1="600" y1="308" x2="768" y2="308" stroke="#556a95" stroke-width="2.5" marker-end="url(#ah-slate)"/>
  <text x="684" y="298" text-anchor="middle" font-size="15.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">① sends context</text>
  <line x1="768" y1="342" x2="602" y2="342" stroke="#556a95" stroke-width="2.5" marker-end="url(#ah-slate)"/>
  <text x="684" y="362" text-anchor="middle" font-size="15.5" font-weight="700" fill="#3f4f74" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">② its next step</text>
  <text x="684" y="382" text-anchor="middle" font-size="14" fill="#8a94a6" stroke="#ffffff" stroke-width="5" paint-order="stroke" stroke-linejoin="round">loops until done</text>
</svg>

The harness is the local actor — it reads and runs whatever you point it at and runs the loop; the model only ever sees what the harness sends across the perimeter to Anthropic's server. **Deciding what Claude Code may read is your responsibility.** Public data and your own code are fine; personal (PII), NDA/licensed, or health (PHI) data must not be sent — and the tool won't hold them back for you. What's approved depends on the data and the tool: see [Responsible AI at Stanford](https://uit.stanford.edu/security/responsibleai) for which AI tools are cleared for which data-risk levels, and the [GSB Library's eResources usage policy](https://www.gsb.stanford.edu/library/research-resources/usage-policy) for whether a licensed dataset may be used this way. We map out these data categories in full on Day 2.

{: .note }
> Full details and the request links live at [uit.stanford.edu/service/claude](https://uit.stanford.edu/service/claude). Your instructor can point you to the exact sign-up link in class.

---

## Claude Code acts as you

When Claude Code runs a command, edits a file, or pushes to GitHub, it does so with **your** credentials and **your** permissions. To the Yens, to GitHub, to anything it touches, the action looks exactly like *you* did it — there is no way for those systems to tell you apart from Claude acting on your behalf.

That has a blunt consequence: **Claude Code can do anything you can do.** It can read, change, or delete any file you can, run any command you could run, and reach any system your account can reach. You can *ask* it to steer clear of something — "don't touch the `data/` folder," "never force-push" — and it will try, but that's a request, not a boundary the system enforces. Nothing outside your own judgment stops it.

{: .warning }
> Treat it like handing your keyboard to a fast, capable assistant. Use **plan mode** when you want to see the plan before anything happens, review actions that are hard to undo (deleting files, force-pushing, sending data off your machine), and don't point it at anything you wouldn't do yourself.

---

## Take It for a Spin

{: .important }
> **Do this now.** On the Yens, load Claude Code, sign in through Stanford, and give it a first real task. This is the one Claude Code step everyone should complete.

You've been working on the Yens all along — Claude Code runs there too. Connect the way you did in [Connecting to a Cluster](../ssh-gate/) if you're not already on:

```bash
ssh SUNetID@yen.stanford.edu
```

**1 — Load Claude Code.** It's available as a module on the Yens, just like `gh` and `python`:

```bash
module load claude
```

{: .note }
> If `module load claude` can't find the module, ask an instructor for the exact name — the module list changes over time.

**2 — Make a working folder and launch it from there.** Create a `cctest` directory in your home directory, move into it, and start Claude Code:

```bash
mkdir -p ~/cctest
cd ~/cctest
claude
```

**3 — Sign in** with your **SUNet ID** the first time (see *Claude at Stanford* above).

**4 — Learn two controls.** Try each once:

- Type `/cost` — see how many tokens this session has used (the *Tokens* box explains why this matters).
- Press `Shift+Tab` — flip between plan mode and auto mode (see *Plan mode vs. auto mode* above).

**5 — Give it a real task.** No need to download anything yourself — just point Claude at the grimoire on GitHub and say what you want:

```
> Download and unzip the grimoire from https://raw.githubusercontent.com/gsbdarc/rf-bootcamp-2026/main/docs/assets/data/grimoire.zip and tell me, for each element, the longest spell name(s).
```

Claude fetches the archive, unzips it, reads the filenames, and reports one spell per element. Notice what you *didn't* do: no `curl`, no `unzip`, no wildcards or pipes — you said what you wanted, and it worked out how. That's the shift Claude Code represents.

{: .note }
> Stuck on loading or sign-in? Raise your hand — we'll get you going, and you won't fall behind.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d1-familiars-den" data-key="main"> Took Claude Code for a spin</label>

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

## Optional Practice — Put Claude Code to Work

{: .important }
> **Optional practice:** Have Claude Code make a real change to your course site — switch it to **dark mode** — and open a pull request. A bonus walks the same change the way a pro would: inspect, plan, then act.

Optional — the Day 1 Challenge only needs the exercise from Version Control with Git. This is extra practice.

### Make a real change: dark mode

<details markdown="1">
<summary>Show steps</summary>

Now let Claude Code do real work on your own site. Launch `claude` inside `rf-bootcamp-2026` and give it a concrete, checkable task — switch the site to dark mode and drive the whole git loop for you:

```
> Switch this site's theme to dark mode, commit it on a new branch, and open a pull request.
```

Then confirm it worked: on your fork on GitHub, a new **branch** and a **pull request** should have appeared with the theme change.

{: .note }
> Look at what it did: the work went on a **branch**, opened as a **pull request**, and the commit **credits Claude** — the good habits happened automatically, because of the github-for-research skill.

</details>

### Bonus — Do it like a pro (plan mode + issues)

<details markdown="1">
<summary>Show steps</summary>

The task above did the job in one line. Here's how you'd handle a real change more carefully — look before you leap, and review a plan before any file changes. (Do this on a fresh branch, or instead of the one-liner above.)

1. **Inspect the repo.** In `claude`, ask how the site is themed:
   ```
   > How is this site's theme and colours set up, and which files control them?
   ```
2. **Review what's open.** Have Claude survey the project's issue tracker:
   ```
   > Summarise the open issues in this project.
   ```
3. **Plan before acting.** Press `Shift+Tab` to enter **plan mode**, then ask:
   ```
   > Propose a plan to move the whole site to dark mode — colours, code blocks, and the diagrams.
   ```
   Claude investigates and shows a plan **without changing anything**. Read it; refine it if you want.
4. **Approve, implement, and open a PR.** Accept the plan (it switches to auto mode), let it make the changes, and have it open a pull request.

{: .tip }
> This is the everyday Claude Code loop for anything non-trivial: **look → plan → approve → act.** Plan mode is your safety net — you see exactly what it intends before a single file changes.

</details>

### Also try — Ask a real research repo questions

<details markdown="1">
<summary>Show steps</summary>

A well-kept repository is one you can *ask questions*. We'll use a real Stanford project — an analysis of whether San Francisco's graffiti 311 reports fell during COVID.

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

<label class="quest-check"><input type="checkbox" data-room="d1-familiars-den" data-key="side1"> Optional practice complete</label>

---

## What You Learned

- How Claude Code works — model vs. harness, models, modes, tokens, context, memory, skills, terminal vs. app
- What a token is, and why context and cost are both measured in tokens
- What leaves your machine on an AI call — and why sensitive data can't go to an external LLM
- How to get Claude through Stanford's managed service
- Install Claude Code and run your first task on real data — in plain English, no commands to memorize
- Have Claude Code make a real change (dark mode) and open a pull request — using plan mode to review before it acts
- Interrogate a real research repo with Claude Code
