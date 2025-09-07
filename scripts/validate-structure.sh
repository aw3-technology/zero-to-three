#!/bin/sh
set -eu

summary=book/SUMMARY.md
root=book

echo "Validating SUMMARY entries map 1:1 to files…"

links=""
grep -oE '\[[^\]]+\]\([^)]+\)' "$summary" | sed -E 's/^.*\(([^)]+)\).*$/\1/' | grep -vE '^(https?://|mailto:)' | while read -r l; do
  links="$links\n$l"
done

missing=0
printf "%b" "$links" | while read -r l; do
  [ -z "$l" ] && continue
  if [ ! -e "$root/$l" ]; then
    echo "SUMMARY references missing file: $l" >&2
    missing=1
  fi
done

echo "Checking each chapter file appears in SUMMARY…"
chapters=$(find "$root"/part-* -type f -name 'ch*.md' | sed -E 's#^book/##' | sort)
for c in $chapters; do
  echo "$links" | grep -qx "$c" || { echo "Chapter missing in SUMMARY: $c" >&2; missing=1; }
done

if [ "$missing" -ne 0 ]; then
  echo "Structure validation failed." >&2
  exit 1
fi
echo "Structure validation passed."
