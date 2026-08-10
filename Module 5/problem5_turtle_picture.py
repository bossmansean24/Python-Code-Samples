# Sean Bennett
# August 7, 2026
# This program uses turtle graphics and loops to draw a simple flower.

import turtle

artist = turtle.Turtle()
artist.speed(0)

for petal in range(12):
    for side in range(2):
        artist.circle(60, 60)
        artist.left(120)
    artist.left(30)

artist.penup()
artist.goto(0, -20)
artist.pendown()
artist.begin_fill()
artist.circle(20)
artist.end_fill()

artist.right(90)
artist.penup()
artist.goto(0, -20)
artist.pendown()
artist.forward(180)

artist.left(45)
for leaf in range(2):
    for side in range(2):
        artist.circle(45, 60)
        artist.left(120)
    artist.right(90)

turtle.done()
