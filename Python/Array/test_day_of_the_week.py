# coding: utf-8

def day_of_the_week(day, month, year):
    """
    1185. Day of the Week

    Given a date, return the corresponding day of the week for that date.
    The input is given as three integers representing the day, month and year respectively.
    Return the answer as one of the following values 
    {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

    Example:
        Input: day = 31, month = 8, year = 2019
        Output: "Saturday"
    
    https://leetcode.com/problems/day-of-the-week/
    """
    calendar = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days = 365 * (year - 1971) + day + 4
    
    for i in range(1971, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            days += 1

    if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        days += 1
    
    days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month-1])

    return calendar[days%7]
    
print day_of_the_week(day = 31, month = 8, year = 2019)

def test_day_of_the_week_1():
    assert "Saturday" == day_of_the_week(day = 31, month = 8, year = 2019)

def test_day_of_the_week_2():
    assert "Sunday" == day_of_the_week(day = 18, month = 7, year = 1999)

def test_day_of_the_week_3():
    assert "Sunday" == day_of_the_week(day = 15, month = 8, year = 1993)


