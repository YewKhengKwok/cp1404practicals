"""
class Project file
"""


class Project:

    def __init__(self, name="", start_date="", priority=0,
                 cost_estimate=0, completion_percentage=0):
        """Project class constructor"""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __lt__(self, other):
        """less than magic method"""
        return self.priority < other.priority

    def __str__(self):
        """String return method"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_completed(self):
        """Check project is completed method (100%)"""
        if int(self.completion_percentage) == 100:
            return True
        else:
            return False

    def update_percentage(self, new_percentage):
        """Update completion percentage method"""
        self.completion_percentage = int(new_percentage)

    def update_priority(self, new_priority):
        """Update priority method"""
        self.priority = int(new_priority)