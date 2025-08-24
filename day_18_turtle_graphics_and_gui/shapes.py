from turtle import Turtle
from random import choice

t = Turtle()

colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'purple', 'orange', 'pink']
t.shape('turtle')
for i in range(4, 11):
    for _ in range(i):
        t.color(colors[i - 4])
        angle = 360 / i
        t.forward(100)
        t.left(angle)


t.screen.mainloop()
