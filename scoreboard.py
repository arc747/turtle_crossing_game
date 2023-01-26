from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, align="center", font=FONT)
        self.score += 1
