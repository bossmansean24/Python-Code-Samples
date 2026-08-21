# Sean Bennett
# August 21, 2026
# Problem 5: Use turtle and a function to draw nested squares
# similar to the image shown in the assignment.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
alex.speed(0)

size = 20
for i in range(5):
    drawSquare(alex, size)
    alex.penup()
    alex.right(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(10)
    alex.right(180)
    alex.pendown()
    size = size + 20

wn.exitonclick()
