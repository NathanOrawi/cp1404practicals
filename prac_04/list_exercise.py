"""
CP1404/CP5632 Practical
Intermediate Exercises
"""

"""Basic list operations"""
number_of_entries = 3
numbers = []
for number_of_entry in range(1, number_of_entries + 1):
    number = int(input(f"Enter number {number_of_entry} of {number_of_entries}: "))
    numbers.append(number)
    print(numbers)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average_of_numbers = sum(numbers) / len(numbers)
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average_of_numbers}")

"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("User name: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")