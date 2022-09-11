"""
Usage:
$ python working.py

Description:
This program receives a string with a range of hours in AM/PM format
and return that hour range in a 24-hours format as the next examples shows
- 9:00 AM to 5:00 PM -> 09:00 to 17:00
- 9 AM to 5 PM -> 09:00 to 17:00
- 9 AM to 5:30 PM -> 09:00 to 17:30

Examples:
$ python working.py
Hours: 9 AM to 5:30 PM
09:00 to 17:30
"""
import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    """(stt)->(str)
    """
    # Search the specified string
    extract = re.search(r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)", s)

    # If search does not match
    if extract == None:
        raise ValueError

    # Groups
    h1 = int(extract.group(1))
    m1 = extract.group(2)
    t1 = extract.group(3)
    h2 = int(extract.group(4))
    m2 = extract.group(5)
    t2 = extract.group(6)

    # Check correct hour number
    if h1 > 12 or h2 > 12:
        raise ValueError

    # Convert the hours
    start_hour = to_24h_format(h1, t1)
    end_hour = to_24h_format(h2, t2)

    # Get the minutes (if exist)
    start_min = int(m1) if m1 else ""
    end_min = int(m2) if m2 else ""

    # Check minutes are not over 59
    if start_min != "":
        if start_min > 59:
            raise ValueError
    if end_min != "":
        if end_min > 59:
            raise ValueError

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


def to_24h_format(hour, format):
    """(int,str)->(int)
    """
    if hour == 12 and format == "AM":
        return 0
    elif hour == 12 and format == "PM":
        return 12
    elif format == "PM":
        return hour + 12
    else:
        return hour



if __name__ == "__main__":
    main()