#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

CH_FILE_RE = re.compile(r"^ch(\d{2})-", re.IGNORECASE)
H1_RE = re.compile(r"^#\s*(?:CHAPTER|Chapter|chapter)?\s*(\d+)?\s*[:\-–—]?\s*(.*)$")

def derive_title_from_slug(fname: str) -> str:
    base = os.path.basename(fname)
    # remove prefix chNN-
    m = CH_FILE_RE.match(base)
    tail = base
    if m:
        tail = base[m.end():]
    tail = tail.rsplit('.',1)[0]
    words = tail.replace('_','-').split('-')
    # keep common acronyms uppercase
    acronyms = {"ai":"AI","web3":"Web3","ipfs":"IPFS"}
    titled = []
    for w in words:
        titled.append(acronyms.get(w.lower(), w.capitalize()))
    # touchup common possessives
    s = ' '.join(titled)
    s = s.replace('Founders', "Founder's")
    return s

def normalize_h1(path: Path) -> bool:
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        lines = f.read().splitlines()
    if not lines:
        return False
    mfile = CH_FILE_RE.match(path.name)
    if not mfile:
        return False
    chnum = int(mfile.group(1))
    first = lines[0]
    mh1 = H1_RE.match(first)
    if mh1:
        title = mh1.group(2).strip()
        if not title:
            title = derive_title_from_slug(path.name)
    else:
        # if first line is a heading but not matching, strip leading '#'
        if first.startswith('#'):
            title = first.lstrip('#').strip()
        else:
            # inject a new H1 above current first line
            title = derive_title_from_slug(path.name)
            lines.insert(0, f"# Chapter {chnum}: {title}")
            with path.open('w', encoding='utf-8', newline='') as f:
                f.write('\n'.join(lines) + ('\n' if lines and not lines[-1].endswith('\n') else ''))
            return True
    new_h1 = f"# Chapter {chnum}: {title}"
    if first != new_h1:
        lines[0] = new_h1
        with path.open('w', encoding='utf-8', newline='') as f:
            f.write('\n'.join(lines) + ('\n' if lines and not lines[-1].endswith('\n') else ''))
        return True
    return False

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'book')
    changed = False
    for p in sorted(root.rglob('ch[0-9][0-9]-*.md')):
        if normalize_h1(p):
            print(f"normalized H1: {p}")
            changed = True
    if changed:
        sys.exit(1)

if __name__ == '__main__':
    main()

