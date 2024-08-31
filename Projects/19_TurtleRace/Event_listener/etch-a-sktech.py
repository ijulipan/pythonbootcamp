from turtle import Turtle,Screen

t = Turtle()
screen = Screen()


def forward():
    t.forward(10)


def reverse():
    t.backward(10)


def left():
    t.left(10)


def right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=reverse)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()