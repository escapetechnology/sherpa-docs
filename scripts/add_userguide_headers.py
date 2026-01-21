#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONT_MATTER_FENCE = re.compile(r"^---\s*$")
TITLE_LINE_RE = re.compile(r"^title:\s*(.+)\s*$")
H1_RE = re.compile(r"^#\s+(.*\S)\s*$")


def parse_front_matter(lines: list[str]) -> tuple[int | None, dict[str, str]]:
    """
    If file starts with YAML front matter, return (end_line_index, kv_dict).
    end_line_index is the index of the closing '---' line (0-based).
    """
    if not lines:
        return None, {}
    if not FRONT_MATTER_FENCE.match(lines[0].strip()):
        return None, {}

    data: dict[str, str] = {}
    end_idx: int | None = None

    for i in range(1, len(lines)):
        if FRONT_MATTER_FENCE.match(lines[i].strip()):
            end_idx = i
            break
        m = TITLE_LINE_RE.match(lines[i].strip())
        if m:
            data["title"] = m.group(1).strip().strip('"')

    return end_idx, data if end_idx is not None else ({}, None)[1]


def extract_title_and_range(text: str) -> tuple[str | None, int | None]:
    lines = text.splitlines(keepends=False)
    if not lines:
        return None, None

    end_idx, fm = parse_front_matter(lines)
    title = None
    end_line_num = None

    if end_idx is not None:
        # front matter present
        end_line_num = end_idx + 1  # 1-based
        title = fm.get("title")

    # fallback to first H1 heading if no title
    if title is None:
        start_search = (end_idx + 1) if end_idx is not None else 0
        for i in range(start_search, len(lines)):
            m = H1_RE.match(lines[i])
            if m:
                title = m.group(1).strip()
                break

    return title, end_line_num


def build_header(path: Path, text: str) -> str | None:
    rel_path = path.as_posix()

    filename = path.name
    num_prefix = filename[:2]
    try:
        nav_order = int(num_prefix)
    except ValueError:
        return None

    title, end_line_num = extract_title_and_range(text)
    if title is None:
        return None

    # If no explicit front matter, we still want a sensible range; default to 1-1
    if end_line_num is None:
        end_line_num = 1

    header = f"@{rel_path}:1-{end_line_num} | title=\"{title}\" | nav_order={nav_order}"
    return header


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="assets/userguide",
        help="Root directory for userguide markdown files",
    )
    parser.add_argument(
        "--glob",
        default="[0-9][0-9]*.md",
        help="Filename glob for numbered userguide files",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only print headers that would be inserted")
    args = parser.parse_args()

    root = Path(args.root)
    files = sorted(root.rglob(args.glob))

    changed = []
    for p in files:
        text = p.read_text(encoding="utf-8")
        header = build_header(p, text)
        if not header:
            continue

        lines = text.splitlines(keepends=True)
        # If header already present and identical, skip
        if lines and lines[0].startswith("@") and header in lines[0]:
            continue

        new_text = header + "\n" + text
        changed.append((p, header))
        if not args.dry_run:
            p.write_text(new_text, encoding="utf-8")

    print(f"Found {len(files)} numbered userguide files")
    print(f"{'Would add' if args.dry_run else 'Added'} headers to {len(changed)} files")
    for p, header in changed:
        print(f"{p}: {header}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

