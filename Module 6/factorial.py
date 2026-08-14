# Sean Bennett
# August 14, 2026
# Problem 6: Use a for statement to calculate the factorial
# of a user-entered value and compare it with math.factorial.

import math

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    calculated_factorial = 1

    for value in range(1, number + 1):
        calculated_factorial = calculated_factorial * value

    print("Calculated factorial:", calculated_factorial)
    print("math.factorial result:", math.factorial(number))
