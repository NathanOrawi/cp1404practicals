"""
CP1404
SilverServiceTaxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flag_fall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness

    def __str__(self):
        """Return a string like a Taxi but with fanciness rating."""
        return (f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare_distance} km on current "
                f"fare, ${self.price_per_km * self.fanciness:.2f}/km plus flagfall of ${self.flagfall:.2f}")

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip"""
        return super().get_fare() * self.fanciness + self.flag_fall
