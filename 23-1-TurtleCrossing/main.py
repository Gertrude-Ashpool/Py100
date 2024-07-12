import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.spawn_car(15)
    car_manager.move_cars()
    screen.update()

# Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 30 and player.ycor() - 10 < car.ycor() < player.ycor() + 10:
            game_is_on = False
            scoreboard.game_over()

# Detect when turtle reached the other side
    if player.ycor() > 270:
        scoreboard.increase_level()
        car_manager.level_up()
        player.refresh()

screen.exitonclick()
