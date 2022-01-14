"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : List in Python(Program to get the difference between the two lists.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def difference_of_lists():
    """
       Description:
           Function is used to find the difference of two lists.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the difference of two list.
    """

    list1 = [1, 3, 5, 7, 9]
    list2=[1, 2, 4, 6, 7, 8]
    diff_list1_list2 = list(set(list1) - set(list2))
    diff_list2_list1 = list(set(list2) - set(list1))
    total_diff = diff_list1_list2 + diff_list2_list1
    logging.debug("The difference of two given lists is " + str(total_diff))


if __name__ == "__main__":
    difference_of_lists()