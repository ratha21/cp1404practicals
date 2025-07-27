import random
from car import Car  # Assuming your base Car class is correct

class UnreliableCar(Car):
    """A car that might not drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with given reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on its reliability.

        Generates a random number. If it's less than reliability, drive.
        Otherwise, car fails to drive (returns 0).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
