from manim import *
from manim import ManimColor as Color

class HSVColorExample(Scene):
    def construct(self):
        for j in range(6):
            circle = Circle()
            circle.set_color(Color.from_hsv(j / 5, 1.0, 1.0))
            circle.shift(RIGHT * j)
            self.add(circle)
