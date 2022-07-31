"""
USAGE:
$ python3 plates.py

DESCRIPTION:
Implement a program that prompts the user for a vanity plate
and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user's input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets
all requirements and False if it does not. Assume that s will be a str.
Requirements:
- Must start with at least two letters.
- Must contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end.
  For example, AAA222 would be acceptable; AAA22A would not be acceptable.
  The first number used cannot be a '0'.
- No periods, spaces, or punctuation marks are allowed.

EXAMPLE:
$ python plates.py 
Plate: IAARON
Valid

$ python plates.py 
Plate: CS50
Valid

$ python plates.py 
Plate: CS50P
Invalid
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """str->bool
    """
    numbers = "1234567890"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    len_str = len(s)
    s = s.upper()

    start_zero = 0
    numbers_in_plate = 0

    # Plate must have minimum 2 characters and maximum 6
    if len_str < 2 or len_str > 6:
        return False
    # Numbers not allowed in thefirst and second char
    if not s[0:2].isalpha():
        return False

    for char in s:
        # No periods, spaces or punctuation marks are allowed
        if (char not in numbers) and (char not in letters):
            return False
        # The first number used cannot be Zero
        if char.isdigit():
            numbers_in_plate += 1
            if char == "0" and start_zero == 0:
                return 0
            start_zero += 1

    # Not allowed numbers in the middle
    if numbers_in_plate > 0 and s[len_str-1].isalpha():
        return False

    # After all requirements are OK
    return True


if __name__ == "__main__":
    main()