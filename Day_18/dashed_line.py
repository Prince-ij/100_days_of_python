from turtle import Turtle

t = Turtle()

t.shape('turtle')
t.color('green')

for i in range(10):
    t.fd(10)
    t.up()
    t.fd(10)
    t.down()

t.screen.mainloop()
