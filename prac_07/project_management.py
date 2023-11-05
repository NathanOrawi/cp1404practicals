"""
CP1404 Project Management Program
Do-from-scratch Exercises
Estimated Duration: 1hr 30min
Actual Duration:
"""

from project import Project

projects = []

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
            load_projects()
        elif choice == 'S':
            print("Save")
        elif choice == 'D':
            print("Display")
            display_projects()
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
    """Read file of project details, save as objects, display."""
    # Open the file for reading
    in_file = open('projects.txt', 'r')
    # File format is like: Name,Year,Cost
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are guitar data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip('\n').split('\t')
        # print(parts)  # debugging
        # Construct a Project object using the elements
        # year should be an int
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        # Add the project we've just constructed to the list
        projects.append(project)
    # get project details from user
    # get_project()
    # Close the file as soon as we've finished reading it
    in_file.close()


def save_projects():
    """Loop through and write all project"""
    out_file = open('test.txt', 'w')
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    out_file.close()


def display_projects():
    """Display the Incomplete and Completed projects"""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(project)

    print("Completed projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(project)


def filter_projects_by_date():
    """..."""
    pass


def add_new_project():
    """..."""
    pass


def update_project():
    """..."""
    pass


def quit_project():
    """..."""
    pass


main()
