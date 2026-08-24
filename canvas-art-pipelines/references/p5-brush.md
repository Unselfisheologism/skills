# p5.brush — verified usage notes (p5 build, p5.js 2.x)

Lessons from a real render-to-PNG session (2026-08). The README's Quick Start
understates the pitfalls; these were all hit live and worked around.

## Setup

```html
<script src="https://cdn.jsdelivr.net/npm/p5@2/dist/p5.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/p5.brush@latest"></script>
```

- Requires p5.js **2.x** and `createCanvas(w, h, WEBGL)`. P2D silently does nothing useful.
- CDN scripts do NOT load when the HTML is opened via `file://` (page loads but
  `typeof brush === 'undefined'`). Download `p5.min.js` + `p5.brush.js` locally, or
  serve over `python -m http.server`.
- jsDelivr's bare `p5@2/dist/p5.min.js` path can 404 ("Couldn't find the requested
  file") — use cdnjs for p5 itself.
- All brush drawing functions must be called as `brush.xxx()` — there are no bare
  globals for `flowLine`, `hatch`, `spline`, etc. A bare `flowLine(...)` throws
  ReferenceError mid-sketch.

## CRITICAL: paint inside draw(), never only in setup()

In WEBGL mode p5 clears the drawing buffer at the start of every draw pass.
A one-shot image painted in `setup()` + `noLoop()` ends up **blank white**.

## Verified library quirks (current build)

- **`brush.circle` throws** (`v is not defined`) on large diameters — roughly when the
  circle spans a canvas corner/edge region (~d ≥ 1800–2000 on a 1920×1280 canvas,
  exact threshold depends on position). For full-width washes/gradients use stacked
  translucent `brush.rect` bands instead of giant circles.
- **Custom vector fields crash**: any sketch using `brush.addField(...)` +
  `brush.field(name)` + `flowLine`/`Position.moveTo` dies with
  `Cannot read properties of undefined (reading 'N')` inside the library. Built-in
  fields (`hand`, `curved`, `zigzag`, `waves`, `seabed`, `spiral`, `columns`) work.
  Workaround for wind-bent strokes: noise-bent `brush.spline` segments.
- `brush.polygon(0,0,points)` has an undocumented signature (`t.map is not a function`
  with a plain points array) — use `brush.beginShape()` / `brush.vertex()` /
  `brush.endShape(CLOSE)` instead.
- No brush `ellipse` primitive; use a thin wide `rect` or circles.
- Working calls verified: `set`, `fill(col, alpha)`, `noStroke/noFill`,
  `rect`, `circle` (moderate size), `line`, `spline(points...)`, `hatch(spacing, angle)`
  + shape, `beginShape/vertex/endShape(CLOSE)`.

## Debugging a blank canvas (headless / browser automation)

`canvas.toDataURL()` and `getContext('webgl').readPixels()` return blank/black even
when the canvas LOOKS fine on screen (preserveDrawingBuffer is false by default).
Reliable verification paths:

1. Instrument the sketch: try/catch around paint, stash errors + success flag on
   `window.__dbg`, then eval it from the automation session.
2. Read pixels synchronously *during* the paint pass (inside draw, before the frame
   ends): copy GL rows into a 2D canvas via putImageData, or count non-background
   pixels per band with readPixels row-by-row.
3. Best export: call `saveCanvas('name','png')` from the page (eval it) — downloads
   the true framebuffer content to Downloads. Verify file size > ~100KB for a real image.

## Known-good scene recipe (orchard example)

Layer order: paper background → sky (stacked alpha rect bands) → ground (filled quads
via beginShape/vertex) → trees far-to-near sorted by baseY → grass blades (noise-leaned
splines) → foreground details → thin ink border rect. Per tree: 3–4 layers of
translucent canopy circle lobes (dark→light), highlight lobe, charcoal trunk line +
spline branches, hatch+rect bark, small fruit circles. Seed with randomSeed/noiseSeed;
repaint variants by bumping the seed and re-running the paint pass.
