# Linting and Validation

- Sanitize encoding/control characters: `python3 scripts/sanitize_markdown.py`
- Normalize chapter headings: `python3 scripts/normalize_headings.py`
- Regenerate SUMMARY from files: `python3 scripts/generate_summary.py`
- Check local links: `python3 scripts/check_links.py`

These scripts are used in CI to keep structure consistent and prevent drift.

