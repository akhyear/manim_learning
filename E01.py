from manim import*

'''class MovingObject(Scene):
    def construct(self):
        circle = Circle(color=RED, fill_opacity=0.8)
        square = Square(color=GREEN, fill_opacity= 0.8)
        self.play(FadeIn(circle), run_time = 1.5)
        self.play(ReplacementTransform(circle,square))
        self.play(FadeOut(square))
        self.wait()'''

'''class SecondEx(Scene):
    def construct(self):
        ax = Axes(x_range=(-4,4), y_range=(-3,3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, (-2,0)).set_color(YELLOW)
        
        self.add(ax, curve, area)'''

'''class SecondExAnimate(Scene):
    def construct(self):
        ax = Axes(x_range=(-4,4),y_range=(-4,4))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color= RED)
        area = ax.get_area(curve, x_range=(-2,0)).set_color(YELLOW)

        self.play(Create(ax))
        self.play(Create(curve), run_time = 3)
        self.play(FadeIn(area))'''

class SquareToCircle(Scene):
    def construct(self):
        sq = Square(color= YELLOW, fill_opacity = 0.8)
        cic = Circle(color=RED, fill_opacity = 0.8)

        self.play(DrawBorderThenFill(sq), run_time =2)
        self.play(ReplacementTransform(sq,cic),run_time =2)
# এখানে Transform ব্যাবহার করা হয়নি কারন এটা ব্যবহার করলে blue_circle fade_out 
# করার সময় একটা ধাপ দেয় মানে green_square কেও কি কি বা করে।  তাই ReplacementTransform ব্যাবহার করতে হবে
# যাতে একটা আরেকটাকে রিপ্লেস করে
        # self.play(Indicate(cic).set_color(RED))
        # এটা দিয়ে একটু যুম করে
        self.play(FadeOut(cic))
        self.wait()