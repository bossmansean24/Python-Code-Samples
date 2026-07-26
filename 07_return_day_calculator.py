# Sean Bennett
# July 26, 2026
# This program calculates the return day after a vacation.

days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

try:
    starting_day = int(input("Enter the starting day number (0-6): "))
    stay_length = int(input("Enter the number of nights you will stay: "))

    if starting_day < 0 or starting_day > 6:
        print("The starting day must be a number from 0 through 6.")
    elif stay_length < 0:
        print("The length of stay cannot be negative.")
    else:
        return_day = (starting_day + stay_length) % 7
        print(
            f"You will return on day {return_day}, "
            f"which is {days[return_day]}."
        )
except ValueError:
    print("Please enter whole numbers only.")
