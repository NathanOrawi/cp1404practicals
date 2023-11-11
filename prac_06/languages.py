"""
CP1404 Prac 6 Intermediate Exercises
Nathan Orawi
Estimated Duration: 40 min
Actual Duration: 115 min
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


def main():
    """Displays the name of the programming language that is Dynamic"""
    languages = [python, ruby, visual_basic]
    display_dynamic_language(languages)


def display_dynamic_language(languages):
    """Displays the name of the programming language that is Dynamic"""
    dynamic_languages = [language.field for language in languages if language.is_dynamic()]
    print("The dynamically typed languages are:")
    for dynamic_language in dynamic_languages:
        print(dynamic_language)


main()
