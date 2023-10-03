FILE_NAME_1 = "name.txt"
FILE_NAME_2 = "numbers.txt"


def main():
    """main function, call center. HAHA"""
    # user_name = input("Name:")
    # write_name_to_file(user_name)
    # read_from_file()
    # add_two_numbers_in_file()
    add_numbers_in_file()


# def write_name_to_file(user_name):
#     """writes an input name to a file"""
#     with open(FILE_NAME_1, "w") as out_file:
#         print(user_name, file=out_file)


# def read_from_file():
#     """reads from a file"""
#     in_file = open(FILE_NAME_1)
#     for line in in_file:
#         print(f"Your name is {line}")
#     in_file.close()


# def add_two_numbers_in_file():
#     """add two numbers in a file"""
#     in_file = open(FILE_NAME_2)
#     line = in_file.read()
#     first_number = int(line.strip().split()[0])
#     second_number = int(line.strip().split()[1])
#     add = first_number + second_number
#     in_file.close()
#     print(add)


def add_numbers_in_file():
    """adds any line of numbers in the file"""
    total = 0
    in_file = open(FILE_NAME_2)
    # convert file content to list of integers
    for line in in_file:
        parts = line.strip().split(',')
        number = int(parts[0])
        total += number
    in_file.close()
    print(total)


main()
