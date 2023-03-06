from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
turtles = ["turtle0", "turtle1", "turtle2", "turtle3", "turtle4"]

for i in range(5):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].penup()
    turtles[i].goto(-230, -100+i*50)
    turtles[i].color(colors[i])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if user_bet.lower() == turtle.pencolor().lower():
                print(f"You've won! The {turtle.pencolor()} is the winner!")
            else:
                print(f"You've lost. The {turtle.pencolor()} is the winner.")
            is_race_on = False
        else:
            turtle.forward(random.randint(0, 10))

screen.exitonclick()