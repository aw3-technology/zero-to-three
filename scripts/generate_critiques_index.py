#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

CRIT_RE = re.compile(r"^critique-(\d{2})-.*\.md$")

def read_h1(path: Path) -> str:
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.startswith('# '):
                    return line.strip('# ').strip()
    except Exception:
        pass
    return path.stem

def find_chapter_path(book_dir: Path, num: int) -> str | None:
    patt = f"ch{num:02d}-"
    for part in sorted(book_dir.glob('part-*')):
        for cf in part.glob(f"{patt}*.md"):
            return f"../{part.name}/{cf.name}"
    return None

def main():
    crit_dir = Path('book/critiques')
    book_dir = Path('book')
    items = []
    for p in sorted(crit_dir.glob('critique-*.md')):
        m = CRIT_RE.match(p.name)
        if not m:
            continue
        num = int(m.group(1))
        h1 = read_h1(p)
        ch_path = find_chapter_path(book_dir, num)
        items.append((num, h1, p.name, ch_path))

    lines = []
    lines.append('# Critiques Index')
    lines.append('')
    lines.append('Purpose: one critique per chapter to guide targeted revisions. Each entry links to the original chapter and its critique.')
    lines.append('')
    for num, h1, fname, ch_path in items:
        # Try to extract title from h1 like "Critique — Chapter NN: Title"
        title = h1
        parts = h1.split(':', 1)
        if len(parts) == 2:
            title = parts[1].strip()
        ch_label = f"Chapter {num}: {title}" if title else f"Chapter {num}"
        ch_link = ch_path if ch_path else '#'
        lines.append(f"- {ch_label} — [Chapter]({ch_link}) • [Critique]({fname})")

    out = '\n'.join(lines) + '\n'
    (crit_dir / 'README.md').write_text(out, encoding='utf-8')
    print('critiques/README.md updated')

if __name__ == '__main__':
    main()

