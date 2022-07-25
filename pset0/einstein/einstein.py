"""
Usage: $ python3 einstein.py

Description:
The user gets a prompt to type a numeric value
for <m>, after that the program computes the
formula: E = mc^2

Examples:
$ python3 einstein.py
m: 100
9000000000000000000
"""

m = int(input("m: "))
c = 300000000
E = m*c**2
print(f"{E}")