# Sean Bennett
# August 7, 2026
# This program prints each number in a list and then prints
# each number together with its square.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Numbers:")
for number in numbers:
    print(number)

print("\nNumbers and their squares:")
for number in numbers:
    print(number, number ** 2)
