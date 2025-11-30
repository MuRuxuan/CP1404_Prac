"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifragilisticexpialidocious")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """
    Format a phrase as a sentence starting with a capital and ending with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('this is a test')
    'This is a test.'
    """
    # Capitalize the first letter
    phrase = phrase.capitalize()

    # Ensure it ends with exactly one full stop
    if not phrase.endswith('.'):
        phrase += '.'

    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    # Test Car sets the fuel correctly with default value
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"

    # Test Car sets the fuel correctly with provided value
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set provided fuel correctly"


run_tests()

# Uncomment the following line to run doctests
doctest.testmod()