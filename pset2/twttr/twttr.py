"""
USAGE:
$ python3 twttr.py

DESCRIPTION:
This program prompts to the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.

EXAMPLE:
$ python twttr.py 
Input: Introduction to Programming with Python
Output: ntrdctn t Prgrmmng wth Pythn
"""

def main():
    full_text = input("Input: ")

    # Remove the vowels
    vowels = "aeiouAEIOU"
    # New text without vowels
    new_text = ""
    for character in full_text:
        if character not in vowels:
            new_text += character
    print(f"Output: {new_text}")


if __name__ == "__main__":
    main()