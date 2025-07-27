"""CP1404/CP5632 Practical - Car class example with improvements."""


class Car:
    """Car class for vehicle simulation."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def drive(self, distance):
        """Drive the car a given distance if enough fuel, return the distance actually driven."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance
