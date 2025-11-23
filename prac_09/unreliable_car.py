"""
CP1404 week 9 practical
Unreliable class that inherits from Car
"""
import random
from car import Car

class UnreliableCar(Car):
    """Specialised version of a Car with unreliable driving functionality."""
    def __init__(self, name=" ", fuel=" ", reliability=0.0):
        """Initialise an unreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = max(0.0, min(100.0, reliability))

    def drive(self,distance):
        """Drive the car only if a random number is less than reliability """
        random_chance = random.uniform(0,100)
        if random_chance <= self.reliability:
            return super().drive(distance)
        else:
            return 0.0