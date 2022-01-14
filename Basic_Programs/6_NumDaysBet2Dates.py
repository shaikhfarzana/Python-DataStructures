"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Basic Python(To calculate number of days between two dates.)
"""

from datetime import date
import logging
logging.basicConfig(level=logging.DEBUG)


def to_calculate_number_of_days_between_two_dates():
    """
     Description:
         Function is used to find the number of days between two dates.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the total number of days between two dates.
    """

    first_date = date(2015, 7, 2)
    last_date = date(2016, 7, 11)
    total_number_of_days = last_date - first_date
    logging.debug("The number of days between two dates is " + str(total_number_of_days.days))


if __name__ == "__main__":
    to_calculate_number_of_days_between_two_dates()
