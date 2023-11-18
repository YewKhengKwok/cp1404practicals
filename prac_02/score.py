"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import *


def main():
    """Main"""
    min_score_limit = 0
    max_score_limit = 100
    score = float(input("Enter score: "))
    while score < min_score_limit or score > max_score_limit:
        print("Invalid score");
        score = float(input("Enter score: "))
    output = get_result(score)
    print(output)

    print(f'Your random score is:', get_random_score(min_score_limit, max_score_limit))


def get_result(score):
    """Determine result from score"""
    if score >= 90:
        result = 'Excellent'
    elif score >= 50:
        result = 'Pass'
    else:
        result = 'Bad'
    return result


def get_random_score(min_score, max_score):
    """Generate random score between min and max value set"""
    return randrange(min_score, max_score)


main()
