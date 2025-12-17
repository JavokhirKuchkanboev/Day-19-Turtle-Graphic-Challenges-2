import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Choose your RACER", "On Which turtle are you going to bet? Write the color: ").lower()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []
line = Turtle()
line.hideturtle()
line.penup()
line.goto(230, -200)
line.setheading(90)
line.pendown()
line.forward(400)


def race():
    finish_x = 230
    race_on = True

    while race_on:
        for turtle in turtles:
            turtle.forward(random.randint(5, 55))

            if turtle.xcor() >= finish_x:
                race_on = False
                winning_color = turtle.pencolor()

                if winning_color == user_bet:
                    print(f"You won! The {winning_color} turtle won 🏆")
                else:
                    print(f"You lost! The {winning_color} turtle won 😢")
                break

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])  # 🚀 starting line
    turtles.append(turtle)

race()

screen.exitonclick()