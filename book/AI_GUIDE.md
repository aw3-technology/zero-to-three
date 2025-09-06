# AI Collaboration Guide — Zero to Three

Purpose: Provide clear context, structure, and style rules so AI collaborators can propose focused, high‑quality edits without drifting from the book’s intent.

## 1) Canonical Thesis and Scope
- Thesis: In the AI × Web3 era, the entrepreneurial journey extends beyond “Zero to One” into community, governance, and ecosystem stewardship. Founders evolve from creators to system leaders.
- Scope: Practical, systems‑minded guidance for builders operating across AI, crypto, and internet‑native organizations.
- Promise: Useful mental models, actionable playbooks, and living resources that keep pace with fast change.

## 2) Audience and Voice
- Audience: Founders, operators, technical PMs, protocol designers, researchers, and policy‑adjacent readers.
- Assumed baseline: Software fluency; basic crypto/AI concepts; curiosity about governance and incentives.
- Reading level: Clear, precise, and concise; avoid hype and unexplained jargon.
- Voice: Practical, systems‑thinking, ethically aware; confident but humble; evidence‑seeking; avoids absolutism.

## 3) Repository and File Layout
- Entry points: `book/README.md` (Introduction), `book/preface.md`, `book/SUMMARY.md` (TOC).
- Parts: `book/part-*` directories hold chapters; each part has an `index.md` overview.
- Chapters: Use filenames `chapter-XX-kebab-title.md` within the relevant `part-*` directory.
- Assets: Prefer Mermaid inside Markdown. If exporting images, place under `book/assets/figures/` with `fig-<part><chapter>-<slug>.svg` and include alt text + caption.
- Links: Use relative links between book files; absolute URLs for external sources.

## 4) The Zero → Three Framework (Cheat Sheet)
- ZERO — Foundation: Mindset, asymmetric insight, resilience, differentiated thinking.
  - Goal: Generate non‑obvious, high‑conviction theses; build personal capacity under uncertainty.
- ONE — Creation: Product, protocol, or service that solves a real problem.
  - Goal: Validated architecture, reliable MVP, defensible advantage (data/model/market).
- TWO — Traction: Community, trust, governance, and network effects.
  - Goal: Sustainable contributor pathways, incentive alignment, decentralization roadmap.
- THREE — System Leadership: Platforms, standards, and ecosystems where others build.
  - Goal: Stewardship, protocol evolution, multi‑stakeholder alignment, durable value.
- Recursion: Founders cycle across stages; mastery is knowing where to focus when.

## 5) Writing Guidelines (Do / Don’t)
- Do: Define terms on first use; add short, concrete examples; quantify when feasible; show tradeoffs; cite primary sources; use active voice; keep paragraphs short.
- Don’t: Hype; make unverifiable claims; redefine common terms without notice; overuse neologisms; duplicate points.
- Style: Prefer “you” when giving guidance; use present tense; keep headings descriptive; limit nested lists; avoid lorem and placeholders longer than one line.
- Ethics: Flag risks, privacy implications, and governance concerns. Avoid prescriptive claims where evidence is weak; present options and constraints.

## 6) Web3 × AI Terminology (House Definitions)
- Web3: Decentralized infrastructure enabling user ownership, verifiable state, programmable incentives.
- DAO: Internet‑native organization coordinating via on‑chain rules and off‑chain social norms.
- Token economics: Mechanisms that allocate rights, rewards, and responsibilities among participants.
- LLMs/Multimodal AI: Systems that generate/interpret text, code, images, etc., and can plan/act with tools.
- System leadership: Stewardship that enables others to innovate—via standards, governance, and platforms.

## 7) Chapter Template (Markdown)
```
# <Chapter Title>

One‑sentence outcome promise: what the reader can do after this chapter.

## Why It Matters
- The problem, in one paragraph.

## Core Concepts
- Concept A: short definition + when to use.
- Concept B: short definition + when to use.

## Practical Playbook
- Step 1: Action → expected signal.
- Step 2: Action → expected signal.
- Pitfalls: 2–4 common mistakes and mitigations.

## Example
- A concise, realistic scenario (2–4 paragraphs) with numbers where possible.

## Tools and Further Reading
- Links to primary sources, repos, standards, and key papers.
```

## 8) Figures and Diagrams
- Prefer Mermaid blocks for portability and reviewability.
- Include a one‑line caption and brief alt text description.
- If exporting to SVG, commit to `book/assets/figures/` and reference relatively.

## 9) Citations, Links, and QR Codes
- Use in‑text links to primary sources. For stats, prefer official dashboards, whitepapers, or peer‑reviewed work.
- Add a brief parenthetical qualifier for uncertain or changing data (e.g., “as of 2025‑Q1”).
- QR codes: Include `[QR: <slug>]` placeholders; generation occurs at publishing time.

## 10) Editing Tasks — How To
- Add a new chapter:
  - Create `book/part-<n>-<slug>/chapter-XX-<slug>.md` using the template.
  - Update `book/SUMMARY.md` with a relative link in the correct section.
- Revise an existing section:
  - Keep diffs minimal and scoped; preserve headings and anchors.
  - Summarize rationale at the top of the PR or commit message.
- Add a figure:
  - Start with Mermaid inside the chapter. Export to SVG only if needed for layout.

## 11) Quality Checklist (Pre‑PR)
- Clarity: Each section answers “who, what, why, how” in 2–5 lines.
- Evidence: Claims have a source or are clearly framed as opinion.
- Cohesion: Terms match house definitions; cross‑links added where helpful.
- Utility: At least one actionable step or diagnostic per major concept.
- Brevity: Remove repetition; trim hedging words; prefer concrete verbs.
- Accessibility: Define jargon on first use; add alt text for figures.

## 12) AI Guardrails
- Retrieval: When citing facts or numbers, propose a source; if uncertain, label as directional and request confirmation.
- Consistency: Maintain the framework vocabulary (Zero/One/Two/Three) and house definitions.
- Scope: Avoid adding unrelated commentary or speculative detours.
- Safety: Do not generate legal, medical, or financial advice; present options and tradeoffs instead.

## 13) Commit Messages and Structure
- Atomic changes with descriptive messages:
  - `intro: tighten framing on convergence`
  - `part-2: add resilience diagnostic`
  - `fig: add zero→three recursion diagram (mermaid)`
- Keep changes focused; avoid drive‑by edits across multiple parts unless part of a coherent refactor.

## 14) Open Questions and TODOs
- Use `TODO:` inline for small follow‑ups; open an issue for larger research tasks.
- Tag with `[fact-check]`, `[example-needed]`, `[diagram]`, `[case-study]` as appropriate.

---
This guide is a living document. When you encounter recurring patterns or friction, propose an edit here first to keep contributions aligned and predictable.
