from guitar import Guitar


def main():
    """Read file of guitars details, save as objects, display."""
    guitars = []
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
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all guitars from oldest (using their repr and lt method)
    for guitar in sorted(guitars):
        print(guitar)


main()
