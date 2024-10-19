from manim import *

'''class MovingGroupToDestination(Scene):
    def construct(self):
        group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2 * RIGHT)).scale(1.4)
        dest = Dot([4, 3, 0], color=YELLOW)
        self.add(group, dest)
        self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
        self.wait(0.5)'''

class MovingGroupToDestination(Scene):
    def construct(self):
        group = VGroup(Dot(LEFT),Dot(ORIGIN),Dot(RIGHT, color=YELLOW), Dot(RIGHT*2))
        # In Manim, the class is called VGroup (short for "Vector Group") treating them as a vector-like collection. This allows you to apply geometric transformations (like shifting, rotating, or scaling) to the entire group in a consistent, vectorized way.

        dot = Dot([3,3,0], color=GREEN)
        self.add(group, dot)
        self.play(group.animate.shift(dot.get_center()-group[2].get_center()))
        # The shift() method moves the entire group by a certain vector (translation). The vector is calculated by subtracting two positions
        # dest.get_center(): This retrieves the coordinates of the destination dot, এটা দিতেই হবে
        self.wait()



# manim -pql 7MovingGroupToDestination.py MovingGroupToDestination