from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# initialise playing field
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong's not dead")

# create the two paddles with their starting positions
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

# set screen to listen to keystrokes
screen.listen()
# left paddle listens to w and s key
screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")
# right paddle controlled by up and down arrows
screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")

# main game loop

game_is_on = True

while game_is_on:
    # speed of the ball movement
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball passes left boundary
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if ball passes right boundary
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
