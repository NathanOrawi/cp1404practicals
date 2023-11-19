"""
Prac 9
Walkthrough Example
client code
"""

from prac_09.taxi import Taxi


def main():
    """ Print the details and the current fare of my texi """
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)
    print(f"Taxi driven {my_taxi.drive(40)}km")
    print(f"Taxi fare is ${my_taxi.get_fare()}")
    print(f"-------{my_taxi.start_fare()}-------")
    print(f"Taxi driven {my_taxi.drive(110)}km")
    print(f"Taxi fare is ${my_taxi.get_fare()}")


main()
