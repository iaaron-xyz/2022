"""
USAGE:
$ python3 seasons.py

DESCRIPTION:
The program receives dates in YYYY-MM-DD format
- Then prints how old they are in minutes, rounded to the nearest integer,
- Using English words instead of numerals, just like the song from Rent, without any and between words.
- Assume that the user was born at midnight (i.e., 00:00:00) on that date.
- Assume that the current time is also midnight.

EXAMPLE:
(When today date is: 2022-08-03)
$ python seasons.py
Your Birthdate: 2021-08-03
Five hundred twenty-five thousand, six hundred minutes
"""

# libraries
from datetime import date
import sys
import inflect


p = inflect.engine()

def main():
    """Main Function"""

    # Receives Date
    birthdate = get_date(input("Your Birthdate: "))

    # Compute minutes elapsed from then to today
    total_minutes = minutes_then_now(birthdate)

    # Convert to words and print text
    print(to_song_format(total_minutes))


def get_date(date):
    """
    (str)->(list)

    Get the date and make sure it is typed
    in the correct format
    """
    # Get birthday
    birthdate = date.split("-")

    # Check correct format
    if len(birthdate) != 3:
        sys.exit("Date format: 'YYYY-MM-DD'")
    # Check correct number of digits
    if len(birthdate[0]) != 4 or len(birthdate[1]) != 2 or len(birthdate[2]) != 2:
        sys.exit("Valid format: 'YYYY-MM-DD'")

    return birthdate


def minutes_then_now(birthdate):
    """(list)->(int)"""

    # convert input to datetime.date() class
    user_date = date( int(birthdate[0]), int(birthdate[1]), int(birthdate[2]) )
    # Get current datetime
    current_date = date.today()
    # Computes the diference
    difference = current_date - user_date

    # Convert to minutes and return
    return int(difference.total_seconds()/60)


def to_song_format(minutes):
    """(str)->(str)"""

    words = p.number_to_words(minutes)
    return words.replace(" and", "").capitalize() + " minutes"


if __name__ == "__main__":
    main()
