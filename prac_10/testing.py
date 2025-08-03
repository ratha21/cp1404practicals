"""
Prac 10 - Testing Practice
Simple testing using assert statements and doctest
"""

import doctest
from car import Car  # Correct import of the Car class


def repeat_string(s, n):
    """Repeat string s, n times with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Check if a word is at least as long as the given length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_to_sentence(phrase):
    """
    Format a phrase into a proper sentence with capital and period.

    >>> format_phrase_to_sentence("hello")
    'Hello.'
    >>> format_phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_to_sentence("my sentence")
    'My sentence.'
    """
    phrase = phrase.strip().capitalize()
    if not phrase.endswith("."):
        phrase += "."
    return phrase


def run_tests():
    """Run some assert tests."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    def run_tests():
        """Run some assert tests."""
        assert repeat_string("Python", 1) == "Python"
        assert repeat_string("hi", 2) == "hi hi"

        # Car tests
        car1 = Car()
        assert car1.odometer == 0, "Default odometer should be 0"
        assert car1.fuel == 0, "Default fuel should be 0"

        car2 = Car(fuel=20)
        assert car2.fuel == 20, "Fuel should be set to 20"

        # Format phrase tests
        assert format_phrase_to_sentence("hello") == "Hello."
        assert format_phrase_to_sentence("It is an ex parrot.") == 'It is an ex parrot.'
        assert format_phrase_to_sentence("my sentence") == 'My sentence.'
