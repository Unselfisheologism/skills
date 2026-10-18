# Staged notes: six small jobs, one file each

This is a working method for writing an illustrated article or study notes in stages. Each stage ends in one file you can read and check, and the next stage starts from that file. If the final page is wrong, you know which file to fix.

Provenance, stated plainly: the six-file shape comes from a public X post by @francescoinweb3 about making videos (https://x.com/francescoinweb3/status/2111393917899808880) and the article it points to (https://x.com/i/article/2108867565233614848). It was written for video. Here it is adapted for the page: timing becomes reading order and reveal order, and motion becomes figures. It is one practitioner's claim of what works, it was not measured here, and it is not part of the 3Blue1Brown study. What was and was not checked is at the end.

Which tool does which job, and which of its docs to read first, is in references/tool-playbook.md. Read that before stage 1 and again before stage 4.

## The files

| Stage | File | One sentence |
| --- | --- | --- |
| 1. Reference | `spec.md` | What a page you like does and why it works, plus the rules for this page. |
| 2. Facts | `facts.json` | Every number, claim and worked example, each with its source or computation. |
| 3. Outline | `outline.md` | One idea, one concrete seed, three beats, the pause points and the holes for figures. |
| 4. Figures | `figures/` and `model.*` | One figure per conceptual state, all drawn from the same numbers. |
| 5. Page edits | `page.html` (or the document) and `tune.*` | Order, captions, color map and reveal order in one place. |
| 6. Review | `review.md` plus screenshots | Rendered page checked against spec, facts and rubric, then the user's approval. |

## Stage 1: reference to `spec.md`

Start from: a page or article the user likes, or this skill's page patterns if there is none.
Do: read it and write down what makes it work: what the reader sees first, where the first exercise appears, how a pause-and-reveal is set up, how captions state the inference, how much text sits between figures. Mark each line observed, inferred, or a rule for this page.
Rules: describe, never copy. For a page, what you read is what you can observe; do not claim a reader's experience you did not test. No sentences, figures or layouts reproduced. Add the rules this skill already needs: one color per meaning, figures bound to the prose by color, legible at 390 px.
Output: `spec.md`.

## Stage 2: facts to `facts.json`

Start from: the question the page answers.
Do: collect every figure, claim and example before drawing anything. Record a source, a link or a computation beside each. For maths, run the computation. List assumptions and what was left out.
Rules: a wrong number in a polished figure is a more convincing wrong number. Unverified claims stay marked unverified and are either dropped or stated as unverified on the page.
Output: `facts.json`, for example `{"id": "total", "value": 5050, "how": "100*101/2 computed by script", "status": "verified"}`.

## Stage 3: outline to `outline.md`

Start from: `spec.md` and `facts.json`.
Do: write the page as an outline in words. Name the reader, the sentence "After this, a reader can ___", the concrete seed shown first, the hero figure, and three beats. Mark where each exercise pauses and where its reveal sits. Leave a labeled hole where each figure goes. Add the reader's likely objection and the caveat you will state.
Rules: write one coherent argument, and mark every place where the text depends on a figure. Under each beat, add a line "Needs on screen:" naming what the reader must see for the next paragraph to make sense. Figures can carry essential reasoning, so do not pad the prose to replace one. Do check that no paragraph leans on a figure you have not listed, and that each figure has alt text and a caption that say what it shows. See references/page-patterns.md.
Output: `outline.md`.

## Stage 4: figures

Start from: the outline holes and `facts.json`.
Do: make one figure per conceptual state (references/figures-and-engines.md). Draw every figure from the same numbers, so a change to `facts.json` or the model changes each figure that depends on it. Write alt text and a caption that states the inference.
Rules: a short sequence of stills often beats a loop that hides the decisive step. Colors follow `spec.md`.
Output: the figure files and the model they read.

## Stage 5: page edits to `tune.*`

Start from: the assembled page and the user's notes in plain words.
Do: keep reading order, reveal order, captions and the color map in one place. Turn each plain note into one edit: "the reveal comes too early" moves one block; "this caption is vague" changes one caption. Re-render and check the changed spot.
Rules: one note, one change, one re-render. If a note needs a different figure, go to stage 4. If it needs a different idea, go to stage 3.
Output: the updated page.

## Stage 6: review and approval

Start from: the rendered page.
Do: screenshot at 390 px and at desktop width. Check each against `spec.md`, check every number on the page against `facts.json`, and run references/review-rubric.md. Also check keyboard use, reduced motion and the path with scripts off if the page uses any. Write what you checked and what you could not check (a real reader test) in `review.md`.
Rules: the first render is a draft. Do not call it ready from file existence. Get the user's approval before anything is published or sent.
Output: `review.md`, screenshots, and the approved page.

## Going back

Fix the earliest file that is wrong and redo only the stages after it. A wrong figure goes to `facts.json`, a confusing order goes to `outline.md`, a vague caption goes to `tune.*`.

## What this method does not claim

- It has not been tested by a build of its own. No page has been made with these six stages and then reviewed with this skill's rubric.
- No one measured that six small jobs beat one large prompt. That is the original poster's experience.
- The study of the 3Blue1Brown lesson pages does not show that the site works this way. Do not describe the stages as that site's process.
- The source is about video. The page adaptation is a judgment made here.
