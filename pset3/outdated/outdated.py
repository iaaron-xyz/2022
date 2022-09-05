"""
USAGE:
$ python outdated.py


DESCRIPTION:
This program prompts the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format.
If the user's input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.


EXAMPLE:
$ python outdated.py
Date: December 13, 1989
1989-12-13

$ python outdated.py
Date: 12/13/1989
1989-12-13

$ python outdated.py
Date: 1989-12-13
Valid Input: MM/DD/YYYY or Month Day, Year
Date: 12 December 1991
Date: 12/12/1991
1991-12-12
"""

def main():
    date = update()
    year = date[0]
    month = date[1]
    day = date[2]

    print(f"{year}-{month:02}-{day:02}")

def update():
    # Months list
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            # Get the date
            old_date = input("Date: ")
            date_numbers = []
            # Split the date
            if ',' in old_date:
                old_date = old_date.replace(',', '')
                date_elements = old_date.split(' ')
                # Append in year-month-day in order and number format
                date_numbers.append(int(date_elements[2]))
                date_numbers.append(months.index(date_elements[0].title()) + 1)
                date_numbers.append(int(date_elements[1]))
            elif ' ' not in old_date:
                date_elements = old_date.split('/')
                date_numbers.append(int(date_elements[2]))
                date_numbers.append(int(date_elements[0]))
                date_numbers.append(int(date_elements[1]))
            else:
                continue
        except ValueError:
            print("Valid Values: MM/DD/YYYY or Month Day, Year")
        except IndexError:
            print("Valid Input: MM/DD/YYYY or Month Day, Year")
        else:
            # Check the correct span of the days and months
            if (date_numbers[1] > 0 and date_numbers[1] < 13) and (date_numbers[2] > 0 and date_numbers[2]< 32):
                return date_numbers
            else:
                continue

if __name__ == "__main__":
    main()