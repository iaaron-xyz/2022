"""
USAGE:
$ pytest test_plates.py

DESCRIPTION:
This program tests the is_valid function in the plates.py file.
"""

from plates import is_valid

def test_is_valid():
    # Catches when not starting with 2 letters
    assert is_valid("M33") == False
    # Valid string
    assert is_valid("MEXICO") == True
    # Catches when non alphanumerical used
    assert is_valid("MX-50") == False

def test_max_min_characters():
    # Catches when less than 2 chars
    assert is_valid("") == False
    assert is_valid("C") == False
    # Valid strings
    assert is_valid("CS") == True
    assert is_valid("CSPYTN") == True
    # Catches when more than 6 chars
    assert is_valid("PYTHONCS") == False

def test_numbers():
    # Catches when start with number
    assert is_valid("50") == False
    # Valid string
    assert is_valid("CS50") == True
    # Catches when first number is zero
    assert is_valid("JB007") == False
    # Carhces when digits in the middle of letters
    assert is_valid("CS50PY") == False