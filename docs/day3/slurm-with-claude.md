---
layout: default
title: "Writing a Slurm Job with Claude"
parent: "Day 3 — Cluster Computing"
nav_order: 8
permalink: /day3/slurm-with-claude/
---

# Writing a Slurm Job with Claude

<div data-room-id="d3-slurm-with-claude"></div>

---

You just wrote a Slurm script **by hand**, submitted it, and got it working. That working setup is the raw material for a **skill** — a set of standing instructions Claude Code pulls in automatically so it follows your conventions without you re-explaining them every time.

The best skills come from work you've already gotten right. The pattern is always the same three steps:

1. **Work with Claude** on a real task until you're happy with the result.
2. **Ask Claude to make a skill** from what you just accomplished.
3. **Invoke the skill** on the next, similar task — and watch it follow your conventions.

You'll do this twice, for the two kinds of knowledge that go into your work:

- **How the Yens work** — partitions, resource requests, `%j` log naming, email. True for *every* job you run on the cluster, so it belongs in a **global** skill. You'll distill it from the job you *just* ran.
- **How this project does things** — its figure house style, where results go, which script does what. Specific to *this* pipeline, so it belongs in a **project** skill. You'll distill it from a figure you make.

You'll always **review what Claude writes** — you're the one who submits and checks the work.

## Two homes for a skill

On Day 1 you *installed* a skill (`github-for-research`). Every skill is its own **directory** holding a single file named exactly `SKILL.md` (uppercase). The directory name is the skill's name — **lowercase letters, digits, and hyphens only** (no spaces, no underscores), up to 64 characters — and it's also how you invoke the skill: a folder `form3-plots/` gives you the `/form3-plots` slash command.

Where that directory lives decides the skill's **scope**:

- **Global skill** → `~/.claude/skills/<skill-name>/SKILL.md` — in your **home** directory (`~/.claude/`), so it loads in *every* project you work on. That's where the Day 1 skill lives. Best for **conventions that follow you** across projects (like how the Yens work).
- **Project skill** → `<your-repo>/.claude/skills/<skill-name>/SKILL.md` — in the **repo's own** `.claude/` (no `~/`), so it loads only in *this* repo and, once committed, ships to anyone who clones it. Best for **repo-specific** conventions (how this project makes figures, where results land, which script to run).

You'll make one of each.

## Main quest — Write Two Skills for Claude

{: .important }
> **Task:** Have Claude write two skills — a **global** Yen skill and a **project** plotting skill — then invoke each on a new task.

You'll do this from Claude Code running on the Yens. Load the module and launch it inside your repo:

```bash
ml claude-code
cd ~/gsb-research-computing-ai-skills
claude
```

### 1. A global skill — distilled from the job you just ran

You already got a batch Slurm script working by hand. Rather than describe the Yen conventions from scratch, point Claude at that script and have it **capture the reusable parts** (step 2 of the pattern):

> Read `slurm/extract_form_3_batch.slurm` and turn its reusable **Yen conventions** into a **global** skill at `~/.claude/skills/yen-slurm/SKILL.md`: partition choice, email, `%j` log naming, always setting `--time`/`--mem`/`--cpus-per-task`, and checking current limits on [RCpedia](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits). Keep it short and **repo-agnostic** — no project paths.

**Check what it wrote.** A good skill is short, and its **`description`** is what makes Claude reach for it later — so open the file and read it:

```bash
cat ~/.claude/skills/yen-slurm/SKILL.md
```

It should look something like this — a little frontmatter, then a few bullet conventions:

```markdown
# ~/.claude/skills/yen-slurm/SKILL.md
---
name: yen-slurm
description: Write and check Slurm batch scripts for Stanford's Yen cluster — partitions, email, %j logs, resource requests. Use when writing a .slurm job.
---

When writing a Yen job script:
- Choose a partition: `normal` for production, `dev` for short jobs (limits on RCpedia)
- Always set `--time`, `--mem`, and `--cpus-per-task`
- Email on completion: `--mail-type=ALL`, `--mail-user=SUNetID@stanford.edu`
- Name logs `logs/<job-name>_%j.out` and `.err`
```

The **`description` is the trigger** — Claude reads it to decide when to pull the skill in. Leave it vague ("slurm stuff") and it won't fire when you need it; say what it does *and when to use it*.

Then invoke it (step 3) on a fresh job. Claude Code turns each skill's folder name into a `/`-command, so the `yen-slurm/` folder gives you `/yen-slurm` — type it and add your request:

> /yen-slurm write a Slurm job for a new run and save it as `slurm/extract_form_3_batch_claude.slurm`

**Submit and review:** the conventions should come straight from the skill, matching what you hand-wrote. But the global skill is repo-agnostic — it says nothing about *how this project plots a figure*. That's a **project** specific: the next skill.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-with-claude" data-key="global"> I distilled a global Yen skill from the job I ran, checked its `SKILL.md`, and invoked it on a fresh job</label>

### 2. A project skill — your figure house style

Skills shine when Claude follows *your* world's conventions instead of generic defaults — a house style so every figure comes out consistent.

**Step 1 — work with Claude until the figure looks right.** Ask it to make and run a small plotting job:

> Write `scripts/plot_letter_distribution.py` that reads every JSON in `results/` and counts how often each letter a–z appears across all the extracted text fields (`insider_name`, `company_name`, and the roles). Save a bar chart to a new `figures/` directory (`figures/letter_distribution.png`), creating the directory if it doesn't exist. Use our Stanford palette: cardinal-red (`#8C1515`) bars, Stanford-black (`#2E2D29`) title and axis labels, white background. Then write `slurm/plot.slurm` to run it on the `dev` partition, and submit it.

Iterate with Claude on colours, title, and axis labels until you like it. (Open `figures/letter_distribution.png` in JupyterHub to see it.)

{: .note }
> 💡 **Example prompts to iterate with Claude** — you don't need to know matplotlib, just describe the look:
> - Make every other bar a lighter cardinal shade (`#B83A4B`) so adjacent bars are easy to tell apart.
> - Add a title "Letter frequency across 10 Form 3 filings" and label the axes ("Letter" on x, "Count" on y).
> - Sort the bars from most to least frequent instead of alphabetical.
> - Bump the figure size and dpi so it's readable in a slide, and add light gridlines.

**Step 2 — distill the style into a skill.** This one is a **project** skill, so it goes in **this repo's own `.claude/`** — *not* your home `~/.claude/` — so it ships with the project to anyone who clones it. Once you're happy with how the figure looks:

> Turn the plotting style we just settled on into a **project** skill in **this repo** at `./.claude/skills/form3-plots/SKILL.md` (the repo's `.claude/`, not `~/.claude/`) — this repo's figure house style: the Stanford palette (cardinal `#8C1515` bars, `#2E2D29` text), figure size, dpi, axis-label conventions, and that PNGs save to `figures/`. Keep it to *this* project.

**Step 3 — invoke it on a *different* plot** to prove it fires. Either just describe the task and let the skill's `description` trigger it automatically, or call it explicitly with `/form3-plots` — no style instructions either way:

> /form3-plots plot the distribution of insider roles across the 10 filings

It should come out in the same house style automatically — that's the skill doing its job.

**Takeaway:** the global skill knows *how the Yens work* — it lives in your home `~/.claude/`, so it follows *you* to every project. The project skill knows *how this project does things* — it lives in the repo's own `.claude/` (no `~/`), so committing it ships the skill to anyone who clones. Both come from work you already did right — you just asked Claude to remember it.

{: .warning }
> **You're still the reviewer.** A skill makes Claude follow your conventions, but Claude can still invent partition names, time limits, or QoS caps that don't exist. Check its choices against RCpedia — the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits) page and `sacctmgr show qos <partition>` — and against your own profiling. The script you submit is yours.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-with-claude" data-key="project"> I made a figure with Claude, distilled its house style into a project plotting skill, invoked it on a different plot, and can explain project vs. global scope</label>

---

## Side quests

{: .note }
> Finished early? Try this one.

**Side quest — Claude in one shot (`claude -p`)**

Everything above used Claude Code **interactively**. For a quick, one-off question — or to script it — Claude also runs **non-interactively**: `claude -p "…"` (print mode) runs a single prompt, prints the answer, and exits. No session, no back-and-forth.

Point it at a file — e.g. review one of the broken scripts from the [**Debug** side quests](../slurm-job/#side-quests):

```bash
claude -p "review scripts/extract_form_3_one_file_broken.py and explain what it does"
```

Or **pipe** data straight into it. On Linux, every command-line program has two text streams: **standard input** (`stdin`, the text coming *in*) and **standard output** (`stdout`, the text it prints *out*). The pipe symbol `|` connects them — it takes the `stdout` of the command on its left and feeds it as the `stdin` of the command on its right. Because `claude -p` reads from `stdin`, you can pipe a file's contents straight into Claude instead of typing them. Take a failed job's error log from the [**Debug** side quests](../slurm-job/#side-quests) (run those first, so the `logs/fix_me_*.err` files exist) and let Claude diagnose it in one line:

```bash
cat logs/fix_me_*.err | claude -p "this Slurm job failed — explain the error and suggest a fix"
```

Because it's just another command that reads `stdin` and prints to `stdout`, you can even drop `claude -p` **inside a Slurm job or a shell script** — have a batch job summarize its own results, flag anomalies, or write a note to your log, all without you watching it run.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-with-claude" data-key="side1"> I used `claude -p` to review a script, and piped a failed job's log to Claude for a one-shot diagnosis</label>
