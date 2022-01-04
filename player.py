from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE = 270

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False