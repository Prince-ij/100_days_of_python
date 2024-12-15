from random_walk import random_colors
import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.shape('classic')
t.ht()

colors = []
for i in range(42):
    colors.append(random_colors())

pos = -200
t.up()
t.setpos(-200.0, pos)

for i in range(10):
    pos += 50
    for j in range(10):
        t.dot(20, random.choice(colors))
        t.fd(50)
    t.setpos(-200.0, pos)
t.screen.mainloop()
