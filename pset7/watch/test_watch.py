"""
Usage:
$ pytest test_watch.py

Description:
This program tests the parse(s) function in the
watch.py file.
"""

from watch import parse


def test_watch_exist():
    s = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(s) == "https://youtu.be/xvFZjo5PgG0"

    s = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(s) == "https://youtu.be/xvFZjo5PgG0"

    s = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(s) == "https://youtu.be/xvFZjo5PgG0"

def test_watch_noexist():
    s = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(s) == None