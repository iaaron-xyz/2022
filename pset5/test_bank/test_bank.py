"""
USAGE:
$ pytest test_bank.py

DESCRIPTION:
This program tests the value function in the bank.py file.
"""

from bank import value

def test_hello():
    assert value("hello, sir!") == 0
    assert value("Hello, everybody!") == 0

def test_h():
    assert value("Hi!") == 20
    assert value("How are you today!") == 20

def test_other_greet():
    assert value("Good Morning!") == 100
    assert value("What's up!") == 100