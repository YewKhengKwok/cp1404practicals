"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # car1
    car1 = Car("CarBrand", 180)
    car1.drive(30)
    print(f"Car has fuel: {car1.fuel}")
    print(car1)

    # limo1
    limo1 = Car("LimoBrand", 100)
    limo1.add_fuel(20)
    print(f"Limo has fuel: {limo1.fuel}")
    limo1.drive(115)
    print(limo1)


main()
