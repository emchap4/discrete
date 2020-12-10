from manim import *

class equa(Scene):
    def construct(self):
        title1 = MathTex(r'P(k)')

        base = MathTex(r'9^k -1', r'=', r'8b')
        ex_base = Text("For some integer greater than 0 for k and for some integer b")
        ex_base.scale(0.75)

        base.next_to(title1, direction=DOWN)
        ex_base.next_to(base, direction=DOWN)

        self.play(Write(title1))
        self.play(ShowCreation(base))
        self.play(ShowCreation(ex_base))
        self.wait(1)
        var = MathTex(r'\exists k\ \exists b,\ k \in \mathbb{Z} \land k>0 \land b \in \mathbb{Z}')
        var.next_to(base, direction=DOWN)

        self.play(Transform(ex_base, var))

        self.play(Uncreate(title1), Uncreate(base), Uncreate(ex_base))
        self.wait(2)

        title2 = MathTex(r'P(k) \implies P(k+1)')
        self.play(ShowCreation(title2))
        self.wait(1)
        self.play(Uncreate(title2))

        start = MathTex(r'9^', r'{k}', r'-1=8', r'b')
        start[1].set_color(RED)
        start[3].set_color(BLUE)

        start_ex = Text("Where b is some integer")
        start_ex_logic = MathTex(r'b \in \mathbb{Z}')
        start_ex.next_to(start, direction=DOWN)
        start_ex_logic.next_to(start, direction=DOWN)
        title3 = MathTex(r'P(', r'k', ')')
        title3[1].set_color(RED)
        title3.next_to(start, direction=UP)
        self.play(ShowCreation(start), ShowCreation(start_ex), ShowCreation(title3))
        self.wait(1)
        self.play(Transform(start_ex, start_ex_logic))
        self.wait(2)
        self.play(Uncreate(start_ex))

        ind_step = MathTex(r'9^', r'{k+1}', r'-1')
        ind_step[1].set_color(RED)
        title4 = MathTex(r'P(', r'k+1', r')')
        title4[1].set_color(RED)
        title4.next_to(start, direction=UP)
        self.play(Transform(start, ind_step), Transform(title3, title4))
        self.wait(2)

        exi = MathTex(r'9*9^', r'{k}', r'-1=8')
        exi[1].set_color(RED)
        self.play(Transform(start, exi))
        self.wait(2)

        exii = MathTex(r'9*(8', r'b', r'+1)-1')
        exii[1].set_color(BLUE)
        self.play(Transform(start, exii))
        self.wait(2)

        exiii = MathTex(r'9^', r'{k+1}', r'-1=', r'72',r'b',r'+8')
        exiii[1].set_color(RED)
        exiii[4].set_color(BLUE)
        self.play(Transform(start, exiii))
        self.wait(2)

        exiv = MathTex(r'9^', r'{k+1}', r'-1=8*(9', r'b', r'+1)')
        exiv[1].set_color(RED)
        exiv[3].set_color(BLUE)
        self.play(Transform(start, exiv))
        self.wait(2)
