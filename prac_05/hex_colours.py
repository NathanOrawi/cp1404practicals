"""
CP1404/CP5632 Practical
Colour hex code in a dictionary
"""

COLOUR_TO_HEX = {"Thistle": "#d8bfd8", "Baby Blue": "#89cff0", "Sage": "#bcb88a", "Cardinal": "#c41e3a",
                 "Smoky Black": "#100c08", "Lilac": "#c8a2c8", "Dark Moss Green": "#4a5d23",
                 "French Mauve": "#d473d4", "Khaki": "#f0e68c", "Poppy": "#fcc200", "Gray21": "#363636",
                 "HotPink4": "#8b3a62"}


def main():
    """Asks the user for the colour name and prints the hex code for it"""
    display_dictionary(COLOUR_TO_HEX)
    colour_name = (input("Enter Colour: ")).title()
    display_value(colour_name)
    """Write manu to select which function to call"""


def display_dictionary(dictionary):
    """Nicely Display the dictionary one item a line"""
    max_length = max(len(colour_name) for colour_name in list(COLOUR_TO_HEX.keys()))
    for colour, hex in COLOUR_TO_HEX.items():
        print(f"{colour:{max_length}} : {hex}")


def display_value(key):
    """Display the value of a dictionary given a key"""
    while key != "":
        try:
            print(key, "is", (COLOUR_TO_HEX[key]))
        except KeyError:
            print("Invalid colour name")
        break


main()
