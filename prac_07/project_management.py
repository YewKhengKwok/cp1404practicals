"""Project Management software
    user can..."""

# import datetime

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
        # Write Header line
        print(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        # Write Contents of each project line by line
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
        for i, project in enumerate(projects_added, 0):
            print(f"{projects_added[i]}")

        print(f"Completed projects:")
        for i, project in enumerate(projects_added, 0):
            if project.is_completed():
                print(f"{projects_added[i]}")
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
        total_choice = 0
        user_choice = 0
        for i, project in enumerate(projects_added, 0):
            print(f"{i} {projects_added[i]}")
            total_choice += 1

        # Ask user to choose project
        # Check if projects loaded
        if total_choice == 0:
            print("No projects loaded")
            is_valid_choice = True
        else:
            is_valid_choice = False
        # Validation check if project exists
        while not is_valid_choice:
            try:
                user_choice = int(input("Project choice: "))
                if (user_choice < 0) or (user_choice > total_choice-1):
                    print("Invalid option, try again: ")
                else:
                    is_valid_choice = True
                    print(f"{projects_added[user_choice]}")

                    # New percentage value, blank is same value
                    new_percentage = input("New Percentage: ")
                    if new_percentage != "":
                        projects_added[user_choice].update_percentage(new_percentage)

                    # New priority value, blank if same value
                    new_priority = input("New Priority: ")
                    if new_priority != "":
                        projects_added[user_choice].update_priority(new_priority)

                    # TESTING
                    print(f"{projects_added[user_choice]}")

            except ValueError:
                print("Not a number, try again: ")

        print(f"")

    else:
        # Invalid input
        print(f"Invalid input")

    print(MENU)
    choice = input("> ").upper()

print(f"Thank you for using custom-built project management software.")
