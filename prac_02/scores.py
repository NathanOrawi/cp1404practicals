"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    result = display_score(score)
    print(result)


def display_score(score):
    if 100 < score > 0:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()
