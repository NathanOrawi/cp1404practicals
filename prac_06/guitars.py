"""
CP1404 Do-from-scratch Exercise
Estimated Duration: 30 min
Actual Duration: 45 min
"""

from guitar import Guitar

CURRENT_YEAR = 2023


def main():
    """Creates a list to store all the user's guitars
    (keep inputting until they enter a blank name), then print their details"""
    guitars = []
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Year and Cost must be a number. Try again!!!")

    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    display_collection(guitars)


def display_collection(guitars):
    """Displays the details of the user's guitar in a readable manner """
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage(CURRENT_YEAR):
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
