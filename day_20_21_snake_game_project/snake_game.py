from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

pos = 0
game_on = True

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase()
        snake.extend()
        food.refresh()

    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
        snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_on = False
        score.game_over()

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()
            game_on = False

screen.mainloop()
