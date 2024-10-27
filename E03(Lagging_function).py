from manim import*

from manim import ManimColor as Color

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=Color.from_hsv((j/90, 1.0, 1.0)), fill_opacity=0.8) for j in range(20)])
# The Color.from_hsv(h, s, v) method allows you to define a color based on 
# its Hue, Saturation, and Value (Brightness) components
        squares.arrange_in_grid(4,5).scale(0.5)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.25))