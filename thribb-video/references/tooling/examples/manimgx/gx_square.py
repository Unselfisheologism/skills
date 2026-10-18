import manimgx as m

class EqualAreas(m.Scene):
    def construct(self):
        square = m.Square(side_length=2, color=m.BLUE, fill_opacity=0.25)
        label = m.MathTex(r"A = 2^2 = 4").next_to(square, m.DOWN, buff=0.4)
        self.play(m.Create(square), run_time=1)
        self.play(m.Write(label), run_time=1)
        self.wait(1)
