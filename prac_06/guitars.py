# guitars.py
"""
CP1404/CP5632 Practical 06
Guitars Client Program
This program allows users to input details of multiple guitars, stores them in a list,
and displays the collected information in a formatted manner. It includes input validation
for numeric fields and handles empty input to terminate data entry.
"""

from guitar import Guitar

def main():
    """
    Main function to handle user interaction for guitar data entry and display.
    Collects guitar details until user enters empty name, then displays all
    collected guitars with appropriate formatting and vintage indicators.
    """
    print("My guitars!")
    get_valid_email()  # Validate user email before proceeding

    guitars = []  # Plural noun for list containing multiple guitars

    while True:
        name = input("Name: ")
        if not name:
            break

        # Validate year input
        while True:
            try:
                year = int(input("Year: "))
                break
            except ValueError:
                print("Please enter a valid year (integer).")

        # Validate cost input
        while True:
            try:
                cost = float(input("Cost: $"))
                break
            except ValueError:
                print("Please enter a valid cost (number).")

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    # Demonstrate word count functionality
    description = input("Enter a description of your guitar collection: ")
    target = input("Enter a word to count in the description: ")
    count = count_word_occurrences(description, target)
    print(f"The word '{target}' appears {count} times in the description.\n")

    if guitars:
        print("These are my guitars:")
        for index, guitar in enumerate(guitars, 1):  # Meaningful loop variable name
            vintage_indicator = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {index}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_indicator}")
    else:
        print("No guitars added.")


def get_valid_email():
    """
    Prompt user for email address and validate it contains "@".
    Continuously reprompts until a valid email is provided.
    Returns the valid email string.
    """
    while True:
        email = input("Enter your email address: ")
        if "@" in email:
            return email
        print("Invalid email format. Please include '@' in your email.")


def count_word_occurrences(input_string, target_word):
    """
    Count how many times a target word appears in the input string.
    Converts both string and word to lowercase for case-insensitive counting.
    Returns the integer count of occurrences.
    """
    return input_string.lower().count(target_word.lower())

main()