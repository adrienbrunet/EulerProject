# coding: utf-8

'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def main():
    year = 1901
    day = 1 + 365  # start at year 1901
    list_month_classic = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    list_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nb_sunday_first = 0

    while year < 2001:
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            _list = list_month_leap_year
        else:
            _list = list_month_classic

        for month in _list:
            day += month
            if day % 7 == 6:
                nb_sunday_first += 1
        year += 1

    return nb_sunday_first


if __name__ == '__main__':
    print(main())
    # 171 in 197usec
