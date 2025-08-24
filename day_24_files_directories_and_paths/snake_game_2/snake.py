from turtle import Turtle

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self):
        self.snakes = []
        self.pos = 0
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for current in range(3):
            self.add()

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.pos = 0
        self.head = self.snakes[0]

    def add(self):
        current = Turtle('square')
        current.color('white')
        current.up()
        current.setpos(self.pos, 0)
        self.pos -= 20
        self.snakes.append(current)

    def extend(self):
        self.add()


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x_cor = self.snakes[i - 1].xcor()
            y_cor = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x_cor, y_cor)
        self.snakes[0].fd(20)
