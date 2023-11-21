"""
print(random.randint(5, 20))  # line 1
Smallest number: 5
Largest number 20

print(random.randrange(3, 10, 2))  # line 2
Smallest number: 3
Largest number: 9
Line 2 cannot produce 4 as increment of 2 from 3 is already 5

print(random.uniform(2.5, 5.5))  # line 3
Smallest number: 2.5
Largest number: 5.5
"""

from random import *

print(randint(1, 100))
