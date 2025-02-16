import random

# Line 1: Generates a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))
# Smallest possible: 5, Largest possible: 20

# Line 2: Generates a random integer from 3 to 9 with a step of 2
print(random.randrange(3, 10, 2))
# Smallest possible: 3, Largest possible: 9
# Line 2 could not have produced a 4 because it increments by 2 (3, 5, 7, 9)

# Line 3: Generates a random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
# Smallest possible: 2.5, Largest possible: 5.5

# Generate a random number between 1 and 100 inclusive
print(random.randint(1, 100))
