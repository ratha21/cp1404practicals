"""
CP1404/CP5632 Practical - ProgrammingLanguage class and client code
Estimate: 25 minutes
Actual: __ minutes
"""

class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation of ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

def main():
    """Demo test code for ProgrammingLanguage class."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print each language
    print(python)
    print(ruby)
    print(visual_basic)

    # Store them in a list
    languages = [python, ruby, visual_basic]

    # Print only dynamic languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
