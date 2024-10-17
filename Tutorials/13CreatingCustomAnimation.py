
from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        # number: DecimalNumber এটার অর্থ number অবশ্যই DecimalNumber class এর instanse হতে হবে
        # If you delete DecimalNumber, the code will still run, but it's best to leave it for clarity.
        # -> None: is a return type hint that indicates the function does not return any value. t’s used to make the code more readable and tell developers that this method initializes the object and doesn't provide a return value.
        super().__init__(number,  **kwargs)
        # অর্থাৎ Aimation class এ যত **kwargs আছে সব Count class এ চলে আসবে। 
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        #এই আলফা টা ০ থেকে ১ প্রজন্ত জাইতে থাকে fps এর হিসেবে। এই কাজ টা করে Animation class, interpolate_mobject method
        # এর মাধ্যমে। যখন আলফা এর মান ০ তখন .moobject  এখানে সেটা DecimalNumber এর value self.start আর ১ হলে 
        # value= self.end অর্থাৎ এভাবেই সকল value দেখাবে ০ থেকে ১০০ প্রজন্ত। আর  alpha = current frame/total frame
        # আর ফাংশন এর নাম interpolate_mobject না দিলে কাজ করবে না। আর এই ফ্রেম render করে Scene class.
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()

# manim -pql 13CreatingCustomAnimation.py CreatingCustomAnimation