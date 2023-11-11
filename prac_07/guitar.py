"""
CP1404 Intermediate  Exercise
Prac 7
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}({self.year}) : ${self.cost}"

    def __repr__(self):
        return f"{self.name}({self.year}) : ${self.cost}"

    def get_age(self, current_year):
        """Gets the age of the guitar"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Checks if the guitar is 50 years or older, to dim as vintage or not"""
        if self.get_age(current_year) >= 50:
            return True
        return False

    def __lt__(self, other):
        return self.year < other.year


def run_tests():
    """Test to see class methods working as intended"""
    g1 = Guitar("BOB", 1932, 11)
    g2 = Guitar("BEN", 1989, 123)
    print(g1 < g2)


if __name__ == "__main__":
    run_tests()
