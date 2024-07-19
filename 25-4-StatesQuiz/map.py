from turtle import Turtle

FONT = ("Arial", 12, "normal")


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def mark(self, location, name_of_state):
        self.goto(location)
        self.write(name_of_state, align="Center", font=FONT)
