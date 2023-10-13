number_of_entries = 5
numbers = []
for number_of_entry in range(1, number_of_entries + 1):
    number = int(input(f"Enter number {number_of_entry} of {number_of_entries}: "))
    numbers.append(number)
    print(numbers)
