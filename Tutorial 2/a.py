from manim import *

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        # এখানে Transform ব্যাবহার করা হয়নি কারন এটা ব্যবহার করলে blue_circle fade_out 
        # করার সময় একটা ধাপ দেয় মানে green_square কেও কি কি বা করে।  তাই ReplacementTransform ব্যাবহার করতে হবে
        # যাতে একটা আরেকটাকে রিপ্লেস করে
        
        self.play(FadeOut(blue_circle))