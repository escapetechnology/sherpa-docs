#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


EXPORT_KEYS_RE = re.compile(r"^(print_background:|export_on_save:)\s*$", re.MULTILINE)
NUMERIC_HTML_COMMENT_RE = re.compile(r"^\s*<!--\s*\d+\s*-->\s*$")


def find_front_matter_block(text: str) -> tuple[int, int] | None:
    """
    If `text` begins with YAML front matter, return (start_idx, end_idx_exclusive)
    for the entire block including both '---' lines. Otherwise return None.
    """
    if not text.startswith("---"):
        return None

    lines = text.splitlines(keepends=True)
    if not lines:
        return None
    if lines[0].strip() != "---":
        return None

    # Find closing '---' on its own line (second fence).
    end_line_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_line_idx = i
            break
    if end_line_idx is None:
        return None

    start = 0
    end = sum(len(l) for l in lines[: end_line_idx + 1])
    return (start, end)


def strip_export_header(text: str) -> tuple[str, bool]:
    """
    Remove:
      1) Leading front matter if it contains print_background/export_on_save
      2) Immediately following numeric HTML comment line (after optional blank lines)
    """
    fm = find_front_matter_block(text)
    if fm is None:
        return text, False

    fm_text = text[fm[0] : fm[1]]
    if not EXPORT_KEYS_RE.search(fm_text):
        return text, False

    rest = text[fm[1] :]

    # Drop leading blank lines after front matter
    rest_lines = rest.splitlines(keepends=True)
    i = 0
    while i < len(rest_lines) and rest_lines[i].strip() == "":
        i += 1

    # Drop numeric HTML comment line if present
    if i < len(rest_lines) and NUMERIC_HTML_COMMENT_RE.match(rest_lines[i]):
        i += 1
        # Drop blank lines after the comment too
        while i < len(rest_lines) and rest_lines[i].strip() == "":
            i += 1

    new_text = "".join(rest_lines[i:])
    return new_text, True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="assets",
        help="Root directory to search from (default: assets)",
    )
    parser.add_argument(
        "--glob",
        default="[0-9][0-9]*.md",
        help="Filename glob (default: [0-9][0-9]*.md)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print files that would change")
    args = parser.parse_args()

    root = Path(args.root)
    files = sorted(root.rglob(args.glob))

    changed = []
    for p in files:
        text = p.read_text(encoding="utf-8")
        new_text, did_change = strip_export_header(text)
        if did_change and new_text != text:
            changed.append(p)
            if not args.dry_run:
                p.write_text(new_text, encoding="utf-8")

    print(f"Scanned: {len(files)} files")
    print(f"Would change: {len(changed)} files" if args.dry_run else f"Changed: {len(changed)} files")
    for p in changed:
        print(str(p))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

