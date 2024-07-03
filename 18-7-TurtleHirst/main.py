# import colorgram
#
# colors = colorgram.extract('image.jpeg', 10)
#
# colors_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     colors_rgb.append(rgb)
#
# print(colors_rgb)


import random
from turtle import Turtle, Screen

color_list = [(202, 172, 107), (219, 226, 233), (237, 244, 242), (153, 180, 196), (152, 186, 174), (194, 161, 177), (214, 204, 111), (174, 188, 213)]

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(0)
t.hideturtle()
t.penup()


def dot(size):
    color = random.choice(color_list)
    t.dot(size, color)

def line(line_length, dot_size, spacing):
    for i in range(line_length):
        dot(dot_size)
        t.forward(spacing)

def draw_grid(width_dots, height_dots, spacing, dot_size):
    start_x = -((width_dots * spacing) / 2)
    start_y = -((height_dots * spacing) / 2)
    t.setpos(start_x, start_y)
    for i in range(height_dots):
        line(width_dots, dot_size, spacing)
        t.setpos(start_x, start_y+(spacing*(i+1)))


# t.setpos(-250,-250)
draw_grid(20,15,50,30)

screen.exitonclick()