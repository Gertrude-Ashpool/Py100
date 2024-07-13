from turtle import Turtle
import random

# create Food() class
# inherit from Turtle() class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        # render food as small circle
        # move to new random location upon touch
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
