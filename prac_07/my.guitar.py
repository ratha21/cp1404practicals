"""
CP1404/CP5632 Practical - My Guitars combined program
Estimate: 45 minutes
Actual: __ minutes
"""

import datetime

FILENAME = "guitars.csv"
CURRENT_YEAR = datetime.datetime.now().year

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define less than comparison based on year for sorting."""
        return self.year < other.year

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


def main():
    """Read, display, sort, add, and save guitars."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    # Sort guitars by year and display
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Add new guitars from user input
    guitars += get_new_guitars()

    # Write all guitars back to file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display guitars with formatted output."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars():
    """Prompt user for new guitars and return them as a list."""
    print("\nAdd new guitars:")
    new_guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
    return new_guitars


def save_guitars(filename, guitars):
    """Write all guitars to file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
