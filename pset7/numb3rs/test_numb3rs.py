"""
Usage:
$ pytest test_numb3rs.py

Description:
This program tests the validate(ip) function in the
numb3rs.py file.
"""

from numb3rs import validate

def test_validate_numbers():
    assert validate("1.1.1.1") == True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("257.1.2.3") == False
    assert validate("1.512.512.512") == False

def test_validate_incorrect_format():
    assert validate("cat") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1") == False