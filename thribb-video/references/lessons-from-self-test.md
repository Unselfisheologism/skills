# Lessons from building one explainer with this skill

Source: one self-application build (a narrated video about this skill). Observed once, in one project. Not a learner test, and the narration was never listened to by the author; only timing was checked.

## Cueing visuals to narration
- Generate the narration first, get actual durations, then time the scene to them. Never time narration to a drawn scene.
- Cue each visual by a unique spoken phrase and look up that phrase's start time in a word-level ASR of the audio. Fail the build if a phrase occurs twice (a first-match cue once fired a counter on the wrong "one, two, three").
- Anticipation is allowed (showing an object a few seconds after announcing it) but mark it deliberate.
- Do not claim a sync tolerance you did not measure. Measure: frame-difference around each planned cue and report the offset; list cues with no detectable change as unmeasured. The one build here saw 0 to 0.62 s on detectable cues.
- ASR is only a timing aid. It says nothing about prosody or tone.

## Legibility (judge at about 390 px frame width)
- Render a downscaled frame at 390 px wide and read it. At 1280x720 base, 6-10 px text at that width was not readable; scaling all text by about 1.35 helped but the smallest formula line stayed small.
- A roadmap or progress label is a teaching element: 30 pt at 720p, active item highlighted and underlined, inactive at about 0.7 opacity.
- Do not hide teaching in soft subtitles; whatever must be read goes on screen.

## Show decisions, not lists
- Review of "attempt vs rebuild" works as two side-by-side thumbnails with row verdicts, not a bullet list.
- A say/show/why table with a mini diagram for one row beats a paragraph of tool advice. Reveal each column when its name is spoken.
- Tools not actually rendered in the build must be labelled so on screen.

## Claims
- Avoid blanket statements ("induction is weak", "every frame", "3 s sync"). Contrast "correct but unmotivated" instead of caricaturing.
- A palette is a consistent choice per piece, not a law; color terms in formulas by the object they name.
