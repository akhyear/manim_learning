# from manim import *

# class DifferentRotations(Scene):
#     def construct(self):
#         left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
#         right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
#         self.play(
#             left_square.animate.rotate(180), right_square.animate.rotate(360), run_time=2
#         )
#         self.wait()

from manim import *

class DifferentRotation(Scene):
    def construct(self):
        left_square = Square(color=RED, fill_opacity=0.7).shift(3*LEFT)
        right_square = Square(color= GREEN, fill_opacity=0.7).shift(2*RIGHT)
        self.play(
            left_square.animate.rotate(90), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()
# manim -pql DifferentRotation.py DifferentRotations