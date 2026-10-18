# Evidence and coverage ledger (as of 2026-10-18; update before publishing)

Per-item rows: coverage-ledger.csv. Tag meanings: source-key.md. Verification of tools: tooling/verification.json (written by the tooling specialist).

## Channel corpus (246 ids: 153 videos, 83 Shorts, 10 streams)
- English captions fully read: 220 (149 punctuated, 71 auto). 26 ids have no local transcript.
- Frame sheets viewed: 50 items, 356 sheets. Frame sampling only: no motion, no audio.
- No frame review: 196 ids. Of these, 54 were stopped by YouTube's bot check (blocked-by-access, not unavailable); the rest have no local frames. All 196 are UNKNOWN for visuals, not covered.
- Audio: none inspected. No prosody, pacing, tone or music claims anywhere. Captions cannot establish them.
- Guest, collaboration, live-lecture and team-authored items were tagged and kept out of core-style claims.

## Lessons site (176 lesson URLs)
- Fetched text read in full: 176. With article body: 62. Metadata or embed pages: 114 (112 embed stubs, plus 2 interactive tools; 4 interactive-only pages in total).
- Browser inventory (DOM probe plus top screenshot, not viewing): 176 of 176 (gaussian-convolution rerun succeeded). All 114 metadata pages confirmed in a rendered browser (77 or fewer words before the footer).
- Actually viewed in screenshots: 7 articles in depth (sphere-area, quick-eigen, mlp, fourier-transforms, windmills, taylor-series, fourier-series), plus extra body shots of 4 more in a second batch; interactive pages newtons-fractal, hilbert-curve, fourier-series-montage viewed; holomorphic-dynamics page text only. Treat patterns as seen on this subset of the 62.
- Interactions exercised: Reveal/Hide (sphere-area), multiple-choice Check/Try Again/Reset (quick-eigen), Roots stepper (newtons-fractal). Not exercised: draggable handles, most other widgets, embedded video playback.

## Engines (owner of evidence)
- ManimGX and HyperFrames renders validated by the tooling specialist; Anatomy runtime-smoked (output faint at phone size); Manim CE and fframes never rendered; ManimGL untested.

## Samples written for this skill (all silent, original; no speech means no articulation validation)
- samples/staircase-render: ManimGX, 46.04 s, 24 fps, 1105 frames after normalizing the variable-frame-rate raw file with a held tail; layout check 29 samples no problems; frames from 29 s to 45.9 s decoded and viewed, including the row-k argument. Renderer and sequence test only.
- samples/hyperframes-odd-squares: HyperFrames 0.8.168, 20.0 s, 15 fps, 300 frames; strict check browserSkipped false, layout 0 findings, contrast 25/25; frames viewed.
- samples/original-script-staircase-sum.md: long-form script and storyboard, unrendered.
- samples/staircase-narration-timing.md: narration table, untested with any voice. The staircase videos are silent (no speech); they carry on-screen text only.

Quote policy: paraphrased techniques only; no captions, screenshots or lesson text reproduced.

## Added 2026-10-18: staged workflow and related skills (not from the 3Blue1Brown corpus)

references/staged-production.md, references/motion-timing-starters.md and references/tooling/related-skills.md (and references/tool-playbook.md, which draws on the tools' own repos and docs) come from a different source than the channel and lesson-site study: two public X posts by @francescoinweb3 (https://x.com/francescoinweb3/status/2111393917899808880 and https://x.com/francescoinweb3/status/2108882188624121896) and the article linked from the second. The posts and article were read in full through api.fxtwitter.com. The listed repos had license and description checked through the GitHub API, and a few READMEs read; none was installed, run or used to render anything here. The staged method itself has not been tested by a build. The corpus coverage figures above are unchanged by this addition: they describe the 3Blue1Brown study only.
