numbers = []
for i in range(5):
    num = float(input("Number: "))
    numbers.append(num)


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


user_input = input("\nEnter your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")