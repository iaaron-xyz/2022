"""
USAGE: python adieu.py

DESCRIPTION:
Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and  names with  commas and one and, as in the below:
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
- Reuqires the library inflect: pip install inflect
- site: https://pypi.org/project/inflect/

EXAMPLE:
$ python adieu.py
Name: Aaron
Name: Paul
Name: Bryan
Name: Cranston
Name: <CTRL+D>

Adieu, adieu, to Aaron, Paul, Bryan, and Cranston
"""

import inflect

p = inflect.engine()

def main():
    names = []
    get_names(names)
    joint_names = p.join(names)
    print(f"Adieu, adieu, to {joint_names}")

# Get names one by one from the user
def get_names(n):
    # Ask for names until user types control-D
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print('\n')
            break
        else:
            n.append(name)


if __name__ == "__main__":
    main()