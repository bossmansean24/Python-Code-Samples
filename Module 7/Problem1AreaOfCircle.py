# Sean Bennett
# August 21, 2026
# Problem 1: Write a function areaOfCircle(r) which returns
# the area of a circle of radius r using the math module.

import math

def areaOfCircle(r):
    return math.pi * r ** 2

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", areaOfCircle(radius))
