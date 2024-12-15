from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape('circle')
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1


    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def speed_up(self):
        self.move_speed *= 0.5

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.home()
        self.y_move *= -1
        self.x_move *= -1
        self.move_speed = 0.1
