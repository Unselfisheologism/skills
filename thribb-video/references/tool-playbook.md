# Tool playbook: Manim CE, ManimGX, Anatomy and HyperFrames

Use this with references/staged-production.md. It says which of the four tools does which job in a build, and what to read before you touch each one. Install details, flags and tested limits stay in references/engines-and-tooling.md and references/tooling/upstream-skills.md. This file does not repeat them.

Docs read on 18 Oct 2026 from the repos' own files. Nothing here was rebuilt or rendered again today. The earlier tooling checks (what rendered, what install was blocked) are in references/tooling/verification.json and still stand.

## The rule: read the tool's own docs before you author

Each of these tools changes quickly and has its own contract. Writing from memory of "how Manim works" is the common failure. Before you write scene code, open the doc named below for the tool you chose, and write down in `spec.md` which doc you read.

## Who does what

| Tool | Use it for | Do not use it for |
| --- | --- | --- |
| Manim Community (https://github.com/ManimCommunity/manim, docs https://docs.manim.community) | Maths scenes where objects keep their identity while a quantity changes: graphs, equations, transformed grids. Also the reference for the Scene, `play` and `wait` model that ManimGX copies. | Study of Grant's own scene files (that is his ManimGL branch, a different API). Do not report a CE render as tested if you only ran GX. |
| ManimGX (https://github.com/academa-labs/manimgx, docs https://manimgx.academa.ai) | The same kind of maths scenes through a Manim CE compatible Python API, with a GPU renderer and a browser option. Its repo ships its own agent skill at `skills/manimgx/SKILL.md`, an `inspect` step, and a gallery of runnable examples. | A claim that CE and GX behave identically because the names match. Voiceover defaults that call a paid service. |
| Anatomy (https://github.com/wheresryan22/anatomy) | A figure where a physical object's working is the explanation: a gauge, a rig, a lock. Standalone SVG or HTML with a shared model, controls and optional WebGL. Best on a page; in a video use stills or a `setTime` refactor (references/production-contract.md). | Decorating an abstract argument with machinery. A diagram where arrows and boxes already say it. |
| HyperFrames (https://github.com/heygen-com/hyperframes, docs https://hyperframes.heygen.com) | Assembling the video: HTML and SVG scenes, rendered Manim or GX clips, captions, narration, transitions, and the final render. | Mathematics itself. Use it to put maths clips together, and keep the numeric model in your facts file. |

A normal build is one maths engine (CE or GX) for the maths shots, optionally Anatomy for a physical metaphor, and HyperFrames to assemble. Do not use all four on one short video.

## Read first, per tool

### Manim CE
- Version-matched docs: https://docs.manim.community/en/stable/ and the repo's `example_scenes`. Open the example nearest your scene before you write.
- No official agent skill file was found in the repo. Do not invent one.
- Earlier install attempt was blocked on native Pango headers, and no CE render was done. Say so if you recommend CE and have not rendered one yourself.

### ManimGX
- Read `skills/manimgx/SKILL.md` in the repo, then the doc page for any feature you have not used. Do not guess a feature from CE.
- Use its `inspect` step on a draft before you export. Check frame count after export (an export frame-count issue is recorded in the tooling notes).
- Look in its `examples/` folder for the nearest scene, such as the linear maps, derivative or complex maps examples, and adapt the method, not the content.

### Anatomy
- Read the repo's `SKILL.md` first. It says the object is the explanation, and points to eight complete examples. Open the closest one.
- Then the references it names: `references/craft.md`, `kit.md`, `motion.md`, `verify.md`. Its checks need Node 20.10 or newer and Chrome.
- Run its verify loop on your figure. A figure that builds is not a figure that reads at phone size.

### HyperFrames
Read the docs that match the job, not just the quickstart. In the repo's `docs/` folder:

- `concepts/` (compositions, data-attributes, determinism, frame-adapters, variables) before your first composition.
- `prompting/storyboards.mdx` for the plan format used with stage 3: one arc, one direction block every frame inherits, and a light spec per frame.
- `prompting/visual-specs.mdx` and `prompting/specification-dial.mdx` for how much to pin down. Pin technique choices and the order of simultaneous events in words.
- `prompting/recreating-references.mdx` for stage 1 when you match a reference: transcribe the motion with timestamps, then correct one axis at a time with absolute values.
- `prompting/iterating.mdx` for stage 5: one variable per edit, layer one element type at a time, strip back and re-layer when a scene misfires.
- `prompting/explainers.mdx`, `guides/faceless-explainer.mdx` and `guides/general-video.mdx` for explainer workflows. The repo's `skills/` folder has matching workflow skills (`faceless-explainer`, `general-video`, `motion-graphics`) plus `hyperframes-core`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli` and others, listed in references/tooling/upstream-skills.md.
- `guides/gsap-animation.mdx`, `guides/rendering.mdx` and `guides/troubleshooting.mdx` when you animate, render or debug.
- `reference/lint-rules.mdx` and `reference/html-schema.mdx` when a check complains.

The docs themselves warn that lint and check verify structure, not quality, and that a build can pass every gate and still read as sparse. Watch the render. Their quoted percentages ("roughly 90% of a reference") are their own observations, not something to repeat as a promise.

## Where each tool plugs into the six stages

| Stage | Manim CE / ManimGX | Anatomy | HyperFrames |
| --- | --- | --- | --- |
| 1 spec.md | Note which engine and which nearest example you will follow. | Name the physical object, if any, and the nearest shipped example. | Transcribe the reference's motion with timestamps (recreating-references). |
| 2 facts.json | Every number the scene draws comes from here. | Every dimension and readout comes from here. | Text, counts and timings read from here. |
| 3 story.md | The beat's "Needs on screen" line names the shot. | Name the figure the beat needs. | Write the plan as arc, direction block, per-frame spec (storyboards). |
| 4 scene code | Write the scene, draft at low quality, inspect (GX) or render (CE), view stills. | Build the figure, run its verify loop. | Build the composition from clips and HTML, run `check`, take snapshots at your cue times. |
| 5 timing | Durations as named values at the top of the scene. | Control and motion timing in its model, not wall clock. | One timing source; edit one variable per render. |
| 6 review | Stills of first, middle and final states. | Close-ups at phone size. | Decoded final frames, not the preview page. |

## What stays unverified

- No build was made with this combination under the staged workflow.
- Manim CE: only the install attempt was recorded, which was blocked. Anatomy WebGL and 3D modes were not tested. HyperFrames and ManimGX renders were checked in earlier tooling checks, not rebuilt for this change.
