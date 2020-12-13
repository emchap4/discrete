from manim import *

class equa(Scene):
    def construct(self):

        step = MathTex(r'\text{Inductive Step}')
        self.play(ShowCreation(step))
        self.wait(1)
        self.play(Uncreate(step))

        title2 = MathTex(r'P(k) \implies P(k+1)')
        step.next_to(title2, direction=UP)
        self.play(ShowCreation(title2))
        self.wait(1)
        self.play(Uncreate(title2))

        title3 = MathTex(r'P(', r'k', '):\ 9^', r'{k}', r'-1=8', r'b')
        title3[1].set_color(RED)
        title3[3].set_color(RED)
        title3[5].set_color(BLUE)
        start_ex = MathTex(r'\text{Where ', r'b', r' is some integer}')
        start_ex[1].set_color(BLUE)
        start_ex_logic = MathTex(r'b \in \mathbb{Z}')
        start_ex.next_to(title3, direction=DOWN)
        start_ex_logic.next_to(title3, direction=DOWN)
        self.play(ShowCreation(start_ex), ShowCreation(title3))
        self.wait(1)
        self.play(Transform(start_ex, start_ex_logic))
        self.wait(2)
        self.play(Uncreate(start_ex))

        ind_step = MathTex(r'9^', r'{k+1}', r'-1')
        ind_step[1].set_color(RED)
        ind_step.next_to(title3, direction=DOWN)
        title4 = MathTex(r'P(', r'k+1', r'):\ 9^{', r'k+1}', '- 1 = 8', "b'")
        title4[3].set_color(RED)
        title4[1].set_color(RED)
        title4[5].set_color(BLUE)
        self.play(Transform(title3, title4))
        self.wait(1)
        self.play(ShowCreation(ind_step))
        self.wait(2)

        exib = MathTex(r'9*9^', r'{k}', r'-1')
        exib.next_to(title3, direction=DOWN)
        exib[1].set_color(RED)
        self.play(Transform(ind_step, exib))
        self.wait(2)


        exi = MathTex(r'9*', r'9^', r'{k}', r'-1', r'=', r'9*', r'(8', r'b', r'+1)', r'- 1')
        exi.next_to(title3, direction=DOWN)
        exi[2].set_color(RED)
        exi[7].set_color(BLUE)
        self.play(Transform(ind_step, exi[0:4]))
        self.wait(2)
        self.play(
                ShowCreation(exi[4]), 
                ReplacementTransform(exi[0].copy(), exi[5]),
                ReplacementTransform(exi[3].copy(), exi[9])
                )
        self.wait(1)
        self.play(ShowCreation(exi[6:9]))

        exia = MathTex(r'9*', r'(8', r'b', r'+1)', r'- 1')
        exia.next_to(title3, direction=DOWN)
        exia[2].set_color(BLUE)

        self.wait(2)
        self.play(
                Uncreate(exi[:5]),
                Uncreate(ind_step[:5])
                )
        self.wait(1)

        self.play(Transform(exi[5:], exia))
        self.wait(2)

        exiv = MathTex(r'72', r'b', r'+ 9 - 1')
        exiv.next_to(title3, direction=DOWN)
        exiv[1].set_color(BLUE)
        self.play(Transform(exi[5:], exiv))
        self.wait(2)

        exv = MathTex(r'72', r'b' ,r'+ 8')
        exv.next_to(title3, direction=DOWN)
        exv[1].set_color(BLUE)
        self.play(Transform(exi[5:], exv))
        self.wait(2)

        exvi = MathTex(r'8', r'(9', r'b', r'+1)')
        exvi.next_to(title3, direction=DOWN)
        exvi[2].set_color(BLUE)
        self.play(Transform(exi[5:], exvi))
        self.wait(2)

        brace = Brace(exvi[1:], direction=DOWN)
        brace_text = brace.get_text("Integer")
        self.play(ShowCreation(brace), ShowCreation(brace_text))
        self.wait(2)


        final = MathTex(r'8', "b'")
        final.next_to(title3, direction=DOWN)
        final[1].set_color(BLUE)
        self.play(
                Uncreate(brace),
                Uncreate(brace_text),
                Transform(exi[5:], final)
                )
        self.wait(2)
