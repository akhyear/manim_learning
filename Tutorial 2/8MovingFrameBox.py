from manim import *

'''class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff =.1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()'''

class MovingFrameBox(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x) = ", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)" 
        )
        self.play(Write(text))

        framebox1 = SurroundingRectangle(text[1],buff=0.1)
        # buff অর্থ আমরা যে টেক্সট আছে তার চারপাশে কত দূরত্ব রাখতে চাচ্ছি
        framebox2= SurroundingRectangle(text[3], buff=0.1)

        self.play(Create(framebox1))
        self.wait()

        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()
# manim -pql 8MovingFrameBox.py MovingFrameBox