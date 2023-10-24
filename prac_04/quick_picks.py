"""
CP1404/CP5632 Practical
Quick picks generator
"""

from random import randint


def main():
    """asks the user how many "quick picks" they wish to generate"""
    number_of_quick_picks = int(input("How many quick picks? "))
    # generates that many lines of output
    generate_quick_picks(number_of_quick_picks)


def generate_quick_picks(number_of_quick_picks):
    """The function generates argument defined lines of output.
    Each line consists of 6 random numbers between 1 and 45"""
    quick_picks = []
    for number_of_quick_pick in range(number_of_quick_picks):
        for number in range(6):
            quick_pick = [randint(1, 45)]
            quick_picks += quick_pick
        print("{:3}{:3}{:3}{:3}{:3}{:3}".format(*quick_picks[-6:]))


main()
