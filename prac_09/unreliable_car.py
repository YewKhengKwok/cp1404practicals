"""
CP1404/CP5632 Practical
unreliable_car class file
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """UnreliableCar inherit from Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar inherit from Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def drive(self, distance):
        """Drive only when random reliable number is less than car reliability"""
        random_reliable_number = randint(1, 100)
        if random_reliable_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
