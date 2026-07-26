# Sean Bennett
# July 26, 2026
# This program calculates the area of a circle from the radius.

import math

try:
    radius = float(input("Enter the radius of the circle: "))

    if radius < 0:
        print("The radius cannot be negative.")
    else:
        area = math.pi * radius ** 2
        print(
            f"A circle with a radius of {radius:g} has an area of "
            f"{area:.2f} square units."
        )
except ValueError:
    print("Please enter a valid number for the radius.")
