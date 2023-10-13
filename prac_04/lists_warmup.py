"""What values do the following expressions have? Without running the code, record your answers to these questions in your Python file as a comment.
Then use the Python console to see if you were correct."""
numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0]
#     3
# numbers[-1]
#     2
# numbers[3]
#     1
# numbers[:-1]
#     [2, 9, 5, 1, 4, 1, 3]
# numbers[3:4]
#     [1, 4]
# 5 in numbers
#     true
# 7 in numbers
#     false
# "3" in numbers
#     false
# numbers + [6, 5, 3]
#     [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[0] = 10
print(numbers)
"""Change the last element of numbers to 1"""
numbers[-1] = 1
print(numbers)
"""Print all the elements from numbers except the first two (slice)"""
print(numbers[2:])
"""Print whether 9 is an element of numbers"""
print(f"{9 in numbers}")
print(numbers)
