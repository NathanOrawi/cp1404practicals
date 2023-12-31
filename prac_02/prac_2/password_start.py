"""Asks user for password and display stars
the length of the entered characters"""
PASSWORD = "John6"


def main():
    user_password = get_password()
    symbol = hide_character(len(user_password))
    print(f"Correct password\n {symbol}")


def get_password():
    user_password = input("Password: ")
    while user_password != PASSWORD:
        print("Incorrect password")
        hide_character(len(user_password))
        user_password = input("Password: ")
    return user_password


def hide_character(length):
    return '*' * length


main()