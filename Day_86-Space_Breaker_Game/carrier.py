from turtle import Turtle

class Carrier(Turtle):
    def __init__(self, cordinates):
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('#333333')
        self.penup()
        self.speed(10)

        self.goto(cordinates)



    def move_left(self):
        if self.xcor() > -230:
            self.goto(self.xcor() - 70, self.ycor())

    def move_right(self):
        if self.xcor() < 230:
            self.goto(self.xcor() + 70, self.ycor())

    def reset(self, x, y):
        self.goto(x, y)