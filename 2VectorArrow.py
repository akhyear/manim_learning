''''from manim import *

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)'''

from manim import*

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow= Arrow(ORIGIN,[3,3,0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0,0)').next_to(dot,DOWN)
        tip_text = Text('(3,3)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane,dot, arrow, origin_text, tip_text )

# manim -pql 2VectorArrow.py VectorArrow