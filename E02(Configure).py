# from manim.utils.unit import Percent, Pixels
from manim import *

config.background_color = WHITE
config.frame_height = 15
config.frame_width = 20
# config.pixel_height = 1920
# config.pixel_width = 1080

class Configure(Scene):
    def construct(self):
        plane = NumberPlane(x_range= [-4,4],  y_range=[-4,4]).set_color(BLACK)
        t = Triangle(color = GREEN, fill_opacity = 1)
        self.add(plane, t)