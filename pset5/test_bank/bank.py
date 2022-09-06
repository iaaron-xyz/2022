"""
USAGE:
python bank.py

DESCRIPTION:
This is a reimplementation of the problem set 1: bank.py.
This program prompts the user for a greeting.
if greeting starts with 'hello' prints '$0'
if greetings starts with 'h' prints '$20'
anything else prints '$100'

EXAMPLE:
$ python3 bank.py
Greeting: How you doin?
$20
"""

def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    # Quantity you return depends on the greetings received
    if "hello" in greeting.lower():
        return 0
    elif greeting[0].lower() == 'h':
        return 20
    return 100


if __name__ == "__main__":
    main()