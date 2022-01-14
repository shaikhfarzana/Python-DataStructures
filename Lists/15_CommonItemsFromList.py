"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to find common items from two lists.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_find_common_items_from_list():
    """
       Description:
           Function is used to find common items from the list.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the list.
    """
    color1 = "Red", "Green", "Orange", "White"
    color2 = "Black", "Green", "White", "Pink"
    logging.debug("The common items from two given list is {} ".format(set(color1) & set(color2)))


if __name__ == "__main__":
    to_find_common_items_from_list()