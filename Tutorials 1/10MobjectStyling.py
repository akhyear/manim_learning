from manim import*
class MobjectStyling(Scene):
    def construct(self):
        circle = Circle(color=None).shift(LEFT*3)
        square = Square(color=None)
        triangle = Triangle(color=None).shift(RIGHT*3)

        circle.set_stroke(WHITE, width=20)
        square.set_fill(RED, opacity=1)
        triangle.set_fill(GREEN, opacity=0.5)

        self.add(circle,square,triangle)
        self.wait(3)

# manim -pql 10MobjectStyling.py MobjectStyling

