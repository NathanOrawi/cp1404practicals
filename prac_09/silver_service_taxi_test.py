"""..."""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2)
    print(my_taxi)
    print(f"{my_taxi.drive(18)}km")
    print(my_taxi)
    print(f"${my_taxi.get_fare():.2f}")
    print(my_taxi.price_per_km)


main()
