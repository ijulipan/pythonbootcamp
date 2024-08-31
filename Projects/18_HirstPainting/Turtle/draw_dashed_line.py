from turtle import Turtle, Screen


t = Turtle()
screen = Screen()

for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen.exitonclick()