"""
Usage:
$ python professor.py

Description:
This program asks for a level and prompt 10 diferent calculations based on that level.
Levels allowed are the integers: [1, 2, 3]
- If level is 1: Calculations use numbers between 0 and 9 (inclusive).
- If level is 2: Calculations use numbers between 10 and 99 (inclusive).
- If level is 3: Calculations use numbers between 100 and 999 (inclusive).
- If something different is typed, the prompt appears again.
Calculations are additions of the kind: x + y = z.
- x: is a number generated randomly based on the level.
- y: is a number generated randomly based on the level.
- z: is the addition of x and y.
The user is required to type the solution to given calculations.
- If the user get the correct answer, another calculation appears.
- If the user dones not get the correct answer after 3 tries. The answer is showed and get pass to the next calulation.
The program finish once the user complete 10 calculations.
The user gets a score based on how many answers got correctly.

Example:
$ python professor.py
Level: 1
2 + 4 = 6
9 + 8 = 17
3 + 9 = 9
EEE
3 + 9 = 10
EEE
3 + 9 = 11
EEE
3 + 9 = 12
7 + 2 = 9
4 + 4 = 8
9 + 6 = 15
8 + 2 = 5
EEE
8 + 2 = cat
EEE
8 + 2 = dog
EEE
8 + 2 = 10
7 + 2 = 9
5 + 8 = 13
1 + 0 = 1
Score: 8
"""

import random

def main():
    # Get a level among 1,2 and 3
    level = get_level()
    # prompt operations
    print(f"Score: {prompt_operations(level)}")


def get_level():
    """()->int
    """
    # Get valid level
    levels = [1,2,3]
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        # Return valid level
        else:
            if level in levels:
                return level
            else:
                continue


def generate_integer(level):
    """(int)->int
    """
    # Generate random number with <level> orders of magnitude
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise LevelError("Valid levels: 1, 2, or 3")


def prompt_operations(level):
    """(int)->int
    """

    score = 10
    for _ in range(10):
        # Restart tries every new question
        tries = 0
        # Generate new numbers
        x, y = generate_integer(level), generate_integer(level)

        # Reprompt number until correct or reach 3 tries
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            # If it is not a number
            except ValueError:
                if (tries == 2):
                    print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    score -= 1
                    break
                else:
                    print("EEE")
                    tries += 1

            else:
                # When the answer is wrong
                if (answer != x+y):
                    if (tries == 2):
                        print("EEE")
                        print(f"{x} + {y} = {x+y}")
                        score -= 1
                        break
                    else:
                        print("EEE")
                        tries += 1
                # Go to the next equation when correct
                else:
                    break
    # Return final score
    return score



if __name__ == "__main__":
    main()