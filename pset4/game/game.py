"""
How to run the file:
$ python game.py

Program description:
The program ask the user for a number called level.
A random number is generated among (1,level) (inclusive).
User has to guess that random number with feedback in every iteration.
- If it is lower than random, receives "Too small!"
- If it is higher than random, receives "Too high!"
- If it is the same number, receives "Just right!", and the program ends.
When the user enters a non-number, the program prompts the user again.

Example:
$ python game.py
Level: cat
Level: 10
Guess: 5
Too large!
Guess: 3
Just right!
$

$ python game.py
Level: 10
Guess: 2
Too small!
Guess: 3
Too small!
Guess: 7
Too Large!
Guess: 5
Too small!
Guess: 6
Just right!
$
"""



import random


def main():
    # Get the number's user
    level = get_level()
    # Generate the random number
    random_number = random.randint(1,level)
    # Ask the user to guess the number
    return user_guess(random_number)


def get_level():
    """None->int
    """
    while True:
        # Receive an integer
        try:
            number =  int(input("Level: "))
        except ValueError:
            pass
        # Return number if positive
        else:
            if number > 0:
                return number
            else:
                continue


def user_guess(number):
    """(int)->str
    """
    while True:
        # Get the user guess
        try:
            guess = int(input("Guess: "))
        # Reprompt for non numbers
        except ValueError:
            pass
        # Compare number with guess
        else:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too Large!")
            else:
                print("Just right!")
                return True


if __name__ == "__main__":
    main()