from manim import *

'''class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        # dot2 = dot.copy().shift(RIGHT)
        # self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        # self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        # self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.play(MoveAlongPath(dot, line), run_time=2, rate_func=linear)
        self.wait()'''

class PointMovingOnshape(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        dot = Dot()

        line = Line([3,2,0],[5,1,0])

        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(line,LEFT))
        self.play(MoveAlongPath(dot,circle),run_time=3)
        self.play(MoveAlongPath(dot,line),run_time=3)
        self.wait()


# manim -pql 4PointMovingOnShape.py PointMovingOnShape