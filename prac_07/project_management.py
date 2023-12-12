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

projects_added = []

print(MENU)
choice = input("> ").upper()

while choice != "Q":
    if choice == "L":
        # Load Projects
        # Error check if invalid file
        is_valid_file = False
        while not is_valid_file:
            # TESTING
            filename_to_load = 'projects.txt'
            # filename_to_load = input("What is the filename?: ")
            try:
                in_file = open(filename_to_load, 'r')
            except FileNotFoundError:
                print("Invalid filename")
            finally:
                print(f"{filename_to_load} successfully loaded!")
                is_valid_file = True

        # Read file
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split('	')
            # create class objects with parts stripped
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            # Add the project we've just constructed to the list
            projects_added.append(Project)

        # Close file after reading
        in_file.close()

        # TESTING
        print(projects_added)
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
