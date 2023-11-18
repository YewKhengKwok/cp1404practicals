"""
Prints a menu and display user's name in various ways
"""

# Ask for user's name
name = input("Enter name: ")

# Print menu
print("(H)ello", "\n(G)oodbye", "\n(Q)uit")

# Ask for user's menu choice
choice = input()

# Keep menu running unless Quit
while choice != "Q":

    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")

    # Print menu
    print("(H)ello", "\n(G)oodbye", "\n(Q)uit")

    # Ask for user's menu choice
    choice = input()

# Print finished when quit
print("Finished")
