from manim import *

class buff(Scene):
    def construct(self):
        title = MathTex(r'\text{Hi!}')
        self.play(ShowCreation(title))
        self.wait(2)
        self.play(Uncreate(title))

        ind = MathTex(r'\text{Induction:}')
        ind.scale(1.5)
        ind.set_color(BLUE)
        base_case = MathTex(r'\text{Base Case}')
        base_case.next_to(ind, direction=DOWN)
        ind_step = MathTex(r'\text{Inductive Step')
        ind_step.next_to(base_case, direction=DOWN)

        self.play(ShowCreation(ind))
        self.wait(1)
        self.play(
                ShowCreation(base_case),
                ShowCreation(ind_step)
                )
        self.wait(1)
