FILE_NAME = "wimbledon.csv"


def main():
    list_of_lists = account_for_utf8(FILE_NAME)
    # print(list_of_lists )
    count_name_occurrences(list_of_lists)


def account_for_utf8(file):
    """read files in UTF-8 encoding format and creat a list of lists"""
    lines = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            lines.append(parts)
    return lines


def display_champs_country_alphabetically():
    """Display the countries of the champions in alphabetical order"""


def count_name_occurrences(list_of_lists):
    """Count the occurrences of words in a text,
    stores as dictionary, sorts it and displays"""
    try:
        CHAMPS = []
        name_to_count = {}
        # words = sorted(text.split())
        for name in range(len(list_of_lists)):
            champs = list_of_lists[name][2].splitlines()
            CHAMPS += champs
        for name in CHAMPS:
            name_to_count[name] = name_to_count.get(name, 0) + 1
            # max_length = max(len(name) for name in list(name_to_count.keys()))
        for name, count in name_to_count.items():
            print(f"{name} {count}")
    except ValueError:
        print("Invalid input")
        main()


main()
