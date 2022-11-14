from turtle import *
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue", "purple"]
y_position = [-70, -40, -10, 20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230 , y = y_position[turtle_index])
    all_turtles.append(new_turtle)
    
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if user_bet == winning:
                print(f"You've won !!! the {winning} turtle is winner !!!")
            else:
                print(f"You've lost !!! the {winning} turtle is winner !!!")
                
        rando_choice = random.randint(0,10)
        turtle.forward(rando_choice)

screen.exitonclick()