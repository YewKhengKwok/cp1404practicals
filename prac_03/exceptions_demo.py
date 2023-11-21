"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When input is not an integer

2. When will a ZeroDivisionError occur?
- When you try to divide by 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator < 1:
        print('Cannot divide by 0, try again')
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")