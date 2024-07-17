import turtle
from states import States
from map import Map


states = States()
us_map = Map()

screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

guessed_states = []
score = 0

while len(guessed_states) < 50:
    if score != 0:
        answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                        prompt="Name another State!")
    else:
        answer_state = screen.textinput(title="Guess the States",
                                        prompt="Name another State!")
    answer_state = answer_state.title()

    # if states.exists(answer_state):
    if answer_state == "Exit":
        states.states_to_learn(guessed_states)
        break
    if answer_state in states.states_list:
        guessed_states.append(answer_state)
        us_map.mark(states.loc(answer_state), answer_state)
        score += 1

screen.exitonclick()