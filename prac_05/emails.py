"""
CP1404 Prac 5

Word Occurrences
Estimate: 20 minutes
Actual: 50 minutes
"""
EMAIL_TO_NAME = {}


def main():
    """Asks user for email and displays name and email"""
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        EMAIL_TO_NAME[email] = name
        response = input(f"Is your name {name}? (Y/n) ")
        if (response != "Y") and (response != ""):
            correct_name = input("Name: ")
            EMAIL_TO_NAME[email] = correct_name
        email = input("Email: ")
    display_name_and_email()


def extract_name(email):
    """extracts name from email address"""
    name = ' '.join(email.split("@")[0].split("."))
    return name.title()


def display_name_and_email():
    """creates a dictionary of email to name and displays it"""
    # max_length = max(len(name) for name in list(EMAIL_TO_NAME.keys()))
    for email, name in EMAIL_TO_NAME.items():
        print(f"{name} ({email})")


main()
