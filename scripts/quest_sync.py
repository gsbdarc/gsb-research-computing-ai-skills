#!/usr/bin/env python3
"""Sync your Quest Log progress to the leaderboard.

On your personal course site, open the Quest Log (bottom-left corner), click
"Sync", and copy the token. Run this here on the Yens, inside your clone of your
fork. It decodes your progress, writes quest_log.json, and pushes it to your
fork so the leaderboard updates.

    python3 scripts/quest_sync.py <token>
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
QUEST_KEYS = Path(__file__).resolve().parent / "quest_keys.json"


def fnv1a_hex(s):
    """FNV-1a (32-bit) hex digest — must match keyListHash() in quest-log.js."""
    h = 0x811C9DC5
    for ch in s.encode("utf-8"):
        h ^= ch
        h = (h * 0x01000193) & 0xFFFFFFFF
    return format(h, "x")


def decode_token(token):
    """Decode a 'version.hash.bitfield' token into the list of completed keys.

    The hash guards against a token built from a different key list than this
    clone has (e.g. the fork is behind the site).
    """
    parts = token.strip().split(".")
    if len(parts) != 3 or parts[0] != "1":
        sys.exit("Unrecognized token — copy a fresh one from the Quest Log Sync button.")
    _, token_hash, b64 = parts
    keys = json.loads(QUEST_KEYS.read_text())
    if token_hash != fnv1a_hex(",".join(keys)):
        sys.exit(
            "This token was made from a different version of the site than this clone.\n"
            "Run 'git pull' in your fork, reload the site, copy a fresh token, and re-run."
        )
    pad = "=" * (-len(b64) % 4)
    raw = base64.urlsafe_b64decode(b64 + pad)
    return [k for i, k in enumerate(keys)
            if (i >> 3) < len(raw) and raw[i >> 3] & (1 << (i & 7))]


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
        sys.exit(
            "Push failed:\n" + (push.stderr or push.stdout)
            + "\nIf that's an authentication error, sign in once with 'gh auth login' "
            "on the Yens (Day 1's Repository room), then re-run this."
        )
    print("Pushed to your fork. The leaderboard updates within ~2 minutes.")


if __name__ == "__main__":
    main()
