# Tool playbook for pages: Anatomy, ManimGX, Manim CE and HyperFrames

Use this with references/staged-notes.md. It says which of the four tools makes which part of a page, and what to read before you touch each one. Install details, flags and tested limits stay in references/shared/engines-and-tooling.md and references/tooling/upstream-skills.md.

Docs read on 18 Oct 2026 from the repos' own files. Nothing here was rebuilt or rendered again today. The earlier tooling checks (what rendered, what was blocked) are in references/tooling/verification.json and still stand.

## The rule: read the tool's own docs before you author

These tools change quickly and each has its own contract. Writing from memory of "how Manim works" is the common failure. Before you make a figure, open the doc named below for the tool you chose, and write down in `spec.md` which doc you read.

## Who does what on a page

| Tool | Use it for | Do not use it for |
| --- | --- | --- |
| Anatomy (https://github.com/wheresryan22/anatomy) | An interactive isometric figure where a physical object's working is the explanation: a gauge, a rig, a lock. Standalone SVG or HTML, or React, with one shared model for parts, readouts and controls. | An abstract argument that arrows and boxes already say. Decorating a page with machinery. |
| ManimGX (https://github.com/academa-labs/manimgx, docs https://manimgx.academa.ai) | Maths figures and short clips through a Manim CE compatible Python API. Export stills for the page. Its repo ships an agent skill at `skills/manimgx/SKILL.md`. An optional `<manimgx-player>` embeds a scene in a page. | Making the browser player the only explanation: it needs WebGPU and JavaScript. Voiceover defaults that call a paid service. |
| Manim Community (https://github.com/ManimCommunity/manim, docs https://docs.manim.community) | The reference for the Scene, `play` and `wait` model, and for stills of maths scenes. | Study of Grant's own scene files (his ManimGL branch is a different API). Do not report a CE render as tested if you only ran GX. |
| HyperFrames (https://github.com/heygen-com/hyperframes, docs https://hyperframes.heygen.com) | A companion video for the page, or timed HTML and SVG clips, assembled from rendered maths clips, captions and narration. | The page itself, or the mathematics. Keep the numeric model in your facts file. |

A normal page uses one maths engine for its stills, and Anatomy if a physical object really is the explanation. Add HyperFrames only when the page ships a video. Do not use all four on one page.

## Read first, per tool

### Anatomy
- Read the repo's `SKILL.md` first. It says the object is the explanation and points to eight complete examples. Open the closest one before you design.
- Then the references it names: `references/craft.md`, `kit.md`, `motion.md`, `verify.md`. Its checks need Node 20.10 or newer and Chrome.
- Run its verify loop on every figure. An earlier smoke run found fine detail faint at phone size, so check at 390 px and say what is hard to see.
- Keep a still image and a caption for each figure state, so the page still explains without the interactive version.

### ManimGX
- Read `skills/manimgx/SKILL.md` in the repo, then the doc page for any feature you have not used. Do not guess a feature from CE.
- Use its `inspect` step on a draft, then export stills for the page. Look in its `examples/` folder for the nearest scene (linear maps, derivative, complex maps, others) and adapt the method, not the content.
- If you embed the browser player, give the page a meaningful still, a caption and the written argument for readers without WebGPU. Browser rendering was not tested here.

### Manim CE
- Version-matched docs: https://docs.manim.community/en/stable/ and the repo's `example_scenes`. Open the nearest example before you write.
- No official agent skill file was found in the repo. Do not invent one.
- The earlier install attempt was blocked on native Pango headers, and no CE render was done. Say so if you recommend CE and have not rendered one yourself.

### HyperFrames
Read the docs that match the job. In the repo's `docs/` folder:

- `concepts/` (compositions, data-attributes, determinism, frame-adapters, variables) before your first composition.
- `prompting/storyboards.mdx` for a companion video's plan: one arc, one direction block every frame inherits, and a light spec per frame.
- `prompting/visual-specs.mdx` and `prompting/specification-dial.mdx` for how much to pin down.
- `prompting/iterating.mdx` for edits: one variable per edit, layer one element type at a time.
- `guides/faceless-explainer.mdx`, `guides/general-video.mdx`, `guides/rendering.mdx` and `guides/troubleshooting.mdx` for workflow, render and debugging.

The docs themselves warn that lint and check verify structure, not quality, so watch the render.

## Where each tool plugs into the six stages

| Stage | Anatomy | ManimGX / Manim CE | HyperFrames |
| --- | --- | --- | --- |
| 1 spec.md | Name the physical object and nearest shipped example. | Name the engine and nearest example. | Only if the page ships a video. |
| 2 facts.json | Every dimension and readout comes from here. | Every number the figure draws comes from here. | Text and timings read from here. |
| 3 outline.md | The "Needs on screen" line names the figure. | Same. | Plan the video as arc, direction block, per-frame spec. |
| 4 figures | Build, then run its verify loop. | Draft at low quality, inspect (GX), export stills. | Assemble clips, run `check`, snapshot at chosen moments. |
| 5 page edits | Tune controls and captions in the model. | Re-export the one changed still. | One variable per render. |
| 6 review | Close-ups at 390 px. | Stills against `facts.json`. | Decoded final frames. |

## What stays unverified

- No page was built with this combination under the staged workflow.
- Manim CE: only the install attempt was recorded, and it was blocked. Anatomy WebGL and 3D modes and the ManimGX browser player were not tested. HyperFrames and ManimGX renders were checked in earlier tooling checks, not rebuilt for this change.
