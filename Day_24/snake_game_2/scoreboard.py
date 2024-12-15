from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('white')
        self.ht()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "center", font=("Arial", 15, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.increase()
