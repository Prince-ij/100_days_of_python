from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()

img = "blank_states_img.gif"
screen.addshape(img)
screen.title("US 50 states")
screen.tracer(0)
turtle.shape(img)
turtle.penup()

correct_guesses = []
data = pandas.read_csv("50_states.csv")
states = list(data.state)
x = list(data.x)
y = list(data.y)

while len(correct_guesses) < 50:
    screen.update()
    answer = screen.textinput(f"{len(correct_guesses)}/50 States Correct", "What's the name of another state "
                            "in US ? ").title()
    if answer == "Exit":
        break
    for i in range(50):
        if answer == states[i]:
            x_cor = x[i]
            y_cor = y[i]
            turtle.goto(x_cor, y_cor)
            turtle.write(arg=f"{states[i]}")
            correct_guesses.append(answer)
            turtle.home()

states_to_learn = []

for state in states:
    if state not in correct_guesses:
        states_to_learn.append(state)

state_dict = {"States to Learn": states_to_learn}

state_dict = pandas.DataFrame(state_dict)

state_dict.to_csv("states_to_learn.csv")
