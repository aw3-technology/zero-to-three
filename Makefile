.PHONY: sanitize normalize summary links check

sanitize:
	python3 scripts/sanitize_markdown.py

normalize:
	python3 scripts/normalize_headings.py

summary:
	python3 scripts/generate_summary.py

links:
	python3 scripts/check_links.py

check: sanitize normalize summary links

