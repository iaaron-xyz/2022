"""
USAGE:
$ python grocery.py

DESCRIPTION:
This program prompts the user for items, one per line,
until the user inputs control-d.
Then output the user's grocery list in all uppercase,
sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user's input case-insensitively.

EXAMPLE:
$ python3 grocery/grocery.py
Item: apple
Item: Apple
Item: Banana
Item: banana
Item: peach
Item: APPLE
Item: <CTRL + D>

3 APPLE
2 BANANA
1 PEACH

"""

def main():
    grocery_list = {}
    # Enter items until the user stops (control-D)
    while True:
        # Add 1 to existent items
        try:
            item = input("Item: ").lower()
            grocery_list[item] += 1
        # Initialize with 1 new items
        except KeyError:
            grocery_list[item] = 1
        except EOFError:
            print("\n")
            break

    # Get the list of items and order them
    groceries = sorted(list(grocery_list))
    # Print the gorcery items with its quantity
    for grocery in groceries:
        print(f"{grocery_list[grocery]} {grocery.upper()}")


if __name__ == "__main__":
    main()