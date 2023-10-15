from random import randint

# Write a program that asks the user how many "quick picks" they wish to generate
quick_picks = []
number_of_quick_picks = int(input("How many quick picks? "))
# generates that many lines of output
for number_of_quick_pick in range(number_of_quick_picks):
    for number in range(6):
        quick_pick = [randint(1, 45)]
        quick_picks += quick_pick
    print("{:3}{:3}{:3}{:3}{:3}{:3}".format(*quick_picks[-6:]))