"""
Guitars
Ask users for their guitars
Prints all their guitars name, cost and vintage or not
"""

from prac_06.guitar import Guitar

print("My guitars!")
guitars_added = []

# Ask user for their guitars information
name = input("Name: ")
while name != "":
    year = input("Year: ")
    cost = input("Cost: $")
    add_guitar = Guitar(name, year, cost)
    guitars_added.append(add_guitar)
    print(f"{add_guitar} added.")
    name = input("Name: ")

# Test to add more items and debug easier
guitars_added.append(Guitar("GuitarA test text", 2000, 1050.65))
guitars_added.append(Guitar("GuitarB test text", 1965, 5510.05))

# List all guitars added
print("These are my guitars")
for i, guitar in enumerate(guitars_added, 1):

    # use is_vintage method to check if each guitar is vintage (>50 yr old)
    # add (vintage) tag if true for print later
    if guitar.is_vintage():
        add_vintage_tag = "(vintage)"
    else:
        add_vintage_tag = ""

    print(f"Guitar {i}: {guitar.guitar_name:>20}, worth $ {guitar.guitar_cost:10,.2f} {add_vintage_tag}")
