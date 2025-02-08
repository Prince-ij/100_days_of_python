from turtle import Turtle

t = Turtle()
t.shape('turtle')
for i in range(100):
    for c in ('red', 'green', 'blue'):
        t.color(c)
        t.forward(i)
        t.right(30)

t.screen.mainloop()
