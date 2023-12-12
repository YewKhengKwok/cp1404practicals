"""
class Project file
"""


class Project:

    def __init__(self, name="", start_date="", priority=0,
                 cost_estimate=0, completion_percentage=0):
        """Project class constructor"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = completion_percentage

    def is_completed(self):
        """Check project is completed method (100%)"""
        if int(self.completion_percentage) == 100:
            return True
        else:
            return False

    def __lt__(self, other):
        """less than magic method"""
        return self.priority < other.priority