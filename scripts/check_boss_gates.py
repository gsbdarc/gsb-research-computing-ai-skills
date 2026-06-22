"""
DARC Dungeon Boss Gate grader.

Runs on student forks via GitHub Actions after every push to main.
Checks Boss Gate deliverables and updates docs/_data/progress.yml.
No external dependencies — stdlib only.
"""

import sys
import json
import csv
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROGRESS_FILE = REPO_ROOT / "docs" / "_data" / "progress.yml"


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


def save_progress(unlocked: set):
    lines = ["unlocked_floors:"]
    for f in sorted(unlocked):
        lines.append(f"- {f}")
    PROGRESS_FILE.write_text("\n".join(lines) + "\n")


# ── Boss Gate checks ──────────────────────────────────────────────────────────

def check_gate_1():
    """Boss Gate 1: signature_spell.txt contains a .spell filename."""
    candidates = list(REPO_ROOT.glob("**/signature_spell.txt"))
    if not candidates:
        return False, "signature_spell.txt not found in your repo"
    content = candidates[0].read_text().strip()
    if not content.endswith(".spell"):
        return False, f"signature_spell.txt must contain a .spell filename, got: {content!r}"
    return True, f"Spell found: {content}"


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
    """Boss Gate 3: CSV + failed_tasks.txt + README.md."""
    errors = []
    csv_file = REPO_ROOT / "results" / "great_scroll_sweep.csv"
    failed_file = REPO_ROOT / "results" / "failed_tasks.txt"
    readme = REPO_ROOT / "README.md"

    if not csv_file.exists():
        errors.append("results/great_scroll_sweep.csv not found")
    else:
        try:
            rows = list(csv.reader(csv_file.read_text().splitlines()))
            if len(rows) < 2:
                errors.append("great_scroll_sweep.csv appears empty (only a header row)")
        except Exception as e:
            errors.append(f"Could not read CSV: {e}")

    if not failed_file.exists():
        errors.append("results/failed_tasks.txt not found (can be empty if all tasks succeeded)")

    if not readme.exists():
        errors.append("README.md not found — write it in The Chronicle room")

    if errors:
        return False, "; ".join(errors)

    row_count = len(list(csv.reader(csv_file.read_text().splitlines()))) - 1
    return True, f"CSV has {row_count} data rows; failed_tasks.txt present; README.md present"


def check_gate_4():
    """Boss Gate 4: comparison.csv + privacy_ruling.md + README mentioning Ollama."""
    errors = []
    comparison = REPO_ROOT / "results" / "comparison.csv"
    ruling = REPO_ROOT / "results" / "privacy_ruling.md"
    readme = REPO_ROOT / "README.md"

    if not comparison.exists():
        errors.append("results/comparison.csv not found")
    if not ruling.exists():
        errors.append("results/privacy_ruling.md not found")
    if not readme.exists():
        errors.append("README.md not found")
    elif "ollama" not in readme.read_text().lower():
        errors.append("README.md doesn't mention Ollama — update it to document the endpoint swap")

    if errors:
        return False, "; ".join(errors)
    return True, "All Champion's Ascent deliverables present"


# ── Main ──────────────────────────────────────────────────────────────────────

GATES = [
    (2, "Boss Gate 1", check_gate_1),
    (3, "Boss Gate 2", check_gate_2),
    (4, "Boss Gate 3", check_gate_3),
    (5, "Boss Gate 4", check_gate_4),
]

def main():
    unlocked = load_progress()
    changed = False

    print("=" * 55)
    print("  DARC Dungeon — Boss Gate Grader")
    print("=" * 55)
    print(f"  Currently unlocked floors: {sorted(unlocked)}")
    print()

    for unlock_floor, gate_name, check_fn in GATES:
        prereq_floor = unlock_floor - 1
        if prereq_floor not in unlocked:
            continue  # can't check this gate yet
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
    if changed:
        save_progress(unlocked)
        print(f"  Progress saved. Floors now unlocked: {sorted(unlocked)}")
    else:
        print(f"  No changes. Floors unlocked: {sorted(unlocked)}")
    print("=" * 55)
    return 0


if __name__ == "__main__":
    sys.exit(main())
