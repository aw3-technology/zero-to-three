#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

PART_RE = re.compile(r"^part-(\d{2})-(.+)$")

ROMAN = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'
}

def pretty_part_title(folder: str) -> str:
    m = PART_RE.match(folder)
    if not m:
        return folder
    n = int(m.group(1))
    raw = m.group(2)
    words = raw.replace('_','-').split('-')
    acronyms = {"ai":"AI","web3":"Web3"}
    titled = [acronyms.get(w.lower(), w.capitalize()) for w in words]
    s = ' '.join(titled)
    s = s.replace('Founders', "Founder's")
    return f"Part {ROMAN.get(n, str(n))}: {s}"

def read_h1(path: Path) -> str:
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.startswith('# '):
                    return line.strip('# ').strip()
    except Exception:
        return None
    return None

def main():
    book_dir = Path('book')
    parts = []
    for entry in sorted((book_dir).iterdir()):
        if entry.is_dir() and entry.name.startswith('part-'):
            parts.append(entry)

    lines = []
    lines.append('# Zero to Three')
    lines.append('')
    lines.append('## Table of Contents')
    lines.append('')

    # Front matter files if present
    for name in ['00-preface.md', '01-prologue.md', '02-introduction.md']:
        p = book_dir / name
        if p.exists():
            h1 = read_h1(p) or name.rsplit('.',1)[0].replace('-', ' ').title()
            title = h1.split(':',1)[0]
            lines.append(f"### [{title}]({name})")
            lines.append('')

    lines.append('---')
    lines.append('')

    for part in parts:
        lines.append(f"## {pretty_part_title(part.name)}")
        lines.append('')
        ch_files = sorted(part.glob('ch[0-9][0-9]-*.md'))
        for cf in ch_files:
            h1 = read_h1(cf) or cf.name
            lines.append(f"* [{h1}]({part.name}/{cf.name})")
        lines.append('')

    # Tail matter
    for name in ['97-epilogue.md', '98-appendix.md', '99-acknowledgments.md']:
        p = book_dir / name
        if p.exists():
            h1 = read_h1(p) or name.rsplit('.',1)[0].replace('-', ' ').title()
            title = h1.split(':',1)[0]
            lines.append(f"### [{title}]({name})")
            lines.append('')

    # Case studies section if exists
    cs_dir = book_dir / 'case-studies'
    if cs_dir.exists():
        for fn in sorted(cs_dir.glob('*.md')):
            if fn.name.lower().startswith('readme'):
                continue
            h1 = read_h1(fn) or fn.stem.replace('-', ' ').title()
            lines.append(f"### [{h1}]({cs_dir.name}/{fn.name})")
        lines.append('')

    new_summary = '\n'.join(lines) + '\n'
    out_path = book_dir / 'SUMMARY.md'
    orig = out_path.read_text(encoding='utf-8', errors='ignore') if out_path.exists() else ''
    if orig != new_summary:
        # backup legacy
        legacy = book_dir / 'SUMMARY.legacy.md'
        if out_path.exists() and not legacy.exists():
            legacy.write_text(orig, encoding='utf-8')
        out_path.write_text(new_summary, encoding='utf-8')
        print('SUMMARY.md updated')
        sys.exit(1)

if __name__ == '__main__':
    main()

