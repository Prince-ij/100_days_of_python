from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.color('white')
        self.ht()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 15, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", font=("Arial", 15, "bold"))
