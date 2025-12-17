from turtle import Turtle, Screen

timy = Turtle()
current_position = timy.position
screen = Screen()

def forward():
    timy.forward(10)

def backward():
    timy.backward(10)

def counter_clockwise():
    timy.right(-10)

def clockwise():
    timy.right(10)

def clear():
    timy.clear()  # remove drawings
    timy.penup()  # lift pen so it doesn't draw while moving
    timy.home()  # go to center (0, 0)
    timy.pendown()  # start drawing again


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)








screen.exitonclick()