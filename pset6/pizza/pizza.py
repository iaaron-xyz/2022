"""
USAGE:
$ python pizza.py regular.csv
or
$ python pizza.py sicilian.py

DESCIPTION:
Implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio's format, and outputs a table
formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
Format the table using the library's grid format. If the user does not specify
exactly one command-line argument, or if the specified file's name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
This program requires the library tabulate: pip install tabulate
site: https://pypi.org/project/tabulate/

EXAMPLE:
$ python pizza.py sicilian.csv 
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+

 python pizza.py regular.csv 
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+
"""

import sys
import csv
from tabulate import *


def main():
    # check correct number of command-line arguments
    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    if (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    # Check the correct type of the file
    namelen = len(sys.argv[1])
    if namelen < 5 or sys.argv[1][namelen-4:] != ".csv":
        sys.exit("Not a CSV File")

    # Print the table
    print(to_table(sys.argv[1]))


def to_table(data):
    """(str)->()
    """
    # Variables
    keys = []
    pizza_types = []
    smalls = []
    larges = []
    # Read the lines in the file
    try:
        with open(data) as file:
            reader = csv.DictReader(file)
            # Make lists of keys and items
            for row in reader:
                # Store the keys in a list
                if len(keys) == 0:
                    keys = list(row.keys())
                # Store values in individual lists
                pizza_types.append(row[keys[0]])
                smalls.append(row[keys[1]])
                larges.append(row[keys[2]])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Make a dict out of the created lists
    pizza_dict = {
        keys[0]: pizza_types,
        keys[1]: smalls,
        keys[2]: larges
    }

    # Create the table format
    return tabulate(pizza_dict, headers="keys", tablefmt="grid")


if __name__ == "__main__":
    main()