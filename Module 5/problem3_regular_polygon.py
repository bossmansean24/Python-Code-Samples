# Sean Bennett
# August 7, 2026
# This program asks the user for the number of sides, side length,
# line color, and fill color, then draws and fills a regular polygon.

import turtle

number_of_sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

angle = 360 / number_of_sides

pen = turtle.Turtle()
pen.pencolor(line_color)
pen.fillcolor(fill_color)

pen.begin_fill()
for side in range(number_of_sides):
    pen.forward(side_length)
    pen.left(angle)
pen.end_fill()

turtle.done()
