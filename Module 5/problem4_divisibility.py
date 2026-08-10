# Sean Bennett
# August 7, 2026
# This program checks the integers from 1 through 50.
# It prints a message for numbers divisible by 3, 5, or both.

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)
