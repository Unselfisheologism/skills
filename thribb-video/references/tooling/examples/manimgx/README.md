# Tested ManimGX geometry examples

Original sources. Tested with manimgx0.1.1 and Python3.14.7.

```sh
uv venv --python 3.14 .venv
uv pip install --python .venv/bin/python 'manimgx==0.1.1'
.venv/bin/manimgx inspect gx_shear.py ShearPreservesArea -t 0.9,2,4,5,6,7.5,end
.venv/bin/manimgx render gx_shear.py ShearPreservesArea -r 960x540 --fps 24 -o gx-shear.mp4
```

This is a silent renderer/geometry smoke test, NOT a complete lesson, not a measured learning improvement, and not evidence of a creator's exact articulation. A general proof needs the all-heights argument, not only one highlighted slice.

The raw render's static tail was not a conventional constant-FPS stream. See `references/engines.md` for observed counts and the tested explicit CFR derivative. Probe your output rather than assuming the CLI's FPS statement certifies the encoded frame count. Never discard narration when adapting the silent normalization recipe.
