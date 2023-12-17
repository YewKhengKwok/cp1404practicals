"""Project Management software
    user can load, save, display by priority, sort by date, add new and update projects"""

import datetime

from project import Project

MENU = ("(L)oad projects \n" "(S)ave projects \n" "(D)isplay projects \n"
        "(F)ilter projects by date \n" "(A)dd new project \n" "(U)pdate project \n"
        "(Q)uit")


def main():
    """Main function, handles MENU system and calls respective function"""
    projects_added = []

    # MENU system, Q for quit
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "L":
            # Load Projects from file,
            projects_added = load_projects()

        elif choice == "S":
            # Save Projects to file
            save_projects(projects_added)

        elif choice == "D":
            # Sort the projects by priority (highest to lowest)
            display_projects(projects_added)

        elif choice == "F":
            # Filter Projects by date
            filter_projects(projects_added)

        elif choice == "A":
            # Add new Project
            new_project(projects_added)

        elif choice == "U":
            # Update Project
            update_project(projects_added)

        else:
            # Invalid input for MENU
            print(f"Invalid input")

        # Print MENU and ask for user input after selected function before has completed
        print(MENU)
        choice = input("> ").upper()

    # Quit message
    print(f"Thank you for using custom-built project management software.")


def load_projects():
    """Load projects from file function"""
    in_file = ''
    # clear list on each load
    projects_added = []
    # Error check if invalid file
    is_valid_file = False
    while not is_valid_file:
        filename_to_load = input("What is the filename?: ")
        try:
            in_file = open(filename_to_load, 'r')
            print(f"{filename_to_load} successfully loaded!")
            is_valid_file = True
        except FileNotFoundError:
            print("Invalid filename")
    # Read file
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    for line in in_file:
        # Strip newline from end and split it into parts
        parts = line.strip().split('	')
        # create class objects with parts stripped
        # name, start_date, priority, cost_estimate, completion_percentage
        add_project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        # Add the project we've just constructed to the list
        projects_added.append(add_project)
    # Close file after reading
    in_file.close()
    return projects_added


def save_projects(projects_added):
    """Save projects to file function"""
    # Ask user for save file name
    filename_to_save = input("Save as? (eg text.txt): ")
    out_file = open(filename_to_save, 'w')
    # Write Header line
    print(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
    # Write Contents of each project line by line
    for project in projects_added:
        print(f"{project.name}	{project.start_date.strftime('%d/%m/%Y')}	{project.priority}	"
              f"{project.cost_estimate:.1f}	{project.completion_percentage}", file=out_file)
    # Close file after writing
    out_file.close()
    print(f"Saved successfully to {filename_to_save}")


def display_projects(projects_added):
    """Sort the projects by priority (highest to lowest) function"""
    # Sort by priority
    projects_added.sort(key=lambda x: x.priority)
    # Display Projects
    print(f"Incomplete projects:")
    for i, project in enumerate(projects_added, 0):
        if not project.is_completed():
            print(f"{projects_added[i]}")
    print(f"Completed projects:")
    for i, project in enumerate(projects_added, 0):
        if project.is_completed():
            print(f"{projects_added[i]}")


def filter_projects(projects_added):
    """Filter Projects by date function"""
    # User input date to check
    date_string_input = input("Show projects that start after date (dd/mm/yy): ")
    # Convert string to date format
    date_to_check = datetime.datetime.strptime(date_string_input, "%d/%m/%Y").date()
    # Sort the projects by date
    projects_added.sort(key=lambda x: x.start_date)
    # Display projects that starts after the user date
    for i, project in enumerate(projects_added, 0):
        if project.start_date >= date_to_check:
            print(f"{projects_added[i]}")


def new_project(projects_added):
    """Add new Project function"""
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


def update_project(projects_added):
    """Update project function"""
    total_choice = 0
    # Display all projects
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
            if (user_choice < 0) or (user_choice > total_choice - 1):
                print("Invalid option, try again: ")
            else:
                is_valid_choice = True
                print(f"{projects_added[user_choice]}")

                # New percentage value, blank if same value
                new_percentage = input("New Percentage: ")
                if new_percentage != "":
                    projects_added[user_choice].update_percentage(new_percentage)

                # New priority value, blank if same value
                new_priority = input("New Priority: ")
                if new_priority != "":
                    projects_added[user_choice].update_priority(new_priority)

        except ValueError:
            print("Not a number, try again: ")


main()
