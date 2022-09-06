"""
USAGE:
$ pytest test_fuel.py

DESCRIPTION:
This program tests the convert and the gauge functions in the fuel.py file.
"""

import pytest
from fuel import convert, gauge

# Test gauge issues
def test_gauge():
    # Check lower than 1 values
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    # Check higher than 99 values
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    # Check values in the middle
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(71) == "71%"

# Test convert issues
def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("1/1000") == 0

# Test convert Zero division errors
def test_convert_zero_division():
    # Check non numerical values
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test percents bigger than 100
def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("200/100")

# Test non numeric inputs
def test_convert_non_digit():
    with pytest.raises(ValueError):
        convert("hola")