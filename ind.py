from manim import *


class problem(MovingCameraScene):

    def construct(self):

        start_dot = Dot(point=[-5,.25,0])
        end_dot = Dot(point=[4,.25,0])

        # 1st 
        base_line = Line(start=[-5,.25,0], end=[4,.25,0])
        base_line.set_color(RED)
        slice_line = Line(start=[3,0,0], end=[3,.5,0])
        nine_brace = Brace(base_line, direction=UP)
        nine_brace_text = nine_brace.get_text("9")

        self.play(ShowCreation(start_dot))
        self.play(ShowCreation(end_dot))
        self.play(ShowCreation(base_line))
        self.play(ShowCreation(nine_brace))
        self.play(ShowCreation(nine_brace_text))
        self.wait(1)

        self.play(ShowCreation(slice_line))

        eight_line = Line(start=[-5,0,0], end=[(3),0,0])

        base_brace = Brace(eight_line, direction=DOWN)
        base_brace.set_color(BLUE)
        brace_text = base_brace.get_text("8")

        self.play(ShowCreation(base_brace))
        self.play(ShowCreation(brace_text))
        self.wait(2)

        self.play(Uncreate(nine_brace))
        self.play(Uncreate(nine_brace_text))
        self.wait(2)

        # 2nd

        top_left = Dot(point=[-5,9.25,0])
        top_right = Dot(point=[4,9.25,0])

        self.play(ShowCreation(top_left))
        self.play(ShowCreation(top_right))

        self.play(self.camera_frame.move_to, [0,4.75,0],
                  self.camera_frame.set_width, 30)

        rectangle = Rectangle(height=9, width=9)
        rectangle.set_color(RED)
        rectangle.shift([-0.5, 4.75, 0])
        self.play(Transform(base_line, rectangle))
        self.wait(2)

        cut = Rectangle(height=1, width=1)
        cut.set_fill(color=WHITE)
        cut.shift([3.5,.75,0])
        self.play(Transform(slice_line, cut))
        self.wait(2)

        vert_line = Line(start=[-5,.25,0], end=[-5,9.25,0])
        vert_brace = Brace(vert_line, direction=LEFT)
        vert_brace_text = vert_brace.get_text("9")
        self.play(ShowCreation(vert_brace))
        self.play(ShowCreation(vert_brace_text))

        apart = Line(start=[-5,1.25,0], end=[3,1.25,0])
        self.play(ShowCreation(apart))
        self.wait(1)

        vert_line_prime = Line(start=[-4,1.25,0], end=[-5,9.25,0])
        vert_brace_prime = Brace(vert_line_prime, direction=LEFT)
        vert_brace_prime.set_color(BLUE)
        vert_brace_text_prime = vert_brace_prime.get_text("8")

        self.play(Transform(vert_brace, vert_brace_prime))
        self.play(Transform(vert_brace_text, vert_brace_text_prime))
        self.wait(1)

        framebox = Rectangle(width=9.1, height=1.1, stroke_width=7)
        framebox.shift([-.5,.75,0])
        framebox.set_color(YELLOW)
        self.play(ShowCreation(framebox))
        self.wait(2)
