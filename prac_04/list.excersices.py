FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)
    check_user_access()


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


def check_user_access():
    """Check if the entered username is authorized."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input = input("Enter your username: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()