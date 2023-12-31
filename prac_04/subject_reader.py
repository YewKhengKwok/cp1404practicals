"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Formats the input data and prints in the specified format"""
    data = get_data()
    print(data)
    print_subjects(data)


def get_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    input_file = open(FILENAME)
    subjects = []

    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects.append(parts)

    input_file.close()
    return subjects


def print_subjects(data):
    """Print subjects taught by each lecturer and number of students"""
    for data in data:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")


main()
