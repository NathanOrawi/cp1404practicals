"""Band class for CP1404"""


class Band:
    """Musician class"""

    def __init__(self, band=""):
        """Construct a Musician with a name and empty instrument collection."""
        self.band = band
        self.members = []

    def __str__(self):
        """Return a string representation of a Musician and their instruments if any.
        By unpacking dictionary and accessing via dot notation"""
        musician_and_instrument = ""
        for member in self.members:
            musician_and_instrument += f"{member.name} ({member.instruments}),"
        return f"{self.band} ({musician_and_instrument.rstrip(', ')})"

    def __repr__(self):
        """Return a string representation of a Member, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a member to the member collection."""
        self.members.append(member)

    def play(self):
        """Return a string showing the members playing their first (or no) instrument
        by unpacking dictionary and accessing via dot notation"""
        for member in self.members:
            if not member.instruments:
                return f"{member.name} needs an instrument!"
            return f"{member.name} is playing: {member.instruments}"

#
# class Band:
#     """Band class."""
#
#     def __init__(self, name):
#         """Construct values for a Band instance."""
#         self.name = name
#         self.instruments = []
#         self.musicians = []
#
#     def __str__(self):
#         """Return a string representation of a Band."""
#         return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
#
#     def add(self, musician):
#         """Add a musician to the band."""
#         self.musicians.append(musician)
#
#     def play(self):
#         """Return a string showing the musician/s playing their first instrument."""
#         results = []
#         for musician in self.musicians:
#             results.append(musician.play())
#         return "\n".join(results)
