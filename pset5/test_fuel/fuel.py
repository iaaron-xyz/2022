"""
USAGE:
python fuel.py

DESCRIPTION:
This is a reimplementation of the Fuel Gauge from problem Set 3: fuel.py
Restructuring your code per the below, wherein:
- convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
  and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
  If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
  If Y is 0, then convert should raise a ZeroDivisionError.
- gauge expects an int and returns a str that is:
    - "E" if that int is less than or equal to 1,
    - "F" if that int is greater than or equal to 99,
    - and "Z%" otherwise, wherein Z is that same int.

EXAMPLES:
$ python3 fuel.py  
Fraction: 3/4
75%
"""

def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    print(gauge(perc))


def gauge(percent):
    # Full
    if (percent>=99):
        return "F"
    # Empty
    elif percent<=1:
        return "E"
    else:
        return f"{percent}%"


def convert(fraction):
    # Get the percent number
    try:
        # Get a list of 2 numbers
        num_list = fraction.split('/')
        # numerator and denominator
        x, y = float(num_list[0]), float(num_list[1])
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        percent_val = int(x/y*100)
        return percent_val
    # Catch raised errors and raise them again to test purposes
    except ValueError:
        raise
    except ZeroDivisionError:
        raise


if __name__ == "__main__":
    main()