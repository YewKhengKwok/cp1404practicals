def main():
    """Main"""

    user_input_value = input('Please enter your value: ')

    menu = 'C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit'

    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(f"Result: {celsius_fahrenheit(user_input_value):.2f} F")
        elif choice == "F":
            print(f"Result: {fahrenheit_celsius(user_input_value):.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_fahrenheit(user_input_value):
    """Convert celsius to fahrenheit"""
    return float(user_input_value) * 9.0 / 5 + 32


def fahrenheit_celsius(user_input_value):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (float(user_input_value) - 32)


main()
