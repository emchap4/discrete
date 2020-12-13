from manim import *

class outro(Scene):
    def construct(self):
        title = MathTex(r'\text{Thank you!}')

        self.play(ShowCreation(title))
        self.wait(1)

