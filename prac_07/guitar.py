"""
class Guitar file
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Guitar class constructor"""
        self.guitar_name = name
        self.guitar_year = int(year)
        self.guitar_cost = float(cost)

    def __str__(self):
        """String return method"""
        return f"{self.guitar_name} ({self.guitar_year} : ${self.guitar_cost})"

    def get_age(self):
        """Get age of guitar method
            2023-guitar_year"""
        return f"{2023 - self.guitar_year}"

    def is_vintage(self):
        """Check guitar is vintage method,
            (> 50 years old) return true else false"""
        if int(self.get_age()) >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """less than magic method"""
        return self.guitar_year < other.guitar_year
