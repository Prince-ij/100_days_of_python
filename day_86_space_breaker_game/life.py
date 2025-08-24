from turtle import Turtle

class Life(Turtle):
    def __init__(self, cordinates):
        super().__init__()

        self.fillcolor('red')
        self.penup()
        self.goto(cordinates)
        self.shape('circle')
        self.pencolor('white')

    def remove(self):
        self.hideturtle()
