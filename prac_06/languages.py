"""
Languages
Create languages using ProgrammingLanguage class
Print languages that are dynamic
"""

from prac_06.programming_language import ProgrammingLanguage

# creating class objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

# list of ProgrammingLanguages
Programming_languages = [python, ruby, visual_basic]

# print languages that are dynamic
print("The dynamically typed languages are:")
for languages in Programming_languages:
    if languages.is_dynamic():
        print(languages.language_name)
