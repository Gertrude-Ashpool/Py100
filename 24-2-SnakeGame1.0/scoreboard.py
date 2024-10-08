from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="Center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="Center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_high_score(self):
        with open('data.txt', mode='w') as data:
            data.write(f"{self.score}")

    def get_high_score(self):
        with open('data.txt') as data:
            return int(data.read())

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
