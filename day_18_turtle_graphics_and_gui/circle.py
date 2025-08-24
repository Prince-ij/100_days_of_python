import turtle
turtle.colormode(255)
from random_walk import random_colors
t = turtle.Turtle()
t.speed(0)
t.width(2)

for _ in range(360 // 10):
    t.color(random_colors())
    t.circle(100)
    t.setheading(t.heading() + 10)
    t.fd(5)


t.screen.mainloop()
