"""
CP1404
Intermediate Exercises
UnreliableCar Client Code
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    my_taxi = UnreliableCar(name='Hybrid', fuel=100, reliability=60)
    print(my_taxi)
    print(my_taxi.drive(40))


main()
