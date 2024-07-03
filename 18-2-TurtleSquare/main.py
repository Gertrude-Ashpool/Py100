from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("MediumOrchid")

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

screen = Screen()
screen.exitonclick()