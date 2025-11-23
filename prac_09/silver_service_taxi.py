"""
CP1404 week9 Practical
SilverServiceTaxi class that inherits from Taxi
"""
from taxi import Taxi
class SilverServiceTaxi(Taxi):
    """Specialised Taxi subclass with fancy features """
    flagfall = 4.50

    def __init__(self, name=" ", fuel=" ", fanciness=0):
        """Initialise a SilverServiceTaxi instance.
        Inherits name and fuel from Taxi, adds fanciness attribute, and scales price_per_km."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"


    def get_fare(self):
        """Calculate and return the total fare for the trip."""
        base_fare = super().get_fare()
        total_fare = self.flagfall + base_fare
        return round(total_fare, 2)