from turtle import Turtle, Screen

t = Turtle()

t.shape("classic")
t.color("MediumOrchid")

def dash(length):
    t.forward(length/2)
    t.up()
    t.forward(length/2)
    t.down()

for _ in range (15):
    dash(20)

screen = Screen()
screen.exitonclick()