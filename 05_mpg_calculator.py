# Sean Bennett
# July 26, 2026
# This program calculates a car's miles per gallon (MPG).

try:
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons used: "))

    if miles_driven < 0:
        print("Miles driven cannot be negative.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero.")
    else:
        mpg = miles_driven / gallons_used
        print(f"The car's fuel economy is {mpg:.2f} miles per gallon.")
except ValueError:
    print("Please enter valid numbers for miles and gallons.")
