"""
Loops practice
"""

# Print odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Print 10s between 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Print 1 to 20 but in reverse
for i in range(20, 0, -1):
    print(i, end=' ')

# Newline
print()

# Ask user for number of stars
numStars = input("Number of stars? ")

# Print number of stars entered by user
for i in range(0, int(numStars), 1):
    print("*", end='')

# Newline
print()

# Print numbers of stars in ascending pattern
for i in range(0, int(numStars), 1):
    for j in range(0, i+1, 1):
        print("*", end='')
    print()
