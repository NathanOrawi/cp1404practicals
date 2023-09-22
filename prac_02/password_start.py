"""Asks user for password"""
PASSWORD = "John6"


def main():
    user_password = input("Password: ")
    while user_password != PASSWORD:
        print("Incorrect password")
        print_line(len(user_password))
        user_password = input("Password: ")
    print_line(len(user_password))
    print("Correct password")


def print_line(length=20, pen="*"):
    print(pen * length)


main()