"""Project Management"""

import datetime

from project import Project

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

MENU = ("(L)oad projects \n" "(S)ave projects \n" "(D)isplay projects \n"
        "(F)ilter projects by date \n" "(A)dd new project \n" "(U)pdate project \n"
        "(Q)uit")

print(MENU)
choice = input("> ").upper()

while choice != "Q":
    if choice == "L":
        # Load Projects
        print(f"")

    elif choice == "S":
        # Save Projects
        print(f"")

    elif choice == "D":
        # Display Projects
        print(f"")

    elif choice == "F":
        # Filter Projects by date
        print(f"")

    elif choice == "A":
        # Add new Projects
        print(f"")

    elif choice == "U":
        # Update Projects
        print(f"")

    else:
        # Invalid input
        print(f"Invalid input")
        print(MENU)
        choice = input("> ").upper()

print(f"Thank you for using custom-built project management software.")
