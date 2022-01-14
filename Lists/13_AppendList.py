"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to append a list to the second list.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def append_lists():
    """
       Description:
           Function is used to append the list.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the list.
    """
    list1 = [1, 2, 3, 0]
    list2 = ['Red', 'Green', 'Black']
    final_list = list1 + list2
    logging.debug("Appended list is " + str(final_list))


if __name__ == "__main__":
    append_lists()