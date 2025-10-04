"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
        # Set flag to exit loop when valid input is received
    except ValueError:  #  # Catch the specific error when conversion to int fails
        print("Please enter a valid integer.")
print("Valid result is:", result)
