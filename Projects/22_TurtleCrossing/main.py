import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move_player, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.new_car()
    carmanager.move_car()

    # Detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle reached the finish line
    if player.is_at_finish_line() == True:
        player.start()
        carmanager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
