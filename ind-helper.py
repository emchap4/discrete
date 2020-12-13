from manim import *

class indhelper(Scene):

    def construct(self):
        equ = MathTex(r'9^', r'k' ,'-', r'1')
        equ[1].set_color(RED)
        self.play(ShowCreation(equ))

        equi = MathTex(r'1^', r'k')
        equi.set_x(equ[3].get_x())
        equi[1].set_color(RED)
        self.play(Transform(equ[3], equi))
        self.wait(2)
