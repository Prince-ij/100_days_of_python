FONT = ("Courier", 19, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.goto(-280, 260)
        self.clear()
        self.write(arg=f"Level: {self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align='center', font=FONT)
