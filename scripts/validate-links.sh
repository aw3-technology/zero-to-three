#!/bin/sh
set -eu

root=${1:-book}
code=0

echo "Checking markdown links under $root…"
find "$root" -type f -name '*.md' | while read -r file; do
  grep -oE '\[[^\]]+\]\([^)]+\)' "$file" 2>/dev/null | while read -r link; do
    # Extract target path (ignore anchors and external links)
    target=$(echo "$link" | sed -E 's/^.*\]\(([^)#]+)(#[^)]+)?\).*$/\1/')
    echo "$target" | grep -Eq '^https?://' && continue
    path=$(dirname "$file")/"$target"
    # Normalize path (basic)
    norm=$(cd / && cd "$(dirname "$path")" 2>/dev/null && pwd)/"$(basename "$path")"
    if [ ! -e "$norm" ]; then
      echo "Broken link: $file -> $target" >&2
      code=1
    fi
  done || true
done

exit $code
