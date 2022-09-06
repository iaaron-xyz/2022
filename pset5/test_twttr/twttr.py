"""
USAGE:
python twttr.py

DESCRIPTION:
Reimplementation from the problem set 2: twwtr.py.
restructuring the code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

EXAMPLES:
$ python twttr.py 
Input: Introduction to Programming with Python
Output: ntrdctn t Prgrmmng wth Pythn
"""

def shorten(full_text):
    # Characters on vowels will be removed
    vowels = "aeiouAEIOU"
    # New string without vowels
    new_text = ""
    for character in full_text:
        if character not in vowels:
            new_text += character
    return new_text

def main():
    full_text = input("Input: ")
    print(f"Output: {shorten(full_text)}")


if __name__ == "__main__":
    main()