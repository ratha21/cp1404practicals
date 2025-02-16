"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: this line is now added to break the loop once a valid integer is entered
    except ValueError:  # TODO - catching ValueError to handle non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)
