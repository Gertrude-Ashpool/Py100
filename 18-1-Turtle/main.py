from turtle import Turtle, Screen

# initiate our instance based on the turtle class
timmy_the_turtle = Turtle()
# change the shape to an arrow
timmy_the_turtle.shape("arrow")
# change the color
timmy_the_turtle.color("lightsteelblue")
# move the turtle
timmy_the_turtle.forward(100)
# rotate the turtle
timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
