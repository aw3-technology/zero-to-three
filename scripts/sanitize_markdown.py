#!/usr/bin/env python3
import os, sys

ALLOWED = {"\n", "\r", "\t"}

def sanitize_file(path: str) -> bool:
    with open(path, 'rb') as f:
        data = f.read()
    try:
        s = data.decode('utf-8')
    except UnicodeDecodeError:
        # attempt best-effort decode and re-encode
        s = data.decode('utf-8', 'ignore')
    changed = False
    out_chars = []
    for ch in s:
        if ord(ch) < 32 and ch not in ALLOWED:
            changed = True
            continue
        out_chars.append(ch)
    out = ''.join(out_chars)
    if changed:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(out)
    return changed

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else 'book'
    changed_any = False
    for r, _, files in os.walk(root):
        for name in files:
            if name.endswith('.md'):
                p = os.path.join(r, name)
                if sanitize_file(p):
                    print(f"sanitized: {p}")
                    changed_any = True
    if changed_any:
        sys.exit(1)

if __name__ == '__main__':
    main()

