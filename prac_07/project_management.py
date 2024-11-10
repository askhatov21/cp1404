"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""

class ProgrammingLanguage:
    """A class to model a programming language's characteristics."""
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialize a new ProgrammingLanguage instance with specified attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Provide a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}," \
               f"Pointer Arithmetic ={self.pointer_arithmetic}"

    def is_dynamic(self):
        """Check if the programming language uses dynamic typing."""
        return self.typing == "Dynamic"


def run_tests():
    """Execute test cases to demonstrate the ProgrammingLanguage class functionality."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
