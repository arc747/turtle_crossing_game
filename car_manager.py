import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # super().__init__()
        # self.t = Turtle()
        self.all_cars = []

    def create_car(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(1, 2)
        t.color(random.choice(COLORS))
        t.penup()
        t.goto(250, random.randrange(-220, 220, 20))
        t.setheading(180)
        self.all_cars.append(t)
        # for i in (range(-240, 240, 20)):
        #     self.t.goto(250, i)

    def move_car(self):
        for car in self.all_cars:
            if car.xcor() > -250:
                car.fd(STARTING_MOVE_DISTANCE)
            else:
                car.goto(250, random.randrange(-220, 220, 20))
                car.fd(STARTING_MOVE_DISTANCE)
    #
    # def create_cars(self):
    #     for i in (range(-240, 240, 20)):
    #         self.t.goto(250, i)
    #         self.move_car()
