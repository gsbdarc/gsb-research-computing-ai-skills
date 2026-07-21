#!/usr/bin/env python3
"""Sync your Quest Log progress to the leaderboard.

On your personal course site, open the Quest Log (bottom-left corner), click
"Sync to leaderboard", and copy the command it shows you. Run that command here
on the Yens, inside your clone of your fork. It decodes your progress, writes
quest_log.json, and pushes it to your fork so the leaderboard updates.

    python scripts/quest_sync.py <token>
"""

import argparse
import base64
import json
import subprocess
import sys
from pathlib import Path

CLASS_REPO = "gsbdarc/gsb-research-computing-ai-skills"
REPO_ROOT = Path(__file__).resolve().parent.parent
QUEST_LOG = REPO_ROOT / "quest_log.json"


def decode_token(token):
    token = token.strip()
    pad = "=" * (-len(token) % 4)
    raw = base64.urlsafe_b64decode(token + pad).decode("utf-8")
    return [k for k in raw.split(",") if k]


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=str(REPO_ROOT), capture_output=True, text=True
    )


def require_fork():
    url = git("remote", "get-url", "origin").stdout.strip()
    if not url:
        sys.exit("No git 'origin' remote found — run this inside your cloned fork.")
    if CLASS_REPO in url:
        sys.exit(
            "Your 'origin' points at the class repo (%s), not your own fork.\n"
            "Pushing here would write to the shared repo. Point origin at your\n"
            "fork first, then re-run this." % CLASS_REPO
        )
    return url


def main():
    ap = argparse.ArgumentParser(description="Sync Quest Log progress to your fork.")
    ap.add_argument("token", help="the token from the Quest Log 'Sync to leaderboard' button")
    args = ap.parse_args()

    try:
        keys = decode_token(args.token)
    except Exception:
        sys.exit("That token could not be decoded — copy it again from the Sync button.")
    if not keys:
        sys.exit("No completed quests in that token — nothing to sync.")

    require_fork()

    QUEST_LOG.write_text(json.dumps({k: True for k in keys}, indent=2) + "\n")
    print("Recorded %d completed quest%s in %s" % (len(keys), "" if len(keys) == 1 else "s", QUEST_LOG.name))

    git("add", str(QUEST_LOG))
    commit = git("commit", "-m", "Sync quest log")
    if commit.returncode != 0 and "nothing to commit" in (commit.stdout + commit.stderr):
        print("Already up to date — nothing new to push.")
        return
    push = git("push", "origin", "HEAD:main")
    if push.returncode != 0:
        sys.exit("Push failed:\n" + (push.stderr or push.stdout))
    print("Pushed to your fork. The leaderboard updates within ~2 minutes.")


if __name__ == "__main__":
    main()
