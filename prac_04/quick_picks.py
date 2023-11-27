"""Quick Pick"""
import random

RANDOM_MIN = 1
RANDOM_MAX = 45
NUMBER_OF_COLUMN = 6

number_of_picks = int(input("How many quick picks? "))

# ROW
for i in range(0, number_of_picks, 1):
    quick_pics = []
    # COLUMN
    for j in range(0, NUMBER_OF_COLUMN, 1):
        # get random number
        random_number = random.randint(RANDOM_MIN,RANDOM_MAX)

        # if number already exist, randomise again
        while random_number in quick_pics:
            random_number = random.randint(RANDOM_MIN, RANDOM_MAX)

        # once number is not same as existing, append to list
        quick_pics.append(random_number)

    # sort list in ascending order
    quick_pics.sort()

    # print all elements in the list
    for number in quick_pics:
        print(f"{number:2}", end=" ")
    print()
