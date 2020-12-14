from manim import *

class thumbnail(Scene):
    def construct(self):
        top = MathTex(r'\text{Is } ', r'9^', r'n', r' -', r'1')
        middle = MathTex(r'\text{always divisible by }', r'8', r'\text{?}')
        ind = MathTex(r'\text{Proof by Induction}')

        top[2].set_color(BLUE)
#k        top[1].set_color(RED)
#k        top[4].set_color(RED)

        middle[1].set_color(RED)

        top.scale(2.25)
        middle.scale(2.25)

        top.next_to(middle, direction=UP)
        ind.next_to(middle, direction=DOWN)

        self.play(
                ShowCreation(ind),
                ShowCreation(top),
                ShowCreation(middle)
                )
        self.wait(1)
