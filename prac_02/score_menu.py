def main():
    """Main function with menu option"""
    menu = '(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit'

    score_val = get_valid_score()

    print(menu)
    menu_choice = input('Please select an option: ').upper()

    while menu_choice != 'Q':
        if menu_choice == 'G':
            score_val = get_valid_score()

        elif menu_choice == 'P':
            print(get_result(score_val))

        elif menu_choice == 'S':
            print_stars(score_val)

        else:
            print("Invalid option")
        print(menu)
        menu_choice = input('Please select an option: ').upper()
    print('Thank You!')


def get_valid_score():
    """Ask user for a core with validation"""
    min_score_limit = 0
    max_score_limit = 100

    score_val = int(input("Enter score: "))
    while score_val < min_score_limit or score_val > max_score_limit:
        print("Invalid score")
        score_val = int(input("Enter score: "))
    return score_val


def get_result(score):
    """Determine result from score"""
    excellent_score = 90
    pass_score = 50

    if score >= excellent_score:
        result = 'Excellent'
    elif score >= pass_score:
        result = 'Pass'
    else:
        result = 'Bad'
    return result


def print_stars(num_stars):
    """Print stars according to number pass to function"""
    for i in range(0, num_stars, 1):
        print("*", end='')
    print()


main()
