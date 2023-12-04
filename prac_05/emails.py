"""
Emails
"""

email_to_names = {}

email = input("Email: ")
while email != "":
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    check_name = input(f"Is your name {name}? (Y/n)")

    # correct name
    if check_name.upper() == "Y":
        email_to_names[email] = name
        email = input("Email: ")

    # wrong name, ask user for correct name
    elif check_name.upper() == "N":
        new_name = input("Name: ")
        new_name = new_name.title()
        email_to_names[email] = new_name
        email = input("Email: ")

# Display all items in dictionary
for key, name in email_to_names.items():
    print(f"{name} ({key})")