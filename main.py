from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Crossie Yertle")
screen.tracer(0)

yertle = Player()
car_manager = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkeypress(yertle.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when Turtle Collides with Cars
    for car in car_manager.all_cars:
        if car.distance(yertle) < 25:
            score.gameOver()
            game_is_on = False

    # Detect sucessful crossing
    if yertle.finish_line():
        yertle.go_to_start()
        car_manager.level_up()
        score.increaseScore()

screen.exitonclick()