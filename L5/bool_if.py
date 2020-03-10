# Write program that defines a bool function is_within(month,day,year), returning:
# (a) True if the date month/day/year falls between the two dates 9/1/1939 and 9/2/1945, inclusive, and
# (b)  False otherwise.  You can assume that the entered date is valid.
# Your program should have a main() method that reads three int values month,day,year,
# then prints out the value (True or False) returned from calling is_within(month,day,year).
#
# Hint: Use multiple alternative decisions (chained conditionals using if..elif..elif..else).
# First check the year for immediate exclusion (earlier than 1939 or later than 1945).
# If not immediate exclusion, check for immediate inclusion (between 1940 and 1944, inclusive).
# If neither of these, then year is either 1939 or 1945.  In each case of these latter cases,
# check for immediate inclusion/exclusion by examining the month, and so on.

import datetime

# 9/1/1939
earlierYear = 1939
earlierMonth = 9
earlierDate = 1

# 9/2/1945
laterYear = 1945
laterMonth = 9
laterDate = 2


def is_within(month, day, year):
    if year > laterYear or year < earlierYear:
        return 0
    elif earlierYear <= year <= laterYear:
        return 1
    elif month > laterMonth or year < earlierMonth:
        return 0
    elif earlierMonth <= month <= laterMonth:
        return 1
    elif day > laterDate or day < earlierDate:
        return 0
    elif day >= earlierDate and day <= laterDate:
        return 1


def main():
    day = int(input('Enter day'))
    month = int(input('Enter month'))
    year = int(input('Enter year'))
    isWithin = is_within(day, month, year)
    if (isWithin):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L5/bool_if.py
Enter day1
Enter month1
Enter year1938
False

Process finished with exit code 0'''