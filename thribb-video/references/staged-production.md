# Staged production: six small jobs, one file each

This is a working method for building an explainer video in stages. Each stage ends in one file you can read and check, and the next stage starts from that file. If something looks wrong in the final render, you know which file to fix, and nothing upstream is re-rolled.

Provenance, stated plainly: the six-file shape comes from a public X post by @francescoinweb3 (https://x.com/francescoinweb3/status/2111393917899808880) and the article it points to (https://x.com/i/article/2108867565233614848, "Build Your Own AI Production Studio With Claude"). It is a practitioner's claim of what works for him, not something measured here, and it is not part of the 3Blue1Brown study. Here it is rewritten in original words, with the teaching rules of this skill inside each stage, so you apply them as you go. What was and was not checked is listed at the end.

Which tool does which job, and which of its docs to read first, is in references/tool-playbook.md. Read that before stage 1 and again before stage 4.

## The files

Keep them together in one project folder, in this order.

| Stage | File | One sentence |
| --- | --- | --- |
| 1. Reference | `spec.md` | What the reference does and why it works, plus the rules you will follow. |
| 2. Facts | `facts.json` | Every number or claim the video states, with its source or derivation beside it. |
| 3. Story | `story.md` | One idea, one concrete seed, three beats, before anything moves. |
| 4. Motion | scene code (engine of your choice) | Every frame as code, reading its numbers from `facts.json`. |
| 5. Direct | `timing.*` (any plain config) | All durations, cue times and holds in one place. |
| 6. Review | `review.md` plus rendered stills | Stills checked against spec, facts and the rubric, then the user's approval. |

## Stage 1: reference to `spec.md`

Start from: a video the user likes, or the principles in this skill if there is none.
Do: study it and write down what makes it work: where the first motion lands, how long the opening thing sits before any talk, how labels enter, how often the picture changes, how the payoff is paced. Separate three kinds of line: observed (you can point to it), inferred (a guess about why), and rules for this project.
Rules: sampled frames and captions are enough for visual observations (layout, where the first motion lands, how labels enter, how often the picture changes). They tell you nothing about narration, speech pacing, tone, music or sound, so do not write those into the spec unless you actually heard the reference. Describe, never copy. No lines from its script, no imitation of a voice, no reuse of its artwork. Take the structure, write new content. Add to the spec the visual rules this skill already needs (one color per meaning, one persistent diagram, legible at phone size).
Output: `spec.md`, short enough to reread before every later stage.

## Stage 2: facts to `facts.json`

Start from: the question the video answers.
Do: gather every figure, claim and worked example before animating anything. Next to each, record where it comes from: a link, a formula, or a script that computes it. For maths, the check is a computation (for the staircase sum, 100 x 101 / 2 = 5050), not a memory. Also list assumptions, ranges and what was left out.
Rules: a wrong number animated well is a more convincing wrong number. Do not move on while any figure has no source. Unverified claims stay in the file marked unverified, and the story either drops them or says they are unverified on screen.
Output: `facts.json`, for example `{"id": "total", "value": 5050, "how": "100*101/2, computed in check.py", "status": "verified"}`.

## Stage 3: story to `story.md`

Start from: `spec.md` and `facts.json`.
Do: write the piece as words, with no motion. Name the audience and the sentence "After this, a viewer can ___". Pick the one idea, the concrete seed a viewer can look at in the first ten seconds, and the one hero figure from `facts.json`. Lay out three beats, then add the viewer's likely objection, the visible failure of a naive attempt if the idea needs one, and the caveat you will say out loud. Use references/script-template.md for the visual column.
Rules: write one coherent explanation, and mark every place where the words depend on a picture. Under each beat, add a line "Needs on screen:" naming what the viewer must see for the next sentence to make sense (the staircase filled in, the red cross on the wrong guess). The visual can carry essential reasoning, so do not rewrite a beat just to make it work without one. Do check that no beat depends on a picture you have not listed. If you need a second idea, make a second video.
Output: `story.md`.

## Stage 4: motion to scene code

Start from: all three files above.
Do: build each scene with the scene specification in references/production-contract.md. Read every number, label and position from `facts.json` so a change is made once. Choose the engine by the reasoning operation (references/engines-and-tooling.md). Build a low-quality draft first.
Rules: motion mirrors the maths. Time-like parameters are linear; easing is for camera and layout only. Colors follow `spec.md`.
Output: scene files plus a draft render.

## Stage 5: direct to `timing.*`

Start from: the draft render and the user's notes in plain words.
Do: keep every duration, delay, hold and cue time in one timing file. Turn each plain note into one edit: "the title is a beat late" moves one value; "draw the line slower" changes one duration. Re-render and check the changed cue. Where narration exists, tie each meaningful visual change to a cue and measure per-line duration against the audio.
Rules: one note, one change, one re-render. If a note needs a different picture, go back to stage 4. If it needs a different idea, go back to stage 3.
Output: `timing.*` and a new draft.

## Stage 6: review and approval

Start from: the render.
Do: export stills at the key cues. Check each against `spec.md` (does the first motion land when it should), against `facts.json` (is every number on screen the number in the file) and against references/review-rubric.md. Look at frames at phone size. Write what you checked and what you could not check (audio heard, a learner test) in `review.md`.
Rules: the first export is a draft. Do not call it ready from file existence. Get the user's approval before anything is published or sent.
Output: `review.md`, stills, and the approved render.

## Going back

When a check fails, fix the earliest file that is wrong and redo only the stages after it. A wrong figure goes to `facts.json`, a late title goes to `timing.*`, a confusing order goes to `story.md`.

## What this method does not claim

- It has not been tested by a build of its own. Nobody has made a video with these six stages and then reviewed it with this skill's rubric.
- No one measured that six small jobs beat one large prompt. That is the original poster's experience.
- The study of 3Blue1Brown does not show that the channel works this way. Do not describe the stages as that channel's process.
