from random import randint

# Write a program that asks the user how many "quick picks" they wish to generate
QUICK_PICKS = []
number_of_quick_picks = int(input("How many quick picks? "))
# generates that many lines of output

# for quick_pick in range(6):
for number_of_quick_pick in range(number_of_quick_picks):
    for number in range(6):
        QUICK_PICK = [randint(1, 45)]
        QUICK_PICKS += QUICK_PICK
    quick_picks_row = (QUICK_PICKS[-6:])
    print(sorted(quick_picks_row))
    # for i in range(len(quick_picks_row)):
    #     print(quick_picks_row[i])