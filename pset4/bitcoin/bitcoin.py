"""
Usage:
$ python bitcoin.py n
- n: any integer or float number

Description:
This program gets the bitcoin information through the coindesk api: https://api.coindesk.com/v1/bpi/currentprice.json
Filters only the current price information.
Returns the price times n.
Requires the library requests: pip install requests
site: https://pypi.org/project/requests/

Example:
$ python bitcoin.py 1
$29,422.3082
$ python bitcoin.py 1.5
$44,133.4623
$ python bitcoin.py 2
$58,844.6164
"""

import requests
import sys


def main():
    # Check correct number of arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line arguments.")

    # Get the total amount
    try:
        # unitary price
        current_price = float(get_price())
        # total price
        total_amount = float(sys.argv[1]) * current_price
    # handle not number arguments
    except ValueError:
        sys.exit("Command-line argument is not a number.")
    # print total amount in dollars format
    else:
        print(f"${total_amount:,.4f}")


def get_price():
    # Get the json file information
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # Handle request errors
    except requests.RequestException:
        print("Request gone wrong!")
    # Return the unitary plain price value
    else:
        info = response.json()
        return info["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()