from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

colours = ["blue", "lime", "red", "yellow", "blue violet", "medium spring green", "black", "sienna", "pale goldenrod"]

def different_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_size_n in range(3, 11):
    t.color(random.choice(colours))
    different_shape(shape_size_n)