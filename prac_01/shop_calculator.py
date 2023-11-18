"""
Calculates total price for number of items entered
10% discount it more than $100
"""

totalPrice = 0

# Ask user for number of items
numItems = input("Number of items? ")

# Validation check if numItems is less than 0, ask again
while int(numItems) < 0:
    print("Invalid number of items!")
    numItems = input("Number of items? ")

# Total the price of all items
for i in range(0, int(numItems), 1):
    itemPrice = input("Price of item: ")
    totalPrice = float(totalPrice) + float(itemPrice)

# If price more than 100, apply discount
if totalPrice > 100:
    totalPrice = totalPrice - totalPrice/10

# Print total price
print("Total price for", numItems, "items is $", "{:.2f}".format( totalPrice ))
