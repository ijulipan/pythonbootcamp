# Documentations

# Turtle graphics documentation: https://docs.python.org/3/library/turtle.html
# Turtle colors documentation: https://cs111.wellesley.edu/reference/colors

from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
print(timmy)

#Object attribute
print(my_screen.canvheight)

#Object method
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen.exitonclick()