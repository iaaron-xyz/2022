"""
USAGE:
python scourgify.py before.csv after.csv

DESCRIPTION: implement a program that:
- Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, whose columns are
    assumed to be, in order, name and house, and
    - the name of a new CSV to write as output, whose columns should be, in
    order, first, last, and house.
- Converts that input to that output, splitting each name into a first name
and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first
cannot be read, the program should exit via sys.exit with an error message.

EXAMPLE:
python scourgify.py before.csv after.csv
<produces a file called after.csv as specified in the description>
"""

import sys
import csv

def main():
    # Check correct number of inputs
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check the input file is a csv file
    slen = len(sys.argv[1])
    slen2 = len(sys.argv[2])
    if slen < 4 or sys.argv[1][slen-4:] != ".csv" or sys.argv[2][slen2-4:] != ".csv":
        sys.exit("Not a CSV file")

    # split columns of the csv and make a new one
    split_columns(sys.argv[1], sys.argv[2])


def split_columns(oldfile, newfile):
    """(str)->(None)
    """
    # New file
    after_list = []

    # Read current CSV file
    try:
        with open(oldfile) as table:
            reader = csv.DictReader(table)
            for row in reader:
                # split the name and the lastname
                names = row['name'].split(',')
                # New list of dicts with splitted name
                after_list.append({"first": names[1].strip(), "last": names[0].strip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Write new CSV file
    with open(newfile, "w") as new_table:
        writer = csv.DictWriter(new_table, fieldnames=list(after_list[0].keys()))
        # Write the rows of the new CSV file
        writer.writeheader()
        writer.writerows(after_list)

if __name__ == "__main__":
    main()