"""
Sync new fork owners into docs/_data/students.yml.

Queries GitHub for everyone who has forked the class repo and adds anyone
missing from the roster, so students show up on the leaderboard without the
instructor needing to already know their GitHub username. Requires the `gh`
CLI, authenticated. No external dependencies — stdlib only.

Usage:
    python3 .instructor/sync_forks_to_students.py            # dry run, report only
    python3 .instructor/sync_forks_to_students.py --apply     # write new entries
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
STUDENTS_FILE = REPO_ROOT / "docs" / "_data" / "students.yml"
CLASS_REPO = "gsbdarc/rf-bootcamp-2026"


def list_fork_owners():
    out = subprocess.run(
        ["gh", "api", f"repos/{CLASS_REPO}/forks", "--paginate", "--jq", ".[].owner.login"],
        capture_output=True, text=True, check=True,
    )
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


def load_existing_usernames():
    text = STUDENTS_FILE.read_text()
    usernames = set()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- username:"):
            usernames.add(stripped.split(":", 1)[1].strip().strip("'\""))
    return usernames


def guess_display_name(username):
    out = subprocess.run(
        ["gh", "api", f"users/{username}", "--jq", ".name"],
        capture_output=True, text=True, check=True,
    )
    full_name = out.stdout.strip()
    if not full_name or full_name == "null":
        return username
    parts = full_name.split()
    if len(parts) == 1:
        return parts[0]
    return f"{parts[0]} {parts[-1][0]}."


def append_students(new_entries):
    lines = ["\n"]
    for username, name in new_entries:
        lines.append(f'- username: {username}\n  name: "{name}"\n')
    with STUDENTS_FILE.open("a") as f:
        f.writelines(lines)


def main():
    apply = "--apply" in sys.argv[1:]

    fork_owners = list_fork_owners()
    existing = load_existing_usernames()
    new_usernames = [u for u in fork_owners if u not in existing]

    if not new_usernames:
        print("No new forks found — roster is already up to date.")
        return 0

    new_entries = [(u, guess_display_name(u)) for u in new_usernames]

    print(f"Found {len(new_entries)} new fork(s):")
    for username, name in new_entries:
        print(f'  - username: {username}\n    name: "{name}"')
    print("\nNames are best-effort from public GitHub profiles — double-check before class.")

    if apply:
        append_students(new_entries)
        print(f"\nAppended {len(new_entries)} entries to {STUDENTS_FILE.relative_to(REPO_ROOT)}.")
    else:
        print("\nDry run — no changes written. Re-run with --apply to update students.yml.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
