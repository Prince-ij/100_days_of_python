from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cordinates):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(cordinates)

    def up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
