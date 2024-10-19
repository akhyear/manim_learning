from manim import*

class a(Scene):
    def construct(self):
        dot1= Dot(color=RED)
        dot2 = Dot(color=GREEN)
        dg = Group(dot1,dot2).arrange(RIGHT, buff=2)
        l1 = Line(dot1.get_center(),dot2.get_center()).set_color(YELLOW)


        a = ValueTracker(0)
        b = ValueTracker(0)

        dot1.add_updater(lambda z: z.set_y(a.get_value()))
        dot2.add_updater(lambda z: z.set_x(b.get_value()))
        # l1.add_updater(lambda z: z.become(dot1,dot2))
        l1.add_updater(lambda z: z.become(Line(dot1,dot2)))

        self.add(l1, dot1,dot2)
        self.play(a.animate.set_value(4))
        self.play(b.animate.set_value(5))

# manim -pql a.py a