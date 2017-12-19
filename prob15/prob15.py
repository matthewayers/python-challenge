#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob15
whom?

picture of a calendar 1*6 with Jan 26 circled

URL: http://www.pythonchallenge.com/pc/return/uzi.html
soln: http://www.pythonchallenge.com/pc/return/mozart.html
"""

import datetime as dt


def find_target_year():

    for year in range(1006, 1996, 10):
        if dt.datetime(year, 1, 26).weekday() == 0:
            try:
                dt.datetime(year, 2, 29)
                print(f"{year}")
            except Exception as e:
                pass


def main():
    """
    ok, so first step is figure out what year that is.
    Enumerate all calendars where Jan 26 is a Monday

    noticing that it's a leap year (calendar in bottom right), we narrow the search

    in the comments, he's not the youngest, he's the second, gives us 1756

    flowers, tomorrow, gives us Jan 27,1756 -- mozart's birthday
    """
    find_target_year()


if __name__ == '__main__':
    main()
