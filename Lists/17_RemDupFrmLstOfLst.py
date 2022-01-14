"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to remove duplicates from a list of lists.)
"""
import itertools
import logging
logging.basicConfig(level=logging.DEBUG)


def remove_duplicates_from_list_of_list():
    """
       Description:
           Function is used to remove duplicates from the list.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the list.
    """
    num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    logging.debug("Original List: {}".format(num))
    num.sort()
    new_num = list(num for num, _ in itertools.groupby(num))
    logging.debug("New List: {}".format(new_num))


if __name__ == "__main__":
    remove_duplicates_from_list_of_list()