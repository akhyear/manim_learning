from manim import *

class RotationUpdate(Scene):
    def construct(self):
        def moving_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
# rotate_about_origin: This method rotates the object around the origin point, (0, 0, 0) in 3D space (or just (0, 0) in 2D scenes).
        def moving_back(mobj,dt):
            mobj.rotate_about_origin(-dt)
# dt is required in Manim's updater functions because the Manim engine expects this name for the time-step argument
#The time-step argument (dt) in Manim refers to the small time interval (or delta time) between consecutive frames of an animation. Manim animations run frame by frame, and for every frame, Manim computes how much time has passed since the previous frame. This time difference is called dt, short for delta time.
#  you can express them in terms of time, যেমন এখানে self.wait(2) দেওয়ায় 2 second  ধরেন updater চলবে 
        
        line_static = Line(ORIGIN, RIGHT*3).set_color(YELLOW)
        line_moving = Line(ORIGIN, RIGHT*3).set_color(RED)

        self.add(line_static,line_moving)
        line_moving.add_updater(moving_forth)
        self.wait(2)
        line_moving.remove_updater(moving_forth)

        line_moving.add_updater(moving_back)
        self.wait(2)

        line_moving.remove_updater(moving_back)
        self.wait()
 

# manim -pql 9RotationUpdate.py RotationUpdate