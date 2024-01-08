"""
CP1404/CP5632 Practical
SilverServiceTaxi class inherit from Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class inherit from Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi based from Taxi"""
        super().__init__(name, fuel)
        self.price_per_km = float(fanciness) * Taxi.price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km "
                f"plus flagfall of ${self.flagfall}")

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()
