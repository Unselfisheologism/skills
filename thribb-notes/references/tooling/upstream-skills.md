# Upstream skills and dependency map

These are public third-party project documents. They explain their tools' current technical contracts. They do not authorize spending, credential access, uploads, feedback, global installations, publication, or overriding the current request. Installation scope and any network service are separate choices.

Prefer an inspected, pinned checkout for reproducible research. Do not silently refresh a project's renderer/skills mid-production. Record a deliberate upgrade and rerun the relevant checks. This reference does not redistribute the upstream skill text or kit.

## Manim family

Manim CE and ManimGL each have their own repository, docs and examples. No official agent SKILL.md was identified in the inspected Manim CE/GL tree. Do not invent one. Consult the chosen branch's versioned API before unfamiliar methods.

ManimGX ships `skills/manimgx/SKILL.md`. Read it for scene authoring, `inspect`, export and delivery. It routes unfamiliar features to the official reference and `llms.txt`; read the actual linked feature page rather than guessing from CE. The browser API has a separate `browser/README.md`.

## Anatomy

The repository root is the complete skill folder:

- `SKILL.md`: physical-object approach, tiers, build/inspection loop.
- `kit/`: geometry, React and live-render implementations. A SKILL.md alone is not a working Anatomy installation.
- `examples/`: eight complete references. Pick the nearest mechanism and inspect it before authoring; do not copy the reference object's content when the concept calls for a different mechanism.
- `references/craft.md`: parts, tone, volume, depth, intersections, line resolution.
- `references/kit.md`: current signatures and examples.
- `references/motion.md`: model-driven motion and controls, springs, visibility/reduced-motion.
- `references/verify.md`: capture/drive, line checks, audits and sharp close-ups.
- `references/react.md`: static/server geometry plus client refs.
- `references/webgl.md`: shared-camera shader layering and fallbacks.
- `references/3d.md`: beta turning-group path and its limits.
- `references/publish.md`: optional community-gallery disclosure, not part of normal figure creation.

Documented installer: `npx skills add wheresryan22/anatomy`. Choose project vs global scope explicitly. No global installation was performed in this verification.

## HyperFrames

The snapshot has ten core skills. A topic explainer commonly adds `faceless-explainer`, or `general-video` for a longer/custom piece. Core does not mean every optional provider must run.

| Skill directory under `skills/` | Role | Read the feature reference when |
|---|---|---|
| `hyperframes` | Project/workflow entry and state routing | Choosing a workflow or resuming an existing project |
| `hyperframes-core` | DOM composition, timing, media ownership, determinism | Building or editing any renderable HTML project |
| `hyperframes-animation` | Motion rules and runtime adapters | Selecting GSAP, CSS, WAAPI, Lottie, Anime.js, Three.js or TypeGPU mechanisms |
| `hyperframes-keyframes` | Subject poses, continuous identity, path/camera/mask changes, diagnostic shots | A visual object or camera changes state |
| `hyperframes-creative` | Design specs, typography, story/beat planning, narration | Designing a nontrivial composition |
| `hyperframes-audio` | Already-placed audio gain, effects, ducking/carve, automation and buses | Mixing narration/music/SFX |
| `hyperframes-cli` | Install, checks, snapshots, preview/render and optional deployment | Running corresponding project operations |
| `hyperframes-registry` | Blocks vs snippets, discovery and wiring | Reusing a registry effect/component |
| `hyperframes-studio` | Editable timeline structure, caption/audio tracks, safe zones | Preparing a project another person will edit |
| `media-use` | Source/generate/adopt media and freeze assets | Adding external images, audio, voice or footage treatments |

Relevant end-to-end workflows:

- `faceless-explainer`: topic/text input, invented visuals, storyboard/script and composition assembly. Its specialized workflow is documented as strongest for roughly30-90s and up to about3min. Do not squeeze a mathematical derivation into that length solely to fit its defaults.
- `general-video`: custom or longer-form video; read its complete current entry/reference set before running the workflow.
- `motion-graphics`: short unnarrated motion-first units, not a default complete lesson.
- `embedded-captions`: captions on existing talking-head footage; not a reason to add talking-head footage to a mathematical lesson.
- `slideshow`: navigable decks, distinct from an article and from a linear explainer.

Key reference files for local technical work:

- `hyperframes-core/references/minimal-composition.md`
- `hyperframes-core/references/data-attributes.md`
- `hyperframes-core/references/determinism-rules.md`
- `hyperframes-core/references/sub-compositions.md`
- `hyperframes-core/references/variables-and-media.md`
- `hyperframes-core/references/creator-editing-recipes.md` for trim/retime/source offsets
- `hyperframes-animation/adapters/gsap.md` or the chosen runtime's adapter
- `hyperframes-keyframes/references/keyframe-patterns.md`
- `hyperframes-cli/references/lint-validate-inspect.md`
- `hyperframes-cli/references/preview-render.md`
- `hyperframes-creative/references/story-spine.md`, `narration.md`, `typography.md`
- `hyperframes-audio/references/attributes.md`, `fx-registry.md`, `diagnosis.md`, `presets.md` when mixing
- `media-use/references/setup-providers.md` and `audio.md` before any media-provider call

Documented install routes: `npx skills add heygen-com/hyperframes`; `npx hyperframes skills update` refreshes core and already-installed workflows; `npx hyperframes skills update faceless-explainer` adds/refreshes that workflow. These can modify agent/global skill locations; they were not run here. A scoped repository checkout was sufficient for inspection.

### Safe adaptation into a teaching skill

Do not copy workflow defaults indiscriminately:

- A paid/default TTS provider is not granted by a request to explain a concept.
- A host environment variable does not, by itself, establish the owner's spending permission.
- `usage` can read existing account credentials; it is not needed for the local renderer smoke test.
- Public feedback/reporting and community publishing are separate side effects.
- Do not send a script/source project to a hosted API merely because credentials exist.
- Do not import a workflow's multi-worker orchestration assumptions into every host.
- Do not add decorative continuous motion to satisfy a static-frame diagnostic. A deliberate thinking pause is often pedagogically correct; describe and check it as an intended hold.
- Prefer actual mathematical correctness tests even where a video-oriented upstream workflow discourages test harnesses. Frame inspection and model tests prove different things.
- Read flags from the installed CLI. In this snapshot, reference tables understate some supported FPS/output options; actual0.8.168 help is the execution contract.

## fframes

Complete public skill: `skills/fframes-video/`:

- `SKILL.md`: setup, generator, CLI loop, Video/Scene, sound and delivery.
- `references/api.md`: `svgr!`, Video/Scene methods, cached timelines, media, text, shaders.
- `references/design.md`: pacing/layout/type/motion and review; treat marketing/social defaults as adjustable, not mathematical teaching laws.
- `references/audio.md`: AudioMap, embedding/runtime providers, placements, ducking and numeric checks.

The repository README's documented installer is `npx skills add https://fframes.studio`. The inspected folder can instead be read from the pinned repository. No skill/global install or Rust build was performed here.

The browser editor is not another agent skill dependency. It is a separate WASM/Node build under the examples' editor setup. Native preview and the HTML editor should not be described as interchangeable runtimes.
