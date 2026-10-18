# From reasoning to rendered proof

This reference is a neutral implementation bridge. The corpus-derived teaching skill should supply its teaching principles and source evidence separately.

## Shared scene specification

Before coding a scene, write these fields:

- `claim`: exactly what the viewer should infer.
- `prerequisites`: what the viewer must already understand.
- `initial_state`: visible objects and what each means.
- `operation`: the mathematical or causal change, not merely an entrance animation.
- `invariant`: what is preserved and why.
- `proof_states`: first state, intermediate states, final state and any counterexample.
- `narration_cue`: original words tied to that change, with intended pause.
- `model`: equations/data/functions that drive geometry, labels and readout together.
- `timing`: explicit seconds or frame ranges; source of duration.
- `fallback`: what a reader sees with animation/JS/GPU disabled.
- `checks`: numerical tests plus visual/audio checks.

Example: a horizontal shear `(x,y) -> (x+k*y,y)` preserves each horizontal slice's length and vertical spacing. The determinant of its matrix is1. A visual should show the same slice sliding, not resize it or replace it with an unrelated line. Do not infer a general integral/area theorem from only a single highlighted slice without explaining why the same property holds at every height.

## Composition routes

### Math video

1. Keep a renderer-neutral numeric model.
2. Author mathematical objects in the chosen Manim branch/GX.
3. Export a short diagnostic clip, then inspect initial/intermediate/final states.
4. Export narration separately from an approved voice/recording path. Never clone a person's voice as a shortcut.
5. Align meaningful changes to words or explicit cues; test audio-video timing, not only total duration.
6. Either finish in the math engine or place rendered clips into HyperFrames/fframes. Avoid unnecessary transcoding layers.

### Article/notes

1. Write a complete argument that works without autoplay.
2. Use a static SVG or sharp PNG for each conceptual state, with useful alt text and a caption that states the inference.
3. Use an interactive Anatomy figure when a physical mechanism genuinely explains the concept. Make every displayed value and moving part share one model.
4. Optionally add GX WebGPU playback or a small video, but retain static fallback and visible controls.
5. A sequence of stills is often better than a loop that hides the decisive step.
6. Verify at390px and a desktop width, keyboard-only, reduced-motion, no-JS/static path and print/PDF if that is a target. Check text/figure contrast independently of overflow.

### Anatomy into a video

Anatomy's normal live loops and pointer controls are not automatically seek-safe video. Options:

- Render static SVG/PNG states and animate them in HyperFrames or fframes.
- Refactor the pure model and drawing update into `setTime(t)`/`setState(state)`, with no wall clock or input dependence. Register that deterministic runtime through the composition's supported adapter, then verify arbitrary forward/backward seeks.
- Capture a real interaction only when the interaction itself is the lesson, and label the footage as a capture.

Do not simply iframe a realtime page and assume each video frame will reproduce the same state. Dynamic HTML export, screenshot, and source SVG are different delivery types.

### Math clips into HyperFrames

- Use verified MP4 dimensions, duration, FPS and audio status.
- Keep media timing on the `<video>` or its wrapper, not both.
- Use explicit source offsets for trims. Carry object continuity across cuts, or make the change of representation clear.
- Keep narration captions and geometry labels distinct. Do not cover the very object the sentence names.
- Verify final encoded frames at the same cue times as the math-engine render.

### SVG states into fframes

- Prefer generated geometry from the numeric model or self-contained vector assets.
- Prepare media/fonts before rendering; avoid file I/O/heavy computation in each frame.
- Keep scene-relative and global clocks explicit.
- Check a sharp frame export for font substitution and unsupported SVG features.
- Do not assume arbitrary HTML/CSS/JS from Anatomy or HyperFrames is accepted by the SVG renderer.

## Verification ladder

Keep these claims distinct:

1. Source/API inspected.
2. Environment installed.
3. Code executed.
4. Artifact rendered.
5. Actual pixels inspected at stated moments and sizes.
6. Audio actually assessed, or only numerically/transcript checked.
7. Teaching claim validated for correctness.
8. A learner can use the explanation without its author filling gaps.

A successful command proves only the rung it reaches. A contact sheet cannot prove every frame smooth; a waveform cannot establish vocal tone; a transcript cannot prove pronunciation; a layout linter cannot prove a diagram's inference.

## Release checks

- Numerical model/invariants checked, including edge/counterexample states.
- Units, signs, domains and boundary assumptions explicit.
- Labels track their objects; color is not the only way to identify meaning.
- No meaningless stock motion, misleading geometry or unearned equation jump.
- Text readable at final viewing size, including fine lines/gray details.
- First frame, transition neighborhoods, proof states, and final readable hold inspected.
- Codec, dimensions, duration, rational FPS, frame count and audio streams probed.
- Raw render and any CFR/resize/transcode derivative separately named.
- Article fallback works without animation, GPU, sound or hover.
- Editable sources, dependency versions/lockfile, source provenance and licenses accompany the result.
- Known limitations remain attached to the output rather than buried in a log.
