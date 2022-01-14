"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to find the repeated items in Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def repeated_items_in_tuple():
    """
       Description:
           Function is used to find the repeated items in Tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    tuple=(1, 3, 4, 32, 1, 5, 31, 32, 12, 21, 2, 3)
    logging.debug("The items which are repeated are as follows:")
    [logging.debug(i) for i in tuple if tuple.count(i) > 1]


if __name__ == "__main__":
    repeated_items_in_tuple()