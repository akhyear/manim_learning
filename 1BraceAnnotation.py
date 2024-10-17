from manim import *

'''class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)'''

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2,-1,0])
        dot2 = Dot([2,1,0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(YELLOW)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal Distance")
        b2 = Brace(line, direction= line.copy().rotate(PI/2).get_unit_vector())
        # অর্থাৎ brace তো সবসময় Horizontal হয়। তাই নতুন যে line.copy().rotate(PI/2)
        # বানানো হয়েছে সেটা তো লাইন এর ৯০ ডিগ্রি তে হবে। আর Brace হবে তার Horizontal
        # অর্থাৎ আসল লাইন এর থিক উপরে। আর দিক ঠিক করার জন্য get_unit_vector() নিয়েছে
        # যার মান ১ আর সেটা vector এর দিক নির্দেশ করে মূলবিন্দু হতে।
        #  এখানে get_unit_vector() দিতে হবে কারন এটা একক vector নির্দেশ করে
        # নতুন যে direction হবে সেটা যেন মূলবিন্দু থেকে উৎপন্ন হয়। 
        
        b2text = b2.get_tex("x-x_1")
        # its tex not text
        self.add(line, dot, dot2, b1, b2, b1text, b2text)
        self.play(FadeIn(line, dot, dot2, b1, b2, b1text, b2text),rum_time= 5)
        self.wait()
        self.play(FadeOut(line, dot, dot2, b1, b2, b1text, b2text),rum_time= 5)
        self.wait()

# manim -pql 1BraceAnnotation.py BraceAnnotation