"""
Usage: $ python3 playback.py

Description:
The spaces in the string entered by the user
are changed by 3 dots.

Examples:
$ python3 playback.py
Text: how you doing?
how...you...doing?
"""

text = input("Text: ")
print(f"{text.replace(' ', '...')}")