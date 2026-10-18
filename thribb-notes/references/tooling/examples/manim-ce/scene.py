import manim as m

class AreaExample(m.Scene):
    """Untested CE adaptation. No successful CE install or render in verification."""
    def construct(self):
        title = m.Text("A slant changes shape, not area", font_size=32).to_edge(m.UP)
        a, b, c, d = (-2, -1, 0), (1, -1, 0), (1, 1, 0), (-2, 1, 0)
        region = m.Polygon(a, b, c, d, color=m.BLUE, fill_opacity=0.3)
        slice0 = m.Line((-2, 0, 0), (1, 0, 0), color=m.YELLOW, stroke_width=6)
        length = m.MathTex(r"\text{each horizontal slice has width }3", font_size=30).to_edge(m.DOWN)
        self.play(m.Write(title), m.Create(region), run_time=1)
        self.play(m.Create(slice0), m.Write(length), run_time=1)
        sheared = m.Polygon(a, b, (2.3, 1, 0), (-0.7, 1, 0), color=m.BLUE, fill_opacity=0.3)
        slice1 = m.Line((-1.35, 0, 0), (1.65, 0, 0), color=m.YELLOW, stroke_width=6)
        self.play(m.Transform(region, sheared), m.Transform(slice0, slice1), run_time=3, rate_func=m.linear)
        conclusion = m.MathTex(r"A = \text{base}\times\text{height} = 3\times 2 = 6", font_size=34).to_edge(m.DOWN)
        self.play(m.Transform(length, conclusion), run_time=1)
        self.wait(2)
