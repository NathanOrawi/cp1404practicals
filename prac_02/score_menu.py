"""Score menu"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """main function"""
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter score: "))
            while 0 > score > 100:
                print("Invalid score input")
                score = float(input("Enter score: "))
            print("score is valid")
        elif choice == 'P':
            score = float(input("Enter score: "))
            result = display_score(score)
            print(result)
        elif choice == 'S':
            score = int(input("Enter score: "))
            as_many_stars = show_star(score)
            print(as_many_stars)
        else:
            print("Invalid error message")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Taa!")


def display_score(score):
    """displays the result of score"""
    if 100 < score > 0:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def show_star(length):
    """displays equivalent star of score """
    amount = '*' * length
    return amount


main()
