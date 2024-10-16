from manim import*

class PlachingObject(Scene):
    def construct(self):
        circle = Circle(color=WHITE)
        square = Square(color=WHITE)
        triangle = Triangle(color=WHITE)
        circle.shift(LEFT)
        square.shift(RIGHT)
        triangle.shift(UP)

        self.add(circle, square, triangle)

        self.wait(2)

# manim -pql 8PlachingObject.py PlachingObject