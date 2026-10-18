---
name: thribb-notes
description: Write an illustrated article or set of study notes in the teaching style studied from the 3Blue1Brown lesson pages - concrete seed, exercises with pause-and-reveal, figures bound to the prose by color, motivated notation, honest caveats - with figures made in Anatomy, Manim/ManimGX or plain SVG. Use for illustrated notes, lesson pages, written companions to a video. Original wording and figures only; never copy lesson text or artwork.
---

Naming: "thribb" is the owner's independent name for this skill. It is not an official 3Blue1Brown product, not endorsed by that channel, and not a quality or parity guarantee. The method was studied from public material; see references/evidence-and-coverage.md for what was and was not reviewed.

# Illustrated notes in the style of a great visual teacher

This folder is self-contained. Read [references/shared/articulation-playbook.md](references/shared/articulation-playbook.md) first (the same articulation rules as the video skill; copied here so nothing depends on a sibling folder), then [references/shared/visual-grammar.md](references/shared/visual-grammar.md). Engine setup lives in [references/shared/engines-and-tooling.md](references/shared/engines-and-tooling.md). The shared files are verbatim copies from thribb-video and may mention it; ignore those mentions. This skill covers what changes on the page: [page patterns](references/page-patterns.md), [figures and engines](references/figures-and-engines.md), [review rubric](references/review-rubric.md), [coverage](references/evidence-and-coverage.md), and a [sample note](samples/staircase-note/note.html).

## Evidence limits (read first)
- Lesson site: 176 lesson URLs, fetched text read for all 176. 62 have an article body; 114 are embed stubs or interactive tools. Do not generalize from stubs.
- Browser review of the official site (exact counts in references/evidence-and-coverage.md): 176 of 176 probed (inventory only); 7 articles viewed in depth plus 4 more with body screenshots; 3 interactive pages viewed by screenshot and 1 read as text only; interactions exercised: Reveal, multiple-choice Check, one stepper. Patterns below come from that subset.
- Guest and team-written lessons are tagged separately and not used for core-style claims.
- Captions and page text cannot tell you tone of voice. Do not claim to know how anything sounds.
See references/evidence-and-coverage.md.

## Workflow
1. One idea, one reader, one sentence: "After this page the reader can ___."
2. Seed: a picture or puzzle visible above the fold. Text before the first figure stays short.
3. Draft as discovery: smallest case, naive attempt, failure, fix, general statement. Name things after what the reader just saw.
4. Mark 1-3 decision points as exercises (references/page-patterns.md): figure, prompt, notepad space, reveal with a worked answer that has its own small figure.
5. Make figures (references/figures-and-engines.md). Same palette, same object, same meaning of each color across the page. Principle written on the figure in the color of where it is used.
6. Put caveats in the open: what you simplified, where the full version is.
7. Review with references/review-rubric.md. View every figure as an image at reading width. Do not report ready from file existence.

For larger pages, run the same steps as six small jobs that each leave one file (spec.md, facts.json, outline.md, figures, a page-edits file, review.md) so a wrong result is fixed at the file that caused it. See references/staged-notes.md. Before you author, read references/tool-playbook.md: it says what Anatomy, ManimGX, Manim CE and HyperFrames each do on a page and which of their own docs to read first. That method comes from a public practitioner post about video, adapted here for the page, and has not been tested by a build here. Related third-party skills and their licenses: references/tooling/related-skills.md (read-only review, none installed or run).

## Page rules
- Light reading column, dark figure canvases. Figures full column width, captioned in one line.
- Equations: color-match terms to the figure parts they name. Box or arrow only the entries that change between steps.
- Linked panels get plain-word labels, not symbols alone.
- Prose-only stretches are fine when no picture would add anything. Do not decorate.
- A check question never leaks the answer on a wrong try. Solutions appear after an attempt.
- Interactives: labelled axes, a small number of controls (stepper, draggable handle, reset), live readout of the quantity being discussed. Make a static fallback figure and say what the control does.
- Credits and sources at the top, paraphrase only for anything you cite.

## Hard rules
No copied passages or artwork. No claim of having watched or heard what was not inspected. Do not publish transcripts, screenshots or raw captions from the source. Original sample: samples/staircase-note.

## Lessons from a self-test build
See references/lessons-from-self-test.md (single build, no learner test).
