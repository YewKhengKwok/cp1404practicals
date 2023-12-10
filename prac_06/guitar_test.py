"""
Guitar_test
test expected output of each method
"""

from prac_06.guitar import Guitar

# create Guitar objects
Gibson = Guitar("Gibson L-5 CES", 1972, 1500)
Ribbon = Guitar("Ribbon 5-L SEC", 1995, 2000)

# test get_age() method
print(f"Gibson get_age() - Expected 51. Got {Gibson.get_age()}")
print(f"Ribbon get_age() - Expected 28. Got {Ribbon.get_age()}")

# test is_vintage() method
print(f"Gibson is_vintage() - Expected True. Got {Gibson.is_vintage()}")
print(f"Ribbon is_vintage() - Expected False. Got {Ribbon.is_vintage()}")