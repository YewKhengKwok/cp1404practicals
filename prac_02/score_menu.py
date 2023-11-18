def main():
    """Main function with menu option"""
    menu = '(G)et a valid score' + '\n' + '(P)rint result' + '\n' + '(S)how stars' + '\n' + '(Q)uit'

    score_val = get_valid_score()

    print(menu)
    menu_choice = input('Please select an option: ').upper()

    while menu_choice != 'Q':
        if menu_choice == 'G':
            score_val = get_valid_score()

        elif menu_choice == 'P':
            print(get_result(score_val))

        elif menu_choice == 'S':
            for i in range(0, int(score_val), 1):
                print("*", end='')
            print()

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
    if score >= 90:
        result = 'Excellent'
    elif score >= 50:
        result = 'Pass'
    else:
        result = 'Bad'
    return result


main()
