---
layout: default
title: "Writing a SLURM Job with Claude"
parent: "Day 3 — Cluster Computing"
nav_order: 8
permalink: /day3/slurm-with-claude/
---

# Writing a SLURM Job with Claude

<div data-room-id="d3-slurm-with-claude"></div>

---

You just wrote a SLURM script **by hand** — the `#SBATCH` block, the log naming, the email lines, `cd` into the repo, `source .venv/bin/activate`, resources from your profiling. Those conventions are the *same on every job you'll ever submit to the Yens*. Re-typing them into Claude every time would be tedious and error-prone.

So instead of explaining them again and again, you'll **teach Claude once** — with a **skill**.

## Where skills live

On Day 1 you *installed* a skill (`github-for-research`). A **skill** is a reusable set of instructions Claude Code pulls in whenever it's relevant, so it follows a way of working without being told each time. Now you'll *write* one. Skills live in one of two places:

- **Global (personal)** — `~/.claude/skills/<name>/SKILL.md`. Loads in **every** project you work on — that's where the Day 1 `github-for-research` skill lives. Best for conventions that follow *you*.
- **Project** — `<your-repo>/.claude/skills/<name>/SKILL.md`. Committed to the repo and shared with anyone who clones it. Best for conventions that belong to *one specific project*.

Your Yen SLURM conventions apply to **all** your Yen work — every batch job, every project — so you'll make `yen-slurm` a **global** skill.

## Main quest — write the `yen-slurm` skill

Create the file `~/.claude/skills/yen-slurm/SKILL.md`. A skill is just Markdown with a little YAML front matter: a `name` and a `description`. The **description is how Claude decides when to load the skill**, so make it specific.

Here's the skeleton — fill in the body with *your* conventions (write it yourself, or have Claude draft it and then read every line):

```markdown
---
name: yen-slurm
description: How to write SLURM batch scripts for Stanford's Yen cluster — partitions, resource requests, logging, email, and environment setup. Use whenever creating or editing a .slurm file for the Yens.
---

# Writing SLURM jobs on the Yens

## Environment (SLURM starts a fresh shell — set everything up in the script)
- `cd $HOME/gsb-research-computing-ai-skills`
- `source .venv/bin/activate`

## #SBATCH directives (always include these)
- `--job-name`, `--output=logs/<name>_%j.out`, `--error=logs/<name>_%j.err`
- `--time`, `--mem`, `--cpus-per-task`
- Email me: `--mail-type=ALL` and `--mail-user=<SUNetID>@stanford.edu`
- `mkdir -p logs` before submitting, so the log paths exist

## Resources
- Take `--time` / `--mem` / `--cpus-per-task` from the Profiling README — measure first, don't guess.

## Partitions
- `normal` for production runs; `dev` only for short debug jobs (tighter time limit, faster turnaround).
- Check current limits/QoS before requesting: https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits and `sacctmgr show qos <partition>`. Pick the partition that minimizes time in the queue.
```

Fill in every convention you used in the hand-written script — the goal is that Claude, reading this skill, would write the *same* kind of script you did.

{: .note }
> Check Claude picked it up — ask it `> do you have the yen-slurm skill?` (just like you did for the Day 1 skill). If not, make sure the file is at `~/.claude/skills/yen-slurm/SKILL.md`.

## Now let Claude use it

With the skill in place, the prompt gets *short* — you don't repeat the conventions, because the skill carries them:

> Write a SLURM batch script for `scripts/extract_form_3_batch.py` (it processes `NUM_FILINGS` = 10 SEC Form 3 filings from `data/aws_links.csv` into `results/`). Save it as `slurm/extract_form_3_batch_claude.slurm`.

Notice how little you had to say. Everything about email, logging, the venv, partitions, and resources came from the skill — that's the point.

## Compare with your hand-written script

Open Claude's `slurm/extract_form_3_batch_claude.slurm` next to the `slurm/extract_form_3_batch.slurm` you wrote by hand — same job, two scripts — and check whether the **skill** made Claude follow your conventions:

- **Email** — did it add `--mail-type=ALL` / `--mail-user`?
- **Logs** — `logs/<name>_%j.out` and `.err`, with `mkdir -p logs`?
- **Environment** — `cd` into the repo and `source .venv/bin/activate`?
- **Partition** — `normal` (not `dev`) for this real run?
- **Resources** — `--time` / `--mem` / `--cpus-per-task` that match your Profiling README (10 filings ≈ 10× the wall-clock of one, but still API-bound and single-core)?

Anything it missed is a gap in your skill — tighten the wording and try again. That loop *is* the skill-writing skill.

{: .warning }
> **You're still the reviewer.** A skill makes Claude follow your conventions, but Claude can still invent partition names, time limits, or QoS caps that don't exist. Check its numbers against RCpedia — the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits) page and `sacctmgr show qos <partition>` — and your own profiling. The final script is yours.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d3-slurm-with-claude" data-key="main"> I wrote a global `yen-slurm` skill capturing our Yen SLURM conventions, used it to have Claude draft the batch SLURM, and compared it to my hand-written one — and I can explain global vs. project skills</label>
