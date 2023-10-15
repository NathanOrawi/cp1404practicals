"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    """Asks the user for their 'short' state and prints the full state once"""
    display_dictionary(CODE_TO_NAME)
    state_code = (input("Enter short state: ")).upper()
    display_value(state_code)
    """Write manu to select which function to call"""


def display_dictionary(dictionary):
    """Display the dictionary one item a line"""
    for state_code in dictionary:
        print(f"{state_code:3} is {dictionary[state_code]:3}")


def display_value(key):
    """Display the value of a dictionary given a key"""
    while key != "":
        try:
            print(key, "is", CODE_TO_NAME[key])
        except KeyError:
            print("Invalid short state")
        break

main()
