"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when user enter a value that cannot be converted to an integer for either the numerator or the denominator.
2. When will a ZeroDivisionError occur?
when user enter 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
we can check if the denominator is zero before performing the division and handle it appropriately.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")