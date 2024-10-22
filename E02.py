from manim import*

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next_to
        cir = Circle(color=RED, fill_opacity=0.5)
        sq = Square(color= GREEN, fill_opacity = 1)
        sq.next_to(cir, RIGHT, buff= 2)
        self.add(cir, sq)