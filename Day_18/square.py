from turtle import Turtle, Screen

t = Turtle()

t.shape('turtle')
for _ in range(4):
    t.forward(100)
    t.left(90)

t.screen.mainloop()
