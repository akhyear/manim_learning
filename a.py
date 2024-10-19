from manim import *

from manim import *

from manim import *

class RotateLine(Scene):
    def construct(self):
        # Create the static reference line (for comparison), from the origin to the right
        line = Line(ORIGIN, RIGHT).set_color(WHITE)
        
        # Create the moving line, also from the origin to the right
        line_moving = Line(ORIGIN, RIGHT).set_color(YELLOW)
        
        # Add both lines to the scene
        self.add(line, line_moving)
        
        # Rotate line_moving from 0 to 90 degrees (PI/2 radians)
        self.play(line_moving.animate.rotate_about_origin(PI / 2))
        self.wait(1)  # Pause for 1 second
        
        # Rotate line_moving back to the original position (0 degrees)
        self.play(line_moving.animate.rotate_about_origin(-PI / 2))
        self.wait(1)  # Pause for 1 second to show the final state


# manim -pql a.py a