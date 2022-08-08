from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_FORWARD = 10
FINISH_LINE = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.backward_move = 0
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)



    def go_up(self):
        self.forward(MOVE_FORWARD)

    def is_at_stating_line(self):
        if self.ycor() > -280:
            self.backward_move = 10
        else:
            self.backward_move = 0

    def go_down(self):
        self.backward(self.backward_move)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
         if self.ycor() > FINISH_LINE:
             return True
         else:
             return False





