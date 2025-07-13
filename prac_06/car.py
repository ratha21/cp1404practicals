"""CP1404/CP5632 Practical - Car class example with improvements."""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        if amount < 0:
            raise ValueError("Fuel amount must be >= 0")
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out. Return the distance actually driven.
        """
        if distance < 0:
            raise ValueError("Distance must be >= 0")
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def get_odometer(self):
        """Return the car's odometer reading."""
        return self._odometer

    def __str__(self):
        return f"Car(fuel={self.fuel}, odometer={self._odometer})"
