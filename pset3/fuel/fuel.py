<<<<<<< HEAD
"""
USAGE: python3 fuel.py

DESCRIPTION: Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)

EXAMPLES:
$ python fuel.py
Fraction: 1/4
25%
$ python fuel.py
Fraction: 3/65
4%
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
=======
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
>>>>>>> 5e186c8d07e775d311d825211e1165fef1590674
    main()