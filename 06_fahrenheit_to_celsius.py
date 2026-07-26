# Sean Bennett
# July 26, 2026
# This program converts Fahrenheit to Celsius.

try:
    fahrenheit = float(
        input("Enter the temperature in degrees Fahrenheit: ")
    )
    celsius = (fahrenheit - 32) * 5 / 9
    print(
        f"{fahrenheit:g} degrees Fahrenheit is "
        f"{celsius:.2f} degrees Celsius."
    )
except ValueError:
    print("Please enter a valid temperature.")
