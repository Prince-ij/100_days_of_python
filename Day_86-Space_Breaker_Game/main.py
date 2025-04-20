import turtle
from turtle import Screen
from carrier import Carrier
from bricks import Brick
from life import Life
import time
from random import choice
from ball import Ball

x_pos = [x for x in range(-200, 200, 40)]
y_pos = [y for y in range(0, 240, 40)]

brick_pos = [(choice(x_pos), choice(y_pos)) for _ in range(150)]

screen = Screen()

screen.bgcolor('#04ff56')
screen.screensize(400, 500)
screen.tracer(0)
screen.title('Space Breaker')


carrier = Carrier((0,-230))
screen.update()
turtle.hideturtle()
turtle.write('Welcome to Space Breaker Game, Destroy the bricks and Win the Alien Wars',
             False,
             align='center',
             font=('Monospace', 12, 'bold')
             )
screen.update()
time.sleep(3)
turtle.clear()



lives = []

x = -350
for _ in range(3):
    lives.append(Life((x := x + 40, 260)))

bricks = []

for pos in brick_pos:
    brick = Brick(pos)
    bricks.append(brick)


ball = Ball((0, -200))
screen.update()
turtle.penup()
turtle.goto((-30, -100))


secs = 3

for _ in range(3):
    turtle.write(f'🏀 game starts in {secs}',
                 False,
                 align='center',
                 font=('Monospace', 14, 'bold')
                 )

    screen.update()
    secs -= 1
    time.sleep(1)
    turtle.clear()


turtle.penup()
turtle.goto(-320, 0)
turtle.left(90)
turtle.pendown()
turtle.fd(300)
turtle.right(90)
turtle.fd(630)
turtle.right(90)
turtle.fd(600)
turtle.right(90)
turtle.fd(630)
turtle.right(90)
turtle.fd(300)


while True:
    screen.listen()

    screen.onkey(carrier.move_left, 'Left')
    screen.onkey(carrier.move_right, 'Right')

    ball.move()
    time.sleep(0.01)
    for brick in bricks:
        if ball.distance(brick) < 20 and brick.isvisible():
            ball.bounce_y()
            brick.crush()
            bricks.remove(brick)
            screen.update()
    if not bricks:
        turtle.penup()
        turtle.home()
        turtle.write('Congratulations, You Cleared the Game !!!',
                     False,
                     align='center',
                     font=('Monospace', 18, 'bold')
                     )
        break
    if ball.ycor() > 250:
        ball.bounce_y()
    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.bounce_x()

    if carrier.distance(ball) < 60 and ball.ycor()  > -230:
        ball.bounce_y()
        ball.off()

    if ball.ycor() < -250:
        carrier.reset(0, -230)
        ball.reset(0, -200)
        if len(lives) > 1:
            lives.pop().remove()
            screen.update()
            time.sleep(2)
        else:
            lives.pop().remove()
            screen.update()
            turtle.home()
            turtle.write('Game Over !!!',
                         False,
                         align='center',
                         font=('Monospace', 14, 'bold')
                         )
            break

    screen.update()

screen.mainloop()