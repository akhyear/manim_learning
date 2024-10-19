from manim import *

'''class MovingDots(Scene):
    def construct(self):
        d1,d2=Dot(color=BLUE),Dot(color=GREEN)
        numberplane = NumberPlane(
            x_range=(-10,10,1),y_range=(-10,10,1),x_length=15,y_length=15
            )
        
        dg=Group(d1,d2).arrange(RIGHT,buff=2)
        l1=Line(d1.get_center(),d2.get_center()).set_color(RED)
        x=ValueTracker(0)
        y=ValueTracker(0)

        d1.add_updater(lambda z: z.set_x(x.get_value()))
        d2.add_updater(lambda z: z.set_y(y.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(),d2.get_center())))
        self.add(numberplane,d1,d2,l1)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()'''


class movingdot(Scene):
    def construct(self):
        dot1,dot2=Dot(color=RED),Dot(color=GREEN)
        dg = Group(dot1,dot2).arrange(RIGHT,buff=1)
        l1 = Line(dot1.get_center(),dot2.get_center()).set_color(YELLOW)

        a = ValueTracker(0)
        b = ValueTracker(0)

        dot1.add_updater(lambda z: z.set_y(a.get_value()))
        dot2.add_updater(lambda z: z.set_x(b.get_value()))
        l1.add_updater(lambda z: z.become(Line(dot1,dot2)))

        #This is a lambda function, which is a way to define a small, anonymous function in Python. In this case, z is a parameter that represents the dot1 dot itself.
        # The lambda function is a short way of saying, "for whatever z is, do the following."

        self.add(dot1,dot2,l1)

        self.play(a.animate.set_value(4))
        self.play(b.animate.set_value(5))

# manim -pql 6MovingDots.py MovingDots