"""
Usage:
$ python numb3rs.py

Description:
This program asks for an ip address (IPv4)
If valid prints True
otherwise prints False

Example:
$ python numb3rs.py
IPv4 Address: 1.2.3.4
True
$ python numb3rs.py
IPv4 Address: 257.1.8.12
False
$ python numb3rs.py
IPv4 Address: cat
False
"""


import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #numlist = []
    # Check correct IPv4 Address format
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        # append numbers within a list
        numlist = [int(matches.group(i)) for i in range(1,5)]
        # ip's non-valid if numbers over 255
        if max(numlist) > 255:
            return False
        else:
            return True
    # any other outcome should be False
    return False


if __name__ == "__main__":
    main()