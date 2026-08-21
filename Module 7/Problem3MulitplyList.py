# Sean Bennett
# August 21, 2026
# Problem 3: Multiply all numbers in the list [5, 2, 7, -1].

def multiplyList(numbers):
    product = 1
    for number in numbers:
        product = product * number
    return product

numbers = [5, 2, 7, -1]
print("Product:", multiplyList(numbers))
