from turtle import *
import math

charles = Turtle()

setup(500,300)
x_pos = 0
y_pos = 0
charles.setposition(0,0)

charles.pendown


square_sides = 4
for count in range(square_sides):
    begin_fill("red")
    charles.right(90)
    charles.forward(50)
    end_fill("red")

exitonclick()
