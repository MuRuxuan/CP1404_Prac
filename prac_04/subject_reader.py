"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function to load and display subject data."""
    subjects = load_data(FILENAME)
    display_subject_details(subjects)


def load_data(filename=FILENAME):
    """Read data from file and return as list of subject details."""
    subjects = []

    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects

def display_subject_details(subjects):
    """Display all subject details in a formatted way"""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")

main()