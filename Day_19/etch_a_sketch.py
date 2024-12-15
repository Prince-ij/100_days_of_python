import turtle

t = turtle.Turtle()
turtle.listen()

def w():
    t.fd(10)

def s():
    t.bk(10)

def a():
    t.left(10)


def d():
    t.right(10)

def c():
    t.clear()
    t.up()
    t.home()
    t.down()

turtle.onkeypress(w, 'w')
turtle.onkey(s, "s")
turtle.onkey(a, "a")
turtle.onkey(d, "d")
turtle.onkey(c, "c")


t.screen.mainloop()
