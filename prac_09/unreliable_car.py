"""
CP1404/CP5632 Practical
unreliable_car class inherit from car class file
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """UnreliableCar inherit from Car"""

    def __init__(self, name, fuel, reliability: float):
        """Initialise an UnreliableCar inherit from Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only when random reliable number is less than car reliability"""
        if randint(1, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
