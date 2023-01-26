import time
from turtle import Screen
from player import Player
from border import Border
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

b = Border()
b.create_border()
p = Player()

cars = CarManager()

sr = Scoreboard()
screen.onkey(p.move_turtle, "w")
screen.listen()
# cars.all_cars
count = 0
game_is_on = True
while game_is_on:
    if count % 6 == 0:
        cars.create_car()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(p) < 20:
            game_is_on = False
    count += 1
    if p.reset():
        sr.update_score()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
