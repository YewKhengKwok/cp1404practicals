"""Q1"""
out_file = open('name.txt', 'w')

user_name = input("May I have your name: ")
print(user_name, file=out_file)

out_file.close()

"""Q2"""
in_file = open('name.txt', 'r')

print(f"Your name is {in_file.readline()}")

in_file.close()

"""Q3"""
in_file = open('numbers.txt', 'r')

number1 = int(in_file.readline())
number2 = int(in_file.readline())

in_file.close()

print(number1 + number2)

"""Q4"""
in_file = open('numbers.txt', 'r')

total = 0

for line in in_file:
    total = total + int(line)

in_file.close()

print(total)
