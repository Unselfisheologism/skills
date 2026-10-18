# Making the figures

Pick by operation, not by taste.
- Static stepwise diagrams (most figures): plain SVG written by hand or script, exported to PNG; or Anatomy-style diagrams if that skill is available. Fast to inspect and fix.
- Geometry or algebra that moves (a piece slides, flips, recolors): ManimGX (validated: inspect, render, storyboard) or Manim CE; export a still per step or a short loop. Probe the video, normalize frame rate if needed, then extract the frames you want.
- Clean timed motion or HTML-native figures: HyperFrames (validated by the tooling check, strict browser run had 0 findings).
- Evidence ownership: a tooling specialist validated ManimGX and HyperFrames renders and runtime-smoked Anatomy (its output was faint). fframes and Manim CE were never rendered. Test before relying on them.
- Never use a paid text-to-speech option by default. Notes need no audio.
Palette: black figure canvas, a small fixed set of colors with one meaning each (for example blue = the thing you are counting, orange = its copy, red = the failed attempt, yellow = the quantity being asked). Keep contrast readable at column width. Check by viewing the exported PNG.
Interactives: only build when a static figure cannot show the dependence. Provide a static fallback.

Detailed per-engine setup, install notes, validated versions and caveats (Anatomy, ManimGX, HyperFrames, fframes, Manim CE) live in references/shared/engines-and-tooling.md. Read the section for the engine you pick. Anatomy is a skill and geometry kit for mechanical or isometric figures, good for article figures; do not publish to its community gallery without a separate user decision.
