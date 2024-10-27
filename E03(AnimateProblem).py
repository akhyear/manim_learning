from manim import*

class AnimateProblem(Scene):
    def construct(self):
        s1 = Square(color = WHITE, fill_opacity = 0.5)
        s2 = Square(color = RED,  fill_opacity = 0.5)
        a = VGroup(s1, s2).arrange(RIGHT, buff=1)
        self.add(a)
        self.play(s1.animate.rotate(PI), Rotate(s2, PI), run_time =3)
# এমন হওয়ার কারন, .annimate ফাংশন সুধু start point ও end point হিসাব করে। তাই s1 এর প্রথম কোণা 
# ৯০ ডিগ্রি যাবে সোজাসুজি। rotate এর মত ঘুরে যাবে না।
        self.wait()