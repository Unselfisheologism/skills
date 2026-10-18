# fframes recipe, not executed

Rust/Cargo were absent. No compile/render/visual verification was performed. This is a guide for a future compatible machine, not a working-artifact claim.

Start with the actual generator so its media, CLI, renderer and codec features match its resolved release:

```sh
cargo install --locked cargo-fframes
cargo fframes new area-proof --format landscape --fps 30 --backend cpu --yes
cd area-proof
cargo build --release
```

Then retain the generated Video/CLI scaffolding and replace its placeholder content with a subject-specific mathematical scene. Inside its `render_frame` method, a shear model can produce an SVG polygon:

```rust
let k = ((frame.seconds() - 1.0) / 2.0).clamp(0.0, 1.0);
let top_shift = 100.0 * k;
let points = format!(
    "180,270 380,270 {},110 {},110",
    380.0 + top_shift,
    180.0 + top_shift,
);
let slice_shift = 50.0 * k;
// In the generated svgr! tree, preserving its root/canvas and background:
// <polygon points={points} fill="#58c4dd" fill-opacity="0.35"
//          stroke="#58c4dd" stroke-width="3" />
// <path d={format!("M{},190 H{}",180.0+slice_shift,380.0+slice_shift)}
//       stroke="#ffff88" stroke-width="3" fill="none" />
```

This excerpt is not a standalone crate and has not been syntax/type checked. Read the current `skills/fframes-video/references/api.md` for accepted `svgr!` attribute expressions and cached timeline forms. Do not promise that source inspection proves compatibility with a registry release.

Verification once a complete project builds:

```sh
cargo run --release -- timeline
cargo run --release -- inspect
cargo run --release -- strip -n 12
cargo run --release -- frame 0s,2s,end
cargo run --release -- render -o area-proof.mp4
ffprobe -v error -show_streams -show_format area-proof.mp4
```

Inspect actual output PNGs, confirm slice lengths and area numerically, and separately verify audio if added. CPU mode does not offer the GPU native preview. Prefer a supported Skia backend when that capability and its build dependencies are available.
