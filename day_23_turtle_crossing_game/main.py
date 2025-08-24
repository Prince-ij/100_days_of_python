import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tom = Player()
scorer = Scoreboard()
cars = CarManager()

screen.listen()

screen.onkey(tom.move, 'Up')
tom.move()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    cars.create_cars()
    cars.move()
    if tom.level_up():
        scorer.level_up()
        cars.speed_up()
        cars.new_cars()

    for car in cars.cars:
        if tom.distance(car) < 35:
            scorer.game_over()
            game_is_on = False
    screen.update()
screen.mainloop()
