"""
Programming language class
"""


class ProgrammingLanguage:
    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return str(self)

    def is_dynamic(self):
        """Indicates if language type is Dynamic or Static"""
        dynamic = self.typing
        if dynamic == "Dynamic":
            return True
        else:
            return False

