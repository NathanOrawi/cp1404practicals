"""
CP1404
Intermediate Exercises
UnreliableCar Module
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability rating"""

    def __init__(self, reliability: float, **kwargs):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with a reliability rating"""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self, distance):
        """ Generate a random number between 0 and 100, and only drive the
        car if that number is less than the car's reliability. """
        reliability = randint(0, 100)
        if self.reliability > reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven