try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a nonzero value.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(f"Result: {fraction}")
except ValueError:
    print("Error: Numerator and denominator must be valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Questions and Answers:
# 1. A ValueError will occur if the user enters a non-integer value for the numerator or denominator.
# 2. A ZeroDivisionError will occur if the denominator is zero.
# 3. To avoid ZeroDivisionError, a while loop is added to prompt the user until they enter a nonzero denominator.
