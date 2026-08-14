# Sean Bennett
# August 14, 2026
# Problem 5: Convert a user-entered value in radians to degrees.
# Print the manually calculated value and math.degrees result.

import math

radians = float(input("Enter a value in radians: "))

calculated_degrees = radians * 180 / math.pi

print("Calculated degrees:", calculated_degrees)
print("math.degrees result:", math.degrees(radians))
