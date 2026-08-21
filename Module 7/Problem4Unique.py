# Sean Bennett
# August 21, 2026
# Problem 4: Return a new list containing unique elements
# from [1, 3, 3, 3, 6, 2, 3, 5] using append.

def uniqueValues(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

numbers = [1, 3, 3, 3, 6, 2, 3, 5]
print("Unique list:", uniqueValues(numbers))
