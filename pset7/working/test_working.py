"""
Usage:
$ pytest test_working.py

Description:
This program tests the convert(s) function in the
working.py file.
"""
import pytest
from working import convert


def test_convert_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert_hour_verror():
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")

def test_convert_min_verror():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert_format_verror():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")