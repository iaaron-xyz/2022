"""
Usage: $ python3 tip.py

Description:
This program computes the tip to give after a meal, the user type the cost
of the meal and the percentage to tip fro thst cost.
The program returns the tip value in dollars.
- User type the cost of the meal in dollars format: $<dollars>.<cents>
- User should type tip value in percent form: <int_number>%
- Program returns the tip to give in dollars: $<dollars>.<cents>

Examples:
$ python3 tip.py
How much was the meal? $200.00
What percentage would you like to tip? 10%
Leave $20.00
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """str->float
    """
    number_str = d[1:len(d)]
    return float(number_str)


def percent_to_float(p):
    """str->float
    """
    number_str = p[0:len(p)-1]
    return float(number_str)/100


if __name__ == "__main__":
    main()