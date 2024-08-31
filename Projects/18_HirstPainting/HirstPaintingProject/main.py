## Program used to extract the rgb values from the painting.jpg file and save the values on a separate colour list
import turtle
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

##################################################################################################################

from turtle import Turtle, Screen
import random

colour_list = [
    (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
    (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7),
    (199, 33, 132), (13, 183, 212), (230, 166, 199)
]

t = Turtle()
screen = Screen()
turtle.colormode(255)
t.hideturtle()
t.speed("fastest")
t.penup()

t.setheading(225)
t.forward(320)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(colour_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)




screen.exitonclick()

