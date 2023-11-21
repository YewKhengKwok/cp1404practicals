def main():
    """Main"""
    password_length = 10
    password = get_password(password_length)
    print_stars(password)


def get_password(min_password_length):
    """Get password from user function"""
    password = input('Please enter your password: ')
    while len(password) < min_password_length:
        password = input('Please try again: ')
    return password


def print_stars(input_password):
    """Print stars according to length of input password"""
    for i in range(0, len(input_password), 1):
        print("*", end='')


main()
