---
title: "Day 4 — TODOs (internal)"
nav_exclude: true
search_exclude: true
---

# Day 4 — Content TODOs

**Internal planning note — not a course page.** Tracks known gaps in the Day 4
material. Excluded from site nav and search via front matter.

---

## Agreed Day 4 sequencing plan

Revised lecture flow for Day 4 (from instructor whiteboard, 2026-07-15). This is
the target order; the room files and `index.md` should be restructured to match.
Several open items below are **resolved or reframed** by this plan — noted inline.

1. **Parallelization (conceptual introduction)** — *currently missing; new.*
   - Whiteboard diagram: one input SEC filing, one core moving from filing to
     filing; then compare with multiple cores (ideally more filings than cores).
   - *Potentially:* demo it — a SLURM script that repeatedly invokes the
     single-file script vs. running an array.
   - → Addresses the "Array Cavern jumps straight to hands-on with no *why*" gap.

2. **How to operationalize parallelization** — *The Array Cavern.*
   - Simplest way on the Yens: SLURM array jobs, and combining outputs.
   - **Avoiding recomputation when jobs fail** → this is the fault-tolerance item
     under "Promised-but-missing content" below.

3. **Running LLM jobs on Stanford infrastructure: why?** — *The Engine Room's
   motivate half, hoisted before the GPU rooms.*
   - So far we've used APIs → query + data sent to a third-party server, response
     back.
   - Why use local LLMs / Stanford infra: (i) privacy / data requirements,
     (ii) cost, (iii) reproducibility, (iv) not constrained by API rate limits.
   - *Potentially here (shifted from current order):* the local LLM vs. Stanford
     AI Playground vs. third-party API comparison.
   - → Resolves the "surface the local-vs-cloud rationale earlier" item below.
     Note the split: hoist the *why + comparison table*; the *empirical
     "compare your own 5 outputs" discussion* stays late (see §5 / §6).

4. **Using the GPU partition** — *The Armory + H200 Chamber + Summoning Circle.*
   - Modern LLMs rely on GPUs. **Why?** LLM inference is essentially chained
     matrix multiplication, which GPUs run especially fast → this is the missing
     "why a GPU" motivation below.
   - The Yens have GPUs that facilitate LLM jobs.
   - Understanding GPU types (inference vs. training, high level) and how they map
     to Yen nodes. **Accuracy watch:** A30/A40/H200 differ mainly by *VRAM*; frame
     training-vs-inference as *scale*, not "these nodes are training-only."
   - Submitting a simple GPU-partition job; running an LLM on the Yens; choosing
     between LLMs on the Yens.

5. **LLM failure modes** — *The Trap Garden.*
   - Rules of thumb for validating LLM outputs (e.g., comparing between models);
     make it possible to compare a subset of filings. ← the Engine Room's
     "validation at scale" table moves here, now *after* the hands-on GPU/LLM work.
   - **TODO: re-evaluate the failure-mode list and defenses** (see the OWASP Top 10
     for LLMs 2025 mapping — hallucination→LLM09/05, runaway loops→LLM10, prompt
     injection→LLM01, irreversibility→LLM06).
   - **Wording nit:** the moved discussion prompt opens "you've run both
     pipelines," but the two-model side-by-side run is §6. Present the rubric
     generically here and move the "compare your own 5 outputs" prompt to §6.

6. **Putting it all together** — *Boss Gate 4.*
   - Run an array job and combine outputs, using two different LLMs; compare the
     outputs; write a README.

7. **Staying in touch** — *The Research Guild.*

**Structural note:** §4 folds three current rooms into one arc. Fine as a lecture
outline; if the site keeps the room metaphor, §4 should still render as 2–3 rooms
in that order. Don't lose the Engine Room's `restricted data → local` decision
tree — it belongs in §3.

---

## Broken / missing file references

- [ ] **Create `extract_filing.py` (referenced but does not exist).**
  `array-cavern.md:67` and Boss Gate 4 call
  `python3 ~/rf-bootcamp-2026/extract_filing.py --input "$FILING" --output "…"`,
  but no such file exists in the repo. Three problems:
  1. **Name** — `extract_filing.py` doesn't exist anywhere.
  2. **Path** — referenced at the repo root; real scripts live in `scripts/`.
  3. **Interface** — the closest real script, `scripts/extract_form_3_one_file.py`,
     hardcodes its input path (`FILING_PATH = "…"`) and has **no argparse**, so
     `--input`/`--output` would be ignored and every array task would reprocess
     the same single filing.

  Options considered:
  - New `scripts/extract_filing.py` with argparse (`--input`/`--output`),
    adapted from `extract_form_3_one_file.py`; update Day 4 refs.
  - Add argparse to `scripts/extract_form_3_one_file.py` (default to current
    hardcoded paths); point Day 4 at it.
  - Docs-only path fix (does **not** resolve the interface mismatch — array
    still won't run correctly).

## Promised-but-missing content

- [ ] **The Array Cavern doesn't teach the fault tolerance it's credited with.**
  Fault tolerance ("checkpoint log + skip completed files") is promised in
  `agenda.md:136` and attributed to The Array Cavern in the Boss Gate 4 "Full
  Stack" table (`boss-gate-4.md:63`, "Checkpoint Charm"). But `array-cavern.md`
  only shows the happy path — all 100 tasks succeed. The merge script's `failed`
  list (lines 90–112) records missing/unparseable outputs but never demonstrates
  a failure or the skip-completed re-run pattern. Either:
  - Add a section / side quest that (a) shows a task failing and (b) adds a
    `if output.exists(): continue` skip so re-running only reprocesses failures
    (source material: `rcpedia-reference/day3/06_optimizing-performance-yens.html`,
    "Implement Checkpoints"), or
  - Remove the fault-tolerance claims from `agenda.md` and `boss-gate-4.md` if
    it's out of scope for Day 4.

- [ ] **Teach how to *interactively* use a GPU node on the Yens.** `running-llms.md`
  tells students to run Ollama "on a GPU node (an interactive GPU session, or
  inside a GPU job)" but never shows how to *get* an interactive GPU session —
  e.g. an `srun --partition=gpu --gres=gpu:1 --pty bash` session (confirm the exact
  flags/partition for the current Yen setup). Add a short walkthrough of requesting
  an interactive GPU session, and a line on when to use interactive (exploring,
  pulling a model, quick tests) vs. a batch job (long/production runs). The
  running-an-LLM exercise depends on students being able to do this.

## Side quests & per-section checkpoints

- [ ] **Construct side quests for Day 4 — currently there are none.** Day 3 pages
  include optional **side quests** (registered as `side1…sideN` keys per room in
  `assets/js/quest-log.js`, e.g. `d3-head-chef` has `side1…side7`) and drop a
  `quest-check` checkbox at the end of *each* exercise/quest section (3–6 per page).
  Day 4's active pages have a single checkbox each — `parallelization.md`,
  `slurm-arrays.md`, and `array-exercise.md` (one checkbox at the very end, after
  all five Parts). To match Day 3:
  1. **Write optional side quests** for Day 4 — candidate material: the *chunking*
     pattern as a hands-on side quest (50 tasks / 100 filings); deliberately fail a
     task and re-run to see the skip-if-exists resilience in action; a GPU-room side
     quest once those pages are built.
  2. **Add per-section / per-Part checkpoints** so progress is tracked at the
     granularity Day 3 uses (e.g. a checkbox after each Part of the array exercise).
  Both require registering the new keys under the relevant `d4-*` rooms in
  `quest-log.js` (e.g. `d4-array-exercise` → `part1…part5` and `side1…`).

- [x] **Leaderboard-sync instructions — Day 3 convention adopted.** Day 3 pairs
  *every* checkpoint with a "🔄 **Keep the leaderboard live**" blockquote that tells
  the student to use **Claude Code in the terminal** to set the specific `room.key`
  to `true` in `quest_log.json` at the repo root (creating it if missing), **verify
  with `git remote -v` that `origin` is their own fork, not `gsbdarc/rf-bootcamp-2026`**,
  then commit and push to `main` (see e.g. `day3/ticket-rail.md:88`). This blockquote
  is now added to the single checkpoint on each active Day 4 page
  (`parallelization.md`, `slurm-arrays.md`, `array-exercise.md`). **Remaining:** when
  the per-Part checkpoints and side quests above are built, attach the same sync
  prompt to each new checkpoint. (The archived `boss-gate-4.md` still uses the older
  Day 2 button-and-upload flow — reconcile if that page is revived.)

## Missing motivation / sequencing

> **Both items below are now folded into the "Agreed Day 4 sequencing plan"
> above** (the "why GPU" motivation → §4; the local-vs-cloud rationale + earlier
> placement → §3). Kept here for the specific file/line detail needed when
> restructuring.

- [ ] **The Armory jumps into GPUs without saying why to use one.** `armory.md`
  (nav_order 3, the first GPU room) covers *which* GPU (A30/A40/H200 table),
  *how* to request one (`--gres=gpu:1`), and VRAM as the constraint — but never
  *why* a researcher wants a GPU. Nothing earlier in Day 4 covers this either —
  the Array Cavern is CPU-only. Add a short "Why a GPU?" intro before the GPU
  table, plus a one-sentence bridge from CPU job arrays (Array Cavern) to GPU work.

  **Frame it as "run the GPU yourself vs. rent it via an API," not "CPU vs GPU."**
  Students have used GPUs indirectly since Day 2 — every LLM API call (Playground,
  OpenAI, Anthropic) is GPU-served on the *provider's* hardware. The real Day 4
  leap is running inference *yourself* on the Yens instead of calling out. Make
  the "it's GPUs either way — yours vs. rented" point explicit; it motivates the
  whole GPU Fortress floor.

- [ ] **Strengthen the local-vs-cloud rationale (Engine Room) and surface it
  earlier.** `engine-room.md` (nav_order 6) already compares Ollama-on-Yens /
  Playground / third-party API on data residency, cost, models, and a
  sensitivity-based decision tree — but (a) it lands *after* the Armory, H200
  Chamber, and Summoning Circle, so the "why local" reasoning comes after
  students have already met GPUs and summoned a local LLM; and (b) it omits two
  "why run on Stanford infra" reasons: **reproducibility / model pinning** (you
  control exact weights; API models change silently) and **throughput / no rate
  limits or per-token cost** on large batch jobs. Consider a forward-pointer from
  the Armory to the Engine Room, and add those two reasons.

  **Do NOT simply reorder the Engine Room before the Armory** — it has hard
  dependencies on later rooms: it cites the H200 / 141 GB VRAM (`engine-room.md:28`,
  taught in the Armory), the Ollama setup / `base_url` (lines 30, 39–42, from the
  Summoning Circle), and its discussion (lines 87, 90) tells students to *compare
  Playground vs. Ollama outputs they've already produced* — which only exists after
  the Summoning Circle. The room does two jobs: **motivate** (why local vs. cloud)
  and **synthesize/choose** (compare + decide). Split them: hoist only the
  2–3-sentence motivation into the Armory intro / a floor preamble; leave the
  comparison table, decision tree, and discussion at nav 6 as post-hands-on
  synthesis.

## Reference — why run LLMs locally on the Yens

Rationale to draw on when writing the Armory intro and strengthening the Engine
Room. The choice is **local** (Ollama / vLLM on Yen GPUs) vs. a **hosted API**
(Stanford AI Playground, OpenAI, Anthropic). Per the framing above, both run on
GPUs — so the question is *your* GPU vs. a *rented* one, not GPU vs. no-GPU.

**Reasons to run locally / on the Yens:**

1. **Data privacy & compliance (often a hard requirement, not a preference).**
   Restricted, confidential, or IRB-governed data cannot leave Stanford's
   perimeter. With local inference, prompts and documents never leave the cluster —
   nothing is sent to a third-party vendor. For many research datasets this is a
   legal/ethical *must*. *(Engine Room already covers this.)*

2. **Cost at scale.** No per-token billing. Cluster access is already paid for, so
   local inference is effectively free at the margin. A large batch (e.g. 100k
   filings) that would run up a real bill on a metered API costs nothing extra on
   the Yens. *(Engine Room already covers cost.)*

3. **Reproducibility & model pinning.** You control the exact weights and version.
   Hosted models change or get deprecated silently — "gpt-4o" today is not
   guaranteed to be the same model next year — which quietly breaks
   reproducibility, a core research value. Local weights are frozen, versioned, and
   citable, so a reviewer or your future self can rerun the identical pipeline.
   *(Missing from Engine Room — add.)*

4. **Throughput, no rate limits.** APIs impose request/token rate limits and quotas
   that throttle a big parallel job array. Locally you're bounded only by your own
   GPU allocation, so a thousand-task array isn't rate-limited or metered.
   *(Missing from Engine Room — add.)*

5. **No external-dependency risk.** API outages, model deprecations, or billing /
   account / vendor-policy changes can halt a pipeline. A local run is
   self-contained and reruns years later even if the vendor discontinues the model.

6. **Control & customization.** Fine-tune, quantize, swap models, adjust sampling,
   inspect internals — none of which a closed API allows. Ties into the fine-tuning
   and NVIDIA NIM side material.

7. **Understanding the stack.** Serving a model yourself (weights → GPU →
   OpenAI-compatible endpoint) demystifies what an API call actually is — and
   because the interface is OpenAI-compatible, the *only* code change vs. the
   Playground is `base_url`.

**Honest counterweight — when the cloud/API is the better choice** (name this so
the room presents a real tradeoff, matching the Engine Room's decision tree):

- **Capability:** frontier proprietary models (GPT-4o, Claude) are often stronger
  than what fits on a single H200; for the hardest tasks, the API wins.
- **Convenience:** an API key and one line of code — no GPU job, no `ollama serve`,
  no VRAM budgeting, no queue wait.
- **Elastic scale:** the H200 caps at 141 GB VRAM; very large models or high
  concurrency can exceed local capacity, while a hosted API scales on demand.

Rule of thumb (already in the Engine Room's tree): **restricted data → local, no
exceptions**; otherwise weigh cost / reproducibility / throughput (favor local)
against capability / convenience (favor the API).

## Related gaps

- [ ] **`argparse` / CLI flags are never introduced in Days 1–3**, but the Array
  Cavern depends on an argparse-enabled script. Either introduce it earlier or
  add a short aside in Day 4 before first use.
- [ ] **Keyword arguments are used from Day 2 onward but never explained.**
  Students type `name=value` (OpenAI client, pandas) many times without the
  positional-vs-keyword distinction ever being named. Consider a one-line aside
  in `day2/oracles-chamber.md` at first use.

## Audit still in progress

- [ ] **Finish the cross-page link audit.** Confirmed OK so far: all Day 3 child
  links resolve; all referenced images/assets exist. **Not yet verified:**
  whether every internal page link resolves — cross-day links to check include
  `day2/human-vs-llm`, `scroll-transfer`, `cartographers-room`, and `claude-code`.
  (Scan was interrupted before completion.)

---

*Drafted by Claude (Opus 4.8) from a Day 4 content audit — verify each item before acting.*
