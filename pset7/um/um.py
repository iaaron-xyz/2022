"""
usage:
python um.py

description:
implement a function called count that expects a line of text as input as
a str and returns, as an int, the number of times that “um” appears in
that text, case-insensitively, as a word unto itself, not as a substring
of some other word.
For instance, given text like hello, um, world, the function should return 1.
Given text like yummy, though, the function should return 0.

example:

"""

import re


def main():
    print(count(input("Text: ")))

def count(s):
    """(str)->(int)
    """
    ums = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(ums)

if __name__ == "__main__":
    main()