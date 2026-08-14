# Sean Bennett
# August 14, 2026
# Problem 3: Use random.choice to select a day of the week
# from a list and print that day.

import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

random_day = random.choice(days)
print("Random day:", random_day)
