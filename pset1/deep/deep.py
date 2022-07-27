"""
Usage:
$ python3 deep.py

Description:
This program asks the "What is the aswer to the great question of life ..."
if the user prompts "42" , "forty two" or "forty-two" (case insentively)
then prints "yes" otherwise prints "no"

Example:
$ python3 deep.py
What is the answer to the great Question of Life, the Universe, and Everything? FOrtY-Two
Yes
"""

# Get the user input
answer = input("What is the answer to the great Question of Life, the Universe, and Everything? ")

# Check if the asnwer is correct and reply properly
if answer.replace(" ","")=="42" or answer.lower()=="forty-two" or answer.lower()=="forty two":
    reply = "Yes"
else:
    reply = "No"
# Print the reply
print(reply)