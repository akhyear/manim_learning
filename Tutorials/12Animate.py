from manim import *

class Animate(Scene):
    def construct(self):
        square= Square().set_fill(RED, opacity=1)
        self.add(square)

        self.play(square.animate.set_fill(GREEN), run_time= 3)
        # self.wait(1.5)

        self.play(square.animate.shift(UP*3), run_time=3)
        self.wait(1)

# manim -pql 12Animate.py animate