"""
USAGE:
$ python lines.py filename.py

DESCRIPTION:
implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines. If the user does not specify exactly one command-line argument,
or if the specified file's name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.
Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

EXAMPLE:

"""

import sys

def main():
    # Check correct number of arguments in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check the file is a valid python file
    nlen = len(sys.argv[1])
    if nlen < 4 or sys.argv[1][nlen-3:] != ".py":
        sys.exit("Not a Python file")

    # Print the number of lines in the program file
    print(count(sys.argv[1]))


def count(filename):
    """(str)->(int)
    """
    # Read the lines in the file
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Count only valid lines
    # - No comments
    # - No new lines
    counter = 0
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        if len(line.rstrip()) == 0:
            continue
        counter += 1

    return counter


if __name__ == "__main__":
    main()