# Zero to Three — Style Guide

- Headings: Use `# Chapter NN: Title` for chapter H1. Use `##` and below for subsections. Avoid all-caps like `CHAPTER`.
- Filenames: `chNN-kebab-case-title.md` within `book/part-XX-kebab-case-part-name/`.
- Parts: Directory names `part-XX-name`, where `XX` is two digits. Part titles auto-derived in SUMMARY.
- Punctuation: Use a colon after chapter number. Keep titles concise; avoid trailing punctuation in H1.
- Encoding: UTF-8 only; no control characters. Run `scripts/sanitize_markdown.py` to clean.
- Links: Prefer relative links to other chapters. Use file-relative paths. Avoid dead links; verify with `scripts/check_links.py`.
- Cross-refs: Refer to chapters as “Chapter NN: Title” and link to the file.
- Assets: Place images under `book/assets/` and link relatively.
- Voice: Prefer actionable, structured sections over essay-style blocks. Use consistent tone and specificity.

