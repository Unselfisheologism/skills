import manimgx as m

S = 0.85
BLUE_C, ORANGE_C = m.BLUE, m.ORANGE
X0, Y0 = -1.7, 1.6   # center of top-left cell

def cell(c, r, color, x0=X0, y0=Y0, op=0.55):
    return m.Square(side_length=S, color=color, fill_opacity=op, stroke_width=2).move_to((x0 + c*S, y0 - r*S, 0))

def blue_cells(): return [cell(c, r, BLUE_C) for r in range(4) for c in range(r+1)]
def orange_cells(x0=X0): return [cell(c, r, ORANGE_C, x0) for r in range(4) for c in range(r+1, 5)]

def say(t, color=m.WHITE, size=34, edge=m.UP):
    return m.Text(t, font_size=size, color=color).to_edge(edge)

class TwoStaircases(m.Scene):
    """Original silent sample: two staircases make a rectangle, then n. Statements appear only after what they describe is on screen."""
    def construct(self):
        title = say("How many blocks in this staircase?")
        blue = m.VGroup(*blue_cells())
        self.play(m.Write(title), m.Create(blue), run_time=2)
        count = m.MathTex(r"1+2+3+4=\;?", font_size=48, color=m.YELLOW).to_edge(m.DOWN)
        self.play(m.Write(count)); self.wait(2)
        # naive attempt
        gap = m.VGroup(*[cell(c, r, m.RED, op=0.15) for r in range(4) for c in range(r+1, 4)])
        self.play(m.Create(gap))
        t2 = say("Too many: 4 x 4 = 16 counts the red ones", m.RED, 30)
        self.play(m.Transform(title, t2)); self.wait(2)
        self.play(m.FadeOut(gap))
        # twin appears away from the staircase, fits, THEN the claim
        t3 = say("Make a copy, turn it upside down", m.WHITE, 32)
        twin = m.VGroup(*orange_cells(X0 + 4.8))
        self.play(m.Transform(title, t3), m.Create(twin))
        self.play(twin.animate.shift(m.LEFT*4.8), run_time=3, rate_func=m.linear)
        t4 = say("It fits with no gaps and no overlap", m.WHITE, 32)
        self.play(m.Transform(title, t4)); self.wait(2)
        # labelled dimensions
        right = X0 + 4*S + S/2; top = Y0 + S/2; bottom = Y0 - 3*S - S/2; left = X0 - S/2
        wb = m.Brace(m.Line((left, bottom, 0), (right, bottom, 0)), m.DOWN)
        wl = m.MathTex("5", font_size=44, color=m.YELLOW).next_to(wb, m.DOWN, buff=0.1)
        hb = m.Brace(m.Line((left, top, 0), (left, bottom, 0)), m.LEFT)
        hl = m.MathTex("4", font_size=44, color=m.YELLOW).next_to(hb, m.LEFT, buff=0.1)
        self.play(m.FadeOut(count), m.Create(wb), m.Create(hb), m.Write(wl), m.Write(hl))
        eq = m.MathTex(r"4\times 5 = 20", font_size=48, color=m.YELLOW).to_edge(m.DOWN)
        self.play(m.Write(eq)); self.wait(2)
        t5 = say("Two equal staircases: each is half", m.WHITE, 32)
        half = m.MathTex(r"20 \div 2 = 10", font_size=48, color=m.YELLOW).to_edge(m.DOWN)
        self.play(m.Transform(title, t5), m.Transform(eq, half))
        self.play(twin.animate.set_fill(ORANGE_C, opacity=0.2), run_time=1)
        self.wait(2)
        # general n: keep the rectangle, relabel the sides, formula stays tied to the picture
        self.play(twin.animate.set_fill(ORANGE_C, opacity=0.55), m.FadeOut(eq))
        self.play(*[o.animate.shift(m.UP*0.75) for o in (blue, twin, wb, hb, wl, hl)])
        t6 = say("Nothing special about 4: n rows, n+1 columns", m.WHITE, 32)
        wl2 = m.MathTex("n+1", font_size=44, color=m.YELLOW).move_to(wl)
        hl2 = m.MathTex("n", font_size=44, color=m.YELLOW).move_to(hl)
        self.play(m.Transform(title, t6), m.Transform(wl, wl2), m.Transform(hl, hl2))
        # row-k argument: every row of the rectangle has n+1 blocks
        rowbox = m.Rectangle(width=5*S, height=S, color=m.YELLOW, stroke_width=6).move_to((X0 + 2*S, Y0 - S + 0.75, 0))
        rk = m.MathTex(r"\text{row } k:\; k + (n+1-k) = n+1", font_size=40, color=m.YELLOW).move_to((0,-2.4,0))
        ex2 = m.MathTex(r"\text{row } 2:\; 2 + 3 = 5", font_size=40).move_to((0,-3.2,0))
        self.play(m.Create(rowbox), m.Write(rk)); self.wait(1)
        self.play(m.Write(ex2)); self.wait(3)
        self.play(m.FadeOut(rowbox, rk, ex2))
        f1 = m.MathTex(r"2\,(1+2+\cdots+n) = n\,(n+1)", font_size=42, color=m.YELLOW).move_to((0,-2.4,0))
        f2 = m.MathTex(r"1+2+\cdots+n = \frac{n\,(n+1)}{2}", font_size=46).move_to((0,-3.2,0))
        self.play(m.Write(f1)); self.wait(2)
        self.play(m.Write(f2)); self.wait(4)
