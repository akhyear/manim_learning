'''class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen'''

from manim import *

class SquareandCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED,opacity=1)

        square = Square()
        square.set_fill(GREEN, opacity=1)

        square.next_to(circle,RIGHT,buff=0.5)
        self.play(Create(circle),Create(square))

        # manim -pql square_and_circle.py SquareandCircle