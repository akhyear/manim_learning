from manim import*

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        '''# next_to
        cir = Circle(color=RED, fill_opacity=0.5)
        sq = Square(color= GREEN, fill_opacity = 1)
        sq.next_to(cir, RIGHT, buff= 2)
        self.add(cir, sq)

        #shift
        sq2= Square(color = PINK, fill_opacity = 0.9)
        sq2.shift(UP*3+LEFT*3)
        self.add(sq2)

        #move_to
        sq3 = Square(color= PURPLE, fill_opacity = 0.7)
        sq3.move_to([3,4,0])
        self.add(sq3)'''

        #align_to
        c0 = Circle(color=PINK)
        c1 = Circle(radius=0.5, color=WHITE, fill_opacity=0.4)
        c2 = c1.copy().set_color(ORANGE)
        c3 = c1.copy().set_color(BLUE)

        c1.align_to(c0, LEFT)
        c2.align_to(c0, RIGHT)
        c3.align_to(c0, UP)
        self.add(c0,c1, c2,c3)
    ''' align_to doesn't necessarily move the objects away
     It only aligns the boundary of the objects with respect to the direction (like RIGHT or UP).
     As a result, c2 and c3 might end up overlapping or placed in ways you don't expect.'''