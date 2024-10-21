from manim import*

class MovingAround(Scene):
    def construct(self):
        square = Square(color=YELLOW, fill_opacity=1)

        self.play(square.animate.move_to(RIGHT*3))
        self.play(square.animate.scale(0.3), run_time=3)
        self.play(square.animate.scale(5), run_time=3)
        self.wait(1.5)

# manim -pql 5MovingAround.py MovingAround