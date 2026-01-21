#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONT_MATTER_FENCE = re.compile(r"^---\s*$")
H1_RE = re.compile(r"^#\s+(.*\S)\s*$")


def strip_existing_front_matter(lines: list[str]) -> list[str]:
    """If the file starts with YAML front matter, remove it and return remaining lines."""
    if not lines:
        return lines
    if not FRONT_MATTER_FENCE.match(lines[0].strip()):
        return lines

    end_idx = None
    for i in range(1, len(lines)):
        if FRONT_MATTER_FENCE.match(lines[i].strip()):
            end_idx = i
            break
    if end_idx is None:
        return lines

    return lines[end_idx + 1 :]


def extract_title_from_h1(lines: list[str]) -> str | None:
    for line in lines:
        m = H1_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def build_front_matter(filename: str, title: str) -> str:
    num_prefix = filename[:2]
    nav_order = int(num_prefix)
    fm_lines = [
        "---",
        "layout: default",
        f"title: {title}",
        "parent: User Guide",
        f"nav_order: {nav_order}",
        "---",
        "",
    ]
    return "\n".join(fm_lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="assets",
        help="Root directory containing markdown assets",
    )
    parser.add_argument(
        "--glob",
        default="**/[0-9][0-9]*.md",
        help="Glob for numbered markdown files under root",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only report changes")
    args = parser.parse_args()

    root = Path(args.root)
    files = sorted(root.rglob(args.glob))

    changed = []
    skipped_no_h1 = []

    for p in files:
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)

        # Remove existing front matter if present
        content_lines = strip_existing_front_matter(lines)

        # Extract title from first H1
        title = extract_title_from_h1([l.rstrip("\n") for l in content_lines])
        if not title:
            skipped_no_h1.append(p)
            continue

        fm = build_front_matter(p.name, title)
        # Ensure we don't duplicate trailing newline handling
        new_text = fm + "".join(content_lines)

        if new_text != text:
            changed.append(p)
            if not args.dry_run:
                p.write_text(new_text, encoding="utf-8")

    print(f"Found {len(files)} numbered markdown files under {args.root}")
    print(f"{'Would change' if args.dry_run else 'Changed'} {len(changed)} files")
    for p in changed:
        print(f"- {p}")

    if skipped_no_h1:
        print("Skipped (no H1 found):")
        for p in skipped_no_h1:
            print(f"- {p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

