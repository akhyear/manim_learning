from manim import *
# class TwoTransforms(Scene):
#     def transform(self):
#         a = Circle()
#         b = Square()
#         c = Triangle()
#         self.play(Transform(a, b))
#         self.play(Transform(a, c))
#         self.play(FadeOut(a))

    # def replacement_transform(self):
    #     a = Circle()
    #     b = Square()
    #     c = Triangle()
    #     self.play(ReplacementTransform(a, b))
    #     self.play(ReplacementTransform(b, c))
    #     self.play(FadeOut(c))

    # def construct(self):
    #     self.transform()
    #     self.wait(0.5)  # wait for 0.5 seconds
        # self.replacement_transform()


class TwoTransformer(Scene):
    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a,b))
        self.play(ReplacementTransform(b,c))
        self.play(FadeOut(c))

    def construct(self):
        self.replacement_transform()
        self.wait(0.5)
        

# manim -pql 6twotransform.py TwoTransformer

'''Transform: Smoothly morphs one object into another (ideal for related shapes or transitions).
    ReplacementTransform: Replaces one object with another, as if swapping them (best for distinctly different objects).'''