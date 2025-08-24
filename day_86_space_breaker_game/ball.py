from turtle import Turtle

class Ball(Turtle):
    def __init__(self, cordinates):
        super().__init__()

        self.shape('circle')
        self.color('white')

        self.penup()
        self.goto(cordinates)
        self.x_move = 5
        self.y_move = 5



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def off(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset(self, x, y):
        self.goto(x, y)
