"""
USAGE: python figlet.py

DESCRIPTION:
In a file called figlet.py, implement a program that:
- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message
- This requires the library pyfiglet: pip install pyfiglet
- site: https://pypi.org/project/pyfiglet/0.7/

EXAMPLE:
$ python pyfiglet.py
Input: hello!
Output:
 _          _ _         _ 
| |__   ___| | | ___   / \
| '_ \ / _ \ | |/ _ \ /  /
| | | |  __/ | | (_) /\_/ 
|_| |_|\___|_|_|\___/\/   
"""

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():
    # Check correct number of inputs
    args = len(sys.argv)
    # Check for correct number of inputs
    if args != 3 and args != 1:
        sys.exit("Correct usage: $ python figlet.py [-f fontName]\n Text between square brackets is optional.")

    # Get list of valid fonts
    fonts = figlet.getFonts()
    if args == 3:
        # Check for correct flag usage
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Flag: [-f] or [--font]")
        # Check for valid font name
        if sys.argv[2] not in fonts:
            sys.exit("Font name not found.")

    # Input user text
    text = input("Input: ")
    print("Output:")

    # Font defined by the user
    if args == 3:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
    # Font defined randomly
    elif args == 1:
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(text))
    else:
        sys.exit("Something went wrong!")


if __name__ == "__main__":
    main()