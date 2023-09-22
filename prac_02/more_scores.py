"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Main function"""
    number_of_scores = int(input("Enter number of scores: "))
    text_file = open('results.txt', 'w')
    for score in range(number_of_scores):
        current_score = random.randint(0, 100)
        result = display_score(current_score)
        text_file.write(f"{current_score} is {result}\n")
    text_file.close()


def display_score(score):
    """Display result of score"""
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
