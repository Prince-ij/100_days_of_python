from turtle import Turtle
from random import choice

colors = ['magenta', 'red', 'blue', 'orange', 'yellow']

class Brick(Turtle):
    def __init__(self, cordinates):
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(colors))

        self.penup()
        self.goto(cordinates)

    def crush(self):
        self.color('black')
        self.shape('triangle')
        self.hideturtle()