---
title: "Day 4 — TODOs (internal)"
nav_exclude: true
search_exclude: true
---

# Day 4 — Content TODOs

**Internal planning note — not a course page.** Tracks the remaining known gaps in
the Day 4 material. Excluded from site nav and search via front matter.

The Day 4 rewrite (de-fantasized pages, new content, leaderboard/quest wiring) is
complete; the sequencing plan, `extract_form_3_cli.py`, fault-tolerance/skip-if-exists,
the "why a GPU" and local-vs-cloud motivation, the interactive GPU session, and the
Day 3-style leaderboard sync are all done. What's left:

---

## Open items

### Side quests & per-section checkpoints
Day 3 pairs 3–6 `quest-check` checkboxes per page (registered as `side1…sideN` keys
per room in `assets/js/quest-log.js`) and offers optional side quests. Day 4's pages
mostly have a single checkbox each — `running-llms.md` is the exception
(`main` / `exercise` / `side1`). To match Day 3's granularity:

- Write optional side quests — candidates: the *chunking* pattern (50 tasks /
  100 filings) as a hands-on side quest; deliberately fail a task and re-run to see
  the skip-if-exists resilience in action; a further GPU side quest.
- Add per-Part checkpoints (e.g. a checkbox after each Part of the array exercise).
- Register any new keys under the relevant `d4-*` rooms in `quest-log.js`, and attach
  the "🔄 Keep the leaderboard live" sync prompt to each new checkpoint.
  (`TOTAL_CHECKS` is now derived from the registry, so new keys are counted
  automatically — but keep `leaderboard.md`'s `TOTAL` in sync.)

### Introduce prerequisites used but never taught
- **Passing command-line arguments** — `extract_form_3_cli.py` reads `sys.argv`, but
  passing arguments to a script is never introduced in Days 1–3. Add a short aside
  before first use (in `slurm-arrays.md`, where the CLI script appears).
- **Keyword arguments** (`name=value`) — used since Day 2 (OpenAI client, pandas)
  but never named. Consider a one-line aside in `day2/oracles-chamber.md` at first use.

### Finish the cross-page link audit
Confirmed OK: all Day 3 child links resolve; referenced images/assets exist.
Not yet verified: whether *every* internal page link resolves — cross-day links still
to check include `day2/human-vs-llm`, `scroll-transfer`, `cartographers-room`, and
`claude-code`.

---

*Drafted by Claude (Opus 4.8) from a Day 4 content audit, then pruned to open items only. Verify each item before acting.*
