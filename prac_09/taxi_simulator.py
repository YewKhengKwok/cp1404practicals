"""
CP1404/CP5632 Practical
Taxi simulator
Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
classes. Each time, until they quit:
The user should be presented with a list of available taxis and get to
choose one. Then they should say how far they want to drive.
At the end of each trip, show them the price and add it to their bill.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    # main function
    current_taxi = None
    total_bill = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 40, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(f"Lets drive!")
    print(f"{MENU}")

    # MENU system, Q for quit
    choice = input("> ").upper()
    while choice != "Q":

        # choose taxi
        if choice == "C":

            # List all available taxis
            print(f"Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

            # Choose taxi using index with error check
            user_select = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[user_select]
            except IndexError:
                print(f"Invalid taxi choice")
            except ValueError:
                print(f"Invalid taxi choice")

            # print latest total bill
            print(f"Bill to date: ${total_bill:.2f}")

        # drive
        elif choice == "D":

            if current_taxi is None:
                # if taxi not chosen
                print(f"You need to choose a taxi before you can drive")
            else:
                # taxi chosen already, ask distance
                current_taxi.start_fare()
                user_distance = int(input("Drive how far? "))
                current_taxi.drive(user_distance)

                # Show current fare
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")

                # calculate latest total bill with current taxi fare
                total_bill = total_bill + current_taxi.get_fare()

            # print latest total bill
            print(f"Bill to date: ${total_bill:.2f}")

        else:
            print(f"Invalid option")

        # Print MENU and ask for user input after selected function before has completed
        print(MENU)
        choice = input("> ").upper()

    # Quit
    # print latest total bill
    print(f"Bill to date: ${total_bill:.2f}")

    # List all available taxis
    print(f"Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
