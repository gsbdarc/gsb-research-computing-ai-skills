# `yen-slurm` Skill — Reference Key

**Instructor use only.** A model `SKILL.md` for the Day 3 "Writing a SLURM Job with Claude" main quest. Students author their own at `~/.claude/skills/yen-slurm/SKILL.md` (global scope) — show this *after* they've attempted it. There's no single right answer; look for the conventions below being captured clearly enough that Claude would reproduce the hand-written script's shape.

A complete example `~/.claude/skills/yen-slurm/SKILL.md`:

```markdown
---
name: yen-slurm
description: How to write SLURM batch scripts for Stanford's Yen cluster — partitions, resource requests, logging, email, and environment setup. Use whenever creating or editing a .slurm file for the Yens.
---

# Writing SLURM jobs on the Yens

SLURM starts a **fresh shell** on the compute node — no venv, no working directory.
Put every setup step in the script.

## Environment
- `cd $HOME/gsb-research-computing-ai-skills`
- `source .venv/bin/activate`
- `mkdir -p logs` before submitting

## #SBATCH directives (always include)
- `--job-name=<short-name>`
- `--output=logs/<name>_%j.out`
- `--error=logs/<name>_%j.err`   (%j = job ID, so runs don't overwrite each other)
- `--time=<HH:MM:SS>`, `--mem=<RAM>`, `--cpus-per-task=<cores>`
- `--mail-type=ALL`
- `--mail-user=<SUNetID>@stanford.edu`

## Resources
Take `--time` / `--mem` / `--cpus-per-task` from the Profiling README — measure first,
don't guess. Our extraction is API-bound and single-core, so RAM and cores stay flat;
wall-clock scales with the number of filings.

## Partitions
- `normal` — production runs (default choice here).
- `dev` — short debugging jobs only (tighter time limit, faster turnaround).
- Check current limits/QoS before requesting:
  https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits
  and `sacctmgr show qos <partition>`. Pick the partition that minimizes queue time.
```

What to look for in a student's skill:
- **Front matter** — a `name` and a *specific* `description` (the description is what makes Claude auto-load it).
- **Email** and **`%j` log naming** captured as always-on conventions.
- **Env setup** (`cd` + `source .venv/bin/activate`) and the fresh-shell reasoning.
- **Resources from profiling**, not guessed.
- **Partition** guidance (`normal` vs `dev`) with the RCpedia/QoS check.

Then they should confirm Claude loads it (`> do you have the yen-slurm skill?`), use it to draft `slurm/extract_form_3_batch_claude.slurm`, and compare against their hand-written `slurm/extract_form_3_batch.slurm`.
