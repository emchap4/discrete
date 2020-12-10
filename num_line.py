from manim import *
class number_line(Scene):
    def construct(self):
        ## Number Line Section - What is induction?
        line = NumberLine()
        self.play(ShowCreation(line))
        self.wait()

        point = Dot(point=[-1,0.25,0])
        bct = Tex("Base Case")
        bct.next_to(point, direction=UP)
        self.play(ShowCreation(point))
        self.play(ShowCreation(bct))
        self.wait()

        line1 = Line(start=[-1,-.25,0], end=[0,-.25,0])
        brace = Brace(line1)
        brace.generate_target()
        brace.target.set_width(5, stretch=True)
        #brace.target.shift(2*RIGHT)

        brace_text = brace.get_tex(r'P(k) \implies P(k+1)')
        brace_text.generate_target()
        brace_text.target.move_to([0,2.5,0])

        self.play(ShowCreation(brace))
        self.play(ShowCreation(brace_text))
        self.wait()
        self.play(MoveToTarget(brace_text))
        self.play(MoveToTarget(brace))



        self.wait(duration=2)

        # Dimensions: (9^n) - (1^n)
        # Formula: 8(9((9^k - 1)/8) + 1)
        # TODO: Summary
