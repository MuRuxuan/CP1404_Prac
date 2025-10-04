# 1. Write name to name.txt
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# 2. Read name from name.txt and print
name_file = open("name.txt", "r")
name = name_file.read()
name_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt and sum
with open("numbers.txt", "r") as numbers_file:
    first_num = int(numbers_file.readline().strip())
    second_num = int(numbers_file.readline().strip())
sum_of_two = first_num + second_num
print(sum_of_two)

# 4. Calculate total of all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as in_files:
    for line in in_files:
        total += int(line.strip())
print(total)