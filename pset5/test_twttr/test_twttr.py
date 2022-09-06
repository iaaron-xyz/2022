"""
USAGE:
$ pytest test_twttr.py

DESCRIPTION:
This program tests the shorten function in the twttr.py file.
"""

from twttr import shorten

def test_shorten():
    assert shorten("murcielago") == "mrclg"
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("CS50") == "CS50"
    assert shorten("Aaall right! This is CS50!") == "ll rght! Ths s CS50!"