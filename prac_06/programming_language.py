"""
class ProgrammingLanguage file
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True, year=0):
        """ProgrammingLanguage class constructor"""
        self.language_name = name
        self.typing_type = typing
        self.is_reflection = reflection
        self.created_year = year

    def is_dynamic(self):
        """Boolean check if programming language is dynamic
            if dynamic true else false"""
        if self.typing_type == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """String return method"""
        return f"{self.language_name}, {self.typing_type} Typing, Reflection={self.is_dynamic()}, First appeared in {self.created_year}"
