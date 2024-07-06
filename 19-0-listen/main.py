from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# tell the screen object to start listening
screen.listen()

# bind the space bar to triger the move_forward() function
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()


