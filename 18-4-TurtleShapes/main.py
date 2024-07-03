import random
from turtle import Turtle, Screen

t = Turtle()

t.shape("classic")
t.color("MediumOrchid")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    t.color(R, G, B)

def draw_shape(corners):
    for corner in range(corners):
        t.forward(100)
        t.right(360/corners)

for corners in range(3, 11):
    change_color()
    draw_shape(corners)

screen = Screen()
screen.exitonclick()
