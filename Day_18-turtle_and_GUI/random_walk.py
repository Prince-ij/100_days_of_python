from turtle import Turtle
import random
import turtle as t


def random_colors():
        r = random.randint(200, 255)
        g = random.randint(100, 255)
        b = random.randint(0, 100)
        return (r, g, b)

if __name__ == '__main__':
    t.colormode(255)

    directions = [0, 90, 180, 270]
    t = Turtle()
    t.speed(0)
    t.width(15)

    for i in range(200):
        t.pencolor(random_colors())
        t.fd(25)
        t.seth(random.choice(directions))

    t.screen.mainloop()
