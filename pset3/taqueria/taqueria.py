"""
USAGE:
$ python taqueria.py

DESCRIPTION:
This program enables a user to place an order,
prompting them for items, one per line, until the user inputs control-d
After each inputted item, display the total cost of all items inputted thus far,
prefixed with a dollar sign ($) and formatted to two decimal places.
The user input is case insensitively.
Ignore any input that isn't an item. Assume that every item on the menu will be titlecased.

EXAMPLE:
$ python3 taqueria.py 
Item: Hamburguesa
This item is not in the menu
$0.00
Item: Quesadilla
$8.50
Item: Quesadilla
$17.00
Item: Tortilla salad
$25.00
Item: 

"""

def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # total cost
    total = 0
    # request item until user exits (control-d)
    while True:
        try:
            # item input
            item = input("Item: ").title()
            total += menu[item]
        # Handle frequent errors
        except KeyError:
            print("This item is not in the menu")
        except EOFError:
            print("\n")
            break
        # print total with two decimals format
        total_float = "{:.2f}".format(total)
        print(f"${total_float}")

if __name__ == "__main__":
    main()