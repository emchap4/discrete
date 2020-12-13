from manim import *

class base_case(Scene):
    def construct(self):
        pred = MathTex(r'P(', r'k', r'):\ 9^', r'k', r'-1 = 8', r'b')
        pred[1].set_color(RED)
        pred[3].set_color(RED)
        pred[5].set_color(BLUE)
        title = MathTex(r'\text{Base Case:}')

        self.play(ShowCreation(title))
        self.wait(1)
        self.play(Transform(title, pred))
        self.wait(1)

        bc = MathTex(r'9^', r'k', r'- 1 = 8', r'b')
        bc[1].set_color(RED)
        bc[3].set_color(BLUE)
        self.play(Transform(title, bc))
        self.wait(1)

        bc1 = MathTex(r'9^', r'1', r'- 1 = 8', r'b')
        bc1[1].set_color(RED)
        bc1[3].set_color(BLUE)
        self.play(Transform(title, bc1))
        self.wait(1)

        bc2 = MathTex(r'9 - 1 = 8', r'b')
        bc2[1].set_color(BLUE)
        self.play(Transform(title, bc2))
        self.wait(1)

        bc2 = MathTex(r'8 = 8', r'b')
        bc2[1].set_color(BLUE)
        self.play(Transform(title, bc2))
        self.wait(1)

        bc3 = MathTex(r'8 = 8*', r'1')
        bc3[1].set_color(BLUE)
        self.play(Transform(title, bc3))
        self.wait(1)
