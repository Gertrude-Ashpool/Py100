# import the Turtle class from the turtle module
from turtle import Turtle, Screen

# create an object called timmy from the Turtle class (blueprint) in the turtle module
# notice capital letter (pascal case)
timmy = Turtle()

# use the shape method
timmy.shape("turtle")
# change the color
timmy.color("IndianRed1")
# move the turtle forward by a 100
timmy.forward(100)

# create an object called my_screen from the Screen class
my_screen = Screen()

# access an attribute of the object
print(my_screen.canvheight)

# use a method of the object
my_screen.exitonclick()



