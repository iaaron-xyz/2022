"""
USAGE:
python3 meal.py

DESCRIPTION:
In meal.py, implement a program that prompts the user for a time and outputs
whether it's breakfast time, lunch time, or dinner time. If it's not time for a meal,
don't output anything at all. Assume that the user's input will be formatted in 24-hour
time as #:## or ##:##. And assume that each meal's time range is inclusive.
For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.
breakfast: 7 - 8
lunch: 12 -13
dinner: 18 - 19


EXAMPLES:
What time is it? 12:35
lunch time
"""

def main():
    """
    Based on an input, decide if is breakfast time,
    lunch time or dinner time.

    breakfast: 7 - 8
    lunch: 12 -13
    dinner: 18 - 19
    """
    
    # input
    time = input("What time is it? ")
    # Decide if it is time for breakfast, lunch or dinner or none.
    time_decimal = convert(time)
    if time_decimal>=7.0 and time_decimal<=8.0:
        print("breakfast time")
        return 0
    elif time_decimal>=12.0 and time_decimal<=13.0:
        print("lunch time")
        return 0
    elif time_decimal>=18.0 and time_decimal<=19.0:
        print("dinner time")
        return 0
    else:
        return 1


def convert(time):
    """string->float"""
    time_arr = time.split(":")
    time_frac = float(time_arr[0]) + round(float(time_arr[1])/60.0,1)
    return time_frac


if __name__ == "__main__":
    main()