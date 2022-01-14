"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to generate all permutations of a list in Python.)
"""

import itertools
import logging
logging.basicConfig(level=logging.DEBUG)


def permutation_of_list(lst):
    """
        Description:
            Function is used to find the permutation of the given list.
        Parameter:
           List as a parameter required.
        Return:
            Returns nothing but prints the permutations of given lists.
    """
    logging.debug("The permutation of the given list is " + str(list(itertools.permutations(lst))))


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
    permutation_of_list(lst)


if __name__ == "__main__":
    create_list()
