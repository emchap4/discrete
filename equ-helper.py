from manim import *

class equahelp(Scene):
    def construct(self):
        pred = MathTex(r'P(', r'k', r'):\ 9^{', r'k', '} - 1 = 8', r'b')
        pred[1].set_color(RED)
        pred[3].set_color(RED)
        pred[5].set_color(BLUE)
        exp = MathTex(r'9^{', r'k', r'} - 1 = 8', r'b')
        exp[1].set_color(RED)
        exp[3].set_color(BLUE)
        exp.next_to(pred, direction=DOWN)
        expi = MathTex(r'9^{', r'k', '} = 8', r'b', r' + 1')
        expi[1].set_color(RED)
        expi[3].set_color(BLUE)
        expi.next_to(pred, direction=DOWN)

        self.play(ShowCreation(pred), ShowCreation(exp))
        self.wait(1)
        self.play(Transform(exp, expi))
        self.wait(2)




