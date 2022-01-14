"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python( Python function that takes two lists and returns True if they have atleast one common member.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def user_input():
    """
       Description:
           Function is used to print the output.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the boolean value after list comparison.
    """
    logging.debug(common_member([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
    logging.debug(common_member([1, 2, 3, 4, 5], [6, 7, 8, 9]))


def common_member(list1, list2):
    """
       Description:
           Function is used to compare between List1 and List2.
       Parameter:
          Take two lists as a parameter.
       Return:
           Returns boolean value.
    """
    for x in list1:
        if x in list2:
            return True
    return False


if __name__ == "__main__":
    user_input()


