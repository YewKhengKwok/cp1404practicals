numbers = []

for i in range(0,5,1):
    input_number = int(input('Number: '))
    numbers.append(input_number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/5}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

try_username = input("Whats your username? ")

if try_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
