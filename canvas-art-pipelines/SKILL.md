---
name: canvas-art-pipelines
description: "Use when generating artwork as code, e.g. p5.js sketches."
version: 1.0.0
license: MIT
metadata:
  hermes:
    tags: [creative-coding, p5js, webgl, generative-art, verification]
---

# Canvas Art Pipelines

Use when generating an image/artwork **as code** (user says "don't use image_generate,
write code"), when a sketch uses third-party canvas libraries (e.g. p5.brush), or when
verifying a canvas render headlessly.

## Hard-won rules

1. **Paint inside `draw()`.** In p5 WEBGL mode the buffer is cleared at the start of
   every draw pass; one-shot painting in `setup()` + `noLoop()` yields blank white.
   Pattern:
   ```javascript
   let painted = false;
   function draw() {
     if (painted) return;
     painted = true;
     try { paint(); } catch (e) { window.__dbg = String(e); }
     noLoop();
   }
   ```
2. **Instrument before shipping.** Wrap the paint pass in try/catch stashed on
   `window.__dbg` — library errors otherwise vanish invisibly in headless checks.
3. **CDN scripts don't load over `file://`.** Either download the lib files next to the
   HTML or serve via `python -m http.server` (background=true) and open localhost.
4. **Verify pixels, not assumptions.** `canvas.toDataURL()`/`readPixels()` after the
   frame returns black/blank (preserveDrawingBuffer=false). Reliable checks:
   row-by-row `readPixels` executed *during* the paint pass, counting non-background
   pixels per band; final export via `saveCanvas('name','png')` evaluated from the page.
5. **Library APIs need prefixes and exact signatures** — e.g. all p5.brush calls are
   `brush.xxx()` (`brush.hatch`, `brush.spline`, `brush.flowLine`); bare globals throw
   mid-sketch. Read the library's README via its raw/CDN URL before writing code.
6. Third-party libs have sharp edges: see `references/p5-brush.md` for verified
   p5.brush quirks (large-circle crash, broken custom vector fields) and a known-good
   scene recipe.

## Workflow

1. Fetch/read the target library's docs (raw.githubusercontent README works well).
2. Write one self-contained HTML; keep local copies of CDN scripts beside it.
3. Serve locally if needed; load in browser; check `window.__dbg`.
4. Verify pixel content per screen band; iterate on any crash until paintOk=true.
5. Export full-res PNG via `saveCanvas()` from the page; confirm file lands on disk.
