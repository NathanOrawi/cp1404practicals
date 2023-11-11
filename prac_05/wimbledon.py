"""CP1404 Prac 5

Write a program to read this file, process
the data and display processed information."""

FILE_NAME = "wimbledon.csv"


def main():
    """"read file, process the data and display processed information"""
    winners_data = account_for_utf8(FILE_NAME)
    display_champs_and_victories(winners_data)
    display_champs_country_alphabetically(winners_data)


def account_for_utf8(file):
    """read files in UTF-8 encoding format and creat a list of lists"""
    lines = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            lines.append(parts)
    return lines


def display_champs_country_alphabetically(list_of_lists):
    """Display the countries of the champions in alphabetical order"""
    champs_country = []
    country_to_count = {}
    for country in range(len(list_of_lists)):
        countries = list_of_lists[country][1].splitlines()
        champs_country += countries
    for country in champs_country:
        country_to_count[country] = country_to_count.get(country, 0) + 1
    number_of_country = len(country_to_count)
    country = ', '.join(sorted(list(country_to_count.keys())))
    print(f"\nThis {number_of_country} countries have won Wimbledon: \n{country}")


def display_champs_and_victories(list_of_lists):
    """Count the occurrences of words in a text,
    stores as dictionary, sorts it and displays"""
    champs = []
    name_to_count = {}
    for name in range(len(list_of_lists)):
        champ = list_of_lists[name][2].splitlines()
        champs += champ
    for name in champs:
        name_to_count[name] = name_to_count.get(name, 0) + 1
    for name, count in name_to_count.items():
        print(f"{name} {count}")


main()
