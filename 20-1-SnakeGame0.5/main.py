import time
from turtle import Screen
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jake the Snake")
screen.tracer(0)



# create the initial snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.left, key="a")
screen.onkey(snake.right, key="d")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()