#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

LINK_RE = re.compile(r"!{0,1}\[[^\]]*\]\(([^)]+)\)")

def is_external(target: str) -> bool:
    return target.startswith('http://') or target.startswith('https://') or target.startswith('mailto:')

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'book')
    broken = []
    for p in root.rglob('*.md'):
        if '.legacy.' in p.name:
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        for m in LINK_RE.finditer(text):
            href = m.group(1)
            if is_external(href):
                continue
            # strip anchors
            path_part = href.split('#',1)[0]
            if not path_part:
                continue
            candidate = (p.parent / path_part).resolve()
            if not candidate.exists():
                broken.append((str(p), href))
    if broken:
        print('Broken links found:')
        for src, href in broken:
            print(f"- {src} -> {href}")
        sys.exit(1)

if __name__ == '__main__':
    main()
