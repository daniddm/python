import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #crossing ok
    
    if turtle.is_at_finish_line():
        turtle.go_to_star()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()