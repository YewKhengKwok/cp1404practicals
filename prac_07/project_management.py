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
in_file = ''

print(MENU)
choice = input("> ").upper()

while choice != "Q":
    if choice == "L":
        # Load Projects from file, clear list on each load
        projects_added = []
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
            add_project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            # Add the project we've just constructed to the list
            projects_added.append(add_project)

        # Close file after reading
        in_file.close()

        # TESTING
        print(projects_added)
        print(f"")

    elif choice == "S":
        # Save Projects to file
        # Ask user for save file name
        # TESTING
        filename_to_save = 'test.txt'
        # filename_to_save = input("Save as?: ")
        out_file = open(filename_to_save, 'w')
        # Header
        print(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        # Contents
        for project in projects_added:
            print(f"{project.name}	{project.start_date}	{project.priority}	"
                  f"{project.cost_estimate:.1f}	{project.completion_percentage}", file=out_file)

        # Close file after writing
        out_file.close()
        print(f"Saved successfully to {filename_to_save}")
        print(f"")

    elif choice == "D":
        # Sort by priority (highest to lowest)
        projects_added.sort(key=lambda x: x.priority)
        # Display Projects
        print(f"Incomplete projects:")
        for project in projects_added:
            if not project.is_completed():
                print(f"{project.name}, start: {project.start_date}, priority {project.priority}, "
                      f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

        print(f"Completed projects:")
        for project in projects_added:
            if project.is_completed():
                print(f"{project.name}, start: {project.start_date}, priority {project.priority}, "
                      f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

        print(f"")

    elif choice == "F":
        # Filter Projects by date
        print(f"")

    elif choice == "A":
        # Add new Project
        print(f"Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = input("Priority: ")
        cost_estimate = input("Cost estimate: $")
        percent_completed = input("Percent Completed: ")

        # create class objects with user input details
        add_project = Project(name, start_date, priority, cost_estimate, percent_completed)
        # Add the project we've just constructed to the list
        projects_added.append(add_project)

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
