MENU = """ E - Show the even numbers from x to y
O - Show the odd numbers from x to y
S - Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
Q - Exit the program
"""
start_number = int(input("Enter starting number: "))
end_number = int(input("Enter ending number: "))
print(MENU)
operation = input(">>> ").upper()
while operation != "Q":
    if operation == "E":
        is_start_number_even = start_number % 2
        if is_start_number_even == 0:
            for even_number in range(start_number, end_number, 2):
                print(even_number)
        else:
            for even_number in range(start_number + 1, end_number, 2):
                print(even_number)
    elif operation == "O":
        is_start_number_odd = start_number % 2
        if is_start_number_odd == 0:
            for odd_number in range(start_number + 1, end_number, 2):
                print(odd_number)
        else:
            for odd_number in range(start_number, end_number, 2):
                print(odd_number)
    elif operation == "S":
        for number_to_square in range(start_number, end_number):
            squared_number = number_to_square * number_to_square
            print(squared_number)
    else:
        print("wrong letter entered. try again")
    print(MENU)
    operation = input(">>> ").upper()
print("Exit the program")