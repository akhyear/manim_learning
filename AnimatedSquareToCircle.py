'''class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen'''

'''from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square,circle))
        self.play(square.animate.set_fill(PINK, opacity=0.5))'''

# manim -pql AnimatedSquareToCircle.py AnimatedSquareToCircle

from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(circle))
        self.play(circle.animate.rotate(PI/4))
        self.play(Transform(circle, square))
        self.play(circle.animate.set_fill(PINK, opacity=0.5))