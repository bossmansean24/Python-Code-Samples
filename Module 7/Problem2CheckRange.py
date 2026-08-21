# Sean Bennett
# August 21, 2026
# Problem 2: Check whether a number is in range(1, 10)
# and print whether it is in or not in the range.

def checkRange(number):
    if number in range(1, 10):
        print(number, "is in the range.")
    else:
        print(number, "is not in the range.")

number = int(input("Enter a number: "))
checkRange(number)
