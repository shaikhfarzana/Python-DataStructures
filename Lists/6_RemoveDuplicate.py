"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to remove duplicates from a list.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def duplicate_value_remove_from_list(lst):
    """
       Description:
           Function is used to remove duplicate value from the list.
       Parameter:
          List as a parameter required.
       Return:
           Returns nothing but prints the lists.
    """

    new_list = sorted(set(lst))
    logging.debug("The list after removing duplicate items is " + str(new_list))


def create_list():
    """
       Description:
           Function is used to create a List.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the lists.
    """
    # creating an empty list
    lst = []

    # number of elements as input
    user_input = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, user_input):
        element = int(input())
        lst.append(element)  # adding the element
    logging.debug(lst)
    duplicate_value_remove_from_list(lst)


if __name__ == "__main__":
    create_list()
