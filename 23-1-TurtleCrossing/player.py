from turtle import Turtle

STARTING_POSITION = (0, -280)
UP = 90
DOWN = 270
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.seth(UP)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
