"""
USAGE: python emojize.py

DESCRIPTION: implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
- Make sure to install emoji: pip install emoji
- site: https://pypi.org/project/emoji/

EXAMPLES:
$ python emojize.py
Input: :thumbs_up:
Output: 👍
"""

import emoji

def main():
    e = input("Input: ")
    print(emoji.emojize(f"Output: {e}"))

if __name__ == "__main__":
    main()