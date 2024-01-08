"""
CP1404/CP5632 Practical
SilverServiceTaxi client file
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

FancyTaxi1 = SilverServiceTaxi("Hummer", 200, 2)

print(FancyTaxi1)

FancyTaxi1.drive(18)

print(f"{FancyTaxi1}, Current fare: ${FancyTaxi1.get_fare():.2f}")
