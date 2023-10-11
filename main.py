from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    newturtle = Turtle(shape="turtle")
    newturtle.color(colors[turtle_index])
    newturtle.penup()
    newturtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(newturtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race!")
            else:
                print(f"You lost. The {winning_color} turtle won the race.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.home()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")

screen.exitonclick()