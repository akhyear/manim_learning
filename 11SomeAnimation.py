from manim import*

class SomeAnimation(Scene):
    def construct(self):
        circle = Circle(color=None).shift(LEFT*3)
        square = Square(color=None)
        triangle = Triangle(color=None).shift(RIGHT*3)

        circle.set_stroke(WHITE, width=20)
        square.set_fill(RED, opacity=1)
        triangle.set_fill(GREEN, opacity=0.5)

        #Animation
        self.play(FadeIn(circle,square,triangle))
        self.play(Rotate(triangle, angle=2*PI))
        self.play(Rotate(square, angle=2*PI))
        self.play(FadeOut(circle,square,triangle))


# manim -pql 11SomeAnimation.py SomeAnimation