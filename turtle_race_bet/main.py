from turtle import Turtle,Screen
import random

screen = Screen()

screen.setup(width=500,height=400)

is_game_on = False

user_bet = screen.textinput(title="Make your bet",prompt="On which turtle you bet on?")

color = ["blue","red","purple","orange"]
Y_position = [-40,-10,20,50]
turtle_list = []

for turtle_index in range(0,4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=Y_position[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle is winner")
            else:
                print(f"You lost! The {winning_color} turtle is winner")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()