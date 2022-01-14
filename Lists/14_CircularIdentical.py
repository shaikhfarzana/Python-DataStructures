"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to check whether two lists are circularly identical.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def circular_lists_identical():
    """
       Description:
           Function is used check whether the list is circularly identical or not.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the list.
    """
    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    list3 = [1, 10, 10, 0, 0]

    logging.debug('Compare list1 and list2')
    logging.debug(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
    logging.debug('Compare list1 and list3')
    logging.debug(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


if __name__ == "__main__":
    circular_lists_identical()

