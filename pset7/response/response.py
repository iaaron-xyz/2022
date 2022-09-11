"""
Usage:
$ python response.py

Description:
This program receives an email  and returns Valid or Invalid
based on if the email has a valid syntaxis or not.
Make use of the library validators.

Example:
$ python response.py

"""
import validators


def main():
    print(email_validator(input("What's your email address? ")))


def email_validator(email):
    """(str)->(str)
    """
    if validators.email(email):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()