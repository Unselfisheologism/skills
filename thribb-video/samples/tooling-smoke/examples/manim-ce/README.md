# Untested Manim Community recipe

`scene.py` is an original adaptation of the GX geometry test, but it was NOT rendered in CE. Installation of0.22.0 failed because pangocairo development metadata was absent. This directory is not a successful CE test.

After setting up the chosen version's documented native dependencies:

```sh
uv venv --python 3.14 .venv
uv pip install --python .venv/bin/python 'manim==0.22.0'
.venv/bin/manim -ql scene.py AreaExample
.venv/bin/manim -s scene.py AreaExample
```

Inspect final artifact pixels and mathematical geometry before using it. Do not substitute ManimGL commands/imports into this project.
