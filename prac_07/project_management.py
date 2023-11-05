"""
CP1404 Project Management Program
Do-from-scratch Exercises
Estimated Duration: 1hr 30min
Actual Duration:
"""

from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """main function"""
    print(MENU)
    choice = input("Choice: ").upper()
    # score = int(input("Enter score: "))
    while choice != 'Q':
        if choice == 'L':
            print("Load")
        elif choice == 'S':
            print("Save")
        elif choice == 'D':
            print("Display")
        elif choice == 'F':
            print("Filter")
        elif choice == 'A':
            print("Add")
        elif choice == 'U':
            print("Update")
        else:
            print("Invalid error message")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Quit Project")


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects_by_date():
    pass


def add_new_project():
    pass


def update_project():
    pass


def quit():
    pass


main()
