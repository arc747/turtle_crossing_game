from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):

    def __init__(self):
        super().__init__()
        # self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.goto(0, self.ycor() + 10)

    def reset(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
