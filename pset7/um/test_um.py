"""
Usage:
$ pytest test_um.py

Description:
This program tests the count(s) function in the
working.py file.
"""

from um import count


def test_um_counts():
    assert count("um") == 1
    assert count("Hello, um, world.") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2