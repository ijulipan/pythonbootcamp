from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


# Initiates the program to start listening for user input
screen.listen()
# Sets what should happen when a certain key is pressed
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()