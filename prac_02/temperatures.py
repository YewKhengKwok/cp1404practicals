def main():
    """Main"""

    user_input_value = input('Please enter your value: ')

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            output = celsius_fahrenheit(user_input_value)
            print(f"Result: {output:.2f} F")
        elif choice == "F":
            output = fahrenheit_celsius(user_input_value)
            print(f"Result: {output:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_fahrenheit(user_input_value):
    """Convert celsius to fahrenheit"""
    fahrenheit = float(user_input_value) * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_celsius(user_input_value):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (float(user_input_value) - 32)
    return celsius


main()
