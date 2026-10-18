# Sources and licensing notes

Inspected2026-10-17. Commits below identify inspected repositories, not necessarily the exact build of a registry package. Only repository roots and source URLs actually obtained from the sources are listed.

| Project | Source | Inspected commit | Version context | License context |
|---|---|---|---|---|
| Manim CE | https://github.com/ManimCommunity/manim | `b31c77e181d57d66ba30baa617328afaf52eb061` | 0.22.0 | MIT |
| ManimGL | https://github.com/3b1b/manim | `fafa083a4fb274bba9cabde0b6e2f50ba6da0622` | not installed | MIT |
| ManimGX | https://github.com/academa-labs/manimgx | `cfd33af5aa7cc0d6aa7dfe13919744e2124629dc` | 0.1.1 | MIT source; compound bundled-dependency notices |
| Anatomy | https://github.com/wheresryan22/anatomy | `e9488296a44211c42701ff71705b7901470ec78f` | repository skill | MIT |
| HyperFrames | https://github.com/heygen-com/hyperframes | `c4440dfb200def5e0c0afee938778f05b5985039` | 0.8.168 | Apache-2.0 |
| fframes | https://github.com/dmtrKovalenko/fframes | `44745c09a6c8c51071609097326a820cf59d087b` | 1.2.0 manifest; not installed | MIT source; codec/dependency terms separate |

## Source files used

- Manim CE: README.md, pyproject.toml, LICENSE, LICENSE.community.
- ManimGL: README.md, example_scenes.py, requirements.txt, LICENSE.
- ManimGX: README.md, pyproject.toml, skills/manimgx/SKILL.md, browser/README.md, browser/package.json; docs/content/user-guide/coming-from-manim-ce.md and sound-and-voice.md; rendering and scene source consulted for static holds; LICENSE and third-party notice list.
- Anatomy: README.md, SKILL.md, LICENSE, examples/dial-indicator/build.mjs and built themes; kit and verification reference signatures, capture script. Other feature references are mapped but not all optional shader/3D recipes were run.
- HyperFrames: README.md, package manifests, LICENSE, skills-manifest.json; all ten core SKILL.md entries and faceless-explainer/SKILL.md; minimal composition, CLI lint/check/snapshot and preview/render references; structure lint, browser and telemetry policy source; docs/guides/skills.mdx.
- fframes: README.md, Cargo manifests, LICENSE.txt; skills/fframes-video/SKILL.md and API/design/audio references; generator templates.

## Additional documentation and source leads

- https://docs.manim.community/en/stable/installation.html
- https://docs.manim.community/en/stable/faq/installation.html
- https://manimgx.academa.ai/user-guide/coming-from-manim-ce/
- https://manimgx.academa.ai/user-guide/sound-and-voice/
- https://manimgx.academa.ai
- HyperFrames web documentation at /developers/skills returned CRAWL_NOT_FOUND. Do not use that URL as evidence. The inspected repository file docs/guides/skills.mdx is the detailed skill-installation source.
- https://fframes.studio (homepage identified by repository; do not infer its hosted editor was tested).
- https://crates.io/crates/fframes (package-registry search evidence for stable1.2.0; not a successful local install).
- https://docs.rs/crate/fframes/latest/source/Cargo.toml (package-registry documentation search evidence, not proof latest API and main are identical).

## License handling

This handoff contains original implementation guidance and tiny original examples, not wholesale upstream skill copies, source-video frames, transcripts, or a vendored renderer. Repository licenses do not grant blanket rights to a creator's videos, artwork, voice, logos, every bundled font or unrelated media.

- If copying or adapting substantial MIT source/skills/kit examples, retain their copyright and MIT notice with the copied material.
- If vendoring HyperFrames source or skills, preserve the Apache2.0 license and applicable notices; mark substantial modifications as required. Do not relabel upstream text as wholly original.
- ManimGX's top-level MIT file is not the full distribution license story. Its pyproject lists bundled FFmpeg/x264, fonts and other components under several licenses, including GPL/LGPL and font-specific terms. Keep the relevant upstream notice bundle when distributing those components.
- fframes' MIT source license does not replace FFmpeg/codec/font/media obligations; examine selected build features before distributing binaries.
- GSAP is installed from its npm package by the example setup, not vendored here. Respect that package's license if the generated local JS asset is distributed.
- Generated output rights depend on inputs/assets and applicable law; do not claim that using an MIT engine makes all input media reusable.
- Choose/preserve the destination repository's license for the newly authored material. This guide is not legal advice and does not silently change that repository's licensing.

## Not tested

No hosted media providers, voice cloning, TTS, audio mixing, cloud render/deployment, Anatomy gallery publish, GitHub publication, GX browser player, Anatomy shaders/3D, fframes compilation/editor, or ManimGL rendering.
