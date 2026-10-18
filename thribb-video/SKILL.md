---
name: thribb-video
description: Plan, script, and build a visual explainer video in the teaching style studied from the 3Blue1Brown channel - concrete-first openings, honest simplification, motivated notation, color-bound equations, one persistent diagram - using Manim CE, ManimGX, ManimGL, Anatomy, HyperFrames or fframes as fits. Use when asked for an explainer video, an animated math or science explanation, or a script and storyboard in that style. Original wording and visuals only; never imitate a voice or copy scripts.
---

Naming: "thribb" is the owner's independent name for this skill. It is not an official 3Blue1Brown product, not endorsed by that channel, and not a quality or parity guarantee. The method was studied from public material; see references/evidence-and-coverage.md for what was and was not reviewed.

# Explain it like a great visual teacher (video)

This skill encodes teaching techniques observed in a close reading of the 3Blue1Brown channel and lesson site. It teaches a method. It does not teach you to copy a voice, reproduce a script, or reuse artwork. Everything you write must be original in wording, examples and drawings.

## Read this first: what the evidence does and does not cover

- Evidence base: full English captions of 220 channel items were read end to end, and about 50 items were reviewed as sampled frame sheets (no audio). The lesson site was read and browsed separately.
- Not established: voice, pacing, pauses, tone, music, timing of reveals. Captions carry none of that. When this skill talks about "delivery", it means word choice and structure only. Do not claim to have heard anything.
- About 196 channel uploads have no frame review. Visual claims below come from the reviewed items and from criteria the creator states in the SoME2 results video (https://www.youtube.com/watch?v=cDofhN-RJqg) and other reviewed items. Treat them as strong patterns, not laws.
- Guest, collaboration, live-lecture and team-written items were tagged and kept out of the "core style" claims.
See references/evidence-and-coverage.md for the ledger.

## Review checklist (stated criteria plus a working synthesis)

Source anchors: the four criteria and the warning about over-philosophizing introductions are stated in the SoME2 results video (https://www.youtube.com/watch?v=cDofhN-RJqg); layers-of-abstraction and genre advice appear in the SoME announcement (https://www.youtube.com/watch?v=ojjzXyQCzso). The remaining items below (loud music, audio quality, animate-by-program caution, start niche) are a working synthesis from the reviewed material, not verified single quotes. Use the list as the final review. The four criteria: motivation (why care, at the scale of the whole topic and of each step), clarity, novelty, memorability. Failures to watch for (the first is stated in the SoME2 video, the others are working synthesis): opening with abstract philosophy, loud music under explanation, and formulas handed down with no reason. Working advice list: go from concrete to abstract; spend more effort choosing the topic than polishing it; start niche; pick a genre and honor its obligations (distant explainer, discovery story, worked example, demo); motivate every definition; audio quality matters; animate by program only when the program mirrors the math.

## Workflow

1. Pin the audience and the one idea. Write: "After this, a viewer can ___ and feels ___." If you need two ideas, make two videos or a series.
2. Find the concrete seed: a physical scene, a surprising number, a puzzle with a visible answer, a failed intuition. The seed must be something a viewer can look at in the first ten seconds.
3. Pick the genre (references/articulation-playbook.md, "genres"). It sets what you owe the viewer.
4. Build the argument as discovery. A common arc is smallest case, a naive attempt, why it fails, the fix, then the general statement, but choose the arc the idea needs; a failed attempt is a tool, not a requirement. Notation arrives after the picture it names.
5. Write the script (references/script-template.md) with a visual column beside every line. No line without a thing on screen that carries it.
6. Choose engines (references/engines-and-tooling.md) by the reasoning operation, build at low quality first, check every frame at reading size, then render.
7. Run the review checklist (references/review-rubric.md). Fix, re-render, re-check pixels. Do not report ready from file existence.

For larger builds, run the same steps as six small jobs that each leave one file (spec.md, facts.json, story.md, scene code, timing file, review.md) so a wrong result is fixed at the file that caused it. See references/staged-production.md. Before you author, read references/tool-playbook.md: it says what Manim CE, ManimGX, Anatomy and HyperFrames each do in a build and which of their own docs to read first, including HyperFrames' concepts, storyboard, iterating and recreating-references docs. That method comes from a public practitioner post, not from the 3Blue1Brown study, and has not been tested by a build here. Timing defaults for titles and labels: references/motion-timing-starters.md. Related third-party skills and their licenses: references/tooling/related-skills.md (read-only review, none installed or run).

## Articulation in brief (full detail in references/articulation-playbook.md)

- Open with a thing, not a thesis. Then say plainly what you will do, in one sentence, and give a rough map.
- Voice the viewer's objection before they do ("you might complain that..."), then answer it by building something, not by asserting.
- Invite a pause at a real decision point, and make a prediction beat before a reveal.
- Name caveats yourself. If you are simplifying, say so, say what you glossed, and say where the full version lives.
- Withhold the definition until the viewer has felt the need for it. Name things after the behavior they just saw.
- Use small playful names, and keep them consistent, so a quantity can be referred to in two words later.
- Check the result against a special case or a quick simulation, out loud.
- Close by restating the one takeaway in plain words, and say what you left out.
- Warm, direct address ("you", "we" for shared steps, "I" for opinion, motive and confession). Hedge lightly. Superlatives are rare. Beauty is pointed at, not announced in bulk.
- Credit sources and collaborators by name, on screen and in words.

## Visual grammar in brief (full detail in references/visual-grammar.md)

- One consistent color rule: a color means one thing for the whole video. Equation terms take the color of the object they name in the picture.
- One persistent diagram or table that is filled step by step, with finished parts dimmed and the active part lit.
- Progressive reveal. Never show the finished formula and then explain it. Build it term by term, fading earlier terms.
- Smallest numeric case on screen before the general symbol. Live numeric readouts when something moves.
- A pinned roadmap or checklist, with the current item lit and the rest dimmed, returned to at each stage.
- Show failure: mark a wrong conjecture visibly (a red cross, a "wrong" tag) before the fix.
- A viewer-surrogate character (optional) asks the doubt in a thought bubble. If you use one, make it your own design.
- Real footage or a physical prop only where it makes the phenomenon tangible. Credit it.
- Motion mirrors the math. If a parameter is time, drive it linearly; use easing only for camera and layout.
- Legibility: back-stroke or dark background behind text, readable at phone size, no loud audio under explanation.

## Engines

Choose the simplest engine that can express the essential change. See references/engines-and-tooling.md for install, caveats and the verified limits (a tooling specialist validated ManimGX and HyperFrames renders and runtime-smoked Anatomy; Manim CE install was blocked, ManimGL untested, fframes unrendered, GX export frame-count issue, Anatomy fine detail faint at phone size, GX voiceover defaults to a paid service and must never be used silently).

## Hard rules

- Never reproduce lines from a transcript, lesson or song. Paraphrase techniques; write new examples. No verse or jingle.
- Never imply the original creator made, endorsed or voiced your output.
- Ask before any paid service, account sign-in or credential use. A silent video with on-screen script or captions is the default. If voice is wanted, use a recording the user supplies or a service the user picks.
- Report coverage honestly: what was reviewed, what was only metadata, what is unknown.

## Lessons from a self-test build
See references/lessons-from-self-test.md (single build, no learner test).
