"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
DISPLAY MENU
GET choice
WHILE choice is not "Q"
    IF choice is "C"
        DISPLAY "Celsius:"
        GET celsius
        SET fahrenheit = celsius * 9.0 / 5 + 32
        DISPLAY "Result: fahrenheit F"
    ELSE IF choice is "F"
        DISPLAY "Fahrenheit:"
        GET fahrenheit
        SET celsius = 5 / 9 * (fahrenheit - 32)
        DISPLAY "Result: celsius C"
    ELSE
        DISPLAY "Invalid option"
    DISPLAY MENU
    GET choice
DISPLAY "Thank you."

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")