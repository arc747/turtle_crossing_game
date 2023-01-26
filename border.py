from turtle import Turtle

X = 250
Y = 280


class Border:

    def __init__(self):
        self.t = Turtle()
        self.t.ht()
        self.t.speed("fastest")

    def create_border(self):
        self.t.penup()
        self.t.goto(X, Y)
        self.t.pendown()
        self.t.pencolor("black")
        self.t.width(3)
        self.t.goto(X, -Y)
        self.t.goto(-X, -Y)
        self.t.goto(-X, Y)
        self.t.goto(X, Y)

