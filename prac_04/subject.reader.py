"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert student number to integer

            data.append(parts)  # Append processed data to list
    return data


def display_subject_details(data):
    """Display subject details in a formatted manner."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
