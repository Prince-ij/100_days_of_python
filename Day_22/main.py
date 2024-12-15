from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('pong')

y_offset = -300
line = Turtle()
line.ht()
line.color('white')
line.penup()
line.goto(0, y_offset)

while y_offset <= 300:
    y_offset += 20
    line.pendown()
    line.goto(0, y_offset)
    line.penup()
    y_offset += 20
    line.goto(0, y_offset)





l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scorer = ScoreBoard()

game_on = True

while game_on:
    screen.listen()
    time.sleep(ball.move_speed)

    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 380:
        ball.reset()
        scorer.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scorer.r_point()
    screen.update()


screen.mainloop()
