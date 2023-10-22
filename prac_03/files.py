""" different ways to read files """
FILE_NAME_1 = "name.txt"
FILE_NAME_2 = "numbers.txt"


def main():
    """main function, call center. HAHA"""
    user_name = "Bob Gru"  # input("Name:")
    write_name_to_file(user_name)
    read_from_file()
    add_numbers_in_file()


def write_name_to_file(user_name):
    """writes an input name to a file"""
    with open(FILE_NAME_1, "w") as out_file:
        print(user_name, file=out_file)


def read_from_file():
    """reads from a file"""
    in_file = open(FILE_NAME_1)
    for line in in_file:
        print(f"Your name is {line}")
    in_file.close()


def add_numbers_in_file():
    """adds any line of numbers in the file"""
    total = 0
    in_file = open(FILE_NAME_2)
    lines = in_file.readlines()
    for line in lines:
        number = int(line)
        total += number
    in_file.close()
    print(total)


main()
