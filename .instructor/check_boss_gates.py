"""
DARC Dungeon Boss Gate grader.

Runs on student forks via GitHub Actions after every push to main.
Checks Boss Gate deliverables, counts quest log completion, and updates
docs/_data/progress.yml. No external dependencies — stdlib only.
"""

import sys
import os
import json
import csv
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROGRESS_FILE = REPO_ROOT / "docs" / "_data" / "progress.yml"
QUEST_LOG_FILE = REPO_ROOT / "quest_log.json"


# ── Progress file I/O ─────────────────────────────────────────────────────────

def load_progress():
    floors = []
    for line in PROGRESS_FILE.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            try:
                floors.append(int(stripped[2:].strip()))
            except ValueError:
                pass
    return set(floors) if floors else {1}


def save_progress(unlocked: set, completed_checks: int, username: str):
    lines = ["unlocked_floors:"]
    for f in sorted(unlocked):
        lines.append(f"- {f}")
    lines.append(f"completed_checks: {completed_checks}")
    lines.append(f"username: \"{username}\"")
    PROGRESS_FILE.write_text("\n".join(lines) + "\n")


# ── Quest log check count ─────────────────────────────────────────────────────

def count_quest_log():
    if not QUEST_LOG_FILE.exists():
        return 0
    try:
        data = json.loads(QUEST_LOG_FILE.read_text())
        return sum(1 for v in data.values() if v is True)
    except (json.JSONDecodeError, AttributeError):
        return 0


# ── Boss Gate checks ──────────────────────────────────────────────────────────

def check_gate_1():
    """Boss Gate 1: signature_spell.txt contains a .spell filename (anywhere in file)."""
    candidates = list(REPO_ROOT.glob("**/signature_spell.txt"))
    if not candidates:
        return False, "signature_spell.txt not found in your repo"
    content = candidates[0].read_text().strip()
    spell_line = next((l for l in content.splitlines() if l.strip().endswith(".spell")), None)
    if not spell_line:
        return False, f"signature_spell.txt must include a line ending in .spell, got: {content!r}"
    return True, f"Spell found: {spell_line.strip()}"


def check_gate_2():
    """Boss Gate 2: results/mood_ring.json with at least 5 entries."""
    f = REPO_ROOT / "results" / "mood_ring.json"
    if not f.exists():
        return False, "results/mood_ring.json not found"
    try:
        data = json.loads(f.read_text())
        entries = data if isinstance(data, list) else data.get("results", [])
        if len(entries) < 5:
            return False, f"mood_ring.json has {len(entries)} entries — need at least 5"
        return True, f"{len(entries)} entries found"
    except json.JSONDecodeError as e:
        return False, f"mood_ring.json is not valid JSON: {e}"


def check_gate_3():
    """Boss Gate 3: jobs/extract.sh + README.md."""
    errors = []
    job_script = REPO_ROOT / "jobs" / "extract.sh"
    readme = REPO_ROOT / "README.md"

    if not job_script.exists():
        errors.append("jobs/extract.sh not found — write and submit your SLURM batch job script")
    else:
        content = job_script.read_text()
        if "#SBATCH" not in content:
            errors.append("jobs/extract.sh doesn't contain any #SBATCH directives")

    if not readme.exists():
        errors.append("README.md not found — write it in The Chronicle room")

    if errors:
        return False, "; ".join(errors)
    return True, "jobs/extract.sh with #SBATCH directives present; README.md present"


def check_gate_4():
    """Boss Gate 4: great_scroll_sweep.csv + comparison.csv + README mentioning Ollama."""
    errors = []
    sweep = REPO_ROOT / "results" / "great_scroll_sweep.csv"
    comparison = REPO_ROOT / "results" / "comparison.csv"
    readme = REPO_ROOT / "README.md"

    if not sweep.exists():
        errors.append("results/great_scroll_sweep.csv not found — run the array job and merge outputs")
    else:
        try:
            rows = list(csv.reader(sweep.read_text().splitlines()))
            if len(rows) < 2:
                errors.append("great_scroll_sweep.csv appears empty (only a header row)")
        except Exception as e:
            errors.append(f"Could not read great_scroll_sweep.csv: {e}")

    if not comparison.exists():
        errors.append("results/comparison.csv not found — run the side-by-side comparison")

    if not readme.exists():
        errors.append("README.md not found")
    elif "ollama" not in readme.read_text().lower():
        errors.append("README.md doesn't mention Ollama — update it to document the endpoint swap")

    if errors:
        return False, "; ".join(errors)

    row_count = len(list(csv.reader(sweep.read_text().splitlines()))) - 1
    return True, f"Array sweep CSV has {row_count} rows; comparison.csv present; README mentions Ollama"


# ── Main ──────────────────────────────────────────────────────────────────────

GATES = [
    (2, "Boss Gate 1", check_gate_1),
    (3, "Boss Gate 2", check_gate_2),
    (4, "Boss Gate 3", check_gate_3),
    (5, "Boss Gate 4", check_gate_4),
]


def main():
    github_repo = os.environ.get("GITHUB_REPOSITORY", "")
    username = github_repo.split("/")[0] if "/" in github_repo else ""
    completed_checks = count_quest_log()

    # Instructor's repo: keep all floors unlocked for course development and preview
    if github_repo == "gsbdarc/rf-bootcamp-2026":
        save_progress({1, 2, 3, 4}, completed_checks, "gsbdarc")
        print("Instructor repo — all floors unlocked.")
        return 0

    # Student forks: always recompute from scratch so forked state is corrected
    unlocked = {1}
    changed = False

    print("=" * 55)
    print("  DARC Dungeon — Boss Gate Grader")
    print("=" * 55)
    print(f"  Student:               {username or '(local run)'}")
    print(f"  Floors unlocked:       {sorted(unlocked)}")
    print(f"  Quest log checks:      {completed_checks} / 42")
    print()

    for unlock_floor, gate_name, check_fn in GATES:
        prereq_floor = unlock_floor - 1
        if prereq_floor not in unlocked:
            continue
        if unlock_floor in unlocked:
            print(f"  ✓ {gate_name}: already passed")
            continue

        passed, message = check_fn()
        if passed:
            unlocked.add(unlock_floor)
            changed = True
            print(f"  ✓ {gate_name} PASSED → Floor {unlock_floor} unlocked!")
            print(f"    {message}")
        else:
            print(f"  ✗ {gate_name} FAILED")
            print(f"    {message}")

    print()
    save_progress(unlocked, completed_checks, username)
    if changed:
        print(f"  Progress saved. Floors now unlocked: {sorted(unlocked)}")
    else:
        print(f"  No new floors unlocked. Floors: {sorted(unlocked)}")
    print("=" * 55)
    return 0


if __name__ == "__main__":
    sys.exit(main())
