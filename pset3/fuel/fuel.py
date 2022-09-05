"""
USAGE:
$ python3 fuel.py

DESCRIPTION:
This program prompts the user for a fraction in the format X/Y,
being X and Y integers,print out as a percentage rounded to the nearest integer,
how much fuel is in the tank.
- If, 1% or less remains, output E instead to indicate that the tank is essentially empty
- If 99% or more remains, output F instead to indicate that the tank is essentially full.

EXAMPLE:
$ python3 fuel.py  
Fraction: 3/4
75%
"""


def main():
    fuel = fraction_to_percent("Fraction: ")
    # Full
    if (fuel>=99):
        print("F")
    # Empty
    elif fuel<=1:
        print("E")
    else:
        print(f"{fuel}%")

def fraction_to_percent(prompt):
    while True:
        num_list = input(prompt).split('/')
        # Get the percent number
        try:
            percent = int(int(num_list[0])/int(num_list[1])*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            print("You are dividing by Zero!")
        # If numerator not greater than denominator, return percent
        else:
            if percent > 100:
                continue
            else:
                return percent


if __name__ == "__main__":
    main()