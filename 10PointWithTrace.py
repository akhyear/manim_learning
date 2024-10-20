from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        # A VMobject can store a series of points,
        # which makes it ideal for drawing paths or shapes.
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
#The method add_points_as_corners() in Manim is used to add a sequence of 
#points to a VMobject and connect them with straight lines, as if drawing the corners of a polygon.
#When you call add_points_as_corners([point1, point2, ..., pointN]), it takes a list of points (2D or 3D coordinates) and adds them to the VMobject.

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        # self.play(Rotating(dot, radians=PI, about_point= RIGHT run_time=2))
        # self.wait()
        # self.play(dot.animate.shift(UP))
        # self.play(dot.animate.shift(LEFT))
        # self.wait()

# manim -pql 10PointWithTrace.py PointWithTrace
# https://chatgpt.com/share/6714bb81-42b8-8002-ae1a-0c8a779b36ba