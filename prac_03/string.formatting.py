# String formatting examples
name = "Gibson L-5 CES"
year = 1922
cost = 16036

# Using f-string formatting
print(f"{year} {name} for about ${cost:,.0f}!")

# Using a for loop with f-strings to generate the required output
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
