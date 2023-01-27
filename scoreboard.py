from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-230, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ", align="center", font=FONT)