"""
CP1404
Do-from-scratch Exercises
taxi simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)choose taxi, d)rive"""
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
         SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]


def main():
    """
    Taxi manu is executed here.
    Why? Because, Sir Taxi Manu is the main criminal,
    that is why.  :)
    """
    print("Let's drive!")
    menu()


def menu():
    """ Taxi manu"""
    current_taxi = None
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            if current_taxi is not None:
                current_taxi = drive(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date $0.00")
        elif choice == 'C':
            print(f"Taxis available:")
            display_taxi()
            current_taxi = choose_taxi()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    quit_taxi(current_taxi)


def choose_taxi():
    """enables the user to be able to choose from a list of available taxis"""
    current_taxi = int(input("Choose taxi: "))
    while current_taxi != "":
        try:
            if current_taxi == 0:
                print(f"Bill to date: ${TAXIS[current_taxi].get_fare()}")
            elif current_taxi == 1:
                print(f"Bill to date: ${TAXIS[current_taxi].get_fare()}")
            elif current_taxi == 2:
                print(f"Bill to date: ${TAXIS[current_taxi].get_fare()}")
            else:
                print("Invalid taxi choice")
            return current_taxi
        except ValueError:
            print("Choose taxi Must be a number. Try again.")
        current_taxi = int(input("Choose taxi: "))


def drive(current_taxi):
    """allows user to choose how far they want to drive"""
    distance = int(input("Drive how far? "))
    TAXIS[current_taxi].drive(distance)
    print(f"Your {TAXIS[current_taxi].name} cost you ${TAXIS[current_taxi].get_fare()}")
    print(f"Bill to date: ${TAXIS[current_taxi].get_fare()}")
    return current_taxi


def quit_taxi(current_taxi):
    """At the end of each trip, show them the trip cost and add it to their bill"""
    if current_taxi is not None:
        total_trip_cost = 0.0
        for i in range(len(TAXIS)):
            total_trip_cost += TAXIS[i].get_fare()
        print(f"Total trip cost: ${total_trip_cost}")
    print("Taxis are now:")
    display_taxi()


def display_taxi():
    """Formats list of taxi in a human-readable manner"""
    i = 0
    taxis_available = """"""
    for taxi in TAXIS:
        taxis_available += f"{i} - {taxi}\n"
        i += 1
    print(taxis_available.rstrip('\n'))


main()
