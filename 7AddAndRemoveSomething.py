from manim import *

class AddAndRemoveSomething(Scene):
    def construct(self):
        a = Circle(color=WHITE)
        self.add(a)
        self.wait(2)
        self.remove(a)
        self.wait(1)
