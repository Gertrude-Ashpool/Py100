import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
t.width(15)
t.speed(0)
t.hideturtle()


def random_palette(number_of_colors):
    palette = []
    for _ in range(number_of_colors):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        color = [r, g, b]
        palette.append(color)
    return palette


def cycle_color():
    global d
    c = int(d % len(palette))
    tup = (int(palette[c][0]), int(palette[c][1]), int(palette[c][2]))
    t.color(tup)
    d += 1


palette = random_palette(10)
steps = 5000
length = 30
d = 0
directions = [0, 90, 180, 270]

for step in range(steps):
    t.setheading(random.choice(directions))
    t.forward(length)
    cycle_color()

screen.exitonclick()