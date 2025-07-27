from taxi import Taxi

# Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40 km
my_taxi.drive(40)

# Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Restart the meter (start a new fare)
my_taxi.start_fare()

# Drive the taxi 100 km
my_taxi.drive(100)

# Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
