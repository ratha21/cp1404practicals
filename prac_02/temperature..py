def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Temperature Conversion Program")
    choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? ").upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
