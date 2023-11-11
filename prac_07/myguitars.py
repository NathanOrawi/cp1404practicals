from guitar import Guitar

GUITARS = []


def main():
    """Read file of guitars details, save as objects, display."""
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are guitar data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        print(parts)  # debugging
        # Construct a Guitar object using the elements
        # year should be an int
        guitar = Guitar(parts[0], parts[1], parts[2])
        # Add the language we've just constructed to the list
        GUITARS.append(guitar)
    # get guitar details from user
    get_guitar()
    # Close the file as soon as we've finished reading it
    in_file.close()

    load_guitar()


def load_guitar():
    """Loop through and write all guitars from oldest (using their repr and lt method)"""
    out_file = open('guitars.csv', 'w')
    for guitar in sorted(GUITARS):
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def get_guitar():
    """Creates objects to store all the user's guitars
    (keep inputting until they enter a blank name), then print their details"""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        try:
            input_year = int(input("Year: "))
            year = str(input_year)  # Class takes string
            input_cost = int(input("Cost: "))
            cost = str(input_cost)  # Class takes string
            GUITARS.append(Guitar(name, year, cost))
        except ValueError:
            print("Year and Cost must be a number. Try again!!!")
        name = input("Name: ")
    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)


main()
