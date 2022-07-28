"""
USAGE:
$ python3 camel.py

DESCRIPTION:
This program implement a program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case. Assume that the user's input will indeed be in camel case.

EXAMPLE:

"""

def main():
    # Get the user input in camelCase
    original_text = input("camelCase: ")

    # Convert text to snake case style
    new_text = ""
    for character in original_text:
        if (character.isupper()):
            new_text += '_' + character.lower()
        else:
            new_text += character

    # Return the result
    print(f"snake_case: {new_text}")


if __name__ == "__main__":
    main()
