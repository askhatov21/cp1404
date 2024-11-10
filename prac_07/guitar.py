CURRENT_YEAR = 2023
VINTAGE_MINIMUM_YEAR = 50

class Guitar:
    """A class to represent a guitar, including its name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with a name, year of manufacture, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string describing the guitar."""
        return f"{self.name} ({self.year} : ${self.cost})"

    def __lt__(self, other):
        """Compare guitars by their year of manufacture for sorting."""
        return self.year < other.year

    def get_age(self):
        """Calculate age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is considered vintage based on its age."""
        return self.get_age() >= VINTAGE_MINIMUM_YEAR
