"""
USAGE:
$ python3 coke.py

DESCRIPTION:
This program prompts the user to insert a coin,
one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.

EXAMPLE:
$ python coke.py 
Amount Due: 50
Insert Coin: 12
Amount Due: 50
Insert Coin: 12
Amount Due: 50
Insert Coin: 5
Amount Due: 45
Insert Coin: 10
Amount Due: 35
Insert Coin: 25
Amount Due: 10
Insert Coin: 10
Change Owed: 0

"""

def main():
    # Initial due
    print("Amount Due: 50")
    due = 50

    # Compute for specified coins until due is equal or lower to zero
    while True:
        coin = int(input("Insert Coin: "))
        if (coin != 25) and (coin != 10) and (coin != 5):
            print(f"Amount Due: {due}")
            continue
        else:
            due -= coin
            if due > 0:
                print(f"Amount Due: {due}")
            else:
                print(f"Change Owed: {abs(due)}")
                break


if __name__ == "__main__":
    main()