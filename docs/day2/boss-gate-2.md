---
layout: default
title: "Day 2 Challenge"
parent: "Day 2 — The Alchemist's Lab"
nav_order: 8
permalink: /day2/boss-gate-2/
---

# Day 2 Challenge

<div data-room-id="d2-boss-gate"></div>

<img src="{{ '/assets/images/day2-boss-gate.png' | relative_url }}" alt="An illustration titled Boss Gate 2, The Genre Tribunal: scale a research judgment call with LLM-as-a-judge, then route the contested cases to a human. A cloaked figure stands in a vaulted hall before three lit panels. On the left, First Call: Classify — an LLM reads the overview and predicts a genre, shown as a ranked list of candidate genres with scores. In the centre, above a hooded judge on a throne, LLM-as-a-Judge — a second call in which the judge evaluates and rules, agree, disagree, or unsure — with a Judge Reasoning panel below giving a sample rationale. On the right, Judgment — the judge's verdict compared against the rules, with Agree ticked, Disagree crossed, and Unsure marked with a question mark. A banner above reads: route contested cases to a human when the stakes are high, and a scribe at a desk to the right is labelled Human Review, for contested cases a human makes the final call. Two open pages at the bottom show the input and the codebook: a Movie Overview blurb on the left, and Genre Guidelines on the right defining Action, Adventure, Drama, Sci-Fi, and Fantasy. Flasks in the foreground are labelled prompt, rules, features and eval, rules, thresholds." style="display:block;width:100%;max-width:900px;height:auto;margin:1.5rem auto">

---

## The Challenge: The Genre Tribunal

Research runs on **judgment calls**. Is this firm distressed? Is this response positive? Does this paper meet the inclusion criteria? Is this filing disclosing a related-party transaction? Calls like these get made by trained humans working from a codebook, and they are contested at the margins. Two careful coders will disagree, and the disagreement is informative rather than embarrassing.

Genre is a stand-in for all of them. *Angels & Demons* is defensibly **Thriller** or **Mystery**; there is no answer key. So this gate is not "get the right answer at scale." For a judgment call there may be no single right answer to get. It is this instead:

> **Make many judgment calls consistently, document how each one was made, and know which ones you cannot delegate.**

{: .boss }
> **Boss Battle: The Genre Tribunal**
>
> The course repo ships a dataset at `data/top_rated_movies.csv`. It has `id`, `title`, `overview`, and more, but **no genre column**. That is the point: you are going to derive the genre for the **first 10 movies**, have a second model check each call, and route the contested ones to a human.
>
> Produce `results/genre_verdicts.json`, then commit and push it.

**Step back: what are you actually building?** Nothing you haven't built already. Every piece came from [The Oracle's Chamber](../oracles-chamber/): an API call, a Pydantic schema sent in the prompt, `response_format`, validation, logging, a JSON write. What's new is *composing* two calls into one pipeline and adding a decision of your own on the end.

### The template

Every pipeline like this makes the same five moves. Learn them here on movie genres, and you can swap in SEC filings, interview transcripts, or open-ended survey answers without changing the shape:

{: .important }
> **MENU → PICK → CHECK → DECIDE → RECORD**

| Step | What happens | Why it's done this way |
|:---:|---|---|
| **1. Menu** | Give the model a **fixed list** of 17 genres to choose from, plus `Other` for genuine misfits. A Pydantic `Enum` is what enforces it. | Ask an open question and you get open answers: "Sci-Fi Thriller," "Dramedy," a fresh label every tenth movie. A menu is what makes 10,000 answers comparable to each other. |
| **2. Pick** | The **first model** reads the overview, picks one genre, and writes **one sentence on why**. | The reason is how you catch a right answer reached for the wrong reason. Without it, you have a label you can't defend to a reviewer. |
| **3. Check** | A **second, different model** sees the movie and the genre that was picked — **but not the reason** — and says whether it agrees, and how sure it is from 0 to 100. | This is a genuine second opinion, which is exactly what a second human coder gives you. |
| **4. Decide** | **Your code** — not a model — flags the rows a human should look at: *disagreed, or less than 70% sure.* | A rule written in Python is one line a colleague can read, argue with, and change. The models advise; you decide. |
| **5. Record** | Write every verdict to a file: both reasons, the certainty, which model played which role, and whether it got flagged. | Six months from now, this file is the only thing that can answer "how was this label actually reached?" |

Two of those moves are easy to get wrong, and both are deliberate choices rather than arbitrary rules:

- **The checker never sees the first model's reasoning.** Show it a confident-sounding explanation and it will tend to agree with it. Withholding the reason is the whole thing that makes the second opinion worth having.
- **The checker is a *different* model.** A model asked to grade its own answer agrees with itself far more than it should. Pointing the second call at another model id is the cheapest quality improvement available to you, and your `base_url` never changes: same gateway, two roles.

<svg viewBox="0 0 1045 375" role="img" aria-labelledby="tribunal-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:1045px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="tribunal-title">The Genre Tribunal pipeline. One movie row (id, title, overview) goes to a Classifier running gemini-2.5-flash-lite, which picks one of seventeen genres and gives a one-sentence reason. The overview and that predicted genre, but deliberately not the reason, go to a Judge running a different model, gpt-5-mini, which reports whether it agrees, a certainty from 0 to 100, a reason, and a suggested alternative genre. Those two steps are the models proposing. Then your own code, not the model, applies the policy: needs_human_review is true when the judge disagrees or certainty is below 70. The finished verdict row is appended to results slash genre_verdicts.json, and a summary of agreement rate, certainty spread, and flag count is printed.</title>
  <defs>
    <marker id="gt-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#556a95"/></marker>
  </defs>

  <!-- zones -->
  <rect x="192" y="110" width="416" height="185" rx="14" fill="none" stroke="#6f8fbf" stroke-width="1.6" stroke-dasharray="7 6"/>
  <text x="400" y="100" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="0.6" fill="#3f4f74">TWO LLM CALLS  ·  THE MODEL PROPOSES</text>

  <rect x="622" y="110" width="241" height="185" rx="14" fill="none" stroke="#2e8b57" stroke-width="1.6" stroke-dasharray="7 6"/>
  <text x="742" y="100" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="0.6" fill="#1f6b45">YOUR CODE  ·  YOU DECIDE</text>

  <!-- 1. one movie -->
  <rect x="15" y="135" width="150" height="140" rx="14" fill="#fdf6ea" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="90" y="181" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">📄  one movie</text>
  <text x="90" y="209" text-anchor="middle" font-size="11.5" fill="#9a8a68">from the CSV</text>
  <text x="90" y="237" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#6a5326">id · title</text>
  <text x="90" y="255" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#6a5326">overview</text>

  <!-- 2. classifier -->
  <rect x="205" y="135" width="175" height="140" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="292" y="176" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">🤖  Classifier</text>
  <text x="292" y="197" text-anchor="middle" font-size="11.5" fill="#6a7280">the apprentice</text>
  <text x="292" y="221" text-anchor="middle" font-size="8.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2f6fb0">gemini-2.5-flash-lite</text>
  <text x="292" y="245" text-anchor="middle" font-size="11.5" fill="#6a7280">1 of 17 genres</text>
  <text x="292" y="263" text-anchor="middle" font-size="11.5" fill="#6a7280">+ a one-line reason</text>

  <!-- 3. judge -->
  <rect x="420" y="135" width="175" height="140" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="507" y="176" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">⚖️  Judge</text>
  <text x="507" y="197" text-anchor="middle" font-size="11.5" fill="#6a7280">the master</text>
  <text x="507" y="221" text-anchor="middle" font-size="8.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#2f6fb0">gpt-5-mini · different model</text>
  <text x="507" y="245" text-anchor="middle" font-size="11.5" fill="#6a7280">agrees? how sure?</text>
  <text x="507" y="263" text-anchor="middle" font-size="11" font-style="italic" fill="#8a94a6">reports, never decides</text>

  <!-- 4. your code -->
  <rect x="635" y="135" width="215" height="140" rx="14" fill="#eaf6ee" stroke="#a9d4b8" stroke-width="1.8"/>
  <text x="742" y="181" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">🐍  your code</text>
  <text x="742" y="207" text-anchor="middle" font-size="11.5" fill="#4a7d60">one line, auditable</text>
  <rect x="648" y="220" width="189" height="42" rx="6" fill="#ffffff" stroke="#a9d4b8" stroke-width="1.2"/>
  <text x="742" y="238" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#1f6b45">needs_human_review =</text>
  <text x="742" y="254" text-anchor="middle" font-size="10.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#1f6b45">not agrees or certainty &lt; 70</text>

  <!-- 5. output -->
  <rect x="890" y="135" width="140" height="140" rx="14" fill="#fbe9cf" stroke="#dcae6a" stroke-width="1.5"/>
  <text x="960" y="176" text-anchor="middle" font-size="15" font-weight="700" fill="#2c3e50">📜  the scroll</text>
  <text x="960" y="203" text-anchor="middle" font-size="9.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#8a6d3b">results/</text>
  <text x="960" y="219" text-anchor="middle" font-size="9.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#8a6d3b">genre_verdicts.json</text>
  <text x="960" y="243" text-anchor="middle" font-size="11" font-style="italic" fill="#9a8a68">10 rows, committed</text>
  <text x="960" y="262" text-anchor="middle" font-size="11" font-style="italic" fill="#9a8a68">+ printed summary</text>

  <!-- arrows -->
  <line x1="167" y1="205" x2="201" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#gt-ah)"/>
  <line x1="382" y1="205" x2="416" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#gt-ah)"/>
  <line x1="597" y1="205" x2="631" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#gt-ah)"/>
  <line x1="852" y1="205" x2="886" y2="205" stroke="#556a95" stroke-width="2.5" marker-end="url(#gt-ah)"/>

  <!-- what flows along each arrow -->
  <text x="184" y="322" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">overview</text>
  <text x="399" y="322" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">+ predicted_genre</text>
  <text x="399" y="338" text-anchor="middle" font-size="10.5" font-style="italic" fill="#b3611a">reason withheld</text>
  <text x="614" y="322" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">agrees, certainty, reason</text>
  <text x="869" y="322" text-anchor="middle" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">one verdict row</text>

  <text x="522" y="362" text-anchor="middle" font-size="12" font-style="italic" fill="#8a94a6">Flagged rows are routed to a human, never dropped. Repeat for each of the 10 movies.</text>
</svg>

Note where the dashed line falls. The models only *propose*: one names a genre, the other says whether it agrees and how sure it is. Neither is ever asked when a human should step in. That call lives in your code, in one line a reviewer can read and argue with, which is exactly what makes the pipeline auditable and the lesson The Crucible drives home.

---

### 1. Read the first 10 movies

Reach for **pandas**, the standard tool for tabular data in Python and the one you'll use again on Day 3. It reads the CSV, takes the first 10 rows, and hands you each one as a row object:

```python
import pandas as pd

df = pd.read_csv("../data/top_rated_movies.csv").head(10)

for row in df.itertuples():
    print(row.id, row.title, row.overview[:80])
```

`head(10)` is the "first 10 movies" requirement, and `itertuples()` walks them one at a time so you can call the model per movie. You need `id`, `title`, and `overview`; the other columns come along for free and you can ignore them.

{: .note }
> 💡 `pandas` came with the venv you forged in [The Venv Forge](../venv-forge/). If `import pandas` fails, you're on the wrong Python: check that your prompt shows `(.venv)`, or `pip install pandas` into the venv and add it to your `requirements.txt`.

**Zoom out:** *ten short blurbs of unstructured text, which is the same shape of problem as the Form 3 filings, just smaller.*

### 2. Classify: the apprentice names a genre

Send each `overview` to `gemini-2.5-flash-lite` and have it return two things: the single best-fitting genre from the set below, and a **one-sentence reason** (25 words is plenty). A Pydantic `Enum` is the clean way to reject anything off-list.

```text
Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family,
Fantasy, Horror, Mystery, Romance, Science Fiction, Thriller, War, Western, Other
```

Capture the reason even though nothing downstream consumes it. It's what lets you spot a right answer reached for the wrong reason, and it's the difference between a label you can defend to a reviewer and a number you have to take on faith.

{: .note }
> 💡 **This label set is itself a judgment call, and not a great one.** `Animation` is a *medium*, not a genre, so *Attack on Titan* and *Monster House* have no defensible single answer: Animation and Action are both right, and the model must discard one. `Other` is the escape hatch, and a pile-up of `Other` is a signal your label set is wrong rather than that your data is weird.
>
> In real work this is your **codebook**, and it is a research-design decision you will be asked to justify. Notice how much of the pipeline's quality was decided here, before a single API call.

**Zoom out:** *this is Step 6 of The Oracle's Chamber with a different schema. Same call, same validation, new fields.*

### 3. Judge: an independent second opinion

Now the second call, and the two design rules from the template both apply here.

**Use a different model.** Point the judge at `gpt-5-mini`. Your `client` and `base_url` don't change; only the `model` argument does, exactly as [The Key Vault](../key-vault/) promised. A model asked to grade its own answer agrees with itself far more than it should, and this is a one-line fix.

**Send the overview and the predicted genre, but not the classifier's reason.** This is deliberate. Hand a judge a confident-sounding explanation and it tends to go along with it; withholding it is what makes the verdict an independent check rather than an echo.

Have the judge return:

| Field | Type | Meaning |
|---|---|---|
| `agrees` | `bool` | Would it have made the same call? |
| `certainty` | `int` | 0 to 100 |
| `reason` | `str` | One sentence |
| `suggested_genre` | `Optional[Genre]` | Its alternative, only when it disagrees |

Validate this reply with Pydantic too; a certainty of `"high"` instead of `85` should fail loudly, not sneak through.

**Zoom out:** *this is LLM-as-a-judge. One model's output becomes the next model's input, which is the basic move behind every multi-stage AI pipeline.*

### 4. Decide: your code, not the model

Mark a movie `needs_human_review` when the judge **disagrees** or its **certainty is below 70**. Write that as a line of Python:

```python
needs_human_review = (not verdict.agrees) or (verdict.certainty < 70)
```

Record `suggested_genre` in your output, but **never apply it automatically**. The judge proposed an alternative; that's evidence for the human who reviews the row, not an instruction to your script. The moment code silently overwrites one model's answer with another's, nobody can reconstruct how a label was reached.

Log as you go, and make it a `WARNING` when something gets flagged so the escalations stand out.

**Zoom out:** *never ask a model to decide when a human should overrule it. A threshold in code is one line a reviewer can read, argue with, and change. A threshold buried in a prompt is none of those things.*

### 5. Write the scroll and commit

All ten results go to `results/genre_verdicts.json`, which is at the **repo root**, so from `day2/` you write to `../results/genre_verdicts.json`. It's a JSON array, one object per movie:

```json
[
  {
    "id": 13448,
    "title": "Angels & Demons",
    "predicted_genre": "Thriller",
    "classifier_reason": "Centers on a conspiracy investigation against a deadline.",
    "agrees": true,
    "certainty": 85,
    "judge_reason": "The overview is driven by investigation and suspense.",
    "suggested_genre": null,
    "needs_human_review": false,
    "classifier_model": "gemini-2.5-flash-lite",
    "judge_model": "gpt-5-mini"
  }
]
```

Every entry must include `id`, `title`, `predicted_genre`, `certainty` (0 to 100), and `needs_human_review`. The rest is what turns a list of labels into a record someone else can audit: both reasons, the judge's alternative, and **which model played which role**, so a reader six months from now can reproduce the run instead of guessing at it.

Then print a summary before you exit. Ten rows is small enough to eyeball, but the habit is what matters, and at 10,000 rows this block is the only thing you'll actually read:

```text
agreement rate ........  7/10  (70%)
certainty  min/med/max   60 / 85 / 95
flagged for review ....  4/10
```

{: .warning }
> **Agreement is not accuracy.** This CSV has no genre column, so you have no answer key, and for a judgment call there may be no single right answer to have. A 70% agreement rate says two models made the same call. That is evidence of *consistency*, not *correctness*: two models trained on similar text can be confidently wrong together. Notice too that the certainty scores cluster high, which is a fact about how models report confidence, not a sign your pipeline is working.
>
> So read your disagreements before your agreements. A film the two models split on usually isn't a failure, it's a genuinely contested case telling you where a human has to make the call. That is exactly what a second human coder does for you.

```bash
source ~/gsb-research-computing-ai-skills/.venv/bin/activate
cd ~/gsb-research-computing-ai-skills/day2
python3 genre_tribunal.py                    # reads ../data/, writes ../results/
git add ../results/genre_verdicts.json
git commit -m "Day 2 Challenge: Genre Tribunal complete"
git push
```

**Zoom out:** *a committed, validated, human-flagged result file is the whole deliverable. It is what a skeptical colleague would ask to see.*

{: .tip }
> **Write `genre_tribunal.py` in `day2/`**, alongside `oracle.ipynb`, and run it from there. That means the paths look like the ones in your notebook: `../data/` to read, `../results/` to write, and `../.env` for the key. (The staged scripts in The Oracle's Chamber live in `scripts/` and run from the repo root instead, which is why theirs have no `../`.)
>
> `results/` is already in the repo, but a script that creates what it needs is more portable than one that assumes:
>
> ```python
> import os
> os.makedirs("../results", exist_ok=True)
> ```
>
> Your `.env` is at the **repo root**, one level up from `day2/`, so load it with `load_dotenv("../.env")` — exactly as you did in `oracle.ipynb`.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d2-boss-gate" data-key="commit"> I classified 10 movies, judged each with a second model, flagged the contested ones in code, and pushed `results/genre_verdicts.json`</label>

---

## Finished early? Climb the leaderboard

Got time left? Go back through Day 2 and knock out any quests you skipped: the extra gateway endpoints in The Oracle's Chamber, the leaked-key hunt in The Key Vault, the kernel hunt in The Venv Forge. Every quest you check off bumps your total and your rank.

---

## Day 2: What You Learned

- **Notebooks and scripts**: running cells in JupyterHub, and knowing when to graduate exploration into a `.py` file you can schedule.
- **Environments**: `$PATH`, `module load`, and forging an isolated venv; registering it as a Jupyter kernel and capturing it as a `requirements.txt` a collaborator can rebuild.
- **Secrets**: loading an API key from `.env`, keeping it out of git, and why a committed key is a leaked key.
- **The API**: the OpenAI-compatible `messages` shape, system vs. user prompts, and the one `base_url` that points the same code at Stanford, a vendor, or a local model.
- **Structured output**: `response_format` constrains the model *while it generates*; Pydantic validates *after* the reply lands; sending `model_json_schema()` in the prompt is what keeps both ends in sync.
- **Reproducibility**: `logging` for diagnostics and files for results, outputs named after their inputs, and a raw reply saved before validation so a failed run still leaves evidence.
- **Governance**: classifying data on Stanford's risk scale, knowing what a coding agent sweeps into its context, and what each path costs.
- **Scaling a judgment call**: generate with evidence, check it with a *different* model that's blind to the first one's reasoning, decide in code rather than in a prompt, and report what happened. Agreement is consistency, not correctness, and the disagreements are the rows worth your attention.

You now have the full loop for an AI-assisted pipeline: **classify the data → pick the tool → prompt → validate → decide → log → commit.**
