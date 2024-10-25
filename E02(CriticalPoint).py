from manim import*
class CriticalPoint(Scene):
    def construct(self):
        circle = Circle(color=RED, fill_opacity = 0.5)
        self.add(circle)

        for d in [(0,0,0), UP, LEFT, RIGHT, DOWN, UL, UR, DL, DR]:
            self.add(Cross(scale_factor=0.2).move_to(circle.get_critical_point(d)))

        sq = Square(color = GREEN, fill_opacity=0.5)
        sq.move_to([1,0,0], aligned_edge=LEFT)
        # মানে square এর LEFT crtical point  এর সাথে align করে থাকবে  [1,0,0]
        self.add(sq)