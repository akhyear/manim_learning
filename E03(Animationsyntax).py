from manim import*

class Animationsyntax(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity = 0.5)
        s = Square(color=YELLOW, fill_opacity = 0.5).next_to(c,LEFT)

        self.add(c,s)
        self.play(c.animate.shift(UP*3))
        self.play(s.animate(rate_functions=linear).shift(RIGHT*4))
        self.play(VGroup(s,c).animate.arrange(RIGHT))
        self.play(c.animate.shift(RIGHT).scale(2))
        self.wait()