"""..."""
# Gibson L-5 CES get_age() - Expected 100. Got 100
# Another Guitar get_age() - Expected 9. Got 9
# Gibson L-5 CES is_vintage() - Expected True. Got True
# Another Guitar is_vintage() - Expected False. Got False

from guitar import Guitar

CURRENT_YEAR = 2023

another = Guitar("another",2013)

age = another.get_age(CURRENT_YEAR)
print(age)
vintage = another.is_vintage(CURRENT_YEAR)
print(vintage)