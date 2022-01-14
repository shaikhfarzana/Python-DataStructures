"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : List in Python(Program to get a lis sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def last(n):
    """
       Description:
           Function is used to find the last element of tuple.
       Parameter:
          Nth tuple as a parameter required.
       Return:
           returns the last element of each tuple in the list of tuples.
    """

    return n[-1]


def sort_list_last():
    """
       Description:
           Function is used to sort the list with respect to last element in tuple.
       Parameter:
          No parameter is required.
       Return:
           Returns sorted list with respect to 2nd element.
    """

    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    return sorted(tuples, key=last)


if __name__ == "__main__":
    logging.debug("The sorted list with respect to second element is " + str(sort_list_last()))

