#!/usr/bin/env python3
"""Auto-sync Codegraph for the workspace (fail-open).

Used by:
  - sessionStart  → quiet catch-up sync at workspace root
  - afterFileEdit → sync when an indexable source file was edited

Sync root = workspace (parents[2] from this hook). Relies on root
`codegraph.json` excludes — no hardcoded app folder (unlike react-app packs).

Optional override: CODEGRAPH_SYNC_ROOTS=comma-separated paths relative to ROOT
(e.g. "DBS-FFW-SPFX,Other-SPFX"). Default: sync ROOT itself.

Fail-open: never block the agent. No secrets.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEBOUNCE_SEC = 2.0
LOCK = ROOT / ".codegraph" / ".autosync-stamp"
INDEXABLE_SUFFIXES = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
    ".py",
}
SKIP_DIR_NAMES = {
    "node_modules",
    "dist",
    "lib",
    "temp",
    "release",
    ".vite",
    ".npm-cache",
    ".codegraph",
    ".cursor",
    "_cursor",
    ".git",
    "__pycache__",
}


def which_codegraph() -> str | None:
    from shutil import which

    return which("codegraph")


def sync_roots() -> list[Path]:
    raw = os.environ.get("CODEGRAPH_SYNC_ROOTS", "").strip()
    if not raw:
        return [ROOT]
    roots: list[Path] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        p = (ROOT / part).resolve() if not Path(part).is_absolute() else Path(part)
        if p.is_dir():
            roots.append(p)
    return roots or [ROOT]


def _under_skip_dir(rel: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in rel.parts)


def should_sync_path(file_path: str) -> bool:
    if not file_path:
        return False
    s = file_path.replace("\\", "/")
    p = Path(file_path)
    try:
        if p.is_absolute():
            rel = p.resolve().relative_to(ROOT.resolve())
        else:
            rel = Path(s)
            # still reject escapes
            _ = (ROOT / rel).resolve().relative_to(ROOT.resolve())
    except ValueError:
        return False
    if _under_skip_dir(rel):
        return False
    if rel.suffix.lower() not in INDEXABLE_SUFFIXES:
        return False
    return True


def debounced() -> bool:
    """Return True if we should skip (synced too recently)."""
    try:
        if LOCK.is_file():
            age = time.time() - LOCK.stat().st_mtime
            if age < DEBOUNCE_SEC:
                return True
        LOCK.parent.mkdir(parents=True, exist_ok=True)
        LOCK.write_text(str(time.time()), encoding="utf-8")
    except OSError:
        pass
    return False


def run_sync() -> None:
    bin_path = which_codegraph()
    if not bin_path:
        return
    if debounced():
        return
    for target in sync_roots():
        try:
            subprocess.run(
                [bin_path, "sync", "-q", str(target)],
                cwd=str(target),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=60,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            pass


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        data = {}

    event = data.get("hook_event_name") or ""

    if event == "afterFileEdit":
        fp = data.get("file_path") or ""
        if should_sync_path(str(fp)):
            run_sync()
    else:
        # sessionStart (and any other callers): catch-up sync
        run_sync()

    if event == "sessionStart" or not event:
        json.dump({}, sys.stdout)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
