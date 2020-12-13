from manim import *

def is_brace(maybe_brace):
    return isinstance(maybe_brace, Brace)

class number_line(Scene):
    def construct(self):
        ## Number Line Section - What is induction?
        line = NumberLine()
        self.play(ShowCreation(line))
        self.wait()

        point = Dot(point=[-4,0.25,0])
        bct = Tex("Base Case")
        bct.next_to(point, direction=UP)
        self.play(ShowCreation(point))
        self.play(ShowCreation(bct))
        self.wait()

        line1 = Line(start=[-4,-.25,0], end=[-3,-.25,0])
        brace = Brace(line1)

        brace_text = brace.get_tex(r'P(k) \implies P(k+1)')
        brace_text.generate_target()
        brace_text.target.move_to([0,2.5,0])

        self.play(ShowCreation(brace))
        self.play(ShowCreation(brace_text))
        self.wait()
        self.play(MoveToTarget(brace_text))
        for i in range(1, 7):
            self.play(ShowCreation(brace.copy().shift(RIGHT*i)))

#        all_braces = list(filter(lambda x: isinstance(x, Brace), self.get_mobject_copies()))

#        self.remove(all_braces[0])

        self.wait(2)

        line2 = Line(start=[-4,-.50,0], end=[3,-.50,0])
        big_brace = Brace(line2)
        self.play(ShowCreation(big_brace))
        self.wait(2)

        end_point = Dot(point=[3,.25,0])
        self.play(TransformFromCopy(point, end_point))

        self.wait(2)
