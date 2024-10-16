from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT*3)
        square.next_to(circle,RIGHT, buff=1)
        triangle.move_to(square.get_center())

        self.add(circle,square,triangle)
        self.wait(3)


# manim -pql 9MobjectPlacement.py MobjectPlacement