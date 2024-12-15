from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                            "Enter a colour: ")
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'orange']
all_turtles = []
pos = -150
is_on = True
for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.up()
    new_turtle.color(color)
    new_turtle.goto(-230, pos)
    pos += 50
    all_turtles.append(new_turtle)

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You win !, the {winner} turtle won")
            else:
                print(f"You lose !, the {winner} turtle won")

        turtle.fd(random.randint(0, 10))



screen.exitonclick()
