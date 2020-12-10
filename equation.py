from manim import *

class equa(Scene):
    def construct(self):
        title1 = MathTex(r'P(k)')
        base = MathTex(r'9^k -1', r'=', r'8b')
        ex_base = Text("For some integer greater than 0 for k and for some integer b")
        ex_base.next_to(base, direction=UP)
        ex_base.scale(.80)
        var = MathTex(r'\exists k\ \exists b,\ k \in \mathbb{Z} \land k>0 \land b \in \mathbb{Z}')
        var.move_to([0,3,0])

        solvek = MathTex(r'9^{k} = 8b +1')
        solvek.next_to(var, direction=DOWN)


        step = MathTex(r'9^{k+1} - 1')
        step1 = MathTex(r'9^{k+1} - 1')
        step2 = MathTex(r'9*', r'9^k', r'- 1')
        step3 = MathTex(r'9*', r'(8b+1)', r'-1')
        step4 = MathTex(r'9^{k+1} - 1', r'72b+8')
        step5 = MathTex(r'9^{k+1} - 1', r'8(9b+1)')

        self.play(Write(base))
        self.play(Write(ex_base))
        self.play(Transform(ex_base, var))
        self.play(Transform(base, solvek))
        self.wait(2)
