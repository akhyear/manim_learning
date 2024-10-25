from manim import *

class ConfingDefault(Scene):
    def construct(self):
        m = Text("DEFAULT").move_to(UP*3)
        self.add(m)
        Text.set_default(color = GREEN, font_size = 100)
        t = Text("Rafin").next_to(m, DOWN)
        s = Text("Sadia").next_to(t, DOWN)
        self.add(t,s)

        Text.set_default(color= ORANGE, font_size = 200)
        r = Text("Default2").next_to(s, DOWN)
        self.add(r)
