"""My Guitars client file
Read guitars from CSV
Add new guitars from user
Amend CSV with new guitars from user
Sorted by oldest to newest
"""
from prac_06.guitar import Guitar


def main():
    guitars_added = []
    # Read guitars in CSV
    in_file = open('guitars.csv', 'r')
    # File format is like: Name, year, cost
    # All other lines are data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # create class objects with parts stripped
        guitar = Guitar(parts[0], parts[1], parts[2])
        # Add the language we've just constructed to the list
        guitars_added.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()

    # Ask user for new guitars to be added
    # blank = no more new guitars
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        add_guitar = Guitar(name, year, cost)
        guitars_added.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("Name: ")

    # sort guitar by oldest to newest (year)
    guitars_added.sort(key=lambda x: x.guitar_year)

    # Open CSV for writing
    in_file = open('guitars.csv', 'w')

    # Write list of guitars into CSV
    print("New guitars added into CSV, guitars are also sorted oldest to newest")
    for guitar in guitars_added:
        print(f"{guitar.guitar_name},{guitar.guitar_year},{guitar.guitar_cost}", file=in_file)

    # close file once done writing in CSV
    in_file.close()


main()
