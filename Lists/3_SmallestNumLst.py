"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to get the smallest number from a list.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def smallest_number_of_list(lst):
    """
       Description:
           Function is used to find the smallest item from the list.
       Parameter:
          List required as a parameter.
       Return:
           Returns nothing but prints the smallest value.
    """
    new_sorted_list = sorted(set(lst))
    logging.debug("The smallest number from the given list is " + str(new_sorted_list[0]))


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
    smallest_number_of_list(lst)


if __name__ == "__main__":
    create_list()