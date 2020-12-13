from manim import * 

class intro(Scene):
    def construct(self):
#        Prove using induction that 9^n - 1 is divisible by 8 for all n > 0 
        problem = MathTex(r'\text{Prove using', r'induction', r'that } 9^', r'n', r'- 1 \text{ is divisible by 8 for all }', r'n', r'>0')
        problem[1].set_color(BLUE)
        problem[3].set_color(RED)
        problem[5].set_color(RED)
        problem.scale(0.9)
        title = MathTex(r'\text{Problem:}')
        title.next_to(problem, direction=UP)
        self.play(ShowCreation(title))
        self.play(ShowCreation(problem))
        self.wait(1)
    
