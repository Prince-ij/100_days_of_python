STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)


    def move(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
