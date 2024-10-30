# বিসাত্রিত Formulas(2) = 12

from manim import*
from manim import ManimColor as Color
class SimpleCustomAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 2 * t
            angle = 2*t * 2*PI
#UpdateFromAlphaFunc repeatedly calls the spiral_out function, 
#passing a parameter t that varies smoothly from 0 to 1 over the run_time.
# t = 0 at the beginning of the animation.
#t = 1 at the end of the animation.
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(Color.from_hsv((t, 1.0, 1.0)))
            mobject.set_opacity(1-t)
        
        d = Dot(color=YELLOW)
        plane = NumberPlane()
        self.add(d, plane)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))
#UpdateFromAlphaFunc in Manim is a special function that allows you to animate an object 
# by updating its properties frame by frame using a custom update function
