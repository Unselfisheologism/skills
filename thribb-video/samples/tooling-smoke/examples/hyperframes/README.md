# Tested local HyperFrames geometry example

Original source. Node22, hyperframes0.8.168, gsap3.14.2, system Chrome, local FFmpeg. No narration/text, no hosted assets, no login/cloud render/publication. Keep these distinctions when adapting it.

```sh
npm install --ignore-scripts
npm run prepare-assets
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1
# Optional, if choosing an existing browser:
export HYPERFRAMES_BROWSER_PATH=/path/to/chrome
npm run check
npm run render
ffprobe -v error -show_streams -show_format hf-area.mp4
```

The strict check actually ran a browser and had no findings across5 sample times. It checked0 text elements, so this does NOT prove text contrast/accessibility. No motion-sidecar assertions were enabled. The MP4 had640x360,15/1 FPS,60 frames,4.000s; sampled decoded frames were visually inspected. It used software screenshot capture, not a hardware speed benchmark.

The horizontal yellow segment retains its length while sliding during the shear. This tiny clip has no complete spoken/written derivation and is a renderer smoke test, not the final teaching-skill validation.

GSAP is not vendored here. `prepare-assets` copies it from the explicitly installed package for deterministic local rendering. Respect its package license if distributing the copied asset.
