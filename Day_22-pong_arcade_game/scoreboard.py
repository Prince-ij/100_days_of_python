from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align='Center', font=("courier", 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align='Center', font=("courier", 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
