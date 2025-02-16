import random

# Constants
FILENAME = "stock_prices.txt"
STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%

price = STARTING_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    if random.randint(1, 2) == 1:
        price *= 1 + random.uniform(0, MAX_INCREASE)  # Increase
    else:
        price *= 1 - random.uniform(0, MAX_DECREASE)  # Decrease

    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()