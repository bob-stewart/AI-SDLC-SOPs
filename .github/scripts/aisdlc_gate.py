#!/usr/bin/env python3
"""AISDLC Gate (bootstrap)

Classifies changed files into "surfaces" and enforces minimal controls:
- If any gateable surface is touched, require EVIDENCE_ID in PR body.

This is intentionally lightweight to bootstrap the AISDLC flywheel.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

GATEABLE = {"privilege", "auth", "network", "config", "env-config"}

PATTERNS = {
    "ci": [re.compile(r"(^|/)\.github/")],
    "ops-scripts": [re.compile(r"(^|/)scripts/")],
    "env-config": [re.compile(r"(^|/)environments/")],
    "config": [re.compile(r"openclaw\.json"), re.compile(r"(^|/)config/")],
    "privilege": [re.compile(r"allowlist|approval|exec|privilege|sudo", re.I)],
    "auth": [re.compile(r"key|token|secret|auth|oauth", re.I)],
    "network": [re.compile(r"bind|listen|port|ingress|firewall|tls|cert", re.I)],
    "governance": [re.compile(r"(^|/)sops/"), re.compile(r"(^|/)diagrams/")],
}


def sh(*args: str) -> str:
    return subprocess.check_output(list(args), text=True).strip()


def classify(paths):
    surfaces = set()
    for p in paths:
        for surf, regs in PATTERNS.items():
            if any(r.search(p) for r in regs):
                surfaces.add(surf)
    # Normalize gateable detection: if anything matches the keywords, it's gateable.
    is_gateable = any(s in GATEABLE for s in surfaces)
    return sorted(surfaces), is_gateable


def main():
    base = os.environ.get("GITHUB_BASE_REF")
    head = os.environ.get("GITHUB_HEAD_REF")

    # On pull_request, GitHub provides refs. Fallback to HEAD~1..HEAD.
    changed = []
    try:
        if base and head:
            sh("git", "fetch", "--no-tags", "origin", f"{base}:{base}")
            out = sh("git", "diff", "--name-only", f"origin/{base}...HEAD")
        else:
            out = sh("git", "diff", "--name-only", "HEAD~1..HEAD")
        changed = [x for x in out.split("\n") if x]
    except Exception:
        changed = []

    pr_body = os.environ.get("PR_BODY", "")

    surfaces, gateable = classify(changed)

    print("AISDLC_GATE")
    print(f"changed_files={len(changed)}")
    print(f"surfaces={','.join(surfaces) if surfaces else '(none)'}")
    print(f"gateable={gateable}")

    if not gateable:
        return 0

    # Minimal enforcement: require EVIDENCE_ID in PR body.
    if not re.search(r"\bEVIDENCE_ID\s*[=:]\s*[0-9]{8}T[0-9]{6}Z?\b", pr_body):
        print("\nFAIL: Gateable surfaces detected but no EVIDENCE_ID found in PR body.")
        print("Add e.g. 'EVIDENCE_ID=20260216T171955Z' to the PR description.")
        return 2

    print("\nOK: EVIDENCE_ID present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
