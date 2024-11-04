import re
import pyperclip

pattern = r'\d{2}/\d{2}/\d{4}'  # A pattern for date in DD/MM/YYYY format.
clipboard = pyperclip.paste()

def get_date(clipboard):
    return re.findall(pattern, clipboard)

def is_leap_year(year):
    # Leap year rules
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def date_sanity(date_str):
    day, month, year = map(int, date_str.split('/'))

    # Check month validity (1-12)
    if month < 1 or month > 12:
        return False

    # Check day validity based on the month.
    if month in {4, 6, 9, 11}:  # Small months
        return 1 <= day <= 30
    elif month == 2:  # February
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:  # Big months
        return 1 <= day <= 31

''' Main Function '''
dates = get_date(clipboard)

if dates:
    print("Dates:")
    for date in dates:
        if date_sanity(date):
            print(date)
else:
    print('No valid dates found.')

