"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to convert a list toa Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def given_list():
    """
       Description:
           Function is used to pass list as an argument to other function.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    list = [1, 2, 3, 4]
    logging.debug("The List to Tuple conversion is {} ".format(list_to_tuple(list)))


def list_to_tuple(list):
    """
       Description:
           Function is used to convert List to Tuple.
       Parameter:
          List as a parameter required.
       Return:
           Returns tuple.
    """
    return tuple(list)


if __name__ == "__main__":
    given_list()


