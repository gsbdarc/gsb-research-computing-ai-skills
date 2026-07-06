---
name: github-for-research
description: Best practices for using GitHub on academic and research projects with Claude — clear attribution, issues for problems, branches for experiments and fixes, careful data checking, reproducible environments, and a history that both people and Claude can read later.
---

# GitHub for Research

This skill helps researchers keep a project on GitHub in good shape — with Claude doing most of the hands-on work. It is written for people who do **not** have a software background. You do not need to memorize commands; you can simply ask Claude to do these things, and Claude will follow the practices below.

## When to Use This Skill

Use this skill whenever you are:
- Working inside a research project that is stored on GitHub (or setting one up).
- Running a study, cleaning or processing data, or trying out research ideas.
- Asking Claude to make a change, save your work, or fix something.
- Asking "what happened in this project?" or "what did we already try?"
- Asking about keeping your work reproducible, well-documented, or properly credited.

## The Core Idea

**Treat the project like a shared lab notebook.** Everything you and Claude do should leave a clear, honest trail that a person *or* Claude can read back later and understand: what you did, why you did it, what went wrong, and what you decided.

Two ideas follow from this:
- **The history is part of the research output**, not just a backup. Months from now you (or Claude) should be able to reconstruct the whole story from the project.
- **Claude is your main way of working with GitHub.** You describe what you want in plain words; Claude does the mechanical steps and follows the conventions here so the trail stays clean.

A few plain-language terms you will see below (a fuller list is in the glossary at the end):
- **Repository ("repo")** — the folder that holds your whole project and its history.
- **Commit** — a saved snapshot of your work with a short note explaining it. Like a dated lab-notebook entry.
- **Branch** — a private copy of the project where you can try something without disturbing the working version.
- **Issue** — a logged note describing a problem, question, or task, kept on GitHub.
- **Pull request ("PR")** — a proposal to fold a branch's changes back into the main project, with a description and a chance to review first.

## Always-Do Checklist (the essentials)

These are the habits that matter most. Ask Claude to follow them every time.

1. **Credit Claude on everything it helps with.** Every saved snapshot Claude makes ends with a line crediting it, and every proposal it writes says it was made with Claude (details below). Anyone reading the project can see exactly what was human-written and what was AI-assisted.
2. **Do new work on a branch, not the main copy.** Trying an idea? Fixing a problem? Ask Claude to make a branch for it. The main version stays clean and working.
3. **Log problems as issues.** When something breaks, looks wrong, or raises a question — even if you fix it right away — record it as an issue so the problem is visible, not just the fix.
4. **Say *why*, not just *what*.** When Claude saves work or proposes a change, the note should explain the reasoning ("switched to the 2019 sample because the 2020 file was missing three sites"), not only the mechanical change.
5. **Keep the environment reproducible.** Save the list of exact software versions your project uses (the "lockfile") so the analysis can be re-run later and get the same result.
6. **Never quietly change raw data, and always check processed data.** Raw data stays untouched; any step that transforms data gets validation checks. If checks are missing, Claude will ask for them before continuing (see next section).

## Accuracy and Data Integrity (non-negotiable)

Research has to be **correct**. The project should be set up so that checking your work is unavoidable, especially with data.

**Keep raw data clean and untouchable.**
- Original data lives in a folder like `data/raw/` and is never edited in place — treat it as read-only, the way you would never write over the original readings in a lab notebook.
- Anything you compute from it goes into a *separate* place, like `data/processed/`. The raw file is never overwritten.
- If raw data changes (a new export, a correction), that is a new file with a clear name and date — the old one is kept.

**Check every data transformation.**
Whenever data is cleaned, merged, filtered, or recomputed, there should be explicit checks saved next to the code that does it. Useful checks include:
- Row counts before and after (did you lose or duplicate rows you didn't mean to?).
- Column types and names are what you expect.
- Values fall in sensible ranges (no ages of 300, no negative counts).
- Missing values and duplicates are counted and handled on purpose.
- Identifiers that should be unique actually are.
- Totals reconcile before and after the step.

**Claude must prompt for checks when they are missing.**
If you ask Claude to process data but don't mention how to verify the result, Claude will **not** just do it silently. It will pause, point out that the step has no validation, and suggest specific checks for *that* transformation in plain language — for example: "Before I merge these two files on participant ID, I'd like to confirm every ID matches and no rows are duplicated. Shall I add those checks?" You can approve, adjust, or explain why a check isn't needed.

**Make the checking visible.** Validation code is saved in the project (not run once and forgotten), it's mentioned in the note for the change that added it, and if a check ever fails, that gets logged as an issue so the problem is on the record.

## Crediting Claude

So that it is always clear who did what:
- **Saved snapshots (commits)** that Claude makes end with a credit line:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
- **Change proposals (pull requests)** that Claude writes include a short note in the description: "🤖 Generated with Claude Code."
- Optionally, proposals and issues that Claude worked on can carry a label such as `claude-assisted`, so you can filter for them on GitHub.

You don't have to do any of this by hand — Claude adds these automatically. The point is transparency: a reviewer, a co-author, or a journal can see the AI's involvement at a glance.

## Issues: Recording Problems

An **issue** is a note on GitHub describing a problem, question, or task. Think of it as flagging something in the margin of your lab notebook.

**Open an issue when:**
- Something breaks or produces a wrong-looking result.
- You hit a dead end or a question you can't resolve yet.
- You notice something to fix or investigate later.

Ask Claude to "open an issue for this," and describe it in plain words. Claude writes it up clearly and can add a label:
- `bug` — something is broken or wrong.
- `data` — a problem with the data itself.
- `experiment` — an idea to try.
- `question` — something to figure out.
- `decision` — a choice that needs to be made or recorded.

**Close issues through a change, not silently.** When the problem is resolved, the proposal that fixes it should reference the issue (Claude writes `Closes #12` in the description) so the problem and its resolution are linked forever. That link is what lets you — or Claude — later trace "this issue → this fix → this reasoning."

## Branches: Experiments and Fixes

A **branch** is a private copy of the project where you can work without touching the main version. Two main uses:

- **Trying a research idea** — ask for an experiment branch (Claude names it something like `experiment/logit-instead-of-ols`). You can explore freely; if it doesn't work, the main version was never affected.
- **Fixing a logged problem** — ask for a fix branch tied to the issue (like `fix/12-missing-sites`). When merged, it closes the issue.

Keep the **main version always working and reproducible** — someone who opens it should be able to run the analysis.

**Preserve failed experiments — don't erase them.** In research, something that *didn't* work is a real finding. If an experiment branch doesn't pan out, don't just delete it. Ask Claude to record what happened and why (in the closing issue note or a short summary), and keep or tag the branch. Later, when you ask Claude "did we already try X?", it can tell you that you did, and what went wrong — saving you from repeating it.

## Reproducible Environments

So the analysis can be re-run and trusted later:
- **Save exact software versions.** Ask Claude to create and commit the "lockfile" for your tools — for example `environment.yml` (conda), `uv.lock` or `requirements.txt` (Python), or `renv.lock` (R). This records the precise versions so a re-run behaves the same.
- **Record randomness.** If your analysis uses any random step, fix and record the random seed so results are repeatable.
- **Mark milestones.** At meaningful points (e.g. a paper submission or a revision), ask Claude to tag a release — a permanent, named bookmark like `submission` or `revision-1` you can always return to.
- **Keep large or sensitive data out of the project, and say where it lives.** GitHub is for code and small files. Big datasets, or anything sensitive or restricted (e.g. human-subjects data), should live in approved storage; note in the project where it is and how to get access, rather than committing it.

## Asking Claude "What Happened Here?"

Because everything above leaves a clean trail, you can later ask Claude to reconstruct the story of the project, and it will look through:
- the issues (what problems came up),
- the proposals/pull requests (what changes were made and why),
- the saved snapshots and their notes (the step-by-step history),
- and the links between them (`Closes #12`) to connect a problem to its fix.

Good habits now — clear notes, logged issues, explained decisions — are what make this work well later. You might ask: "What did we try for the missing-sites problem?" or "Summarize every data-cleaning decision we made," and get a faithful answer drawn from the project's own record.

## Leveling Up (optional, when a project matures)

Once the basics are second nature, ask Claude about these:
- **A citable snapshot (DOI).** Connect the project to Zenodo so a tagged release gets a permanent DOI you can cite in a paper.
- **A citation file.** Add a `CITATION.cff` so others know exactly how to cite your work.
- **Protecting the main version.** Turn on branch protection so changes to main must go through a reviewed proposal.
- **Templates.** Add issue and pull-request templates so every problem and change is described consistently.
- **Large-file handling.** Use Git LFS for large binary files that genuinely need to live with the project.

## Plain-Language Glossary

- **Repository (repo)** — the folder holding your whole project and its full history.
- **Commit** — a saved snapshot of your work with a short note; like a dated lab-notebook entry.
- **Branch** — a private copy of the project for trying or fixing something without disturbing the working version.
- **Issue** — a logged note on GitHub describing a problem, question, or task.
- **Pull request (PR)** — a proposal to merge a branch's changes into the main project, with a description and a review step.
- **Tag / release** — a permanent, named bookmark of the project at a moment in time (e.g. a submission).
- **Lockfile** — a saved list of the exact software versions your project uses, so it can be re-run identically.
- **Merge** — folding one branch's changes into another (usually into the main version).

## Quick Reference

- New idea or fix → **branch** (`experiment/…` or `fix/…`).
- Something wrong or unresolved → **issue** (with a label).
- Every save → **note the *why*** and **credit Claude**.
- Fixing a problem → **link the issue** (`Closes #…`) in the proposal.
- Raw data → **never edited**; processed data → **always validated** (Claude asks if checks are missing).
- Every project → **commit the lockfile**; milestones → **tag a release**.
- Failed experiment → **record why and keep it**, don't delete.
- Big or sensitive data → **keep out of GitHub**, note where it lives.

## Installing This Skill System-Wide

When this skill lives inside a project at `.claude/skills/github-for-research/`, it is active automatically whenever you work inside that project. To use it in **any** project on your computer, copy or link it into your personal skills folder:

```
# copy it (replace the source path with wherever this skill lives)
cp -R /path/to/project/.claude/skills/github-for-research ~/.claude/skills/

# or link it, so it stays up to date with the original copy
ln -s /path/to/project/.claude/skills/github-for-research ~/.claude/skills/github-for-research
```

After that, Claude can use these practices in every project you work on.
