"""project module"""


class Project:
    def __init__(self, name="", start_date="", priority=1, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage} %"

    def __repr__(self):
        return f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage} %"

    def __eq__(self, other):
        return self.name == other.name


def run_tests():
    """Test to see class methods working as intended"""
    pass


if __name__ == "__main__":
    run_tests()
