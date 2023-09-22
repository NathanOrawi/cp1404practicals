from scores import display_score
from password_start import hide_character

MENU = """G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input("Choice: ")
    while choice != 'Q':
        score = float(input("Enter score: "))
        if choice == 'G':
            while 0 > score > 100:
                print("Invalid score input")
                score = float(input("Enter score: "))
        elif choice == 'P':
            result = display_score(score)
            print(result)
        elif choice == 'S':
            as_many_stars = hide_character(score)
            print(as_many_stars)
        else:
            print("Invalid error message")
        print(MENU)
        choice = input("Choice: ")
    print("Taa!")


main()
