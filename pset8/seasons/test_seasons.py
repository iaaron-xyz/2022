"""
Usage:
$ pytest test_seasons.py

Description:
This program tests the seasons.py program
"""

from seasons import get_date

def test_get_date():
    assert get_date("2021-08-03") == ["2021", "08", "03"]
    assert get_date("2020-08-03") == ["2020", "08", "03"]
