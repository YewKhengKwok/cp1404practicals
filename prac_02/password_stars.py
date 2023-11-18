def main():
    """Main"""
    get_password(10)


def get_password(min_password_length):
    """Get password from user function"""
    password = input('Please enter your password: ')
    while len(password) < min_password_length:
        password = input('Please try again: ')

    for i in range(0, len(password), 1):
        print("*", end='')


main()
