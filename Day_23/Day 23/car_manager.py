COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random

from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.cars = []
        self.ht()
        self.car_no = 3
        self.new_cars()



    def create_cars(self):
        i = random.randint(1, 6)
        if i == 5:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-200, 250) )
            self.cars.append(new_car)

    def move(self):
            for car in self.cars:
                car.setheading(180)
                car.fd(MOVE_DISTANCE)

    def speed_up(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT

    def new_cars(self):
         for _ in range(self.car_no):
              self.create_cars()
