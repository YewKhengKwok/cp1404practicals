"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Ask for user's score
score = float(input("Enter score: "))

# Validation check id score is less than 0 or more than 100
while score < 0 or score > 100:
    print ("Invalid score");
    score = float(input("Enter score: "))

# if score is 90 or more
if score >= 90:
    print("Excellent")
# else if score is 50 or more
elif score >= 50:
    print("Pass")
# else less than 50
else:
    print("Bad")

