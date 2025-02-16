# Asking the user for their name and writing it to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Reading the name from the file and printing a greeting
with open("name.txt", "r") as file:
    stored_name = file.read().strip()
print(f"Hi {stored_name}!")

# Reading the first two numbers from numbers.txt and printing their sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
print(first_number + second_number)

# Reading all numbers from numbers.txt and printing their total sum
with open("numbers.txt", "r") as file:
    total = sum(int(line) for line in file)
print(total)