"""
@Author: Farzana Shaikh
@Date: 11-01-2022 06:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 06:00PM
@Title : Basic Python(To print the calendar of a given month and year.)
"""
import calendar
import logging
logging.basicConfig(level=logging.DEBUG)


def display_calender():
    """
     Description:
         Function is used to take month and year as input from the user and display the calendar.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the corresponding calendar.
    """

    month = int(input("Enter the Nth month: "))
    year = int(input("Enter the Nth year: "))
    _calendar = calendar.month(year, month)
    logging.debug("The calendar of given Month and Year\n " + str(_calendar))


if __name__ == "__main__":
    display_calender()
