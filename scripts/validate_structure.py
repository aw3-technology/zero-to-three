#!/usr/bin/env python3
"""
Validate that all markdown files referenced in book/SUMMARY.md exist,
and optionally detect orphan markdown files under book/ not referenced
by SUMMARY.md.

Usage:
  python scripts/validate_structure.py [--strict]

Exit codes:
  0: OK (no missing files; orphans only if not strict)
  1: Validation errors (missing referenced files or strict orphan failures)
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


RE_MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_summary_links(summary_path: Path) -> set[Path]:
    content = summary_path.read_text(encoding="utf-8")
    found: set[Path] = set()
    for match in RE_MD_LINK.finditer(content):
        target = match.group(1).strip()
        # Skip anchors and URLs
        if target.startswith("#"):
            continue
        if re.match(r"^[a-zA-Z]+://", target):
            continue
        # strip anchors like file.md#heading
        target = target.split("#", 1)[0]
        if not target:
            continue
        found.add(Path(target))
    return found


def list_markdown_files(root: Path) -> set[Path]:
    md_files: set[Path] = set()
    for path in root.rglob("*.md"):
        # ignore summary itself
        rel = path.relative_to(root)
        if rel.as_posix() == "SUMMARY.md":
            continue
        # ignore assets or other non-content dirs if any
        parts = rel.parts
        if parts and parts[0] in {"assets"}:
            continue
        md_files.add(rel)
    return md_files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail on orphan files as well")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    book_dir = repo_root / "book"
    summary = book_dir / "SUMMARY.md"
    if not summary.exists():
        print("ERROR: book/SUMMARY.md not found", file=sys.stderr)
        return 1

    referenced = parse_summary_links(summary)
    all_md = list_markdown_files(book_dir)

    # Check referenced exists
    missing: list[str] = []
    for ref in sorted(referenced):
        target = (book_dir / ref).resolve()
        if not target.exists():
            missing.append(ref.as_posix())

    # Orphans: files not referenced
    orphans = sorted(p.as_posix() for p in (all_md - referenced))

    status = 0
    if missing:
        status = 1
        print("Missing files referenced in SUMMARY.md:")
        for m in missing:
            print(f"  - {m}")

    if orphans:
        msg = "Orphan markdown files not referenced by SUMMARY.md:"
        print(msg)
        for o in orphans:
            print(f"  - {o}")
        if args.strict:
            status = 1

    if not missing and not orphans:
        print("Structure OK: All referenced files exist and no orphans detected.")

    return status


if __name__ == "__main__":
    sys.exit(main())

