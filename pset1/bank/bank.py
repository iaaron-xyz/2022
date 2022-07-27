"""
Usage: $ python3 bank.py

Description:
This program prompts the user for a greeting.
if greeting starts with 'hello' prints '$0'
if greetings starts with 'h' prints '$20'
anything else prints '$100'

Example:
$ python3 bank.py
Greeting: How you doin?
$20
"""

# Receive user greetings
greeting = input("Greeting: ")
# function to print answer in proper format
dollars = lambda quantity : "$"+str(quantity)

# Quantity you return depends on the greetings received
if "hello" in greeting.lower():
    print(dollars(0))
elif greeting[0].lower() == 'h':
    print(dollars(20))
else:
    print(dollars(100))