from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()

#For loop to create a square
for rotation in range(4):
    timmy.forward(100)
    timmy.left(90)

screen.exitonclick()