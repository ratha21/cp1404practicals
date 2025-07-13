"""
CP1404/CP5632 Practical - Guitar class, testing, and usage
Estimate: 45 minutes
Actual: __ minutes
"""

import datetime

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

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


def test_guitar():
    """Test the Guitar class methods."""
    # Create guitars for testing
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    # Test get_age()
    print(f"{gibson.name} get_age() - Expected {CURRENT_YEAR - 1922}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {CURRENT_YEAR - 2013}. Got {another.get_age()}")

    # Test is_vintage()
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


def main():
    """Program to input guitars and display details."""
    print("My guitars!")

    guitars = []

    # For quick testing, use pre-defined guitars instead of input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # Uncomment below for real input
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.\n")

    # Display guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    test_guitar()
    main()
